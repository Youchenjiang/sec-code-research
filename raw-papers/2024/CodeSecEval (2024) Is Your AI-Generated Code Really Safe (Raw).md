# 29 CodeSecEval2024 Is Your AI Generated Code Really Safe  E

- **Source File**: [`29_CodeSecEval2024_Is_Your_AI_Generated_Code_Really_Safe__E.pdf`](file:///c:/Users/g1014/Documents/GitHub/Youchen/code-security-research/papers/29_CodeSecEval2024_Is_Your_AI_Generated_Code_Really_Safe__E.pdf)
- **Total Pages**: 12

---

<!-- Page 1 -->

Is Your AI-Generated Code Really Safe? Evaluating Large
Language Models on Secure Code Generation with CodeSecEval
Jiexin Wang
South China University of Technology
China
Xitong Luo
South China University of Technology
China
Liuwen Cao
South China University of Technology
China
Hongkui He
South China University of Technology
China
Hailin Huang
South China University of Technology
China
Jiayuan Xie
South China University of Technology
China
Adam Jatowt
University of Innsbruck
Austria
Yi Cai
South China University of Technology
China

## Abstract

Large language models (LLMs) have brought significant advance-
ments to code generation and code repair, benefiting both novice
and experienced developers. However, their training using unsani-
tized data from open-source repositories, like GitHub, raises the risk
of inadvertently propagating security vulnerabilities. Despite nu-
merous studies investigating the safety of code LLMs, there remains
a gap in comprehensively addressing their security features. In this
work, we aim to present a comprehensive study aimed at precisely
evaluating and enhancing the security aspects of code LLMs. To
support our research, we introduce CodeSecEval, a meticulously
curated dataset designed to address 44 critical vulnerability types
with 180 distinct samples. CodeSecEval serves as the foundation
for the automatic evaluation of code models in two crucial tasks:
code generation and code repair, with a strong emphasis on secu-
rity. Our experimental results reveal that current models frequently
overlook security issues during both code generation and repair
processes, resulting in the creation of vulnerable code. In response,
we propose different strategies that leverage vulnerability-aware
information and insecure code explanations to mitigate these secu-
rity vulnerabilities. Furthermore, our findings highlight that certain
vulnerability types particularly challenge model performance, in-
fluencing their effectiveness in real-world applications. Based on
these findings, we believe our study will have a positive impact on
the software engineering community, inspiring the development of
improved methods for training and utilizing LLMs, thereby leading
to safer and more trustworthy model deployment.
CCS CONCEPTS
• Security and privacy→ Software and application security ;
Software security engineering;
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
Conference’17, July 2017, Washington, DC, USA
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00
https://doi.org/XXXXXXX.XXXXXXX
KEYWORDS
Large Language Models, Code Generation, Code Repair, Security,
Dataset
ACM Reference Format:
Jiexin Wang, Xitong Luo, Liuwen Cao, Hongkui He, Hailin Huang, Jiayuan
Xie, Adam Jatowt, and Yi Cai. 2018. Is Your AI-Generated Code Really
Safe? Evaluating Large Language Models on Secure Code Generation with
CodeSecEval. In Woodstock ’18: ACM Symposium on Neural Gaze Detection,
June 03–05, 2018, Woodstock, NY . ACM, New York, NY, USA, 12 pages.
https://doi.org/XXXXXXX.XXXXXXX

## 1 INTRODUCTION

Large language models (LLMs) such as PALM [ 11], LLaMA [53],
GPT-4 [39], and Claude 3 [3] have demonstrated remarkable perfor-
mance in code generation, enabling developers to quickly transform
ideas into functional code. This capability reduces development
time and effort significantly, as evidenced by the popularity of
GitHub’s Copilot [17], a cloud-based AI assistant that has attracted
over 1.2 million users. However, since these code LLMs are often
trained on data from open-source repositories like GitHub, they
may inadvertently learn and replicate code that contains software
faults, bugs, and security vulnerabilities. The 2022 Open Source
Security and Risk Analysis (OSSRA) report [1] highlights that 81%
of the 2,049 codebases analyzed contain at least one vulnerability,
with 49% harboring high-risk vulnerabilities. Consequently, there
is a risk that these models could perpetuate these vulnerabilities
in their code generation process, potentially producing code that
is not just flawed but also highly susceptible to exploitation and
malicious attacks. For instance, Pearce et al. [41] reveal that Copilot
generates insecure code about 40% of the time, while Khoury et al.
[25] observe that only 5 of the 21 programs produced by ChatGPT
were initially secure. Furthermore, Perry et al. [44] find that par-
ticipants who had access to an AI assistant wrote significantly less
secure code than those without access to an assistant. As AI-driven
programming becomes increasingly prevalent in real-world soft-
ware development, ensuring both the correctness and security of
the generated code is crucial to foster trust in AI solutions and
safeguard software systems against potential attacks.
While multiple studies [5, 8, 25, 41, 44, 50] have investigated code
LLMs from a safety perspective, their limitations are noteworthy:
arXiv:2407.02395v2  [cs.SE]  4 Jul 2024

<!-- Page 2 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
Table 1: Comparison of related datasets. Abbreviations: PAE - "Precise Automatic Evaluation", CG - "Code Generation", CR -
"Code Repair". Note: The "PAE" column indicates whether the dataset supports the precise automatic evaluation like Pass@k,
and the "Complete & Executable Code" column indicates whether the Secure/Insecure Code is fully complete and runnable
without the need for additional context, such as helper functions for full functionality. Additionally, we include the HumanEval
dataset, which is widely used for general code generation task, but does not specifically address code security concerns.
Dataset Size Problem
Len(Avg.)
Insecure Code
Lines(Avg.)
Secure Code
Lines(Avg.)
Test Cases
Num(Avg.)
Complete &
Excutable Code
CWE Types
Num
PAE
CG CR
HumanEval [9] 164 67.85 - 7.49 7.20 ✔ - ✔ ✘
SecurityEval [50] 121 40.90 11.60 - - ✘ 69 ✘ ✘
LLMSecEval[52] 150 55.01 - 21.90 - ✔ 18 ✘ ✘
CyberSecEval [8] 1916 70.24 15.34 - - ✘ 50 ✘ ✘
CodeSecEval 180 78.73 6.73 10.21 3.61 ✔ 44 ✔ ✔
(i) Most research tends to focus on either a select few LLMs or a
narrow range of vulnerability types. For instance, studies such as
[5, 41, 44] exclusively focus on Copilot, whereas [ 25, 36] primar-
ily examine ChatGPT. (ii) Although these studies identify security
vulnerabilities in LLM-generated code, they often fall short in ex-
ploring or sufficiently validating strategies for generating more
secure code. Moreover, the capability of code LLMs to repair in-
secure code, another vital aspect of improving code security, has
been largely neglected. (iii) Existing datasets [8, 41, 50, 52] designed
for evaluating code security exhibit significant limitations, such
as small size, partial and non-executable codes, or even lack of
insecure/secure code examples. Furthermore, for security assess-
ment, they typically rely on rule-based static analyzers, which have
proven to be inaccurate, or on manual checks that are only practical
for a small, sampled set of results and may overlook the correctness
of the code. These issues underscore a critical gap in the existing
research landscape, highlighting the need for more comprehensive
studies that address a broader range of code security challenges
posed by large language models.
In response to these limitations, this study revolves around five
critical research questions, with a twofold objective: firstly, to more
accurately identify security vulnerabilities in code generation and
code repair by current code LLMs; and secondly, to offer strategies
for mitigating the security risks associated with these tasks. To
support our research, we introduce CodeSecEval,1 a meticulously
curated dataset comprising 180 samples that cover 44 critical vul-
nerability types. This dataset represents a significant improvement
over existing datasets [8, 50, 52] by enabling automated evaluations
of code generation and repair tasks. It includes complete and ex-
ecutable code and a set of test cases, which reduces the reliance
on labor-intensive manual assessments and imprecise analytical
tools. Table 1 provides detailed statistics and comparisons with four
related datasets (i.e., HumanEval [9], SecurityEval [50], LLMSecE-
val [52],2 and CyberSecEval [8]), highlighting its distinct features
and advantages. Leveraging the CodeSecEval dataset, we assess the
performance of 7 state-of-the-art code LLMs in the tasks of secure
1CodeSecEval has been uploaded as supplemental material and will be made publicly
available after publication.
2In Table 1, the 150 instances in the LLMSecEval dataset actually correspond to only 51
unique problems. This is because a large proportion of the "NL Prompt" entries (equiv-
alent to "Problem" in this study) are rephrased versions of the same issue, essentially
requiring identical code solutions.
code generation and insecure code repair.3 Our findings indicate
that current models often overlook security concerns during code
generation or repair processes. In response, we propose and validate
strategies that significantly enhance code security during gener-
ation and repair by integrating vulnerability-aware information
and explanations of insecure code. Therefore, this study aims to en-
courage the development of more robust methods for training and
deploying LLMs, leading to safer and more reliable code generation
and repair solutions.
In summary, our contributions are as follows:
(1) We introduce CodeSecEval, a carefully curated dataset consist-
ing of 180 samples covering 44 critical vulnerability types. This
dataset represents a substantial improvement over existing re-
sources by enabling more efficient and automated evaluations
for code security analysis.
(2) Through an extensive evaluation of seven cutting-edge code
LLMs, our work sheds light on their common neglect of se-
curity considerations during code generation and repair. This
analysis offers a detailed critique of the models’ vulnerabilities,
providing a deeper insight into their limitations.
(3) We devise and validate effective strategies to enhance the secu-
rity of code generated or repaired by incorporating vulnerability-
aware information and explanations of insecure code. These
strategies, aimed at significantly mitigating vulnerabilities, of-
fer valuable insights into safer model training methodologies
and more secure program deployment practices.

## 2 RELATED WORK

2.1 Security Issue of LLMs
Beyond natural language understanding, large language models
(LLMs) have greatly advanced the field of programming languages.
Leveraging vast code repositories, LLMs have achieved significant
success across various code-related tasks including code repair [24,
42, 58], code completion [21, 32], code summarization [33, 34], and
code generation [9, 37, 55]. Moreover, advancements in pre-training
techniques have also led to the creation of specialized models like
CodeBERT [15], CodeT5 [56], PyCodeGPT [61], AlphaCode [30],
3It is worth noting that the CodeSecEval dataset can also be easily adapted to other
code-related tasks like code completion [21, 32] and vulnerability classification [13, 54],
with a particular focus on code security.

<!-- Page 3 -->

Is Your AI-Generated Code Really Safe? Evaluating Large Language Models on Secure Code Generation with CodeSecEval Conference’17, July 2017, Washington, DC, USA
and InCoder [16]. However, the frequent neglect of security issues
in both generic LLMs and specialized models poses substantial risks.
Recent research highlights the security vulnerabilities associated
with code generated by LLMs [ 5, 8, 25, 41, 44, 50]. For instance,
Khoury et al. [25] discovered that ChatGPT produced insecure code
in 16 out of 21 security-relevant scenarios, with only 7 cases being
self-corrected after further prompting. Pearce et al. [41] reported
that Copilot, evaluated using CodeQL and manual checks, generated
insecure code about 40% of the time. Moreover, Perry et al . [43]
found that developers using AI model assistance tended to generate
more vulnerabilities, particularly in string encryption and SQL
injection, when interacting with OpenAI’s Codex model [9].
In addition to generating more secure code, enhancing code
security through code repair (or automatic program repair, APR)
presents another viable solution. Although many studies [ 18, 22,
27, 51, 60] have primarily focused on bug fixes with less emphasis
on security, recent research has started to explore LLMs’ ability to
address vulnerabilities [10, 42, 46, 57]. For example, Wu et al. [57]
conducted a pioneering study evaluating both LLMs and APR mod-
els for their effectiveness in repairing Java vulnerabilities, revealing
that they only fix very few Java vulnerabilities.
While previous research has identified security issues in code
generated or repaired by LLMs, these studies often exhibit signif-
icant limitations: (1) Most studies focus on a narrow selection of
LLMs—for instance, Khoury et al. [25] and [51] only evaluate Chat-
GPT, and [57] overlooks advanced models such as GPT-4 [39] or
CodeLlama [47]. Additionally, some studies like [42] are limited to a
few specific vulnerability types, examining only seven. (2) Many of
these studies primarily identify security challenges [41, 42], but do
not sufficiently explore or validate strategies for generating secure
code or repairing insecure code. (3) There is an heavy reliance on
security tools like CodeQL [12] to validate code security, despite
their known inaccuracies [49, 50, 59]. For example, [49] revealed
that static bug detectors identified only a negligible fraction of all
bugs, accounting for only 6 out of 410 bugs (0.01%). Moreover, while
some studies employ manual assessment to focus on security, this
method can sometimes overlook the overall correctness of the code.
2.2 Datasets for code security
Various datasets have been developed for code generation tasks,
including JuICe [2], CONCODE [20], DS-1000 [26], HumanEval [9]
and APPS [19]. However, these datasets primarily focus on general
code generation and do not specifically evaluate the ability to gen-
erate secure code. In terms of datasets related to security concerns,
most are designed for evaluating techniques in vulnerability de-
tection and prediction [4, 38, 45]. For code repair tasks, QuixBugs
[31] includes programs translated to both Python and Java, each
containing a single-line bug. Despite its relevance, this dataset is
relatively small, comprising only 40 instances. Big-Vul[14] contains
3,754 code vulnerabilities spanning 91 different vulnerability types,
all extracted from 348 Github projects. CVEfixes[7] provides a com-
prehensive categorization of vulnerabilities, utilizing the Common
Weakness Enumeration (CWE) types, and further enhances the
assessment of their impact by incorporating CVSS severity scores.
This dataset comprises a collection of 18,249 files and 50,322 func-
tions, encompassing both pre-repair and post-repair code. Both of
these datasets contain vulnerability information along with code
before and after fixes, rendering them invaluable resources in the
field of vulnerability analysis. However, due to the lack of test
cases, automated assessment of the repair code generated by the
models from a security standpoint proves challenging. Focusing
on secure code generation, three notable datasets have been intro-
duced: SecurityEval [50], LLMSecEval [52], and CyberSecEval [8].
SecurityEval, introduced first, comprises 130 Python code samples
across 75 vulnerability types. LLMSecEval followed with 150 in-
stances covering 18 types, and the most recent one, CyberSecEval,
provides a significantly larger collection of 1,916 instances across
50 types.
Despite the availability of these datasets, significant gaps remain
in their ability to comprehensively address code security, as high-
lighted in Table 1. These datasets often fail to provide comparative
examples of insecure and secure code. For instance, each SecurityE-
val sample only includes an ‘ID’, a ‘Prompt’ (equivalent to "Problem"
in this study), and an ‘Insecure Code’, but lacks corresponding se-
cure code examples. Additionally, the code in SecurityEval and
CyberSecEval is not executable as-is, often requiring additional
helper functions or specific configurations. In contrast, while the
code in LLMSecEval is complete, it presents a redundancy issue.
Its 150 instances only represent 51 unique problems, as many of
the "NL Prompt" entries are merely rephrased versions of the same
issue. Furthermore, these datasets do not support precise automatic
evaluation like the Pass@k metric, forcing reliance on imprecise
rule-based static analyzers or manual checks, the shortcomings of
which were discussed previously.
To overcome these limitations, we introduce CodeSecEval, a
meticulously curated dataset designed specifically to evaluate the
security awareness of large language models in code generation
and repair tasks. CodeSecEval includes a broad spectrum of crit-
ical vulnerability types and provides detailed attributes for each
data instance, enabling precise automatic evaluations. By utilizing
CodeSecEval, we aim to more accurately investigate the capabilities
of state-of-the-art LLMs in code generation and repair, while also
proposing effective strategies to enhance security in both tasks.

## 3 STUDY DESIGN

In this work, we aim to evaluate the efficacy of code LLMs in manag-
ing security concerns during code generation and repair. Addition-
ally, we seek to bolster the security of these processes by proposing
and assessing effective strategies. To achieve this, we formulate
several research questions that guide our investigation:
• RQ1: How effective are LLMs in addressing security concerns
during code generation?
• RQ2: What strategies can be devised to improve the security of
code generation by LLMs, and to what extent can they mitigate
security vulnerabilities? Are certain vulnerability types more
likely to be successfully mitigated?
• RQ3: How well do LLMs perform in repairing insecure code?
• RQ4: What strategies can be devised to improve the security
of code repaired by LLMs, and to what extent can these pro-
posed approaches repair security vulnerabilities? Are certain
vulnerability types more likely to be successfully repaired?

<!-- Page 4 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
(a) Example data instance of the SecEvalBase, with "ID" attribute of "CWE-020_author_1", "Entry_Point" attribute of "yaml_load".
(b) Example data instance of the SecEvalPlus, with "ID" attribute of "CWE-78_01", "Entry_Point" attribute of "find_files".
Figure 1: Illustrative examples of the CodeSecEval dataset, comprising two data instances from its two sub-datasets. The
attributes displayed with a white background correspond to the standard attributes of the CodeSecEval dataset. In contrast, the
attributes with a gray background are those introduced specifically, that our investigation aims to validate whether they can
effectively mitigate vulnerabilities, as discussed in Section 3.2.
• RQ5: What are the implications of the research findings for
the broader software engineering community, and how can
developers and researchers leverage LLMs more securely in
real-world applications?
Following this, we present CodeSecEval and elaborate on its
construction process. We then describe the experimental setup,
including five experiments tailored to probe the outlined research
questions. Subsequently, we introduce the code LLMs tested in

<!-- Page 5 -->

Is Your AI-Generated Code Really Safe? Evaluating Large Language Models on Secure Code Generation with CodeSecEval Conference’17, July 2017, Washington, DC, USA
these experiments and the evaluation metrics used to assess the
security-related performance.
3.1 CodeSecEval
3.1.1 Dataset Introduction. We now introduce CodeSecEval,4 a
dataset meticulously curated to evaluate the tasks of secure code
generation and insecure code repair. Comprising 180 samples across
44 vulnerability types, CodeSecEval offers a robust framework for
assessing code security in the Python language. As shown in Ta-
ble 1, this dataset distinguishes itself from existing datasets such as
SecurityEval [50], LLMSecEval [52], and CyberSecEval [8]. Notably,
CodeSecEval includes both executable secure and insecure codes,
as well as incorporates test cases, facilitating automated and precise
evaluations using the Pass@k metric. The dataset is structured with
six distinct attributes for each instance, which are as follows:
• ID: A unique identifier for each data instance, which also
indicates a specific vulnerability type. For example, "CWE-
434_03" refers to a sample of the CWE-434 vulnerability type.
• Problem: A description of a moderately complex programming
problem that needs to be solved.
• Insecure Code: An example of insecure code that exhibits the
specified vulnerability.
• Secure Code: An example of secure code that addresses the
specified vulnerability.
• Test: A set of test cases designed to validate both the functional
correctness and the security of the code, encapsulated in a
function named "check".
• Entry_Point: Name of the function to be implemented.
Based on the characteristics of the vulnerabilities addressed and
the resources utilized, CodeSecEval is further divided into the fol-
lowing two distinct subsets:
(1) SecEvalBase: This subset is constructed using the SecurityE-
val dataset [50], which aggregates instances from four external
sources: CodeQL [12], The Common Weakness Enumeration
(CWE) [35], SonarSource [48], and Pearce et al.[41]. The orig-
inal SecurityEval dataset, however, does not include anno-
tations for "Secure Code", "Test", and "Entry_Point", and its
"Insecure Code" instances are often incomplete, necessitating
additional context such as helper functions or specific config-
urations to ensure full functionality. Therefore, the selection
of instances for SecEvalBase was guided by the practicality of
completing the insecure code and providing necessary annota-
tions for the missing attributes. Finally, SecEvalBase includes
67 instances covering 37 vulnerability types.
(2) SecEvalPlus: This subset focuses on the "2023 CWE Top 25
Most Dangerous Software Weaknesses"5 We excluded eight
types from this list due to their rarity in Python, such as "CWE-
476: NULL Pointer Dereference", or their specific configura-
tions required to conduct testing, like "CWE-918: Server-Side
Request Forgery (SSRF)". We merged "CWE-287", "CWE-863",
"CWE-862", and "CWE-306" into a single category addressing
similar authorization issues. Finally, SecEvalPlus comprises
4CodeSecEval has been uploaded as supplemental material and will be made publicly
available after publication.
5https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html
113 instances across 14 types, providing at least 8 instances
for each type,6 ensuring a robust sample for each category.
Figure 1 showcases two example data instances from the SecE-
valBase and SecEvalPlus of CodeSecEval (displayed with a white
background), each displaying four attributes, with "ID" and "En-
try_Point" noted in the subfigure captions. In SecEvalPlus (Fig-
ure 1b), targeting the CWE-78 vulnerability ("OS Command Injec-
tion"), the "Insecure Code" illustrates a risk where attackers could
inject harmful commands, such as "rm -rf". In contrast, the "Secure
Code" effectively mitigates this vulnerability. The "Test" attribute
includes various test cases designed to assess both the correctness
and security of the code, such as checking for the presence of harm-
ful commands like ‘Test/CWE-78_01/dir1; rm MyImportantFile.txt’.
Furthermore, while SecEvalPlus employs a more natural language
description for the "Problem", SecEvalBase features code statements
combined with a docstring. This deliberate differentiation in dataset
construction aims to evaluate the performance of LLMs across dif-
ferent presentation formats.
3.1.2 Dataset Construction. This subsection outlines the construc-
tion process of the CodeSecEval dataset. To ensure its high-quality,
we engaged eight students specializing in software engineering,
including four Ph.D. and four M.S. students, with research expertise
in areas such as code generation and code summarization. They
were grouped into four pairs, each consisting of one Ph.D. and
one M.S. student, to foster collaboration and leverage diverse skills.
Subsequently, these pairs were tasked with generating instances
for the two subsets of CodeSecEval.
For the SecEvalBase dataset, each group was allocated approxi-
mately 35 records from the existing SecurityEval dataset, represent-
ing about a quarter of its total records. The team members were
tasked with closely collaborating to analyze the assigned instances,
focusing on the executability of the insecure code and the feasibility
of constructing various test cases. Following the initial assessment,
they next annotated five key data elements: "Secure Code", "Test",
and "Entry_Point". Moreover, teams were instructed to add some
input-output examples in the "Problem" and made necessary adjust-
ments to the "Insecure Code" to facilitate testing and better match
the vulnerability contexts. Each record then underwent a rigorous
manual checking process within the group, following these steps:
(1) The "Problem" should be clear, moderately complex, distinct
from previously collected "Problem", and include input-output
examples.
(2) The "Insecure Code" must exhibit the designated vulnerability.
(3) The "Secure Code" needs to effectively address the vulnerabil-
ity present in the "Insecure Code".
(4) The "Test" should comprise various cases that assess both the
correctness and security of the code, with the "Secure Code"
passing all tests while the "Insecure Code" fails.
(5) The "Entry_Point" should solely contain the name of the func-
tion to be implemented.
If any step does not fulfill the requirement, the students are
asked to either correct it to be valid or omit it and generate another
new record. Figure 2 depicts a clear flowchart outlining the manual
filtering steps. Finally, to further ensure the quality of the dataset,
6Only the merged authorization-related type includes 9 instances.

<!-- Page 6 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
Figure 2: The flowchart of the manual filtering process.
we hired 2 additional M.S. students to thoroughly check and clean
each instance in the collected data.
For SecEvalPlus, each group was assigned 3 or 4 vulnerability
types from the selected 14 types listed in the "2023 CWE Top 25 Most
Dangerous Software Weaknesses". The teams were tasked with
generating at least eight instances for each type. Unlike SecEvalBase,
no predefined "Insecure Code" or "Problem" was provided, requiring
groups to either identify real-world scenarios or create new ones
exemplifying these vulnerabilities, inspired by studies like [25, 41].
Finally, each SecEvalPlus record underwent the same meticulous
verification and filtering process as SecEvalBase.
3.2 Assumptions for Vulnerability Mitigation in
Code Generation and Code Repair
This subsection outlines our assumptions designed to potentially
enhance the security of code generated and repaired by LLMs. We
hypothesize that incorporating vulnerability-aware information
into problem descriptions and providing explanations of vulnera-
bilities in insecure code can foster more secure coding practices.
Vulnerability-aware Problem: Inspired by findings from [25],
which demonstrated that further prompting could correct secu-
rity flaws in several coding scenarios, we hypothesize that making
problem descriptions vulnerability-aware can also assist LLMs. This
strategy involves explicitly emphasizing the importance of recogniz-
ing and addressing vulnerabilities. We propose that by integrating
security concerns into problem descriptions, LLMs might be better
prepared to identify and mitigate potential security risks.
Insecure Code Explanation: Considering that it might be too
difficult for models to repair accurately using incorrect code and
problem as input, we assume that providing a brief explanation
of the vulnerabilities present in the insecure code could improve
repair outcomes. This additional information is intended to provide
some context that enables LLMs to focus more precisely on the
security flaws needing correction.
To test these assumptions, the students responsible for con-
structing the dataset were specifically instructed to develop both
vulnerability-aware problems and insecure code explanations. 7
Figure 1 illustrates these enhancements with examples from the
dataset ID "CWE-020_author_1" and "CWE-78_01", displayed in a
gray background.
3.3 Experimental Setup
3.3.1 Designed Experiments. To answer the five formulated re-
search questions, we conduct comprehensive evaluations of the
models using CodeSecEval across code generation and code repair.
We have designed four different experiments to thoroughly investi-
gate the performance and validate the effectiveness of strategies
applied by LLMs in both tasks:
(1) Direct Code Generation: This experiment evaluates the ca-
pability of LLMs to generate secure code directly from problem
statements, aiming to answer RQ1. It explores how effectively
current models address vulnerabilities during code generation.
(2) Code Generation with Vulnerability-aware Problem:This
experiment examines the impact of incorporating vulnerability-
aware information during code generation. It seeks to deter-
mine if enhanced problem descriptions with security details
can lead to fewer vulnerabilities, addressing RQ2.
(3) Direct Code Repair: This experiment addresses RQ3 and
focuses on assessing how well existing large language models
perform in directly repairing insecure code. We aim to under-
stand the models’ capabilities in automatically identifying and
fixing security vulnerabilities in existing code.
(4) Code Repair with Insecure Code Explanation: This ex-
periment provides LLMs with explanations of the vulnera-
bilities present in the insecure code during code repair. This
test addresses RQ4 and explores whether supplying detailed
vulnerability context improves or hinders the repair process.
3.3.2 Tested Models. We test the following seven models:
• InCoder [ 16]: InCoder is pre-trained on a mixture of multi-
lingual code data from GitHub and StackOverflow posts, utilizing
a causal masking objective. For our experiments, we utilized the
InCoder model with 6.7B parameters.
• CodeGen [37]: CodeGen is a family of code language models
available in different parameter sizes (350M, 2.7B, 6.1B, and 16.1B).
For fair comparison with the InCoder model, we used the mono
version with parameter size 6B.
• StarCoder [28]: StarCoder is a 15B parameter model with an
8K window size and FIM (Fill In the Middle, or infilling) capability.
It outperforms many previous open-source large language models
that support generating code from natural language descriptions
7This enriched contextual information has also been uploaded as supplemental material,
aiming to enhance its utility and accessibility for further research.

<!-- Page 7 -->

Is Your AI-Generated Code Really Safe? Evaluating Large Language Models on Secure Code Generation with CodeSecEval Conference’17, July 2017, Washington, DC, USA
and even matches the OpenAI code-cushman-001 model on the
HumanEval [9] and MBPP benchmarks [6].
• CodeLlama-Instruct [47]: CodeLlama-Instruct is a specialized
model crafted for precise instruction comprehension and secure
deployment. By leveraging a dataset from Llama 2 prompts to solve
coding challenges and leveraging CodeLlama to generate relevant
unit tests and solutions, CodeLlama-Instruct significantly enhances
security and usability through fine-tuning. We used the version
with parameter size 7B.
• GPT-3.5 [39]: GPT-3.5 has 175 billion parameters and has been
trained on a diverse range of internet text, enabling it to demon-
strate impressive understanding and generation capabilities.
• GPT-4 [39]: GPT-4 has been trained on an extensive and diverse
data, surpassing the capabilities of its predecessor GPT-3.5.
• Claude 3 Opus [3]: Claude 3 Opus, with 137 billion parameters,
stands as a cutting-edge large language model engineered by An-
thropic, showcasing exceptional performance across a spectrum of
AI benchmarks evaluating expert knowledge, reasoning, and math-
ematical prowess. Demonstrating near-human comprehension on
intricate tasks, Claude 3 Opus excels in analysis, forecasting, nu-
anced content creation, coding, and multilingual conversation.
3.3.3 Metrics. For code generation and code repair, we utilize the
execution-based metric Pass@k, which is widely acknowledged as a
more reasonable measure than match-based methods such as BLEU
[40]. Pass@k is usef for measuring the exact functional correctness
of generated code, where k code samples are generated for each
problem. A problem is considered solved if any sample passes all
the unit tests. Since this computation of Pass@k can have high
variance, we follow [9] and use the unbiased version of Pass@k:
𝑃𝑎𝑠𝑠 @𝑘 =𝐸𝑝𝑟𝑜𝑏𝑙𝑒𝑚𝑠[1−
 𝑛−𝑐
𝑘

 𝑛
𝑘
 ] (1)
where𝑘≤𝑛 is the number of samples and𝑐≤𝑛 is the number of
codes that pass all test cases. 1−(𝑛−𝑐
𝑘)
(𝑛
𝑘) is the estimated Pass@k for
a single problem.𝐸 is the expectation of Pass@k over all problems.
In practice, we compute the average pass@k across all problems,
considering k values equal to 1, 3, 5, 7, and 10.

## 4 RESULTS DISCUSSION

RQ1 How effective are LLMs in addressing security concerns during
code generation?
To address RQ1, we evaluate the models’ performance in gener-
ating code based on "Problem" information, with results presented
in the upper section of Table 2. Among relatively small models (In-
coder, CodeGen, StarCoder, and CodeLlama-Instruct), our analysis
reveals that CodeLlama-Instruct achieves the best results in terms
of Pass@k scores across various k values and datasets most of the
time, with CodeGen ranking second. In contrast, Incoder generally
underperforms in different settings, possibly due to its focus on code
completion tasks and the use of causal masking objectives during
pre-training, which may limit its effectiveness in broader code gen-
eration tasks. More interestingly, despite being more than twice the
size of CodeGen and CodeLlama-Instruct, StarCoder yields inferior
results. When considering models with significantly larger parame-
ters, our analysis reveals that the Claude 3 Opus model achieves
superior results when k is small on the entire CodeSecEval dataset
and SecEvalPlus dataset. However, as k increases, GPT-4 or GPT-
3.5 outperforms Claude 3 Opus. Additionally, on the SecEvalBase
dataset, GPT-4 emerges as the best performer, while showing less
effectiveness on the SecEvalPlus dataset, which features problems
in the form of natural language descriptions.
Overall, these findings highlight the nuanced performance of
Language Model-based Models (LLMs) in code generation tasks, un-
derlining the importance of considering both k-values and dataset
characteristics for optimal results. While smaller models like Code-
Gen or CodeLlama-Instruct show promising outcomes, larger mod-
els such as GPT-4 or Claude 3 Opus demonstrate superior per-
formance under certain conditions. These insights emphasize the
ongoing need for fine-tuning LLMs and tailoring their application
to specific requirements in addressing security concerns during
code generation.
RQ2 What strategies can be devised to improve the security of code
generation by LLMs, and to what extent can they mitigate security
vulnerabilities? Are certain vulnerability types more likely to be suc-
cessfully mitigated?
Next, we aim to explore methods for bolstering the security of
code generation by LLMs. While it’s intuitive to assume that formu-
lating problems to highlight potential vulnerabilities may prompt
LLMs to avoid generating insecure code, this assumption lacks ro-
bust validation in existing studies. To address this, we introduce
"Vulnerability-aware Problems" to assess whether incorporating
vulnerability information improves code generation security. Re-
sults presented in the lower section of Table 2 demonstrate a notable
performance boost across Pass@k for all models, except Incoder.
Notably, relatively smaller models like CodeLLama-Instruct shows
substantial gains, with Pass@1 and Pass@5 metrics increased from
9.22 to 24.33 and from 13.16 to 36.17 on the CodeSecEval dataset,
respectively. Particularly striking is the performance of Claud 3
Oppus, which shows remarkable improvements with Pass@1 and
Pass@5 increasing from 13.83 to 39.89 and from 15.96 to 49.55 on the
CodeSecEval dataset, respectively, and even outperforming GPT-4
on the SecEvalBase dataset.
Next, we analyze the performance of LLMs across various vul-
nerability types, with a particular focus on GPT-4’s performance
on the SecEvalPlus dataset using the Pass@5 metric. Each of the
14 types in this subset contains a more evenly distributed number
of instances. As indicated in the blue column of Figure 3, direct
code generation using GPT-4 generally struggled to generate secure
code for the SecEvalPlus dataset, with only the Pass@5 for CWE-
502 surpassing 50%. Notably, vulnerability types such as CWE-20,
CWE-79, CWE-77, CWE-434, and CWE-787 achieved a 0.0 score.
However, by incorporating "Vulnerability-aware Problem" descrip-
tions, there was a significant improvement in Pass@k rates across
most types, with seven types exceeding a 50.0 score in the Pass@5
metric. Despite these gains, some vulnerability types, like CWE-22
and CWE-276, showed minimal improvement. Interestingly, types
related to injection vulnerabilities, specifically CWE-78 ("OS Com-
mand Injection") and CWE-89 ("SQL Injection"), experienced worse
results. This suggests that GPT-4 may struggle with addressing in-
jection vulnerabilities, or that the vulnerability-aware information
provided may inadvertently complicate the model’s performance
in these scenarios.

<!-- Page 8 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
Table 2: Comparative results of code generation across various models on CodeSecEval and its two subsets (SecEvalBase,
SecEvalPlus), under two different experimental settings.
CodeSecEval SecEvalBase SecEvalPlus
Pass@K Pass@K Pass@KModel
k=1 k=3 k=5 k=7 k=10 k=1 k=3 k=5 k=7 k=10 k=1 k=3 k=5 k=7 k=10
Direct Code Generation
Incoder 0.39 0.84 1.11 1.33 1.67 0.00 0.00 0.00 0.00 0.00 0.62 1.34 1.77 2.12 2.65
CodeGen 5.89 8.00 9.14 10.03 11.11 2.09 3.97 4.86 5.42 5.97 8.14 10.38 11.68 12.77 14.16
StarCoder 4.33 7.32 8.72 9.63 10.56 1.19 2.91 3.90 4.35 4.48 6.19 9.93 11.58 12.76 14.16
CodeLlama-Instruct 9.22 12.28 13.16 13.54 13.89 9.55 12.86 13.92 14.45 14.93 9.03 11.93 12.71 13.00 13.27
GPT-3.5 10.56 14.64 16.18 17.02 17.78 10.75 13.23 14.23 14.73 14.93 10.44 15.48 17.34 18.38 19.47
GPT-4 12.44 15.24 16.28 17.00 17.78 13.43 15.86 16.80 17.36 17.91 11.86 14.88 15.97 16.78 17.70
Claude 3 Opus 13.83 15.58 15.96 16.07 16.11 13.13 13.43 13.43 13.43 13.43 14.25 16.85 17.46 17.64 17.70
Code Generation using Vulnerability-aware Problem
Incoder 0.61 1.30 1.70 1.98 2.22 0.30 0.80 1.16 1.39 1.49 0.80 1.59 2.02 2.33 2.65
CodeGen 13.50 19.82 22.12 23.31 24.44 7.46 12.59 14.69 15.75 16.42 17.08 24.12 26.53 27.80 29.20
StarCoder 14.11 21.32 23.90 25.32 26.67 4.18 6.38 7.34 8.05 8.96 20.00 30.18 33.72 35.57 37.17
CodeLlama-Instruct 24.33 33.04 36.17 37.87 39.44 27.01 33.53 35.77 37.25 38.81 22.74 32.75 36.40 38.23 39.82
GPT-3.5 28.89 43.69 48.75 51.61 54.44 29.85 41.03 44.01 45.25 46.27 28.32 45.27 51.56 55.38 59.29
GPT-4 31.89 41.62 44.46 46.10 47.78 34.48 42.77 45.02 46.31 47.76 30.35 40.93 44.13 45.98 47.79
Claude 3 Opus 39.89 46.63 49.55 51.42 53.33 38.81 45.07 47.49 49.10 50.75 40.53 47.56 50.76 52.79 54.97
Table 3: Code Generation performance results of GPT-4 Using Different Types of Vulnerability-aware Problem
Vulnerability-aware Problem With Steps Vulnerability-aware Problem Without Steps
Pass@K Pass@KModel
k=1 k=3 k=5 k=7 k=10 k=1 k=3 k=5 k=7 k=10
Incoder 0.94 1.76 2.09 2.27 2.35 0.32 0.88 1.35 1.72 2.11
CodeGen 13.76 20.06 22.32 23.54 24.71 13.26 19.61 21.94 23.11 24.21
StarCoder 13.65 19.17 21.11 22.30 23.53 14.53 23.25 26.40 28.03 29.47
CodeLlama-Instruct 22.47 30.98 33.87 35.24 36.47 26.00 34.89 38.22 40.22 42.11
GPT-3.5 32.00 46.93 51.49 54.01 56.47 26.11 40.80 46.29 49.46 52.63
GPT-4 36.82 47.64 51.38 53.80 56.47 27.47 36.23 38.27 39.21 40.00
Claude 3 Opus 42.12 48.32 51.04 53.00 55.29 37.89 45.12 48.21 50.01 51.58
Table 4: Comparative results of code repair across various models on CodeSecEval and its two subsets (SecEvalBase, SecEvalPlus),
under two different experimental settings.
CodeSecEval SecEvalBase SecEvalPlus
Pass@K Pass@K Pass@KModel
k=1 k=3 k=5 k=7 k=10 k=1 k=3 k=5 k=7 k=10 k=1 k=3 k=5 k=7 k=10
Direct Code Repair
Incoder 0.28 0.51 0.55 0.56 0.56 0.75 1.37 1.49 1.49 1.49 0.00 0.00 0.00 0.00 0.00
CodeGen 3.17 4.28 4.60 4.80 5.00 2.39 3.38 3.37 4.03 4.48 3.63 4.81 5.11 5.25 5.31
StarCoder 0.61 1.02 1.27 1.46 1.67 1.19 1.49 1.49 1.49 1.49 0.27 0.74 1.13 1.45 1.77
CodeLlama-Instruct 9.28 13.17 14.66 15.59 16.67 9.55 12.60 13.43 14.03 14.93 9.12 13.51 15.39 16.51 17.70
GPT-3.5 10.67 15.16 17.16 18.44 20.00 12.09 14.04 14.68 14.90 14.93 9.82 15.83 18.63 20.55 23.01
GPT-4 20.44 26.65 29.23 30.92 32.78 17.91 24.88 28.20 30.39 32.84 21.95 27.71 29.84 31.23 32.74
Claude 3 Opus 20.72 24.69 26.23 27.37 28.89 19.55 23.79 25.12 25.95 26.87 21.42 25.23 26.89 28.22 30.09
Code Repair using Insecure Code Explanation
Incoder 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
CodeGen 2.61 3.62 3.83 3.88 3.89 2.09 2.96 2.30 2.30 2.30 2.92 4.01 4.33 4.42 4.42
StarCoder 0.67 1.31 1.70 1.98 2.22 1.04 1.48 1.49 1.49 1.49 0.44 1.21 1.82 2.27 2.65
CodeLlama-Instruct 15.67 21.42 23.68 25.07 26.67 20.00 24.23 26.53 28.56 31.34 13.10 19.76 22.00 23.01 23.89
GPT-3.5 16.59 23.44 26.48 28.35 30.17 19.24 23.33 25.29 26.86 28.79 15.04 23.50 27.17 29.23 30.97
GPT-4 23.44 28.85 30.84 31.91 32.78 21.64 27.48 29.52 30.60 31.34 24.51 29.67 31.62 32.69 33.63
Claude 3 Opus 24.28 27.49 28.44 29.13 30.00 22.09 24.92 26.53 27.96 29.85 25.58 29.00 29.57 29.82 30.09

<!-- Page 9 -->

Is Your AI-Generated Code Really Safe? Evaluating Large Language Models on Secure Code Generation with CodeSecEval Conference’17, July 2017, Washington, DC, USA
Figure 3: Code Generation performance results of GPT-4 across 14 vulnerability types on the SecEvalPlus sub-datasets, under
two different experimental settings.
Figure 4: Code Repair performance results of GPT-4 across 14 vulnerability types on the SecEvalPlus sub-datasets, under two
different experimental settings.
Finally, our analysis of the Vulnerability-aware Problems reveals
that they can be categorized into two types: one with detailed proce-
dural steps, as shown in Figure 1 (a), and one without detailed steps,
as shown in Figure 1 (b). We manually classified these and found that
85 instances included procedural steps, while 95 did not. Further
analysis of GPT-4’s performance on these two types, presented in
Table 3, indicates that problems including steps achieved better per-
formance than those without. This finding aligns with the results of
studies such as [23] and [29], which suggest that using LLMs to plan
and then implement code step-by-step can significantly enhance
code generation performance. However, these studies primarily
focused on general code generation without considering the secu-
rity aspect. Nevertheless, while introducing security-relevant step
information significantly aids in secure code generation, providing
explanations of vulnerabilities, even without a stepwise format,
also contributes positively to generating secure code. This indicates
that both detailed procedural guidance and straightforward vul-
nerability explanations can effectively improve security in code
generation tasks.
RQ3 How well do LLMs perform in repairing insecure code?
Next, we focus on the performance of code LLMs in the code
repair task, where models are tasked with repairing "Insecure Code"
based on the "Problem" input. The results of this experiment are
detailed in the upper part of Table 4. Comparing these results with
those from the direct code generation task shown in Table 2, we
observe a general decline in performance among the three smaller
models in the CodeSecEval dataset, namely Incoder, CodeGen, and
StarCoder. This trend suggests that these models may be less effec-
tive at code repair. Specifically, both Incoder and StarCoder exhibit a
notable drop in effectiveness, with StarCoder experiencing the most
significant decline, where the Pass@1 score falls from 4.33 to 0.61.
Conversely, GPT-3.5, GPT-4, and Claude 3 Opus show enhanced
performance in the code repair task relative to code generation.
Particularly striking is GPT-4, whose Pass@5 score improves from
16.23 to 29.23 on the CodeSecEval, achieving the best results in
most cases.
RQ4 What strategies can be devised to improve the security of code
repaired by LLMs, and to what extent can these proposed approaches

<!-- Page 10 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
repair security vulnerabilities? Are certain vulnerability types more
likely to be successfully repaired?
We then explore whether including Insecure Code Explanation
improves the repair of insecure code. The results are shown in the
lower part of Table 4. Surprisingly, similar to the findings in di-
rect code generation, we observe a general decline in performance
among the same three smaller models (Incoder, CodeGen, and Star-
Coder) when compared with direct code generation. For other four
models, including relatively smaller model CodeLlama-Instruct, all
demonstrate improvements. Again, GPT-4 achives the best results
in most cases, with Claud 3 Opus as the second best model.
Similar to code generation, we next analyze the performance
of LLMs across various vulnerability types in code repair task, fo-
cusing particularly on GPT-4’s performance on the SecEvalPlus
dataset using the Pass@5 metric. As depicted in Figure 4, although
GPT-4 shows the overall improvement when using Insecure Code
Explanation in Table 4, the performance still varies significantly
across different vulnerability types. For some types, there is no
improvement or even a decline when using the insecure code ex-
planations. These findings highlight the complexities involved in
repairing insecure code with current models and underline the
need for advanced approaches in code repair to bolster security in
software development practices.
RQ5 What are the implications of the research findings for the broader
software engineering community, and how can developers and re-
searchers leverage LLMs more securely in real-world applications?
The research findings presented in this study have several im-
plications for the broader software engineering community and
offer insights on leveraging large language models more securely
in real-world applications.
(1) Firstly, the CodeSecEval dataset introduced in this paper serves
as a valuable resource for evaluating code LLMs from a soft-
ware security perspective. It provides a curated collection of
vulnerable and secure code instances, enabling researchers to
benchmark and improve the security-awareness capabilities of
code LLMs. The dataset can aid in evaluating more secure and
robust models for code generation, repair, and vulnerability
classification tasks.
(2) Secondly, our study highlights the potential risks associated
with using large language models for code generation and
code repair. It emphasizes the importance of considering and
mitigating security concerns when employing these models
in software development tasks. Understanding the varying
performance of different models across different vulnerability
types can guide developers in selecting appropriate models
for specific use cases, considering security requirements.
(3) Finally, our findings underscore the need for further research
and advancements in code repair approaches to enhance se-
curity in software engineering practices. As large language
models continue to evolve, addressing the challenges of re-
pairing insecure code effectively is crucial for building more
trustworthy and secure software systems.
To leverage large language models more securely in real-world
applications, developers and researchers should consider:
• Incorporate Security Awareness: When utilizing large language
models for code generation tasks, developers should incorporate
potential vulnerability information into input prompts to encourage
the models to generate more secure code. Furthermore, the research
of transforming Problem to Vulnerability-aware Problem, can also
aid in generating more secure code.
• Validate Repair Capabilities: Before deploying large language
models for code repair tasks, thorough validation of their repair ca-
pabilities, especially concerning security vulnerabilities, is essential
to avoid introducing new security risks.
• Dataset Curation: Building comprehensive datasets like CodeSe-
cEval that encompass various vulnerability types and provide clear
explanations of insecure code can facilitate the development of
more robust and secure models.
• Continuous Model Improvements: Researchers and developers
should continuously work on improving large language models’
security-awareness capabilities, addressing the limitations identi-
fied in our study and other related research.
In conclusion, the findings from this research provide valuable
guidance for enhancing the security of large language models in
code generation and repair tasks, contributing to the overall im-
provement of secure software engineering practices. By understand-
ing the implications of these findings, developers and researchers
can leverage large language models more securely in real-world
applications and mitigate potential security risks associated with
code generation tasks.

## 5 CONCLUSIONS AND FUTURE WORK

This paper provides a comprehensive study that aims to evaluate
and enhance code LLMs from a software security perspective. Exten-
sive experiments on our curated CodeSecEval dataset yield valuable
insights into the strengths and limitations of large language models
in security-critical software engineering tasks. Our proposed ap-
proaches for code generation have demonstrated their effectiveness
in enhancing code security and mitigating security vulnerabilities.
However, we also identified specific weaknesses in existing LLMs’
capabilities, particularly in code repair for certain vulnerability
types. To advance the field of secure code generation, future re-
search should explore the generalizability of our approaches to
other programming languages. Moreover, improving the code re-
pair capabilities of LLMs remains a promising direction, and further
research could investigate the effectiveness of integrating domain-
specific knowledge and feedback mechanisms to produce more
robust and secure code repairs. Overall, this study contributes to a
better understanding of LLMs’ potential and limitations in address-
ing security concerns.

## References

[1] Synopsys 2022. [n. d.]. Open Source Security and Risk Analysis Report. Technical
report, Synopsys Inc.
[2] Rajas Agashe, Srinivasan Iyer, and Luke Zettlemoyer. 2019. JuICe: A Large Scale
Distantly Supervised Dataset for Open Domain Context-based Code Generation.
In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Pro-
cessing (EMNLP-IJCNLP). Association for Computational Linguistics, 5436–5446.
https://aclanthology.org/D19-1546
[3] Anthropic. 2024. Introducing the next generation of Claude. Accessed: March 13,
2024. 2024. url: https://www.anthropic.com/news/claude-3-family.
[4] Steven Arzt, Siegfried Rasthofer, Christian Fritz, Eric Bodden, Alexandre Bar-
tel, Jacques Klein, Yves Le Traon, Damien Octeau, and Patrick McDaniel. 2014.
Flowdroid: Precise context, flow, field, object-sensitive and lifecycle-aware taint
analysis for android apps. Acm Sigplan Notices 49, 6 (2014), 259–269.

<!-- Page 11 -->

Is Your AI-Generated Code Really Safe? Evaluating Large Language Models on Secure Code Generation with CodeSecEval Conference’17, July 2017, Washington, DC, USA
[5] Owura Asare, Meiyappan Nagappan, and N Asokan. 2023. Is github’s copilot
as bad as humans at introducing vulnerabilities in code? Empirical Software
Engineering 28, 6 (2023), 129.
[6] Jacob Austin, Augustus Odena, Maxwell I. Nye, Maarten Bosma, Henryk
Michalewski, David Dohan, Ellen Jiang, Carrie J. Cai, Michael Terry, Quoc V. Le,
and Charles Sutton. 2021. Program Synthesis with Large Language Models. CoRR
abs/2108.07732 (2021). arXiv:2108.07732 https://arxiv.org/abs/2108.07732
[7] Guru Bhandari, Amara Naseer, and Leon Moonen. 2021. CVEfixes: automated
collection of vulnerabilities and their fixes from open-source software. InProceed-
ings of the 17th International Conference on Predictive Models and Data Analytics
in Software Engineering. 30–39.
[8] Manish Bhatt, Sahana Chennabasappa, Cyrus Nikolaidis, Shengye Wan, Ivan Evti-
mov, Dominik Gabi, Daniel Song, Faizan Ahmad, Cornelius Aschermann, Lorenzo
Fontana, et al. 2023. Purple llama cyberseceval: A secure coding benchmark for
language models. arXiv preprint arXiv:2312.04724 (2023).
[9] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira
Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman,
et al. 2021. Evaluating large language models trained on code. arXiv preprint
arXiv:2107.03374 (2021).
[10] Zimin Chen, Steve Kommrusch, and Martin Monperrus. 2022. Neural transfer
learning for repairing security vulnerabilities in c code. IEEE Transactions on
Software Engineering 49, 1 (2022), 147–165.
[11] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav
Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Se-
bastian Gehrmann, et al. 2022. Palm: Scaling language modeling with pathways.
arXiv preprint arXiv:2204.02311 (2022).
[12] CodeQL. 2022. CodeQL. https://github.com/github/codeq.
[13] Yukun Dong, Yeer Tang, Xiaotong Cheng, and Yufei Yang. 2023. DeKeDVer:
A deep learning-based multi-type software vulnerability classification frame-
work using vulnerability description and source code. Information and Software
Technology 163 (2023), 107290.
[14] Jiahao Fan, Yi Li, Shaohua Wang, and Tien N Nguyen. 2020. AC/C++ code
vulnerability dataset with code changes and CVE summaries. In Proceedings of
the 17th International Conference on Mining Software Repositories . 508–512.
[15] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong,
Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, et al. 2020. Codebert: A pre-trained
model for programming and natural languages. arXiv preprint arXiv:2002.08155
(2020).
[16] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi,
Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2022. Incoder: A
generative model for code infilling and synthesis. arXiv preprint arXiv:2204.05999
(2022).
[17] Nat Friedman. 2021. Introducing GitHub Copilot: your AI pair programmer.
URL https://github. blog/2021-06-29-introducing-github-copilot-ai-pair-programmer
(2021).
[18] Luca Gazzola, Daniela Micucci, and Leonardo Mariani. 2018. Automatic software
repair: A survey. In Proceedings of the 40th International Conference on Software
Engineering. 1219–1219.
[19] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora,
Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al . 2021.
Measuring Coding Challenge Competence With APPS. In Thirty-fifth Conference
on Neural Information Processing Systems Datasets and Benchmarks Track (Round
2).
[20] Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, and Luke Zettlemoyer. 2018.
Mapping Language to Code in Programmatic Context. In Proceedings of the 2018
Conference on Empirical Methods in Natural Language Processing . Association
for Computational Linguistics, Brussels, Belgium, 1643–1652. https://doi.org/10.
18653/v1/D18-1192
[21] Maliheh Izadi, Roberta Gismondi, and Georgios Gousios. 2022. Codefill: Multi-
token code completion by jointly learning from structure and naming sequences.
In Proceedings of the 44th International Conference on Software Engineering . 401–
412.
[22] Nan Jiang, Thibaud Lutellier, and Lin Tan. 2021. Cure: Code-aware neural machine
translation for automatic program repair. In 2021 IEEE/ACM 43rd International
Conference on Software Engineering (ICSE) . IEEE, 1161–1173.
[23] Xue Jiang, Yihong Dong, Lecheng Wang, Qiwei Shang, and Ge Li. 2023.
Self-planning code generation with large language model. arXiv preprint
arXiv:2303.06689 (2023).
[24] Harshit Joshi, José Cambronero Sanchez, Sumit Gulwani, Vu Le, Gust Verbruggen,
and Ivan Radiček. 2023. Repair is nearly generation: Multilingual program repair
with llms. In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 37.
5131–5140.
[25] Raphaël Khoury, Anderson R Avila, Jacob Brunelle, and Baba Mamadou Camara.
2023. How Secure is Code Generated by ChatGPT?arXiv preprint arXiv:2304.09655
(2023).
[26] Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettle-
moyer, Scott Wen-tau Yih, Daniel Fried, Sida Wang, and Tao Yu. 2022. DS-1000:
A Natural and Reliable Benchmark for Data Science Code Generation. arXiv
preprint arXiv:2211.11501 (2022).
[27] Claire Le Goues, Michael Pradel, Abhik Roychoudhury, and Satish Chandra. 2021.
Automatic program repair. IEEE Software 38, 4 (2021), 22–27.
[28] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov,
Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. 2023.
StarCoder: may the source be with you! arXiv preprint arXiv:2305.06161 (2023).
[29] Xin-Ye Li, Jiang-Tian Xue, Zheng Xie, and Ming Li. 2023. Think outside the code:
Brainstorming boosts large language models in code generation. arXiv preprint
arXiv:2305.10679 (2023).
[30] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi
Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022.
Competition-level code generation with alphacode. Science 378, 6624 (2022),
1092–1097.
[31] Derrick Lin, James Koppel, Angela Chen, and Armando Solar-Lezama. 2017.
QuixBugs: A multi-lingual program repair benchmark set based on the Quixey
Challenge. In Proceedings Companion of the 2017 ACM SIGPLAN international
conference on systems, programming, languages, and applications: software for
humanity. 55–56.
[32] Shuai Lu, Nan Duan, Hojae Han, Daya Guo, Seung-won Hwang, and Alexey
Svyatkovskiy. 2022. Reacc: A retrieval-augmented code completion framework.
arXiv preprint arXiv:2203.07722 (2022).
[33] Stephen MacNeil, Andrew Tran, Arto Hellas, Joanne Kim, Sami Sarsa, Paul
Denny, Seth Bernstein, and Juho Leinonen. 2023. Experiences from using code
explanations generated by large language models in a web software development
e-book. In Proceedings of the 54th ACM Technical Symposium on Computer Science
Education V. 1. 931–937.
[34] Stephen MacNeil, Andrew Tran, Dan Mogil, Seth Bernstein, Erin Ross, and Ziheng
Huang. 2022. Generating diverse code explanations using the gpt-3 large language
model. In Proceedings of the 2022 ACM Conference on International Computing
Education Research-Volume 2. 37–39.
[35] The MITRE Corporation (MITRE). 2022. Common Weakness Enumeration.
[36] Nathalia Nascimento, Paulo Alencar, and Donald Cowan. 2023. Comparing
software developers with chatgpt: An empirical investigation. arXiv preprint
arXiv:2305.11837 (2023).
[37] Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou,
Silvio Savarese, and Caiming Xiong. 2022. Codegen: An open large language
model for code with multi-turn program synthesis.arXiv preprint arXiv:2203.13474
(2022).
[38] Georgios Nikitopoulos, Konstantina Dritsa, Panos Louridas, and Dimitris
Mitropoulos. 2021. CrossVul: a cross-language vulnerability dataset with commit
data. In Proceedings of the 29th ACM Joint Meeting on European Software Engi-
neering Conference and Symposium on the Foundations of Software Engineering .
1565–1569.
[39] OpenAI. 2023. GPT-4 Technical Report. arXiv:2303.08774 [cs.CL]
[40] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu: a
method for automatic evaluation of machine translation. In Proceedings of the
40th annual meeting of the Association for Computational Linguistics . 311–318.
[41] Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, and
Ramesh Karri. 2022. Asleep at the keyboard? assessing the security of github
copilot’s code contributions. In 2022 IEEE Symposium on Security and Privacy
(SP). IEEE, 754–768.
[42] Hammond Pearce, Benjamin Tan, Baleegh Ahmad, Ramesh Karri, and Brendan
Dolan-Gavitt. 2023. Examining zero-shot vulnerability repair with large language
models. In 2023 IEEE Symposium on Security and Privacy (SP) . IEEE, 2339–2356.
[43] Neil Perry, Megha Srivastava, Deepak Kumar, and Dan Boneh. 2022. Do users
write more insecure code with AI assistants? arXiv preprint arXiv:2211.03622
(2022).
[44] Neil Perry, Megha Srivastava, Deepak Kumar, and Dan Boneh. 2023. Do users
write more insecure code with AI assistants?. In Proceedings of the 2023 ACM
SIGSAC Conference on Computer and Communications Security . 2785–2799.
[45] Serena Elisa Ponta, Henrik Plate, Antonino Sabetta, Michele Bezzi, and Cédric
Dangremont. 2019. A manually-curated dataset of fixes to vulnerabilities of
open-source software. In 2019 IEEE/ACM 16th International Conference on Mining
Software Repositories (MSR). IEEE, 383–387.
[46] Julian Aron Prenner, Hlib Babii, and Romain Robbes. 2022. Can OpenAI’s codex
fix bugs? an evaluation on QuixBugs. In Proceedings of the Third International
Workshop on Automated Program Repair. 69–75.
[47] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiao-
qing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, et al. 2023. Code
llama: Open foundation models for code. arXiv preprint arXiv:2308.12950 (2023).
[48] SonarSource S.A. 2022. SonarSource static code analysis.
https://rules.sonarsource.com.
[49] Jiho Shin, Junjie Wang, Song Wang, Nachiappan Nagappan, et al. 2023. Automatic
static bug detection for machine learning libraries: Are we there yet? arXiv
preprint arXiv:2307.04080 (2023).
[50] Mohammed Latif Siddiq and Joanna CS Santos. 2022. SecurityEval dataset: mining
vulnerability examples to evaluate machine learning-based code generation
techniques. In Proceedings of the 1st International Workshop on Mining Software

<!-- Page 12 -->

Conference’17, July 2017, Washington, DC, USA Jiexin Wang, et al.
Repositories Applications for Privacy and Security . 29–33.
[51] Dominik Sobania, Martin Briesch, Carol Hanna, and Justyna Petke. 2023. An
analysis of the automatic bug fixing performance of chatgpt. In 2023 IEEE/ACM
International Workshop on Automated Program Repair (APR) . IEEE, 23–30.
[52] Catherine Tony, Markus Mutas, Nicolás E Díaz Ferreyra, and Riccardo Scandariato.
2023. Llmseceval: A dataset of natural language prompts for security evaluations.
In 2023 IEEE/ACM 20th International Conference on Mining Software Repositories
(MSR). IEEE, 588–592.
[53] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971 (2023).
[54] Qian Wang, Yuying Gao, Jiadong Ren, and Bing Zhang. 2023. An automatic
classification algorithm for software vulnerability based on weighted word vector
and fusion neural network. Computers & Security 126 (2023), 103070.
[55] Yue Wang, Weishi Wang, Shafiq Joty, and Steven C.H. Hoi. 2021. CodeT5:
Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Un-
derstanding and Generation. In Proceedings of the 2021 Conference on Empir-
ical Methods in Natural Language Processing . Association for Computational
Linguistics, Online and Punta Cana, Dominican Republic, 8696–8708. https:
//doi.org/10.18653/v1/2021.emnlp-main.685
[56] Yue Wang, Weishi Wang, Shafiq Joty, and Steven CH Hoi. 2021. Codet5: Identifier-
aware unified pre-trained encoder-decoder models for code understanding and
generation. arXiv preprint arXiv:2109.00859 (2021).
[57] Yi Wu, Nan Jiang, Hung Viet Pham, Thibaud Lutellier, Jordan Davis, Lin Tan, Petr
Babkin, and Sameena Shah. 2023. How effective are neural networks for fixing
security vulnerabilities. In Proceedings of the 32nd ACM SIGSOFT International
Symposium on Software Testing and Analysis . 1282–1294.
[58] Chunqiu Steven Xia and Lingming Zhang. 2022. Less training, more repairing
please: revisiting automated program repair via zero-shot learning. InProceedings
of the 30th ACM Joint European Software Engineering Conference and Symposium
on the Foundations of Software Engineering . 959–971.
[59] Yiheng Xiong, Mengqian Xu, Ting Su, Jingling Sun, Jue Wang, He Wen, Geguang
Pu, Jifeng He, and Zhendong Su. 2023. An empirical study of functional bugs in
android apps. In Proceedings of the 32nd ACM SIGSOFT International Symposium
on Software Testing and Analysis. 1319–1331.
[60] He Ye, Matias Martinez, Thomas Durieux, and Martin Monperrus. 2021. A
comprehensive study of automatic program repair on the QuixBugs benchmark.
Journal of Systems and Software 171 (2021), 110825.
[61] Daoguang Zan, Bei Chen, Dejian Yang, Zeqi Lin, Minsu Kim, Bei Guan, Yongji
Wang, Weizhu Chen, and Jian-Guang Lou. 2022. CERT: Continual Pre-training
on Sketches for Library-oriented Code Generation. InThe 2022 International Joint
Conference on Artificial Intelligence.


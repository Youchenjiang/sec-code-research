---
title: "A Risk Estimation Study of Native Code Vulnerabilities in Android Applications"
pages: 25
---

# A Risk Estimation Study of Native Code Vulnerabilities in Android Applications

## Page 1

arXiv:2406.02011v1  [cs.CR]  4 Jun 2024

Keywords: Vulnerability Detection, Android App, Native Code

1
Introduction

A Risk Estimation Study of Native Code

Vulnerabilities in Android Applications

Silvia Lucia Sanna1[0009−0002−8269−9777], Diego Soi1[0009−0009−0092−9067],
Davide Maiorca1[0000−0003−2640−4663], Giorgio Fumera1[0000−0001−5300−226X],

and Giorgio Giacinto1[0000−0002−5759−3017]

Department of Electrical and Electronic Engineering, University of Cagliari, Italy

Abstract. Android is the most used Operating System worldwide for
mobile devices, with hundreds of thousands of apps downloaded daily.
Although these apps are primarily written in Java and Kotlin, advanced
functionalities such as graphics or cryptography are provided through
native C/C++ libraries. These libraries can be affected by common vul-
nerabilities in C/C++ code (e.g., memory errors such as buffer overflow),
through which attackers can read/modify data or execute arbitrary code.
The detection and assessment of vulnerabilities in Android native code
have only been recently explored by previous research work. In this pa-
per, we propose a fast risk-based approach that provides a risk score
related to the native part of an Android application. In this way, before
an app is released, the developer can check if the app may contain vul-
nerabilities in the Native Code and, if present, patch them to publish
a more secure application. To this end, we first use fast regular expres-
sions to detect library versions and possible vulnerable functions. Then,
we apply scores extracted from a vulnerability database to the analyzed
application, thus obtaining a risk score representative of the whole app.
We demonstrate the validity of our approach by performing a large-scale
analysis on more than 100, 000 applications (but only 40% contained na-
tive code) and 15 popular libraries carrying known vulnerabilities. The
attained results show that many applications contain well-known vulner-
abilities that miscreants can potentially exploit, posing serious concerns
about the security of the whole Android applications landscape.

The usage of mobile devices is increasingly growing due to their continuous ad-
vancements that allow people to carry out very different tasks, from surfing the
internet to accessing banking or medical accounts. Smartphones are also exten-
sively employed as multimedia devices (e.g., to watch movies or play games)
and as aids for payment authentication and Public Administration services. Un-
fortunately, this variety of usage allows attackers to exploit vulnerabilities (by


---

## Page 2

2
F. Author et al.

resorting to, e.g., phishing emails and messages or by exploiting memory errors)
to take control of the target devices.

Among the various Operating Systems available for mobile devices, Android
is the most used worldwide [1], and many of its applications can feature hundreds
of millions of downloads. These apps often need to interact with native activ-
ities and components (e.g., camera and microphone) available through Native
Code (typically C/C++) implementation, which may be written from scratch
or taken from third-party libraries such as Libpng and OpenCV. For brevity,
we refer to native third-party libraries as products. In most cases, developers use
publicly available libraries such as Libpng (for image management) by import-
ing them into their projects. As native libraries are written in memory-unsafe
languages, they can suffer from typical vulnerabilities caused by wrong source
code programming or design. Improperly managing pointers, arrays, and API
calls can lead to overflow attacks or other vulnerabilities. A simple example of
possible memory errors is buffer overflow, which allows an attacker to send an
input whose size is larger than required, thus writing data outside bounds and
causing unpredictable behaviours. Exploiting vulnerabilities in native libraries
can affect the functionality of the whole application, leading to some data expo-
sure or, in the worst cases, to the loss of control of the device. For this reason,
it is essential to manage the security of the used libraries when developing an
Android application. Previous research works have only recently pointed out the
need for better native code safety and vulnerability analysis [2].

However, finding and analyzing vulnerabilities is a very time and resource-
consuming task requiring in-depth static and dynamic analysis of the native layer
and its interaction with the Java/Kotlin code [2]. Recent works also showed
several validation problems related to the effective reachability of vulnerable
functions [3]. These issues may discourage analyzing the native layer security in
their apps, thus often overlooking even well-known issues of public products. We
propose a probabilistic approach that vulnerability researchers can use to have
a first basic idea of the vulnerability to be checked manually. Our vulnerability
detection on Android Native Code can be included in the process of producing
and maintaining the Software Bill Of Materials (SBOM), a detailed inventory
of software components and their ingredients essential in software security and
supply chain risk management (as described by the American Cybersecurity
and Infrastructure Security Agency [4]). Different organizations worked on that,
such as NIST [5], who released in February 2022 guidelines to be followed by
developers and companies as a means of cyberattack prevention. In fact, SBOM
has been introduced to provide guidance on the level of risk associated with
the software, whether stand-alone or integrated into systems (such as in the
case of Android Native Code). SBOM defines the most dangerous vulnerabilities
and gives a global risk indication of the software vulnerabilities, stating the
components with a greater likelihood of being affected (as in our methodology).

This paper proposes an alternative strategy for Native Code vulnerability
identification that does not involve resource-heavy analyses but leverages on pub-
lic knowledge of known issues. The idea is to yield a quick, lightweight approach


---

## Page 3

2
Technical Background

2.1
ARM

1 https://androzoo.uni.lu/
2 https://www.arm.com/

Risk Algorithm Native Code Vulnerabilities Android
3

that gives an idea of an application’s possible known risks to take immediate
actions to address them. This is done through a a risk assessment algorithm
that leverages a combination of quick code analysis and public domain knowl-
edge to provide a score of possible dangerousness of the application based on the
vulnerabilities found.

More specifically, our contributions can be summarised as follows: (i) we pro-
pose a minimal complexity Native Code analysis strategy oriented to the search
for known vulnerabilities and issues by leveraging public domain knowledge; (ii)
we define a risk assessment algorithm that provides a dangerousness score that
can aid security researchers to take immediate actions to patch the analysed
applications; (iii) we evaluate our methodology through a large scale analysis on
100, 000 APKs taken from the widespread application repository Androzoo1, but
results are focused on 38, 348 apks which are those using at least one native li-
brary. To the best of our knowledge, no risk assessment algorithm or methodology
has been published for vulnerabilities in the Native Code. The results attained
in this paper demonstrate that a risk-based approach can be strongly beneficial
in swiftly assessing vulnerabilities in Android applications, thus addressing this
problem by working on their early detection and prevention.

The remainder of this paper is structured as follows. Section 2 presents a
technical background about Android applications structure and vulnerabilities.
Previous research is illustrated in Section 3, while the applied methodology is
presented in Section 4. Results are reported in Section 5. Finally, Section
6
discusses the limits and the future works that may be conducted to improve this
work.

Before introducing our methodology, some concepts need a brief explanation to
provide the reader with basic knowledge about the core elements of Android
applications and Native Code.

ARM, the acronym for Advanced RISC Machine2, is the hardware architec-
ture on which Android OS and apps are executed. It is commonly implemented in
embedded systems, where developers design and sell the processor’s architecture
to vendors such as Samsung, Lenovo, and Oppo. ARM is based on RISC (i.e.
Reduced Instruction Set Computer), an architecture with a smaller instruction
set than x86/64 but with more general purpose registers and a load/store mech-
anism. As an example, to modify a value of a register, it is required to move the
value to the register (with the instruction load), make the desired arithmetic
operations, and save it back to memory (with the instruction store).


---

## Page 4

4
F. Author et al.

2.2
Android OS

2.3
Android apps

Regarding arithmetic operations, the architecture reduces branch complex-
ity and number of instructions by supporting conditional execution (less than
equal, greater than equal) and barrel instructions (shift and rotation).
ARM is also useful for implementing co-processors by allowing the execution of
different tasks to different cores of one processor. Hence, the program execution
time is inversely proportional to the number of cores.

The proprietary open-source Android OS [6], published by Google in the early
2000s, is the operating system running on ARM hardware and on which apps are
built. Android mostly features six main layers [7]: (i) Android System Apps,
featuring apps for standard activities (e.g. SMS, calendar, emails); (ii) Java
API framework containing Android APIs to make different software compo-
nents communicate with each other; (iii) Native Libraries and core system
services written in C/C++ to manage activities and interact with physical
device components; (iv) Android Runtime to manage runtime for executing
Android apps since Android 5.0; (v) Hardware Abstraction Layer (HAL),
which is a software-hardware interaction layer that employs specific hardware
interface description language (HIDL), allowing detachment between OS and
drivers (autonomous upgrade); (vi) Linux kernel, based on an upgraded ver-
sion of Linux kernel to such platform.

An interesting characteristic of Android OS is the permission level. In low-
level mode, users and groups can access file systems and specific resources. Con-
versely, permissions are restricted in high-level mode, and apps are installed.

Android applications and framework layers are executed in Android Run-
Time (ART). ART is the runtime system that executes Dalvik Executable for-
mat and Dalvik bytecode. Since Android 5.0 Lollipop, it replaces the Dalvik
Virtual Machine (DVM), a register and Java-based virtual machine designed
to give an efficient abstraction layer to the OS. With the DVM, developers had
to partially compile the app, while the DVM did the other parts at runtime.
Instead, in Android RunTime (ART), Dalvik bytecode is compiled for ARM as-
sembly during installation, and the app can run directly by executing machine
instructions.

As described in the previous paragraph, Android apps [8] work in the Android
application layer, which allows developers to extend OS functionalities without
altering lower levels. To build an Android app, developers write source code
in Java/Kotlin that is compiled to .class files. Then, these are translated to
Dalvik bytecode and compiled to a single .dex file (Dalvik Executable), which
is optimized, loaded, and interpreted by the Dalvik Virtual Machine when the
app is run. Once the app is compiled, it is packed as an .APK file, a sort of zip
archive containing all files needed for its execution, and structured as follows:


---

## Page 5

2.4
Native Libraries

2.5
Common Vulnerability Exposure

Risk Algorithm Native Code Vulnerabilities Android
5

– AndroidManifest.xml, a file containing components and permissions

needed by the app;
– classes.dex containing the assembled source code (i.e. list of classes,

methods, and bytecode);
– res, a directory containing all elements related to the visual presentation;
– assets, a directory containing external resources used by the app while

under execution;
– META-INF, a directory with the files used by the Java platform to interpret

and configure the app;
– lib, a directory containing all platform-dependent native libraries written in

C/C++ and compiled in the different ABIs (Application Binary Interface3)
found in different sub-directories.

Each app is also made of four different active asynchronous component types.
These are the activities, entry points for user interaction; services, general-
purpose entry points to keep the app running in the background; broadcast re-
ceivers, intercommunication activities between the apps and the system; content
providers, whose aim is to allow apps to store and share data in the file system.

As explained before, developers use Native Code to interact with native compo-
nents and hardware. Moreover, developers can use Android NDK (Native De-
veloper Kit [9]) to import third-party native libraries without re-implementing
them. These libraries are typically compiled C/C++ code with two kinds of ex-
tensions: .so, which can be defined as native shared libraries; .a, namely native
static libraries, which are those linked to others.

Once compiled, the libraries are ELF (Executable and Linkable Format)
files like the ones resulting from compiling a C code for Linux. The three most
essential headers are (i) ELF header, with the magic number to recognize the
file format, compilation architecture, version, and information about sections;
(ii) program header to create a process image; (iii) section header containing all
the file’s sections (.bss, .data, .text, etc.).

The analysis of an ELF can be performed with several command line tools
(e.g. readelf and elfdump), reverse engineering software such as IDAPro and
Ghidra, or python libraries like pwntools, which was employed in this work as
explained later in Section 4.

Once a vulnerability is found in any application or hardware, it is often disclosed
in a public dataset following the CVE standard [10] with a name featuring the

3 An application binary interface (ABI) is an interface between the operating system
and its applications. Each ABI is defined in Android by the combination of CPU
and instruction set because each device uses its own.


---

## Page 6

6
F. Author et al.

2.6
Risk Assessment

form CVE-DisclosureYear-ProgressiveNumberForThatYear. Each database en-
try contains the product (i.e. an extensive library known commercially, such as
Libpng or OpenCV), the affected product vendors, the publication date, and a
human-readable description. The latter is very important, as it contains informa-
tion about the vulnerability, such as the name of the vulnerable product (with
the version) and the name of the function that allows the attack to be carried
out. Sometimes, the attack and procedure to patch the vulnerability are also de-
scribed. Each CVE is also quantified with a score according to CVSS (Common
Vulnerability Score System) [11]. The latter defines three metric groups:

- Base Metric, a constant severity value over time and across the user platform.

It is composed of the Exploitability metric, which expresses the ease and
technical levels required to exploit the vulnerability, and the Impact metric
that quantifies the damage due to a successful exploit;
- Temporal Metric, a severity value that considers vulnerability’s changes over

time but is constant across the user platform;
- Environmental Metric, which reflects severity scores depending on the user’s

environment, possibly considering the presence of defence systems and secu-
rity controls to mitigate the consequences of an attack.

At the moment of writing this paper, different vulnerabilities have been pub-
lished for Android: about 6305 vulnerabilities in Android OS by Google, more
than 100 by Samsung, and only 2 for Motorola; only 3 vulnerabilities regarding
Android hardware. Additionally, some vulnerabilities directly concern Android
applications (the majority of them regarding Java management). Notably, vul-
nerabilities in Android Native Code cannot be addressed easily and directly as
the Native Code is mostly embedded in other third-party libraries (see later
sections of this work, particularly in Table 4).

Up to now, there are different public databases containing CVEs, such as
Mitre CVE [12], CVE Details [13], and National Vulnerability Database by NIST
(NVD) [14]. Most public databases about vulnerabilities are derived from Mitre,
but they add some details and more technical information.

In this work, we developed a risk assessment algorithm for vulnerabilities in the
Native Code of Android applications. We now provide a brief introduction to
the topic.

Risk assessment includes a set of techniques and methods to determine the
risk of an asset in a specific scenario. It is not only used in cybersecurity, but
it is a general concept that can be applied to almost every field where unde-
sired events could affect and damage the system. Given a specific scenario and
a potential threat to an asset, we have to evaluate the likelihood of the threat
damaging the asset4 in a quantitative (with numbers and specific metric mea-
sure), semi-quantitative (with numbers without a specific metric measure) or

4 In cybersecurity, the asset is the technical infrastructure we have to protect from
cybercriminals.


---

## Page 7

3
Related Works

Risk Algorithm Native Code Vulnerabilities Android
7

qualitative (with specific terms) way. The threat is often considered a deliberate
attack, depending on the attacker’s capability and the infrastructure protection
mechanisms. The damage, of course, is the loss of infrastructure when the at-
tack is successful. Technically, the risk assessment procedure involves tests such
as penetration tests and simulation attacks where the company assesses the like-
lihood of being attacked. In general, after a risk assessment study, the company
takes countermeasures to improve the protection of the assets. Different stan-
dards have been published about risk assessment, such as ISO 27005:2008 [15]
(the one we used in this work) and NIST 800-30.

Identifying Android Native Code vulnerabilities is one of the emerging research
fields of cybersecurity, and as far as we know, very few works have been published
on this topic. The prominent one is Librarian [2], where the authors studied vul-
nerabilities in the top 200 Android apps downloaded from Google PlayStore from
September 2013 to May 2020. They studied a new algorithm called bin2sim, capa-
ble of extracting 6 features from each ELF in the app. Additionally, by applying
binary similarities techniques, the tool correctly identifies different libraries and
versions, implementing a whitelist approach for vulnerability detection. Despite
the accuracy of this tool, their methodology is very heavy from the point of view
of computational complexity. Moreover, they only say whether the APK and the
native library are vulnerable or not without assigning a risk score. Since it is one
of the most recent works on this topic, we decided to compare our methodology
with their results, as we also based the product selection on their criteria and
considered the ± two years time elapsed to patch a vulnerability. As described
in Section 5.3, we had to find a way to compare our risk score on their dataset
with their result because of the lack of score in their results.

Although the early versions of the CVSS score have not been designed as
a metric for risk estimation, over the years, the metric evolved to provide a
reliable measure to evaluate the impact of vulnerabilities and exploits. One of
the seminal works that pointed out the weaknesses of the previous versions of
CVSS was the paper by Allodi and Massacci [16], who in 2014 criticised the usage
of pure CVSS base score without considering the presence of exploits in the wild
for a given vulnerability. The authors proposed a novel way to include known
attacks by merging CVEs published in NVD and exploits released on exploit-db
(repository of computer software exploits and exploitable vulnerabilities), eits
(black markets exploits), and sym (vulnerabilities exploited in the wild). By
employing this methodology, they could assess the limitations of the CVSS score
first version and reduce the risk sensitivity according to the known exploits
of 45%. The third version of CVSS (v3.1, the one used in this work for the
experimental part) is more consistent. A brand new version has been released
during this writing: CVSS v4.0 reinforces the concept of CVSS as not just a
mere base score, as it considers threats, environments, attack requirements, user


---

## Page 8

8
F. Author et al.

interactions and other metrics focused on a more real CVSS value, as suggested
by Allodi and Massacci.

Other works addressed vulnerability detection. For example, Alves et al. [17]
studied the correlation between software metrics and software vulnerabilities.
The authors claim that metrics exist to identify bad software, which is also harder
to verify and maintain, with unnoticed or inadvertently introduced vulnerabil-
ities. The authors compiled 5750 vulnerabilities from Linux Kernel, Mozilla,
Xen Hypervisor, httpd, and glibc. Analyzing 2875 security patches, they distin-
guished vulnerable and safe functions. The results emphasize early vulnerability
management and the need for developers to use multiple metrics for predict-
ing code vulnerabilities. Even Madeiros et al. [18] addressed this topic with a
study on software metrics useful to detect security vulnerabilities in software
development. They analyzed various software metrics, such as complexity and
coupling metrics, as well as other structural quality indicators, and identified
patterns and correlations indicating the presence of security vulnerabilities. The
authors established a correlation between specific project-level metrics and the
number of vulnerabilities present in the software systems. They also found a
specific group of discriminative metrics different across the software systems but
present in all of them and valuable to distinguish between vulnerable and non-
vulnerable code. The software metrics were identified using a genetics algorithm
and a random forest classifier. Instead, in [19], a method called MVP (Match-
ing Vulnerabilities and Patches) has been presented to detect vulnerabilities
using patch-enhanced vulnerability signatures with low false positive and false
negative rates. This methodology can distinguish between already patched vul-
nerabilities and generate accurate vulnerability and patch signatures to improve
vulnerability detection accuracy. Du et al. developed LEOPARD [20], a framework
in a lightweight approach to help security experts detect potentially vulnerable
functions in a code base without prior knowledge of the known vulnerabilities.
Leopard combines complexity and vulnerability metrics to identify potentially
vulnerable functions, providing a more comprehensive vulnerability assessment.
The vulnerability is detected at all levels of complexity without missing the
low-complex ones. For this purpose, the authors used a binning-and-ranking ap-
proach, where functions are grouped into bins based on complexity metrics and
then ranked within each bin using vulnerability metrics. The framework cov-
ers a substantial portion of vulnerable functions identified while only a fraction
is flagged as potentially vulnerable, outperforming machine learning and static
analysis methods.

Another interesting problem regarding vulnerability detection is reachabil-
ity, i.e., analyzing whether or not a vulnerable function is called in the app
during its execution. Borzachiello et al. proposed DroidReach [3], a tool to
detect reachable APIs using heuristic and symbolic execution. They were able
to represent all possible paths a function may take within the Inter-procedural
Control-Flow Graph (ICFG), whose aim is to encode all paths starting from an
application entry point. Due to the complex methodology introduced in their
work and the high computational complexity, we did not implement it in our


---

## Page 9

Risk Algorithm Native Code Vulnerabilities Android
9

work but considered this case in the risk methodology. Instead, we highlighted
the imported library issue in our work as they did.

Recently, Ruggia et al. [21] developed a new methodology to reverse engi-
neer Android apps, focusing on identifying suspicious patterns related to native
components. They used suspicious tags to train a Machine Learning algorithm
for binary classification. In particular, they developed a static tool that ana-
lyzes the code blocks responsible for suspicious behaviours in detail. This work
demonstrates the use of native code in malicious Android applications so that
the analysis is more complex and the maliciousness is better achieved.

One of the first studies on Android Native Code exploits was proposed in
2013 by Fedler et al. [22]. They introduced different techniques to provide vari-
ous levels of protection against all known local root exploits without affecting the
user experience. Their mitigation reduced the exploitability of Android devices.
In those years, very few Android applications used Native Code, and their ap-
proach was unsuccessful in exploiting and targeting flaws in the Dalvik Virtual
Machine. Nowadays, more applications use Native Code, and Android architec-
ture has changed. It is also worth noting that even popular tools for Android
APKs vulnerability detection, such as MobSF [23] and Qark [24], and SEBAS-
TiAn [25] do not look for vulnerabilities in the Native Code, even if are good
vulnerabilities detection tools.

Fuzzing is another technique to detect vulnerabilities, and recently, it has
also been used in Android Native Code. One of the most popular fuzzers is
AFL++, which has been adapted in Frida mode [26] to interact and fuzz Android
applications: detect the vulnerability in the C/C++ code and also check the
interaction with the Java/Kotlin code. Other tools have been released, such as
Android-AFL [27] and Libfuzzer [28]. All these tools are resource-consuming and
sometimes could be more efficient in detecting. Different works [29] are focusing
on fuzzing Android Native components, but, as far as we know at the moment of
writing this paper, none of them focuses on fuzzing Android application Native
Code.

Android CVE analysis has been studied by Brant et al. in [30] with a focus
on the Android security bulletin within the last six years from 2022. According
to them, to have more secure Android systems, security bulletin updates must be
designed with specific tests and improve code coverage of patched files. Only 13%
of security bulletin updates contain fixed test files for that particular update,
and among these, only 42.8% has full patch coverage. Even if the percentage is
still low, this is an interesting result, meaning that the community is beginning
to address Android security and vulnerability detection.

LibRadar [31] demonstrated that a whitelist approach is inefficient because
package names can be modified in many ways. For this reason, they released a
detection tool based on stable code features that are obfuscation-resilient, such
as APIs, which are also obfuscation-resilient. We tried to use their approach,
but at the time of this writing, the tool was no more accessible. Another inter-
esting approach is the one proposed by Li et al. [32], which identifies libraries
according to reference and inheritance relations between Java classes, methods,


---

## Page 10

10
F. Author et al.

and other app metadata. Notably, a Native Library cannot be identified only
according to Java interaction and inheritance, but specific C code syntaxes must
be considered.

Other works such as GoingNative [33], NativeGuard [34] and AppCage [35] fo-
cused only on the isolation and secure sandboxing of Native Code in Android ap-
plications by running the app in a protected but unrealistic environment. These
methodologies are fundamental but cannot be considered in a real-world scenario
where customized sandboxes are rarely employed. On the contrary, Ndroid [36]
and DroidNative [37] focused on data flow between Java and Native Code and
Native Code control flow patterns, also for malware detection. Finally, AdDe-
tect [38] is a framework for advertisement library detection using semantic analy-
sis with machine learning and hierarchical clustering techniques. The interaction
between Native Code and Java Code is critical and must be considered, even if
we are limited to C code vulnerability detection in our work.

As Section 1 mentions, most of these works feature high time and space
computational complexity. For example, using Machine Learning approaches, an
extensive dataset of samples is needed to train the model correctly, and the fine-
tuning of the model can introduce additional complexities. On the other hand,
the methodologies above in the literature have a good accuracy in the results.
Instead, the methodology we propose in this paper needs very few resources; it
is fast to execute even with a large-scale dataset and does not need any dataset
on which to train the Machine Learning algorithms.

One of the scenarios for which this work has been developed is the SBOM,
as explained in Section 1. This concept has been well explained by Zahan et
al. [39], where they discuss the importance of SBOM in improving cyberse-
curity, highlighting its benefits and challenges. The work has been based on
the Log4Shell vulnerability: a zero-day remote code execution vulnerability dis-
covered in Apache Log4j that significantly impacted software organizations in
December 2021 despite a few months earlier, EO (Executive Order) 14028 [40]
recognized SBOMs as a practice for enhancing software supply chain security,
and NTIA released a report of minimum points to use SBOM in risk reduc-
tion. After the Log4Shell vulnerability, NIST recognized SBOM as one of the
official practices organizations must follow to reduce cyber attacks and listed it
in the first version of the Secure Software Development Framework. Moreover,
the industries following SBOMs were able to identify the Log4Shell vulnerability
rapidly and had a more effective response.

In the work, Zahan et al. highlight the benefits of using SBOMs, which include
risk management, vulnerability detection, supply chain transparency, proactive
management of security risks, and effective response to cyber threats. As part
of EO 14028, SBOMs can improve the nation’s cybersecurity, but it still has to
be standardized in the industry, and some challenges still must be solved, such
as the standardization of data requirements, the enhancement of solid guidelines
and the practitioners’ collaboration.


---

## Page 11

4
Methodology and Implementation Details

4.1
Building a custom CVE Database

5 https://www.nltk.org/

Risk Algorithm Native Code Vulnerabilities Android
11

This section illustrates the methodology used for vulnerability detection in the
Native Code of Android applications. First, we describe the creation of the
purpose-specific database. Then, we detail the library extraction algorithm we
developed to analyze the information from each APK studied. Lastly, the risk
assessment algorithm is fully explained.

Given an APK, we extract the native library from its lib directory. As the
compiled library is an ELF file, we need specific reverse engineering tools and
techniques to extract data for vulnerability detection. Such data is the list of
functions and the product name, along with the version to which the library
belongs. Once we have this information, we can match this result with a database
of known vulnerabilities. The database is purpose-specific, containing for each
CVE a field with the affected vulnerable version and function. At the moment
of this writing, there is no publicly available database for this purpose, and with
this specific structure, a system can easily access and read it.

We need a list of N products to construct the database, which are those
whose vulnerabilities we want to look for in the apps. The product matching
process is a whitelist approach that assumes that none of the Android app’s
developers has changed the library name (keeping the real one employed during
compilation time in the NDK). Once we have a match between the library under
analysis and the database, we can assign a risk assessment score to the CVE
found in the analyzed library. Our purpose is to give a risk value to each library
(according to the risk of each CVE found) and, consequently, to each app to
provide an alarm to developers and security researchers. The following sections
will explain in more detail the methodology.

A CVE database is essential to check if the extracted data from the analyzed
library have been declared in a published vulnerability listing. We decided to
employ a custom database to reduce the query time to a public online database.
Hence, our local database is a dump of data contained in the online selected
website of CVEs (e.g., NVD) and with fields organized according to the aim
of the research. As explained in Section 2.5, the essential information about a
vulnerability is the product’s name with the version and the vulnerable functions
of the library. All this information may be found inside the human-readable
description. It does not follow a specific syntax such as "In product P of version
v.n there is a vulnerable function F.", so we need to employ Natural Language
Processing (NLP) techniques to process the description and extract the valuable
data. Specifically, we employed Python nltk library5, adapting it to our use case
and syntax.

The product name is easily matched with one of the N selected products,
and if one is mentioned inside the description, we know that the CVE has been


---

## Page 12

12
F. Author et al.

In product P before version v.n the F function can be
used for buffer overflow.

In product P version v.n, F function can be used for
attack

In product P version v.n and after, F function can
lead to buffer overflow.

4.2
Library Extraction, Analysis and Association

found in that specific product. This can be further confirmed by searching all
vulnerabilities by product name in the public database.

The version of the library affected by the CVE is always a number that
may come after the word version, the product name, or preceding words with
the meaning of after or before. Some examples are described in Table 1: (i) if
there is a word with the meaning of before (i.e., before, prior, earlier, etc.), every
product version lower than the one found in the description is vulnerable; (ii) if
there is a word with the meaning of after (i.e., after, following, successive) every
product version higher than the one found in the description is vulnerable; (iii)
if no word with the precedents meaning is found, the affected product version is
only the one found in the description.

Table 1. CVE descriptions and corresponding vulnerable product version.

Description
Vulnerable product version

every version <= v.n is vulnerable

version == v.n is vulnerable

every version >= v.n is vulnerable

The last data to extract from the description is the function name. We rely
our strategy on how programmers typically recognize function names and give
names to functions. Then, by looking at some CVE descriptions, we noticed that
the function is never declared as, for example, function F, represented uniquely
by its name. The function name usually contains specific symbols (i.e. _, ::, (),
etc.). Moreover, if the name is made up of more than one word, it is camel-
cased. As an example, makeSum is made up of two words: make and Sum. In
other cases, the function is not found, which means that the whole product
version is vulnerable, but no description of the vulnerable function is provided.

This methodology was developed in iterative steps with manual cross-validation
to check if the algorithm worked correctly.

The overall approach, subdivided into library extraction, analysis, and associa-
tion, is depicted in Figure 1. The presented methodology can be used as it is by
vulnerability researchers and adapted for developers to release a secure Android
application.

Library Extraction is the first step of the analysis part, and, as the name
states, it consists of the extraction of the compiled library (ELF file) from the


---

## Page 13

Libraries 
extraction

Android APK

Risk Algorithm Native Code Vulnerabilities Android
13

.so files

Libraries 
Analysis

Library 
Association

Products linked to

APK
Products

Fig. 1. Workflow of the approach to extract, analyse and associate native libraries,
specifically in the use-case of vulnerability researchers.

Android application. It is done by unzipping .so files from the lib directory
of each APK. Indeed, libraries are compiled according to different ABIs and
saved inside the application. We can choose to extract libraries only for specific
architectures or to analyze libraries for all available ABIs. In this work, we con-
sidered all ELF files from armeabi-v7a directory, and if not available, looked
for arm64-v8a or x86_64 as they represent the most popular architectures.

Library Analysis is the part where we need to extract from the library
the data for vulnerability detection. In particular, we need to know the list of
functions in the library and the product name and the version to which the
library belongs. This step can be done with different reverse-engineering tools,
such as Ghidra and its Python extension for automation. Typically, the product
name and its version can be retrieved in the strings section (.rodata section),
while the defined functions in the ELF file can be retrieved from the Symbol
Table section. In this work, we used pwntools [41], a popular Python framework
for binary analysis and exploitation. Specifically, we employed its ELF module,
which allows the analysis of ELF files from which the strings and the list of
functions are extracted. The version is taken from the result of the strings
Linux utility6. At the same time, the functions are found inside the Symbol
Table of the ELF without considering .got and .plt sections. A difficulty
comes when binaries are stripped7 where not all function names are available,
or the names are unrecognizable.

Library Association is the part where each ELF file is associated with at
least one of the selected N products. This is a crucial task: if we do not link each
ELF file to its related product, we cannot determine if the ELF file contains
vulnerabilities, hence assigning a risk assessment score. Section 3 illustrates that
different works used binary similarities techniques or Machine Learning algo-
rithms; however, we decided to apply a simple identification algorithm because
we know that every product uses a clear and unique syntax in strings and func-

6 strings tool in Linux is capable of retrieving all printable sequences of characters
from the .rodata section of an ELF.
7 A stripped binary is a binary without some debugging symbols and so with a lack
of data.


---

## Page 14

14
F. Author et al.

4.3
Risk Assessment Algorithm

– CRITICAL when the CVE is present and surely exploitable;

tion names. For example, in OpenCV, we can find strings like General Configu-
ration for OpenCV v.n to declare the version and xxxx_cv_xxxx in the function
names. For this reason, if we find these syntaxes in strings and functions, we can
link the analyzed ELF file to a product.

Some binaries can be linked to multiple products due to imported libraries.
Indeed, in a compiled library, there can be traces of the primary library and
the secondary libraries (i.e., the ones employed by the primary). We considered
the ELF files belonging to all the retrieved products in this case, as a proper
distinction between primary and secondary libraries can be hard to carry out in
practice (an issue that has also been highlighted by Borzachiello et al. [3]).

When developers use our methodology, thanks to the library association step,
they can find vulnerabilities in the secondary library (i.e. a library contained in
the main library they are importing in the project as described here above) and
take actions to mitigate them. Developers also use the library extraction and
analysis part as we designed because when importing a third-party native library
in an Android project for apk creation, Android Studio compiles the library, and
to analyse it, developers have to extract and analyse the compiled ELF file as
security analysts do. Instead, when developers want to check if the native library
contains vulnerabilities before importing them into the Android Studio project
to create the application, they can immediately check the database, find a version
with fewer vulnerabilities, and patch them.

We developed a risk assessment algorithm to give a risk value to each library
(and consequently to each app) to provide an alarm to security researchers. Even
though a CVE is present in the analyzed libraries within an ELF, we are not
100% sure that it is exploitable due to stripped binaries, imported products, and
without considering the reachability problem. Moreover, developers can rename
the functions, patch their content or use obfuscation techniques. For this reason,
we can approach the problem in probabilistic terms, and we developed a semi-
quantitative risk assessment algorithm.

According to ISO 27005:2008 [15], the risk can be evaluated as the product
between 3 factors:

risk = threat ∗impact ∗vulnerability
(1)

A threat corresponds to an action that negatively impacts the device. Hence,
the threat factor can be associated with the ease with which an attack can be
carried out. To quantify it, we can use the CVSS exploitability value since it
has a similar definition, regardless of the attacker’s capabilities. The impact
is the damage caused to the system if the vulnerability is exploited. It can be
quantified with the CVSS impact value without considering the architecture of
the victim device.


---

## Page 15

Vulnerability

Threat*Impact

Critical
Medium
High
High
Critical
Critical

High
Medium
Medium
High
High
Critical

Medium
Low
Medium
Medium
High
High

Low
Low
Low
Medium
Medium
High

belong to our N products.

Risk Algorithm Native Code Vulnerabilities Android
15

Table 2. Risk matrix to determine the qualitative risk value.

None
Low
Medium
High
Critical

– HIGH when a vulnerable library is found within the application, but we

are uncertain about the CVE exploitability because the vulnerable API is
not reachable, or we did not find the vulnerable function because the binary
is stripped;
– MEDIUM when we can make the same assumptions of HIGH level for

functions, but we cannot find the vulnerable version due to stripped bina-
ries. Indeed, the library could be vulnerable because developers would be
unaware of the dangers of function if the CVE were released after the app’s
publication. Moreover, apps falling in this category feature a difference be-
tween their release and the CVE publication dates, which are inferior to two
years. According to Librarian [2], two years is the time developers use to ap-
ply a patch and mitigate vulnerability effectiveness after its release. Hence,
within this period, it is very likely that the library would be affected.
– LOW when we cannot state whether the CVE is present. So, we establish a

small level of risk when the found version and functions are not associated
with any CVE;
– NONE when no native library is found, or the analyzed ELF files do not

Our study aims to establish a qualitative value of the risk. To do so, we
have to rescale the semi-quantitative product between threat and impact (in a
range between 0 and 100 as both of them have values between 0 and 10) into
qualitative metrics, as detailed in Table 3. The values have been determined
according to the CVSS 3.1 Qualitative Severity Rating Scale. Then, by applying
the equation 1, we evaluate the risk according to the matrix in Table 2. In this
way, we have a qualitative risk assessment score to assign to each CVE present
in each library of each Android application.

The purpose is to give a risk value to each library (and, consequently, to each
app) and to provide swift alarms to security researchers. Once they are informed
about the risks associated with the library or application, they can find a way
to patch the vulnerability (e.g., upgrade the library to a non-vulnerable version,
fix the library, etc.). To this aim, we assigned the highest score of the CVEs


---

## Page 16

16
F. Author et al.

90 ÷ 100
CRITICAL

89 ÷ 70
HIGH

69 ÷ 40
MEDIUM

39 ÷ 0
LOW

5
Results

5.1
Dataset and products

Table 3. Mapping from semi-quantitative to qualitative values of the product between
threat and impact.

Semi-quantitative value
Qualitative value

risk level to each library but also saved the affected CVEs in a log file. For
example, if we find five CVEs with a LOW level and one with a MEDIUM level,
we assign a MEDIUM risk to the library for a more effective alarm. Another
approach could be evaluating the average risk, giving the most representative
risk: in the previous example, the result should be LOW, but in this way, we
would underestimate the risk, which is far from our purpose. The same weighted
approach has been adopted for the application risk level attribution.

In this Section, we illustrate the results of a large-scale analysis conducted
on 100, 000 APKs from Androzoo. Additionally, to prove the efficiency of our
methodology and risk algorithm and to make a comparison between our ap-
proach and Libriarian [2], we applied the approach to 32 apps from the published
dataset [42] by Almanee et al.

Since the Librarian dataset employs apps released between September 2013
and May 2020, we downloaded the updated versions of such apps (February
2023) and whether the vulnerability risk changed in this amount of time.

To apply the study to a large-scale dataset, we downloaded the first 100, 000
applications found in the Androzoo collection, which is a popular dataset de-
veloped by the University of Luxembourg with about 23 million APKs dumped
from different markets and years, also analyzed by various anti-malware engines.
Among the 100, 000 applications, we selected only 38, 348, which contained na-
tive code (see Supplementary Data for the hash list). In particular, since this
study started in September 2021, we downloaded the samples considering the
list of apps from Androzoo csv.

Additionally, we built a dataset of products, i.e., a set of N popular native
libraries within the downloaded samples. This is a necessary step to associate
each ELF file with at least one product, as expressed in Section 4.2. Due to time


---

## Page 17

OpenCV
Real-time Computer Vision
34
5

OpenSSL
Secure
communication
over
net-
work

FFmpeg
Manage multimedia files (audio-
video)

Libav8
FFmpeg fork to manage multimedia
files

Sqlite 3
Database engine
54
8

LibWebp
Alternative to PNG, JPEG, GIF
14
5

Libpng
Handle PNG images
44
5

Libjpeg-turbo Handle JPEG image format
1
16

Lua
Lua language interaction
15
3

Mono
Create
compatible
tools
with
Framework .NET

Folly
Core library components used by
Facebook

Hermes
Fast startup of React Native apps
20
10

React-Native
Use React framework in applica-
tions

Risk Algorithm Native Code Vulnerabilities Android
17

Table 4. The Table shows the 15 selected products to perform the analysis, a brief
description of their purpose, the number of released CVEs in the last five years, and
the percentage of apps in our dataset that contain these products.

Product
Description
# CVE % Dataset

232
1

407
10

106
5

20
11

3
11

1
77

and space constraints, we selected the most representative libraries within the
38, 384 APKs, considering the number of published vulnerabilities (CVE) for
those libraries and the representativeness within the app chosen inside the large-
scale dataset. So, in a similar fashion to what was made by Almanee et al., [2],
given the 38, 384 APKs we made a list of the native libraries’ names, associated
them to their own products, and computed statistics of the products considering
the number of the published known vulnerabilities and their percentage of diffu-
sion in the dataset (considering the top products to be selected). At the end, we
had a dataset of 15 products: OpenCV, OpenSSL, FFmpeg, Libavcodec,
Libavformat, Libswresample, Sqlite 3, LibWebp, Libpng, Libjpeg-turbo,
Lua, Mono, Folly, Hermes, React-Native.


---

## Page 18

![Figure 1](../assets/Risk (2024) Risk Estimation of Native Code/fig_p18_1.png)

18
F. Author et al.

5.2
Large-scale analysis Results

Out of the 100, 000 downloaded APKs, about 40% of them contained Native
Code. In particular, there are 38, 384 APKs with at least one native library and
a total of 225, 638 ELF files. Among these, 44, 225 belongs to at least one of
our 15 products. Regarding applications with Native Code, by considering only

Fig. 2. The pie chart shows the percentage of apps for which a risk level has been
computed by only identifying 15 products. The NONE value means that the found
Native Code does not belong to any of our 15 selected products, but it can have
vulnerabilities related to other libraries.

the products in the library-identification dataset as defined in Table 4, we could
determine the risk for 55% of them. Hence, about 24, 000 APKs belong to at
least one of our 15 products with a risk level HIGH-MEDIUM as reported in
Figure 2.

We also computed some statistics about the apps’ year of release and belong-
ing market.

Figure 3 shows that the apps released from 2011 to 2021 have a medium risk.
Note that the NONE label does not mean that applications are not vulnera-
ble at all, but that they belong to other products (i.e. no product among the
selected ones is found). Expanding the analyzed products dataset may increase
the number of vulnerable apps.

The market with the most vulnerable applications is Google Play, as depicted
in Figure 4. That is a reasonable result because most apps in the dataset are
retrieved from the Google Play Store (Figure 5). The reason is that Google


---

## Page 19

2500

2000

1500

1000

500

0

2011

2012

2013

2014

2015

5.3
Comparison with Librarian results

Risk Algorithm Native Code Vulnerabilities Android
19

HIGH
MEDIUM
NONE

2016

2017

2018

2019

2020

2021

Fig. 3. This histogram shows the risk level per year on the analyzed apps. Each year
has 2 bars: red/left-bottom bar for HIGH risk, orange/left-upper bar for MEDIUM
risk, and grey/right bar for NONE risk.

Play only limits its checks in understanding if an uploaded application can be
classified as malware without considering vulnerabilities.

To demonstrate our methodology’s effectiveness, we compared our results with
the ones obtained by Almanee et al. [2] by downloading their pubic dataset of
32 APKs [42] built in 2021. We could infer almost the same library identification
results by using the same products for library identification.

While the methodology proposed by Almanee et al. was limited in saying
whether the analyzed app was vulnerable (so only a result yes/no), our approach
gives one of the presented risk levels in Section 4.3, we have to find a way to
compare the results of the two methodologies. Hence, when our methodology
gives a level to an application to which the other approach says is vulnerable,
we gave the Librarian results in the same risk level set by our algorithm. On
the other hand, when our methodology gives a level to an application, but the
approach of Amanee et al. says it is not vulnerable, we gave the value of 0 to
the Librarian results. First of all, we infer the same results as the Librarian did
for all applications, except for one which we detected as MEDIUM risk, but the
Librarian says it has no vulnerabilities. From the results, we can affirm that
47% of the apps have a HIGH risk level, 41% MEDIUM risk level, and 12% of
the apps do not have vulnerable Native Code libraries (i.e., their products do
not belong to our or Librarian dataset of products; the products do not contain
CVEs).

8 In our dataset libav consists of three libraries (i.e. Libavcodec, Libavformat,
Libswresample) to code/decode, multiplex/demultiplex, and resample audio, and
video.


---

## Page 20

![Figure 2](../assets/Risk (2024) Risk Estimation of Native Code/fig_p20_2.png)

![Figure 3](../assets/Risk (2024) Risk Estimation of Native Code/fig_p20_3.png)

20
F. Author et al.

5.4
Comparison with updated Librarian dataset

Fig. 4. The histograms show the vulnerability risk levels (HIGH: red/left bar;
MEDIUM: orange/central bar; NONE: grey/right bar) of the apps by markets. On
the left, we plotted the main markets. On the right, we can see a detail of all markets
except the Google Play Store.

The last experiment we performed was on the last version of the Librarian apps,
downloaded on February 2023, used as a dataset to check whether the risk
changed. As Figure 6 shows, We can state that for the 55% of the apps, the
risk was reduced; for the 10% of them, the risk remained constant, and for the
2% of them, it increased. The null results are caused by Native Code that does
not belong to any of the selected 15 products.

As seen in Figure 2, the selected 15 products are still insufficient to scan
all apps, even though they are the most popular. Moreover, Facebook, Insta-
gram, Messenger, and WhatsApp use Native Code developed by Meta instead
of importing third parties as in the Librarian’s version.

From the graph in Figure 3, we have seen that the risk reduces over time,
which is expected if we consider that various vulnerabilities have been addressed
over the years. However, it is also interesting that the risk for various apps has
not changed over time, questioning the quality of vulnerability addressing in
popular applications.


---

## Page 21

107
Androzoo apps
Our dataset apps

106

105

104

103

102

101

100

appchina

fdroid

anzhi

GooglePlay

apk_bang

VirusShare

1mobile

angeeks

freewarelovers

6
Summary, Limitations and Future Works

Risk Algorithm Native Code Vulnerabilities Android
21

proandroid

praguard

unknown

hiapk

mi.com

torrents

genome

slideme

Fig. 5. The histogram compares the number of apps for each market in the Androzoo
dataset (green/left bar) and the apps used for vulnerability detection in our dataset
(blue/right bar).

In this work, we proposed a simple and fast approach for vulnerability detection
in Android Native Code by developing the first database of CVEs for vulner-
ability detection by easily accessing the vulnerable version of each app and its
vulnerable functions. We combined this with developing a risk assessment algo-
rithm for vulnerability management.

We demonstrated that even a simple approach like ours is efficient for vulner-
able library identification, as we have been able to reproduce the same results as
previous works by highlighting vulnerable applications on a much larger scale.
Our methodology can aid developers and security researchers mitigate immedi-
ate risks by recommending fine-grained application patching, thus allowing them
to release more secure Android applications in the different Android markets.

However, our methodology does not consider issues such as reachability to
determine if vulnerable functions are accessible in apps and stripped binaries
to assess the presence of the vulnerable function’s name in the binary. In fact,
our solution gives security researchers and developers a risk score so they can
manually check the vulnerability. To better score the functions’ reachability, se-
curity researchers can refer to other tools such as DroidReach [3]. Additionally,
we do not check whether or not the vulnerable library has been patched. Indeed,
even though the analyzed ELF file matches a vulnerable version or the function
name, developers may have patched the function’s body, for which binary sim-
ilarities techniques must be used. Developers can also rename the functions or
obfuscate their name (as well as the content). For these cases, our whitelist ap-
proach is insufficient to determine the risk and match if the found function is in
the vulnerability database. All these issues can be addressed in future research
works.


---

## Page 22

22
F. Author et al.

HIGH

MEDIUM

NONE

amazon_alexa

alibaba

facebook

calm

adobe

chase

apple_music

framy

fitbit

camerasideas

7
Competing interests

The authors declare no competing interest.

8
Acknowledgments

References

Original Risk
Risk in 2023

snapchat

zoom

whatsapp

instagram

shein

kindle

tiktok

uber

starmakerinteractive

messenger

Fig. 6. The histogram shows the risk level for the librarian apps (left/olive green bar)
and the version on February 2023 (right/coral bar).

In the future, we plan to address these issues by extending the product
dataset and including as many libraries as possible to check how the risk changes.
Concerning library identification, we plan to extract unique functions from each
version of the products and use them as features for Machine Learning algo-
rithms.

This work was carried out while Silvia Lucia Sanna was enrolled in the Ital-
ian National Doctorate on Artificial Intelligence run by Sapienza University of
Rome in collaboration with the University of Cagliari. This work was partially
supported by project SERICS (PE00000014) under the NRRP MUR program
funded by the EU - NGEU.

1. StatCounter-GlobalStats. Mobile operating system market share worldwide. Stat-
Counter. Online accessed.
2. Sumaya Almanee, Arda Ünal, Mathias Payer, and Joshua Garcia. Too quiet in the
library: An empirical study of security updates in android apps’ native code. In
2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE),
pages 1347–1359, 2021.


---

## Page 23

Risk Algorithm Native Code Vulnerabilities Android
23

3. Luca Borzacchiello, Emilio Coppa, Davide Maiorca, Andrea Columbu, Camil
Demetrescu, and Giorgio Giacinto. Reach me if you can: On native vulnerability
reachability in android apps. In Vijayalakshmi Atluri, Roberto Di Pietro, Chris-
tian D. Jensen, and Weizhi Meng, editors, Computer Security – ESORICS 2022,
pages 701–722, Cham, 2022. Springer Nature Switzerland.
4. Software bill of materials. Online accessed: https://www.cisa.gov/sbom.
5. Secure
software
development
framework.
Online
accessed:
https://csrc.nist.gov/projects/ssdf#ssdf-practices.
6. Android operating system. Online accessed: https://source.android.com/.
7. Android
platform
architecture.
Online
accessed:
https://developer.android.com/guide/platform.
8. Android
platform
architecture.
Online
accessed:
https://developer.android.com/guide/topics/manifest/manifest-intro.
9. Android ndk. Online accessed: https://developer.android.com/ndk/guides.
10. Common
vulnerability
and
exposure
(cve).
Online
accessed:
https://www.cve.org/About/Overview.
11. Common
vulnerability
scoring
system
(cvss).
Online
accessed:
https://www.first.org/cvss/v3.1/user-guide.
12. Mitre cve. Online accessed: https://cve.mitre.org/.
13. Cve details. Online accessed: https://www.cvedetails.com/.
14. National vulnerability database from nist. Online accessed: https://nvd.nist.gov/.
15. Iso/iec
27005:2008
information
technology
—
security
techniques
—
information
security
risk
management.
Online
accessed:
https://www.iso.org/standard/42107.html.
16. Luca Allodi and Fabio Massacci. Comparing vulnerability severity and exploits
using case-control studies. ACM Trans. Inf. Syst. Secur., 17(1), aug 2014.
17. Henrique Alves, Baldoino Fonseca dos Santos Neto, and Nuno Antunes. Software
metrics and security vulnerabilities: Dataset and exploratory study.
2016 12th
European Dependable Computing Conference (EDCC), pages 37–44, 2016.
18. Nádia Medeiros, Naghmeh Ramezani Ivaki, Pedro Costa, and Marco Paulo Amorim
Vieira. Software metrics as indicators of security vulnerabilities. 2017 IEEE 28th
International Symposium on Software Reliability Engineering (ISSRE), pages 216–
227, 2017.
19. Yang Xiao, Bihuan Chen, Chendong Yu, Zhengzi Xu, Zimu Yuan, Feng Li,
Binghong Liu, Yang Liu, Wei Huo, Wei Zou, and Wenchang Shi. MVP: Detecting
vulnerabilities using Patch-Enhanced vulnerability signatures. In 29th USENIX
Security Symposium (USENIX Security 20), pages 1165–1182. USENIX Associa-
tion, August 2020.
20. Xiaoning Du, Bihuan Chen, Yuekang Li, Jianmin Guo, Yaqin Zhou, Yang Liu,
and Yu Jiang. Leopard: Identifying vulnerable code for vulnerability assessment
through program metrics. In 2019 IEEE/ACM 41st International Conference on
Software Engineering (ICSE), pages 60–71, 2019.
21. Antonio Ruggia, Andrea Possemato, Savino Dambra, Alessio Merlo, Simone Aonzo,
and Davide Balzarotti. The dark side of native code on android. TechRxiv, 2022.
22. Rafael Fedler, Marcel Kulicke, and Julian Schütte. Native code execution control
for attack mitigation on android. In Proceedings of the Third ACM Workshop on
Security and Privacy in Smartphones & Mobile Devices, SPSM ’13, page 15–20,
New York, NY, USA, 2013. Association for Computing Machinery.
23. Mobile
security
framework
(mobsf).
Available
online:
https://github.com/MobSF/Mobile-Security-Framework-MobSF.


---

## Page 24

24
F. Author et al.

24. Quick
android
review
kit
(qark).
Available
online:
https://github.com/linkedin/qark.
25. Francesco Pagano, Andrea Romdhana, Davide Caputo, Luca Verderame, and
Alessio Merlo. Sebastian: A static and extensible black-box application security
testing tool for ios and android applications. SoftwareX, 23:101448, 2023.
26. Android
greybox
fuzzing
with
afl++
frida
mode.
Available
online:
https://blog.quarkslab.com/android-greybox-fuzzing-with-afl-frida-mode.html.
27. android-afl.
Available
online:
https://github.com/ele7enxxh/andr
oid-
afl/blob/master/README.md.
28. Fuzzing with libfuzzer. Available online: https://source.android.com/docs/secur
ity/test/libfuzzer.
29. Baozheng Liu, Chao Zhang, Guang Gong, Yishun Zeng, Haifeng Ruan, and Jianwei
Zhuge.
FANS: Fuzzing android native system services via automated interface
analysis. In 29th USENIX Security Symposium (USENIX Security 20), pages 307–
323. USENIX Association, August 2020.
30. Christopher D. Brant and Tuba Yavuz. A study on the testing of android security
patches.
In 2022 IEEE Conference on Communications and Network Security
(CNS), pages 217–225, 2022.
31. Ziang Ma, Haoyu Wang, Yao Guo, and Xiangqun Chen. Libradar: Fast and accu-
rate detection of third-party libraries in android apps. In 2016 IEEE/ACM 38th
International Conference on Software Engineering Companion (ICSE-C), pages
653–656, 2016.
32. Menghao Li, Wei Wang, Pei Wang, Shuai Wang, Dinghao Wu, Jian Liu, Rui Xue,
and Wei Huo. Libd: Scalable and precise third-party library detection in android
markets. In 2017 IEEE/ACM 39th International Conference on Software Engi-
neering (ICSE), pages 335–346, 2017.
33. Vitor Monte Afonso, Paulo Lício de Geus, Antonio Bianchi, Yanick Fratantonio,
Christopher Krügel, Giovanni Vigna, Adam Doupé, and Mario Polino. Going na-
tive: Using a large-scale analysis of android apps to create a practical native-code
sandboxing policy. In Network and Distributed System Security Symposium, 2016.
34. Mengtao Sun and Gang Tan. Nativeguard: Protecting android applications from
third-party native libraries. WiSec ’14, page 165–176, New York, NY, USA, 2014.
Association for Computing Machinery.
35. Yajin Zhou, Kunal Patel, Lei Wu, Zhi Wang, and Xuxian Jiang. Hybrid user-level
sandboxing of third-party android apps. ASIA CCS ’15, page 19–30, New York,
NY, USA, 2015. Association for Computing Machinery.
36. Lei Xue, Chenxiong Qian, Hao Zhou, Xiapu Luo, Yajin Zhou, Yuru Shao, and
Alvin T.S. Chan.
Ndroid: Toward tracking information flows across multiple
android contexts.
IEEE Transactions on Information Forensics and Security,
14(3):814–828, 2019.
37. Shahid Alam, Zhengyang Qu, Ryan D. Riley, Yan Chen, and Vaibhav Rastogi.
Droidnative: Semantic-based detection of android native code malware. CoRR,
abs/1602.04693, 2016.
38. Annamalai Narayanan, Lihui Chen, and Chee Keong Chan. Addetect: Automated
detection of android ad libraries using semantic analysis.
In 2014 IEEE Ninth
International Conference on Intelligent Sensors, Sensor Networks and Information
Processing (ISSNIP), pages 1–6, 2014.
39. Nusrat Zahan, Elizabeth Lin, Mahzabin Tamanna, William Enck, and Laurie
Williams. Software bills of materials are required. are we there yet? IEEE Se-
curity & Privacy, 21(2):82–88, 2023.


---

## Page 25

Risk Algorithm Native Code Vulnerabilities Android
25

40. NIST.
Executive order 14028, improving the nation’s cybersecurity.
Avail-
able
online:
https://www.nist.gov/itl/executive-order-14028-improving-nations-
cybersecurity.
41. Pwntools. Online accessed: http://docs.pwntools.com/en/latest/.
42. Librarian
github
repository.
Available
online:
https://github.com/salmanee/Librarian.


---

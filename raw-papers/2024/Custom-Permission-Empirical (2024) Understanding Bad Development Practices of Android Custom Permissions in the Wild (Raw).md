---
title: "Understanding the Bad Development Practices of Android Custom Permissions in the Wild"
author: "Xiaohan ZHANG, Zhiyuan YU, Xinghua LI, Cen ZHANG, Cong SUN, Ning ZHANG, and Robert H. DENG"
pages: 18
---

# Understanding the Bad Development Practices of Android Custom Permissions in the Wild

## Page 1

![Figure 1](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p1_1.png)

Singapore Management University 
Singapore Management University 
Institutional Knowledge at Singapore Management University 
Institutional Knowledge at Singapore Management University

Research Collection School Of Computing and 
Information Systems 
School of Computing and Information Systems

7-2025

Xiaohan ZHANG 
Xidian University

Zhiyuan YU 
Washington University in St. Louis

Xinghua LI 
Xidian University

Cen ZHANG 
Nanyang Technological University

Cong SUN 
Xidian University

See next page for additional authors

Follow this and additional works at: https://ink.library.smu.edu.sg/sis_research

Part of the Information Security Commons

Understanding the bad development practices of Android custom 
Understanding the bad development practices of Android custom 
permissions in the wild 
permissions in the wild

Citation 
Citation 
ZHANG, Xiaohan; YU, Zhiyuan; LI, Xinghua; ZHANG, Cen; SUN, Cong; ZHANG, Ning; and DENG, Robert H.. 
Understanding the bad development practices of Android custom permissions in the wild. (2025). IEEE 
Transactions on Dependable and Secure Computing. 22, (4), 3208-3223. 
Available at:
Available at: https://ink.library.smu.edu.sg/sis_research/10452

This Journal Article is brought to you for free and open access by the School of Computing and Information 
Systems at Institutional Knowledge at Singapore Management University. It has been accepted for inclusion in 
Research Collection School Of Computing and Information Systems by an authorized administrator of Institutional 
Knowledge at Singapore Management University. For more information, please email cherylds@smu.edu.sg.


---

## Page 2

Author 
Author 
Xiaohan ZHANG, Zhiyuan YU, Xinghua LI, Cen ZHANG, Cong SUN, Ning ZHANG, and Robert H. DENG

This journal article is available at Institutional Knowledge at Singapore Management University:

https://ink.library.smu.edu.sg/sis_research/10452


---

## Page 3

![Figure 2](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p3_2.jpeg)

IEEE TRANSACTIONS ON DEPENDABLE AND SECURE COMPUTING, VOL. 22, NO. 4, JULY/AUGUST 2025, pp. 3208-3223. DOI: 10.1109/TDSC.2024.3525049

Understanding the Bad Development Practices of

Android Custom Permissions in the Wild

Xiaohan Zhang
, Student Member, IEEE, Zhiyuan Yu
, Student Member, IEEE, Xinghua Li
, Member, IEEE,
Cen Zhang
, Cong Sun
, Member, IEEE, Ning Zhang
, Member, IEEE, and Robert H. Deng
, Fellow, IEEE

Abstract—Android system provides application developers with
the ability to deﬁne custom permissions, which serve to moderate
the sharing of resources and interactions with other applications.
However, poor development practices of developers can render
the permission mechanism ineffective, weakening the system pro-
tection. This paper presents a comprehensive examination of the
problematic practices surrounding custom permissions employed
by developers, referred to as Bad Practices of Custom Permissions
(BPCP issues). To accomplish this, we conducted an empirical
study and identiﬁed nine common BPCP issue patterns that can
lead to various adverse consequences, such as installation failures,
crashes, or even component hijacking. To automatically identify
these patterns of bad practices, we devised PERMEAGRE, a static
analysis tool. Using PERMEAGRE, we performed a large-scale
analysis of 83,085 applications obtained from seven major app
markets, aiming to detect instances of BPCP issues. The results
revealed that more than 26% of the analyzed apps contained at least
one issue, and a signiﬁcant number of apps had garnered millions
of downloads. Drawing from the empirical results, we further
systemize the underlying root causes of these issues. Consequently,
this analysis sheds light on the potential threat landscape associated
with bad practices in custom permissions, emphasizing the urgent
requirement for effective mitigation strategies.

Index Terms—Android, custom permission, static analysis,
empirical study.

I. INTRODUCTION
T

HE Android operating system holds a prominent position
as the most widely used mobile platform globally, employ-
ing an Inter-Process Communication (IPC) mechanism to facil-
itate inter-application communication. However, vulnerabilities

Received 23 May 2023; revised 8 May 2024; accepted 29 December 2024.
Date of publication 6 January 2025; date of current version 11 July 2025. This
work was supported by the National Natural ScienceFoundation of China under
Grant 62125205, Grant U23A20303, in part by the Key Research and Devel-
opment Program of Shaanxi under Grant 2023KXJ-190 and Grant 2024GX-
YBXM-072, and in part by the 111 Center under Grant B16037. The work of
Ning Zhang was supported by Washington University. (Corresponding author:
Xinghua Li.)

Xiaohan Zhang, Xinghua Li, and Cong Sun are with the State Key Laboratory
of Integrated Service Networks and School of Cyber Engineering, Xidian
University, Xi’an 710071, China, and also with the Engineering Research
Center of Big data Security, Ministry of Education, Xi’an 710071, China
(e-mail: zhangxh@stu.xidian.edu.cn; xhli1@mail.xidian.edu.cn; suncong@
xidian.edu.cn).

Zhiyuan Yu and Ning Zhang are with the Department of Computer Science
and Engineering, Washington University in St. Louis, St. Louis, MO 63130 USA
(e-mail: yu.zhiyuan@wustl.edu; zhang.ning@wustl.edu).

Cen Zhang is with the Nanyang Technological University, Singapore 639798
(e-mail: cen001@e.ntu.edu.sg).

Robert H. Deng is with the Singapore Management University, Singapore
188065 (e-mail: robertdeng@smu.edu.sg).
Digital Object Identiﬁer 10.1109/TDSC.2024.3525049

Fig. 1.
Motivating example.

in this mechanism can lead to the exploitation, undermining
user privacy and security [8], [13], [20], [25], [26], [29]. In
order to mitigate this threat and enable the implementation
of customizable security measures, custom permissions have
been introduced to regulate the sharing of resources and ca-
pabilities among applications. This approach ensures that only
applications meeting the speciﬁed permission requirements are
permitted to engage in such interactions, thereby bolstering the
security of IPC mechanisms.

However, inexperienced developers may encounter chal-
lenges in properly utilizing the custom permission mechanism,
which requires its appropriate declaration, request, veriﬁcation,
and utilization. A search on the Stack Overﬂow website, with
the keyword “Android custom permission”, yields nearly 2,000
questions, illustrating the difﬁculties faced by developers in cor-
rectly implementing custom permission functionality. To ensure
the security and availability of applications, it is crucial to adhere
to the correct usage of custom permissions and follow the best
practices recommended by Google. Otherwise, the adoption
of poor development practices pertaining to custom permis-
sions (referred to as BPCP issues) can render the meticulously
designed protection, making it susceptible to exploitation by
attackers.

During our empirical study, we encountered an illustrative
example of a BPCP issue, as depicted in Fig. 1. This speciﬁc in-
stance was reported on the HackerOne bug bounty platform [4].
The affected application in question is an email application
that maintains a contact database. In its AndroidManifest con-
ﬁguration ﬁle, the “write_contacts” permission is designated
with a “dangerous” protection level, necessitating explicit user


---

## Page 4

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

authorization for any external application attempting to access
the contact resources. However, due to a developer’s error, the
protection permission for the database component was erro-
neously declared as “write” instead of “write_contacts”. Since
the “write” permission is unclaimed, an attacker can deﬁne and
request this permission, subsequently gaining ownership and
acquiring access to the component. This allows the injection
of arbitrary data into the contact database without the user’s
awareness. This example underscores the severe consequences
that can arise from BPCP issues.

Existing Work: Despite the signiﬁcant security and privacy
threats posed by these issues, research in this area has been lim-
ited. Prior studies have focused primarily on identifying design
ﬂaws within the Android custom permission mechanism [3],
[7], [22], [32], rather than examining the introduction of bad
practices by developers. For instance, Tuncay et al. identiﬁed
two vulnerabilities resulting from a lack of separation of trust
between system and custom permissions, enabling unauthorized
access to platform resources [32].

Although some studies have analyzed the improper practices
of custom permissions from the developer’s standpoint, Man-
ifestInspector [18] and Mist [38], which explored mistakes in
manifest conﬁgurations and the exposure of activities, as well
as the works of Wang et al. [36] and Fang et al. [12], which
examined mishandling of runtime permission requests and re-
vocations, these investigations focused solely on speciﬁc types
of issues and did not conduct a comprehensive and systematic
examinationofdevelopers’widespreadbadpracticesthroughout
the entire development stage of custom permissions. As we will
demonstrate later, the issues uncovered in these studies represent
just the tip of the iceberg, revealing a larger underlying problem.

Our Contributions. To bridge the gap, we conducted a com-
prehensive investigation on the improper development practices
ofAndroidcustompermissionsbydevelopers.Ourcontributions
to this ﬁeld can be summarised as follows:

1) Systematic Study and Classiﬁcation: We performed an
empirical study utilizing publicly available vulnerability
reports from the bug bounty platform HackerOne and
questions from Stack Overﬂow. Employing an open cod-
ing procedure, we established a taxonomy encompassing
9 distinct patterns of BPCP issues. These patterns span
the entire development process associated with the use of
the custom permission mechanism and have the potential
to result in severe consequences, including installation
failures,informationleaks,andevencomponenthijacking.
2) Tool Design and Implementation: Building upon these
patterns, we developed PERMEAGRE, a static analysis
tool capable of automatically detecting each type of BPCP
issue pattern. PERMEAGRE has been meticulously de-
signed to avoid repetitive analyses for each BPCP issue
pattern within the target program.1 It effectively employs a
relational database to store pertinent information, encom-
passing static and dynamic declaration details, and con-
verts the detection process into efﬁcient database queries.

1PERMEAGRE
is
openly
available
at:
https://github.com/Han0nly/
PERMEAGRE

Static declaration information is derived from the analysis
of the manifest ﬁle, while dynamic declaration informa-
tion is obtained through optimized backward slicing.
3) Large-Scale Analysis: In order to facilitate a more compre-
hensive examination of real-world applications, we con-
ducted a large-scale analysis, encompassing over 83,000
apps obtained from seven app markets, including Google
Play. Leveraging PERMEAGRE, we systematically iden-
tiﬁed BPCP issues at scale. Our ﬁndings indicate that over
26% of these apps exhibit at least one instance of a BPCP
issue, and a signiﬁcant number of these apps are popular,
boasting millions of downloads.
4) In-depth Reasoning and Suggestions: Our investigation
also delved into the underlying causes of these issues
from the perspective of developers. Our ﬁndings indicate
that many of these issues stem from typographical errors
made by developers. Additionally, we observed that a
notable portion of BPCP issues arise due to the utilization
of third-party libraries, further compounded by a lack of
understanding on the part of app developers. To address
these concerns, we provide recommendations for all stake-
holders involved in the ecosystem, aiming to mitigate the
risks associated with such vulnerabilities.

II. BACKGROUND

A. Android Permission

The Android permission system serves as a fundamental
protective mechanism for sensitive APIs and resources. These
permissions must be granted to applications before they can ac-
cess the associated resources. Each permission is accompanied
by a corresponding protection level, determined by its severity.2

The protection levels are primarily classiﬁed as follows:
r Normal permissions are automatically granted during the

installation process.
r Signature permissions are automatically granted during

installation if the requesting application is signed by the
same developer as the app that deﬁnes the permission.
r Dangerous permissions are granted by the user during

installation or at run-time, depending on the version of the
system.
Android offers a set of system permissions to protect user
assets. Additionally, apps have the ability to deﬁne their own
permissions, called custom permissions, which restrict other
apps’ access to their resources. Custom permissions must be
declared within the app’s AndroidManifest.xml ﬁle, which is
an XML conﬁguration ﬁle containing essential information, in-
cluding component and permission declarations, for the Android
operating system. The protection level for custom permissions
must be speciﬁed during their deﬁnition. An example of a
custom permission declaration is illustrated in Fig. 2. Line 3
deﬁnes a custom permission named “com.example.pe” using
the <permission> element. To use custom permission, an appli-
cation must request it through the <uses-permission> element
within its manifest ﬁle. It is important to note that the deﬁned

2https://developer.android.com/guide/topics/manifest/permission-element


---

## Page 5

Fig. 2.
IPC example.

permission name cannot be identical to an existing permission
on the same device, unless both apps are signed with the same
certiﬁcate.

B. Inter-Process Communication

In Android systems, Inter-Process Communication (IPC)
plays a crucial role in achieving reusability. In this section,
we provide a detailed explanation of how IPC is designed and
protected on Android.

App Components: Android applications are made up of four
major components: Activity, Service, Broadcast Receiver and
Content Provider, each serving different purposes. These com-
ponents can interact with each other using “Intents”. An Intent
is a data structure that speciﬁes a recipient and can optionally
include data. In this study, we refer to the app that exports its
component(s) as the provider app, and the app that interacts
with the exported component(s) as the invoker app.

IPC Process Example: Fig. 2 demonstrates a typical IPC
process. On line 6 in the AndroidManifest ﬁle, an activity
named “com.example.app.act” is declared. The developer sets
the element “android:exported” to “true” to allow inter-app
communication; otherwise, it can only receive intents initiated
within the same app.

The invoker can send an intent to the provider in an explicit or
implicit manner. As shown in lines 16 and 17, an explicit intent
speciﬁes the target application and component of the intent. On
the other hand, an implicit intent aims to perform an action (lines
19-20) and delivers the intent to any application that claims to
handle such an action. The provider can specify the actions it
can handle using the “intent-ﬁlter” element (lines 7-9).

IPC Security: Developers can utilize the custom per-
mission mechanism to restrict access to their components.
When two components communicate, both the caller and the
callee can require the other party to hold speciﬁc permis-
sions for successful communication. For example, the activity

“com.example.app.act” in Fig. 1 is protected by a custom per-
mission named “com.example.app.pe” (line 6). Invokers need
to declare (line 13) and request permission (if the permission is
dangerous) beforesendingintents. Boththird-partyappdevelop-
ers and the system rely on the correct implementation of custom
permissions for security purposes, emphasizing the paramount
importance of ensuring the security of custom permissions.

C. Problem Signiﬁcance

1) Consequences of BPCP Issues: The custom permission
mechanism is designed to protect components and intents
against unauthorized access or interception. Both the provider
and the invoker can face signiﬁcant consequences resulting
from BPCP issues [8]. Provider BPCP issues can compromise
the protective capabilities of the permission mechanism for
components, enabling attackers to carry out unauthorized com-
ponent access, such as malicious broadcast injection, activity
hijacking and service hijacking, through a malicious application.
Similarly, invoker BPCP issues can lead to the interception of
intents by unauthorized receivers, resulting in broadcast theft,
activity hijacking, and service hijacking.

2) Researchers’ Perspective: In recent years, several studies
have analyzed some developers’ mistakes related to Android
custom permissions, focusing on two main aspects of the prob-
lem. To highlight the signiﬁcance of the problem, we provide a
brief overview of these existing studies below. A more detailed
comparison between our work and existing studies can be found
in the related work section (Section III).

Mistakes in manifest ﬁles: Some work has examined errors
in manifest ﬁles and the associated security risks, including
those related to custom permissions. Jha et al. explored devel-
oper mistakes in the AndroidManifest.xml ﬁles by manually
extracting rules from the documentation [18]. They discovered
that developers often make errors when writing manifest ﬁles,
and some of these errors lead to crashes, uninstallations, and
even security vulnerabilities. Yang et al. used Natural Language
Processing (NLP) techniques to extract manifest constraints
from ofﬁcial documentation and validated manifest ﬁles against
these rules to detect misconﬁgurations [39].

Mistakes in runtime permission management: Some studies
have focused on developers’ errors in runtime permission man-
agement [12], [36]. Fang et al. demonstrated the challenges
developers face in handling dynamic permission revocations
by users. They found that more than 70% of the applications
analyzed do not adequately handle exceptions caused by per-
mission revocations, leading to crashes or malfunctions. Wang
et al. conducted systematic research on runtime permission is-
sues, investigating their root causes, prevalence, and remediation
strategies [36]. Runtime permission management also plays a
vital role in the use of custom permissions. Managing custom
permissions at runtime requires not only considering explicit
revocations by users but also addressing implicit revocations
resulting from app removal. Consequently, managing custom
permissions becomes more complex and challenging to imple-
ment correctly.


---

## Page 6

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

TABLE I
COMPARISON BETWEEN OUR WORK AND STATE-OF-THE-ART WORKS

III. RELATED WORK

A. Security of Android Custom Permissions

Most of the existing security research on custom permissions
focuses on the ﬂaws of the Android system itself [22], [29],
[32]. For example, Tuncay et al. [32] present two new classes
of vulnerabilities caused by insufﬁcient isolation of system
permissions and custom permissions, through which an attacker
can utilize custom permissions to obtain unauthorized access to
systemresources. Reardonet al.[29] present covert channels and
side channels that can circumvent Android’s permission model
and gain access to protected data without user consent. Li et
al. [22] found a series of design ﬂaws in the Android permission
framework using fuzzing. All these design ﬂaws are ﬁxed in
different Android versions. Different from these works, our
work analyzes not the design ﬂaws of the Android permission
mechanism but the bad development practices committed by
developers. Developers can only get security guarantees when
using permissions mechanisms correctly, and bad practices will
cause the protection invalid or be bypassed.

The works that are closest to ours are [10], [12], [18], [35],
[36], [38]. Some works studied the developer’s mistakes when
using the Android permission mechanism, some issues can also
be mapped to custom permission. For example, Jha et al. ana-
lyzed the mistakes committed by developers in writing Android
apps, which only focus on manifest-related errors [18]. Yan et
al. [38] performed an empirical study on the misexported activ-
ities and proposed a decision tool to help developers to decide
whether a component should be exported. Wang et al. [36] and
Fang et al. [12] studied the issue of the developers’ mishandling
of runtime permission requests and revocation. Though these
prior studies like ManifestInspector [18] and ManiScope [39]
that address some aspects of bad development practices with
Android custom permissions, our study indeed presents sev-
eral unique contributions that enhance the existing body of
knowledge, as shown in Table I. First, our work advances prior
research by offering a thorough analysis of both bad practices
and dynamic behaviors, surpassing existing works that focus
mainly on manifest misconﬁgurations. Moreover, we introduce
a systematic classiﬁcation of BPCP issues, enhancing both un-
derstanding and practical application in software development.

B. IPC Security in Android

Previous work has demonstrated numerous ways of exploiting
IPC to obtain access to unauthorized resources. Felt et al. [13]
discuss the permission re-delegation vulnerability, which allows
anunauthorizedapptoaccesssensitivesystemresourcesthrough
an authorized app via IPC. Additionally, Chin et al. [8] analyze a
variety of ways of exploiting the IPC mechanism to compromise
user privacy and security, including intent snifﬁng, hijacking,
etc.

There are also a number of works that have designed auto-
mated detection methods to detect these IPC-related vulnerabil-
ities [5], [16], [19], [20], [21], [24], [27], [28], [31], [37]. Bosu
et al. [6] conduct the ﬁrst large-scale detection of malicious
apps that utilize IPCs for privilege escalation and collusive
information leakage. Lu et al. [25] propose a static analysis
method to detect component hijacking vulnerabilities inside
Android apps. Gamba et al. [15] researched the custom per-
mission misuse of pre-installed applications, including exposing
sensitive resources or leaking privacy information.

Different from all these works detecting the pairwise in-
formation ﬂow between components, our work aims to detect
developers’ bad practices of custom permissions, which do not
generate paired information ﬂows in most cases.

C. Malware Detection

Numerous studies have utilized permissions and intents as
features for malware detection in Android apps. For instance,
Kirin [11] employs a security rule-based approach to detect
malware by analyzing the permissions requested by apps. Vet-
Droid [40] advances this by dynamically analyzing how apps
use permissions to access and utilize sensitive system resources.
Droid Detective [23] generates rule sets from combinations of
declared permissions to identify potential malware with unusual
permission requests. PInDroid [17] extracts permissions and
intents from the AndroidManifest.xml, using them as features
alongside ensemble learning methods to detect malware on
resource-constrained mobile devices. Ç¸sahin et al. [30] intro-
duced a linear regression-based feature selection technique to
identify the most discriminative features from app permissions,
enhancing the efﬁciency and accuracy of malware detection
systems. These approaches focus on analyzing the interactions
and behavioral patterns between apps and the Android system
to detect malware. However, PERMEAGRE explores custom
permissions used to safeguard interactions and communications
between apps.

IV. CHARACTERIZING BPCP ISSUES

A. Threat Model

Attackers can exploit existing BPCP issues to perform mali-
cious actions that threaten data privacy or system integrity. In
this study, we consider an adversary with the capability to crawl
app markets, such as Google Play, to download target apps of
interest. The adversary can also perform reverse engineering and
analysis of the ﬁles within the application packages, including
the “AndroidManifest.xml” ﬁles and the class ﬁles, to identify


---

## Page 7

instances of BPCP vulnerabilities. Additionally, the adversary
can develop and distribute malicious apps through app markets
to exploit these BPCP issues and launch attacks on susceptible
apps.

B. Empirical Study of BPCP Issue Patterns

Deﬁnition: We deﬁne BPCP issues as exceptions or secu-
rity vulnerabilities that arise when developers fail to adhere to
best practices during the deﬁnition, enforcement, request, and
resource utilization phases of custom permissions.

Methodology: To the best of our knowledge, this is the ﬁrst
systematic study conducted on the poor practices associated with
custom permissions. To initiate our research on BPCP issues,
we leverage HackerOne, a renowned bug bounty platform that
provides detailed bug disclosure reports and bug ﬁxes, along
with Stack Overﬂow. We collect relevant posts by performing
searches using keywords such as “Android permission” and the
“android-permission” tag. We refrain from using “custom per-
mission” as a keyword, as we observe that many posters do not
explicitly specify whether the question or vulnerability relates
to a custom permission or a system permission. This ambiguity
would result in an incomplete collection of study resources.
We manually ﬁlter out irrelevant results and ultimately gather
11 HackerOne posts (referred to as HO posts) and 861 Stack
Overﬂow posts (referred to as SO posts). The ﬁltering process
follows three criteria. Firstly, the post should directly relate to
the usage of the custom permissions mechanism. Second, the
post should acknowledge the issue by the author/owner. Lastly,
the Stack Overﬂow posts should have accumulated more than
200 views.
To establish a taxonomy of BPCP issues, we conduct a manual
analysis of these posts. We employ a widely used open coding
procedure [9]. Initially, we develop a preliminary taxonomy of
BPCP issues based on the knowledge gained from the preceding
data collection and ﬁltering processes. Next, three authors of this
paper, possessing Android development experience, indepen-
dently analyze each post and classify them accordingly. After
conducting independent analyses and classiﬁcations, the anno-
tators meet to discuss and clarify the boundaries and hierarchy of
the categories. Subsequently, the annotators resume the labeling
process. Following four iterations, the annotators ﬁnally reached
a consensus on the taxonomy.

Consequently, we compile a classiﬁcation of nine BPCP issue
patterns and categorize them based on where the BPCP issue
arises during the custom permission development stage.

Severity and impacts of BPCP issues: To assess the security
severity of the identiﬁed BPCP issue patterns, we classiﬁed them
according to the expected severity using the CVSS (Common
Vulnerability Scoring System) 4.0 scoring metric [14]. This
widely-used metric, employed both in industry and academia,
assigns a severity score to Common Vulnerabilities and Expo-
sures(CVE).TheCVSSscoreincorporates11metrics,including
the attack vector (same network, adjacent network, local, or
physical access), access complexity (whether an attacker can
expect repeatable success or needs speciﬁc conditions), Attack
Requirements, Privileges Required, User Interaction, and its

conﬁdentiality, integrity, availability impact on the vulnerable
system and subsequent system. The CVSS scores for the nine
BPCP patterns are presented in the “Score” column of Table II.
Please note that our assessment of the potential impact on the
system is based on the most severe consequences that the issues
might cause. The speciﬁc outcomes are related to the particular
design and functionality of the affected applications.

According to the CVSS system, out of the nine BPCP issue
patterns that may pose security concerns, six have a medium
severity rating, while three have a low severity rating. These
BPCP issues can lead to various security impacts, such as
component hijacking and application crashes.

C. BPCP Issues in Permission Deﬁnition

This category of BPCP issue patterns occurs during the
process of deﬁning a custom permission. We classify three
anti-patterns into this category, namely incorrect level or at-
tribute of permission deﬁnition elements (Def-Manifest), deﬁn-
ing a permission with a collision-prone permission name (Def-
ColliPerm), deﬁning a permission at invoker-side (Def-Invoker).

1) Incorrect Level or Attribute of Permission Deﬁnition Ele-
ments (Def-Manifest): As mentioned in Section II-A, an app can
use the <permission> element to deﬁne a custom permission
and the <permission-group> element to group some permis-
sions under a speciﬁc category. However, these elements must be
used as a direct child element of <manifest> in the manifest ﬁle
and they have a speciﬁc set of attributes that can be conﬁgured
by the developer.3

Impact: Misplaced elements would not be recognized by
the system, resulting in unsuccessful permission deﬁnition and
abnormal app functionality. Assigning an undeﬁned attribute to
<uses-permission> or <permission> element would be disre-
garded by the system.

2) Deﬁning Permission With a Collision-Prone Permission
Name (Def-ColliPerm): Starting from Android 5.0, two apps
deﬁning the same permissions (including normal or danger-
ous protection level permissions) cannot be installed on the
same device. Therefore, it is crucial to avoid permission name
collisions. It is recommended by the best practice guide to
use reverse-domain-style naming to avoid collisions. However,
Google does not strictly enforce this convention, and it is still
common to ﬁnd apps in the wild that do not adhere to Google’s
recommendednamingstandards. Duringourempiricalstudy, we
encountered numerous posts related to this issue. For instance,
in SO post #28266030, the author deﬁned a permission named
“android.permission.permRead” within the namespace of the
Android Open Source Project. A response pointed out this
problem and advised the author to create a custom permission
using the reverse domain style.

Impact: A permission name that does not adhere to reverse-
domain-style naming standards would increases the probability
of permission name collisions, which may cause the application
to fail to install.

3[Online]. Available: https://developer.android.com/guide/topics/manifest/
manifest-intro


---

## Page 8

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

TABLE II
NINE CUSTOM PERMISSION BPCP ISSUE PATTERNS

Fig. 3.
Demonstration of Def-Invoker Issue. The application marked with a
star is the ﬁrst to be installed on the device.

3) Deﬁning Permission At Invoker-Side (Def-Invoker): Def-
Invoker issue describes a ﬂawed approach where the custom
permission intended to restrict access to a component of the
provider app is deﬁned and declared by the invoker app, rather
than by the provider app itself. In the Android system, for a
custom permission to be effectively granted, the app declaring
the permission must be installed after the app that deﬁnes it. Oth-
erwise, the permission cannot be authorized due to its absence at
the time of the invoker app’s installation. The Def-Invoker issue
occurs when developers incorrectly assume that the invoker app
will be installed before the provider app.

Impact: This above assumption leads to a signiﬁcant security
vulnerability: if a malicious app is installed before the invoker
app, it candeclareanddeﬁnethis permissionat anylevel, thereby
easily gaining unauthorized access to the protected components
oftheproviderapp.Additionally,complicationsarisewhenthere
are multiple invoker apps for a single provider app, as depicted
in Fig. 3. If the app that deﬁnes the permission is uninstalled, the
permission is also revoked. Consequently, even if the provider
app remains installed, other invoker apps can no longer access
its resources.

D. BPCP Issues in Permission Enforcement

We categorize BPCP issues that occur during the process of
restricting interactions with other applications by setting custom
permissions to components into this category. We have identi-
ﬁed three types of BPCP issue patterns related to permission
enforcement: enforcing permission to components incorrectly

(Enf-MisComp), enforcing components with system dangerous
permissions (Enf-SysPerm), and enforcing components with
undeﬁned permissions (Enf-UnDefPerm).

1) Enforcing Permission to Components Incorrectly (Enf-
MisComp): The Enf-MisComp issue encompasses two main
aspects. First, permissions should only be enforced on
<application> and component elements including <activity>,
<service>, <receiver>, and <provider> can be enforced with
permission using the “android:permission” attribute to regulate
the access from the other apps.4 Only apps that meet the permis-
sion requirement can gain access to these components. Second,
different types of components support different attributes, and
setting inappropriate attributes for a component can result in
those attributes being ignored by the system. We have observed
numerous cases on Stack Overﬂow where developers mistakenly
enforce permissions on inappropriate components. For instance,
in SO posts #26304226, 19126687, and 37515478, the authors
mistakenly enforce permissions on the MainActivity, causing
the app to be unable to open directly from the home screen.
This occurs because the home screen activity, which is a com-
ponent of the Android system process, does not hold the custom
permission required by the MainActivity. Similarly, in SO post
#29098381, the author enforces a custom permission on an
<application> component, which means that all components
within the application are subject to this permission, including
the MainActivity.

Impact: If the developer sets the “android:permission” at-
tribute on unsupported elements, it would be ignored. More se-
riously, this issue leads to function failure when permissions are
enforced on inappropriate components such as the MainActivity.

2) Enforcing Components With System Dangerous Per-
missions (Enf-SysPerm): When setting permissions for com-
ponents,
it
is
feasible
to
assign
system
permissions,
such
as
allowing
a
receiver
component
to
use
“an-
droid.permission.BLUETOOTH_CONNECT”
to
listen
for
Bluetooth pairing events broadcast by the Android system.
However, assigning system permissions to protect components
in other contexts presents certain security concerns.

Impact: When a component is enforced with a system danger-
ous permission, any app granted that permission can access the

4Settingthisattributeto<application>isaconvenientwaytosetapermission
that applies to all of the application’s components.


---

## Page 9

component. This could pose security risks, particularly when
the component handles sensitive or private data. The broad
accessibility provided by system permissions might expose the
component to potential misuse by any app that obtains that per-
mission. Moreover, custom permissions are designed to provide
ﬁne-grained access control, supporting more precise security
management for app components. Conversely, if a component’s
protective permission is set to a system dangerous permission,
any app that needs to access this component not only gains the
services provided by the component but also access to other
system resources associated with that permission. Although this
may not necessarily lead to security breaches, it violates the
principle of least privilege, which advocates that an application
should only request the minimal set of permissions necessary
for its functionality.

3) Enforcing Components With Undeﬁned Permissions (Enf-
UnDef-Perm): Enforcing access restrictions to components us-
ing undeﬁned permissions poses a signiﬁcant security risk and
can result in severe breaches. This vulnerability arises because
any other app can deﬁne these permissions and assign arbitrary
protection levels to them. The occurrence of undeﬁned permis-
sions can be attributed to various factors, such as typographical
errors or out-of-sync permission name maintenance between
the provider app and the invoker app. An answer in SO post
#2169294 pointed out that permission names are case-sensitive.
Therefore, if a component is enforced with a permission that
does not match the deﬁned permission’s case, it is considered
undeﬁned. Many developers responded to this answer, sharing
their experiences of spending days troubleshooting their apps,
only to discover that the cause was an undeﬁned permission.

Attack: The illustrative example presented in Section I, Fig. 1,
depicts a typical instance of this pattern. When a component is
enforced with an undeﬁned permission, an attacker can create
an app that deﬁnes and requests this permission, thereby gaining
access to the component. Although executing this type of attack
necessitates installing the attacker’s app prior to the victim’s app,
the attacker can deceive the user into accomplishing this.

E. BPCP Issues in Permission Request

This category of BPCP issue patterns is located in the process
where the developer declares the use of a custom permission in
the manifest ﬁles. We ﬁnd one BPCP issue that are located in
this process, i.e., misplaced permission request elements (Req-
Manifest). The causes and impact of Req-Manifest are the same
with Def-Manifest.

F. BPCP Issues in Resource Utilization

This categoryof BPCPissues pertains totheprocess wherethe
application utilizes intents to interact with other applications for
resources or functionalities. We identify two types of permission
request BPCP issues within this category: failure to check the
granting of custom permissions (RU-NoGrantCheck) and failure
to verify the deﬁnition of custom permissions before sending
intents (RU-NoDefCheck).

1) Failure to Check the Granting of Custom Permissions
Before Sending Intents (RU-NoGrant-Check): Starting from

Android 9.0, dangerous-level permissions must be requested at
runtime and can be revoked by the user. Therefore, developers
are required to verify whether the requested permission has been
granted and take appropriate actions based on the result, rather
than assuming that the app already possesses the permission
and proceeding with execution. Previous research on runtime
permission management [12], [36] has demonstrated that this
issue is prevalent in real-world scenarios.

Impact: Accessing protected components without checking
thegrantingofcustompermissionscanleadtofunctionalfailures
or exceptions. Moreover, if an app initiates an intent without
checking the permissions, it becomes vulnerable to interception,
resulting in unauthorized intent receipt or even information
leakage. For instance, consider a scenario where a provider app
exports a component that is enforced by a speciﬁc permission.
However, the invoker app is installed prior to the provider app
and does not possess that permission. Exploiting this vulnerabil-
ity, an attacker can develop an app that exports a component with
the same “intent-ﬁlter” but without a permission requirement.
In such a case, the intent from the invoker app will be received
by the attacker’s app, leading to unauthorized intent receipt. If
the intent carries private information, it can result in information
leakage.

2) Failure to Verify the Deﬁnition of Custom Permissions
Before Sending Intents (RU-NoDefCheck): Developers should
avoid making assumptions about custom permissions with spe-
ciﬁc names, as any application can deﬁne a permission with
that name and assign it any protection level as long as it is the
ﬁrst to deﬁne it. Therefore, it is essential to verify the deﬁnition
of the permission before performing any related operations,
such as sending an intent. Android provides APIs like getPer-
missionInfo() to retrieve information about the deﬁnition of a
permission.

Impact: An attacker can trick the user into installing a mali-
cious app that deﬁnes the permission with a normal protection
level before the invoker app is installed. If the invoker app fails
to check the deﬁnition of the custom permission and proceeds
to send the intent, the intent can be intercepted by the attacker’s
app, resulting in information leakage when the intent contains
sensitive data.

V. OUR APPROACH

Challenges: Accurately and efﬁciently screening millions of
lines of code for the BPCP issue patterns introduced in the
previous section is not a trivial task. It presents several design
challengesthatneedtobeaddressed.1)Androidappscandeclare
custom permissions and components statically or dynamically,
requiring precise screening of both parts. 2) To achieve efﬁcient
detection of BPCP issues, our approach, PERMEAGRE, needs
to be designed systematically, rather than detecting each BPCP
issue pattern independently. This ensures that all violation pat-
terns are checked in a single analysis iteration. 3) Detecting the
BPCP issue patterns of RU-NoGrantCheck and RU-NoDefCheck
requires PERMEAGRE to distinguish whether the intents are
inter-process.

Design Overview: To overcome the aforementioned design
challenges, PERMEAGRE is designed to consist of three main


---

## Page 10

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

Fig. 4.
Workﬂow of PERMEAGRE.

analysis phases, namely static declaration analysis phase, dy-
namic declaration analysis phase, and invocation analysis phase,
as shown in Fig. 4. To overcome the ﬁrst challenge, PERMEA-
GRE extracts all the static and dynamic declaration information
of permissions and components in the static declaration analysis
phase (Section V-A) and dynamic declaration analysis phase
(Section V-B). In detail, the static analysis phase extract infor-
mation from the manifest ﬁles, and dynamic declaration analysis
leverage backward program slicing techniques with multiple
heuristic optimizations on the class ﬁles to extract dynamic
declaration information. To tackle the second challenge, we
leverage the capability of the relational database to store all
the static and dynamic declaration information. The application
analysis is performed only once, and the detection of BPCP issue
patterns can be realized through database queries. Regarding the
third challenge, in the invocation analysis phase (Section V-C)
PERMEAGRE matches all possible IPC pairs (entry & exit
point) of exported components by comparing the permissions
and the attributes of the intent ﬁlters from the database. Similar
to existing works [6], we use static analysis to identify intent
values.

A. Static Declaration Analysis

First, we utilize Apktool5 to decompile the smali bytecode and
decodetheAndroidManifest.xmlﬁleforeachapp.Next,weparse
the AndroidManifest.xml ﬁle, documenting the declared com-
ponents and permissions, including deﬁnitions and declarations
of permissions. This statically declared information within the
manifest ﬁle will be used for subsequent matching and analysis
of IPC links.

Following this, we conduct checks based on manually
constructed rules for detecting Def-Manifest, Req-Manifest,
and Enf-MisComp. For Def-Manifest and Req-Manifest, we
examine whether the permission-related elements including
<permission>”, <uses-permission>”, and <uses-permission-
sdk-23>” are utilized as direct child elements of the
<manifest>” and whether they are set with unrecognized at-
tributes.

Regarding the Enf-MisComp issue, we inspect from two
aspects. Firstly, we check whether the “android:permission”
attribute is only applied to elements such as <activity>,

5[Online]. Available: https://ibotpeaches.github.io/Apktool/

<provider>, <receiver>, <service>, and <application>. Sec-
ondly, we verify whether components are set with unsupported
attributes.

B. Dynamic Declaration Analysis

Components (e.g., broadcast receivers) and permissions can
be declared dynamically at runtime. For example, Broadcast
receivers can be declared at runtime using the registerReceiver()
methods. Permissions can also be deﬁned at runtime using the
addPermission() method. Therefore, in this phase, we extract
dynamic declaration information and detect BPCP issues by
combing dynamic declaration information and the existing static
declaration information.

We leverage inter-procedural backward program slicing for
extracting dynamic declaration information, which is imple-
mented utilizing Soot [33]. Backward program slicing is to
determine all the statements that affect a certain statement of
a certain parameter in a statement (also known as the slicing
criterion) based on the def-use chain of a program.

For dynamic registered components, we perform inter-
procedural backward slicing using the parameters including
broadcastPermission, ﬁlter of registerReceiver() method as the
criterion to collect the constant values associated with dynami-
cally registered broadcast receivers.

Forruntime-deﬁnedpermissions,wepopulatethepermission-
tree deﬁnition information into the database during the static
declaration analysis phase, and then we check whether there
are apps requesting permissions belonging to these permission
trees. If yes, we use backward slicing on the addPermission()
method to obtain these dynamically deﬁned permissions to see
whether its arguments are inﬂuenced by constant values that are
possible to be the permission name and add these permissions
to our database. Else, we skip the dynamic permission analysis
of this app.

Then we aggregate all the dynamic and static permissions
used to enforce components and match them between the sys-
tem permission set6 and the normal permission set to detect
violations of Enf-SysPerm. We detect the violation of Enf-
UnDefPerm by checking whether the deﬁnitions of the permis-
sions used to enforce components can be found in the same
app. We use the recommended reverse domain naming method

6[Online].
Available:
https://developer.android.com/reference/android/
Manifest.permission


---

## Page 11

as a criterion to detect collision-prone permission names (Def-
ColliPerm).

C. Invocation Analysis Phase

In this phase, we identify all the IPC links between the
provider and invoker, and then detect whether the initia-
tor of the IPC violates their BPCP issues (Def-Invoker, RU-
NoGrantCheck, RU-NoDefCheck).

First, we leverage DIALDROID [6] to obtain IPC links.
DIALDROID is a tool, based on Soot [33] and IC3 [27], to
identify inter-app data ﬂows at scale. Speciﬁcally, DIALDROID
applies COAL solver to precisely infer the intent values and
match these intent values in the component databases to ﬁnd
IPC links. We modiﬁed DIALDROID only to identify possible
IPC links of components enforced by custom permissions so
as to improve efﬁciency. Then, we detect whether the initiator
of the IPC links violate rule Def-Invoker. We consider an app
to violate rule Def-Invoker if the invoker app deﬁnes and de-
clares a permission in its manifest with the same name as the
provider-app’s component enforced with.

For identifying the violation of RU-NoGrantCheck, we take
a similar approach to revdroid [12]. Speciﬁcally, we check
whether the invocation site or its call stack 1) is wrapped by
an exception handler of SecurityException or its superclasses,
or 2) is protected by the permission check method calls such
as checkPermission() and checkSelfPermission(), for which we
perform a dominator analysis leveraging Soot framework [33]
to check whether this call site depends on the return value of
these permission check methods.

Finally, we check whether the initiator of the IPC initiate an
explicit intent, and whether the explicit intent-consuming API
calls (e.g., startService(), startActivity()) are dominated by per-
mission info extraction APIs and identity-checking APIs such
as getPermissionInfo() and hasSigningCertiﬁcate() to detect rule
RU-NoDefCheck. getPermissionInfo() returns a PermissionInfo
object which contains the package name of the application which
deﬁnes this permission. hasSigningCertiﬁcate() checks whether
thetargetapplicationcontainsadesiredcertiﬁcate. Thoughsome
apps may use other APIs to check the identity of the target
application. For example, some applications check the package
name of the target application. However, it should be noted
that just checking the package name of the app that deﬁnes
the permissions does not guarantee the prevention of intent
hijacking, as attackers can still bypass it by forging the package
name.

D. Optimizations

1) Accuracy: PERMEAGRE takes into account various spe-
cial mechanisms of Android to improve detection accuracy.

1. Disabled components. Components can be disabled in the
manifest ﬁle and enabled at runtime by calling setComponen-
tEnabledSetting() API. Most of the related works just presume
that these components are always disabled and simply skip them
when analyzing. We perform backward slicing to detect whether
these components can be enabled at runtime and only label the
rest of them as disabled components.

TABLE III
APP COLLECTION LIST

2. Dead code. Dead code is the code in the application that
will never be executed. Analyzing this code without considering
the dead code will affect the efﬁciency of the analysis and bring
false positives. Therefore, PERMEAGRE uses Soot to build the
call graph of the analysis target and identify the methods that
are not called by others.

2) Scalability: Detecting BPCP issues from millions of lines
of code places high demands on the efﬁciency of detection meth-
ods. Therefore, we employ the following heuristics to achieve
efﬁcient BPCP issue detection.

1. Library awareness. Apps may integrate third-party libraries
to realize speciﬁc functionalities. PERMEAGRE skips the anal-
ysis process of the same library so as to improve efﬁciency.

2. Component awareness. To improve the efﬁciency, we mod-
ify the DIALDROID [6] only to analyze the IPC pair of com-
ponents enforced with permissions rather than all the exported
components.

VI. MEASURING BPCP ISSUES

In this section, we leverage PERMEAGRE
to perform a
large-scale measurement of BPCP issues in the wild. We also
use jadx to obtain human-readable source code for manual
veriﬁcation. Our measurement study is driven by the following
research questions:
r RQ1 (What is the overall distribution of BPCP issues?):

How many apps contain BPCP issues? Is there any cor-
relation between app popularity and app categories? Are
there any differences across app markets? (Section VI-A)
r RQ2 (What is the distribution of different types of BPCP

issues?): Which problems are the most common? What
may be the root cause of these issues? (Section VI-B)
r RQ3 (How many users were affected by BPCP issues?): Is

there a correlation between downloads and BPCP issues?
Are there any well-known apps that have such problems?
(Section VI-C)
Target App Selection: To measure the presence of BPCP
issues, we randomly crawled nearly 83 k apps distributed in 5
years. As listed in Table III, over 44 k of them are crawled from
Google Play, while the remaining nearly 39 k apps are crawled
from other six alternative app markets. This diverse collection
aimstoprovideaglobalperspectiveontheBPCPissuesaffecting
the app ecosystem.

It is noteworthy that the representation of apps from Google
Play in our dataset is markedly higher than those from other
sources, mirroring the actual market dynamics where Google
Play holds a dominant position in the Android app market. This
skewed distribution is a recognized phenomenon in extensive
analyses of Android applications, as corroborated by existing
literature in the ﬁeld [2], [29]. It is crucial to emphasize that our
methodology is not predicated on machine learning algorithms,


---

## Page 12

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

TABLE IV
OVERALL RESULTS OF OUR MEASUREMENT STUDY (# ANY: APPS WITH AT LEAST ONE TYPE OF BPCP ISSUES)

which could be more susceptible to biases stemming from
such data imbalances. On the contrary, our approach employs
rule-based checks, a method that is inherently more robust
against the potential inaccuracies that might arise from unevenly
distributed datasets. Consequently, the integrity and accuracy
of our detection process remain uncompromised, offering a
reliable and unbiased evaluation of BPCP issues across the app
landscape.

A. RQ1: Overall Distributions of BPCP Issues

Overall Statistics: A total of 35,960 custom permission deﬁ-
nitions were identiﬁed in the dataset. Out of the total, 31,648
permissions are deﬁned with either the “signature” or “sig-
natureOrSystem” protection level. Additionally, there are 136
permissions deﬁnedwiththe“dangerous”protectionlevel, while
3,525 permissions are deﬁned at the “normal” protection level.
Among the entire dataset, 57.3% of the applications use custom
permissions, and more than 45.55% of them are reported to
contain at least one BPCP issue. The detailed statistics of our
exploration results are presented in Table IV. A total of 21,664
apps have been found containing at least one issue.

Distribution over App Markets: According to the permissions
analysis, we found that each application from Google Play
deﬁnes an average of 0.24 custom permissions, which is far
lower than that deﬁned in other app stores. Among them, 360,
Baidu, and CoolAPK have the most average custom permission
deﬁnitions, are 2.30, 1.61 and 1.95, respectively. As for the
analysis of BPCP issues, we found that around 9.84% to 58.99%
of apps in each market have been found to contain at least one
issue. Even in Google Play, roughly 19.09% of our crawled apps
have BPCP issues. This result suggests that BPCP issues are
prevalent across markets. Also, the probability of these issues
in third-party app stores is much higher than it is in the ofﬁcial
Google Play store (except Xiaomi app market).

This may be because the vetting mechanisms in most of
the third-party app stores are weaker than ofﬁcial Google Play
stores, leading to a large number of low-quality applications,
which can easily cause a large number of vulnerable apps to
spread.

Distribution over App Categories: In order to understand
the general distribution of BPCP issues across categories, we
statisticize the distribution of BPCP issues over the taxonomy
developed by Wang et al. [34] as each app market implements its
own app taxonomy. The analysis results are shown in Table VIII,
in which each column adds up to 100%.

TABLE V
BPCP ISSUE DISTRIBUTION BETWEEN APP RATINGS

From a prevalence perspective, the NEWS and VIDEO cate-
gories demonstrate notably high probabilities of encountering
BPCP issues. Speciﬁcally, the NEWS category exhibits the
highest prevalence, with 46% of apps having at least one BPCP
issue. Similarly, VIDEO apps show a 40% prevalence of these
issues. This suggests that apps within these categories may often
be developed with less stringent security practices. Conversely,
the MUSIC and PHOTO categories demonstrate relatively low
prevalence rates at 11% and 22%, respectively. This could
indicate either a lower complexity in permission requirements
for these apps or potentially more robust security practices in
managing permissions.

Focusing on speciﬁc types of BPCP issues, the GAME
category shows signiﬁcant occurrences across several areas.
Notably, the highest rates are observed in Def-Manifest (34%),
Enf-MisComp (62%), and RU-NoGrantCheck (13%). While
this is largely due to the prominent representation of GAME
category apps within the entire dataset (accounting for 25%
of the apps), it nonetheless suggests that games need to better
manage their custom permissions, considering their demands
for rich media content and access to various device capabilities.
The PERSONALIZATION category, known for extensively
customizing aspects of the device’s interface and functionality,
shows a particularly high occurrence of the Invoker issue (57%).
Thehighincidenceof Invoker issues inthis categoryunderscores
the critical need for developers to ensure that permissions are
properly deﬁned in the app that owns the component.

Distribution over App Ratings: We collect and analyze app
ratings to investigate if there is a correlation between an app’s
popularity (as indicated by its rating) and the likelihood of
exhibiting the described security issues.

The results of our analysis, as shown in Table V, indicate
that while apps rated between 0 and 1 show a higher incidence
of BPCP issues, there is no clear trend across higher rating
intervals. This suggests that the occurrence of these issues does
not signiﬁcantly correlate with the app ratings, pointing to the
conclusion that even highly rated apps are not immune to the
BPCP issues.


---

## Page 13

TABLE VI
MANIFEST-RELATED ISSUES REPORTED MORE THAN 50 TIMES (INCLUDING

DEF-MANIFEST, ENF-MISCOMP, REQ-MANIFEST)

TABLE VII
TOP 5 SYSTEM PERMISSIONS ENFORCED WITH COMPONENTS

B. RQ2: Distribution of BPCP Issue Types

We then analyze the distribution of BPCP issues according
to their types. Compared with other types of errors, deﬁ-
nition issues are much less. Request issues are most popu-
lar across markets. To our surprise, over 10,790 apps don’t
check the identity of the permission deﬁner, which may lead to
unauthorized intent receipt (RU-NoDefCheck). 9,983 apps don’t
check the grant of custom permissions before sending intent
(RU-NoGrantCheck), which may allow attackers to perform
unauthorized intent receipt. Over 5,200 apps enforce compo-
nents with undeﬁned permissions (Enf-UnDefPerm).

Permission Deﬁnition Issue Results: We found 499 apps use
permission deﬁnition elements incorrectly (Def-Manifest). We
list all the manifest-related issues reported more than 50 times in
TableVI.AsweintroducedinSectionII,<permission>element
can only be used as a direct subelement as <manifest> element.
However, 203 apps mistakenly place the <permission> as a
subelement of the<application> element. Besides, 495apps de-
ﬁned permission with collision-prone names (Def-ColliPerm),
which may cause the app to fail to install. Most of these reports
deﬁne permissions with only one word such as “pStart”, “pEnd”,
“true”, “false”, or even “TODO”. Eight apps deﬁne permission
with the name “signatureOrSystem”, which is a preset value for
the “android:protectionLevel” attribute. The results prove that
the developers do have difﬁculty in understanding the cus-
tom permission mechanism. 168 invoker apps deﬁne permis-
sions that are already deﬁned in the provider apps with different
developer signature (Def-Invoker), which cause function failure
when installing or removing the apps in an unintended order.

Permission Enforcement Issue Results: The most preva-
lent permission enforcement issue is Enf-SysPerm, account-
ing for 24.4% of the apps reported with issues. As shown
in Table VII, 4782 apps enforce their activities with “an-
droid.permission.INSTALL_PACKAGES” permission, which
is a system permission used to allow an application to install
packages. 20 apps enforce “android.permission.INTERNET”
permission to their components, which is used to manage the
apps’ access to the internet. 1387 apps enforce components with

permissions that don’t have deﬁnition (Enf-UnDefPerm), which
is dangerous as the attacker can easily hold these undeﬁned
permissions and performs intent spooﬁng or intent reception. In
all,thereare279permissionsfoundtobeusedwithoutdeﬁnition.
Through our manual analysis, most of the undeﬁned permissions
can be roughly divided into two categories:

1. Platform-deﬁned Permissions: After excluding AOSP–
deﬁned permissions and those associated with Google’s Cloud
Messaging (GCM), we merged and sorted the strings after
removing the last section of the permission name. Then, we
searched these reverse domain style strings in the search en-
gine to identify their belongings. As a result, we found that
more than one-third of these undeﬁned permissions are related
to smartphone manufacturers, operating system providers, or
even third-party libraries that providing analytics or notiﬁcation
pushing services. However, when these apps are installed on an
operatingsystemnotcontainingthedeﬁnitionofthispermission,
these permissions would be unclaimed and an attacker can
perform component hijacking as introduced in Section IV-F. To
prevent this kind of attack, the library must contain a complete
and graceful degrade mechanism to protect the users when the
function providers are not available. We then investigate into the
nine most commonly used third-party permissions and check
their degrade mechanisms. The results can be seen in Table IX.
Three of these providers don’t provide a degrade mechanism and
do not even remind users in the documents to check whether the
current environment meets the requirements, which is dangerous
and can be easily exploited, affecting 100 apps with more than
one billion installs. Three providers adopt a package name based
method to detect the intent sender. However, this solution can
also be exploited since that the attacker’s package name can be
named as the same as the real correct name.

2. Mistyped Permissions: Mistyped permission means that
the developer enters the wrong permission name which can-
not be found with a deﬁnition. Among all the undeﬁned
permissions, 12% of them are due to typo. For example,
three apps mistyped “ACCESS_COARSE_LOCATION” as
“ACCESS_COURSE_LOCATION”. Two apps mistyped “IN-
STALL_PACKAGES” as “INSTALL_PACKAGE”. Moreover,
considering that the Android permission system is case-
sensitive, we ﬁnd that there are four apps that use permission
names with different cases.

1505 apps set inappropriate permission-related attributes
to components (Enf-MisComp). For example, 609 apps en-
force custom permissions to <action> elements, which
will be ignored by the system. 468 apps specify the “an-
droid:protectionLevel” attribute, an attribute can only be set
for <permission> elements to specify the protection level of
the custom permission to be deﬁned, for the component ele-
ments. These issues prove that lots of developers mistake this
attribute for describing a component’s security level.

Permission Request Issue Results: We found that 1204
apps are reported with one or more manifest issues (Req-
Manifest). Among all these issues, ﬁve apps use “|” to connect
two system permissions, e.g. “android.permission.INTERNET
| android.permission.ACCESS_ WIFI_STATE”. However, an-
droid permission system does not recognize the symbol “|”


---

## Page 14

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

TABLE VIII
THE DISTRIBUTION OF CUSTOM PERMISSION-RELATED ISSUES ACROSS APP CATEGORIES

TABLE IX
COMMONLY USED THIRD-PARTY LIBRARY PERMISSIONS

as the “or” operator, thus the permission is recognized as an
independent permission. We also found 370 apps misplac-
ing <uses-permission> elements inside the <application>,
which will be ignored by the system, resulting in func-
tion failure and even intent spooﬁng when the app properly
checks the grant of these permissions. More than 60 apps
mistyped <uses-permission> as <user-permission> or <use-
permission>, which prevents them from successfully declaring
for these permissions. The most prevalent invoker-side issue is
RU-NoDefCheck. Over 10,000 apps failed to properly check the
deﬁnition of the permission before sending intents. 9983 apps
don’t properly check whether the required custom permissions
are granted at runtime (RU-NoGrantCheck). Through manually
inspection of nearly 100 apps exhibiting these issues. We discov-
ered that most of these issues stem from the third-party libraries
used within these apps, which lack proper permission checks.

C. RQ3: The Impact of Vulnerable Apps

Although we have identiﬁed a large number of vulnerable
apps containing BPCP issues, the impact on the wider mobile
app ecosystem is still unknown. One of the most explicit ways to
measure this is the number of app downloads. We divided the app
into six intervals based on downloads, and Fig. 5 summarizes
these results.

As can be seen from the ﬁgure, BPCP issues are common
in any interval (38%–50%). Most of the collected apps are

Fig. 5.
Distribution of the Apps from a perspective of installation count. (The
labels of each range represent the proportion of apps that contain at least one
BPCP issue in apps that use custom permissions).

installed between 0 to 104 times, accounting for around 45%
of the entire dataset. Only about 44% of the apps in this interval
use custom permissions. However, 49% of the apps using cus-
tom permission are reported with issues. Through our manual
analysis, we found that most of the apps in this interval are
developed by small companies or individual developers lacking
testing and user feedback. Apps with higher installs are more
willing to use custom permission mechanisms. We found that


---

## Page 15

TABLE X
PART OF APPS WITH OVER 108 INSTALLS

apps with 108 to ∞installs had a high issue rate because they
used custom permissions more frequently and thus were more
likely to introduce BPCP issues.

Although the apps with less popularity account for a large
portion of the BPCP issues, a considerable number of them are
popular apps with millions of downloads. Most of these apps
were developed by large corporations and went through a well-
tested process. This fully shows that not enough attention has
been paid to these issues. In Table X, we list the apps that were
downloaded more than 108 times but reported with at least one
BPCP issue.

Sogou Novel: “com.sogou.novel”, a popular e-reading app
developed by the well-known Chinese internet technology com-
pany Sogou, mistakenly sets a content provider’s permission
to ‘com.sogou.novel.PROVIDER‘, which was undeﬁned, hence
falling into the category of Enf-UndefPerm issues. Attackers
could exploit this by deﬁning and declaring this permission
to gain access to the content provider. The affected content
provider stores push notiﬁcation information and implements
an ‘insert‘ method which may lack sufﬁcient validation for push
message data and tokens, allowing malicious applications to
trigger improper behaviors or spread incorrect information.

Baidu Netdisk: An early version of “com.baidu.netdisk”,
an app developed by a large Chinese corporation Baidu with
millions of users, deﬁnes and enforces a normal-level permission
“baidu.push.permission.WRITE_PUSHINFOPROVIDER.com.
baidu.netdisk” that can be easily obtained by any other apps to
a content provider, causing unauthorized data injection as any
attacker app can write into that content provider by requesting
this permission. Through our investigation, we found that
this permission is related to BAIDU Cloudpush SDK. In the
developer guides of BAIDU Cloud Push,7 this permission is
required to be deﬁned as signature-level. However, though
developed by the same company, “com.baidu.netdisk” deﬁnes
it as normal permission.

VSCO: “com.vsco.cam” assigned “android:required” at-
tribute to <uses-permission> element. “android:required” is
a predeﬁned attribute of <uses-feature> element rather than
<uses-permission>. We investigated the cause of this problem,
and we found that at the top of the developer document of the
<uses-permission> element,8 it is mentioned that Google Play
assumes the hardware functions that the app needs to use based
on the permissions requested by the app, and ﬁlter the app from

7[Online]. Available: https://push.baidu.com/doc/android/api
8[Online]. Available: https://developer.android.com/guide/topics/manifest/
uses-permission-element

devices that don not offer that functionality. If the developer
wants to disable ﬁltering for a speciﬁc feature, he needs to add
android:required=“false” attribute to <uses-feature> element.
We believe that the introduction of this attribute in the developer
document of <uses-permission> element has misled some de-
velopers, making them mistakenly believe that this attribute is a
predeﬁned attribute of <uses-permission>.

Others: Though harmless, apps like “com.twitter.android”,
“com.tencent.mm”, “cn.wps.mofﬁce_eng” which have millons
of users assign undeﬁned attribute to predeﬁned tags. For exam-
ple, “com.twitter.android” app we downloaded from Xiaomi app
store assign “android:protectionLevel” attribute to <service>
element. “android:protectionLevel” attribute can only be as-
signed to <permission> element to set protection level for
custom permission.

D. FPs and FNs of PERMEAGRE

Due to the lack of a publicly available dataset for verifying
BPCP issues, to validate the FP and FN rates of PERMEAGRE,
we randomly selected 10 apps identiﬁed by PERMEAGRE as
havingBPCPissuesfromeachcategory(totaling90apps)and20
apps not reported as having BPCP issues for manual veriﬁcation.
The results are shown in the table provided.

For detections related to Def-Manifest, Def-ColliPerm, Def-
Invoker, Enf-MisComp, Enf-SysPerm, Enf-UnDefPerm, Req-
Manifest issues, no false positives (FP) or false negatives (FN)
were reported. This is because such issues can be determined
by analyzing the AndroidManifest.xml ﬁle and are judged based
on manually written rules, which eliminates the likelihood of
recognition errors.

For the detection of RU-NoGrantCheck and RU-NoDefCheck
issues, among the reported issues, we found that there were
2 and 3 apps with false positives (FP rates of 20% and 30%,
respectively). Analysis revealed that these false positives mainly
resulted from the lack of support for some outdated APIs: for
example, checkPermission(), checkCallingOrSelfPermission(),
and checkCallingPermission(), which were replaced by check-
SelfPermission() after Android 6.0. Thus, these issues were not
initially detected. After adding support for these APIs, PERME-
AGRE is able to identify these issues in the apps.

Of the 20 apps where BPCP issues were not detected, manual
inspection found that there were 3 and 5 apps with undetected
RU-NoGrantCheck and RU-NoDefCheck issues, respectively
(FN rates of 15% and 25%). We analyzed the causes of these
FNs and found that these apps had packing-based obfuscation
applied, which made it impossible to identify ICC links and the
system APIs for checking authorization and source of permis-
sions through static analysis.

E. Performance of PERMEAGRE

We conducted our tests on a Linux server equipped with an
Intel(R) Xeon(R) Gold 6248 CPU and 128 GB of memory, and
the analysis process for each application was carried out in a
tmpfs environment to optimize speed. We tested a total of 83,085
apps. On average, the analysis time per app was approximately


---

## Page 16

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

57.2 seconds. Our ﬁndings indicate that the performance of
PERMEAGRE is primarily inﬂuenced by the following factors:
r Number of Exported Components: The number of exported

componentsinanappsigniﬁcantlyaffectsthetimerequired
for inter-component communication (ICC) checks. An-
droid applications vary greatly in complexity and the num-
ber of interfaces they expose. Simple applications might
have only one exported activity component, whereas more
complex applications can contain hundreds. For instance,
apps with ten or fewer components had an average analysis
time of 51.9 seconds, whereas apps with more than ﬁfty
components averaged 73.2 seconds.
r Dynamically Declared Permissions and Dynamically Reg-

istered Components: The quantity of dynamically declared
permissions and dynamically registered components adds
to the complexity of the static analysis. These elements
increase the time required for a thorough analysis due to the
additional steps needed to resolve these dynamic aspects.
Comparison with Existing Tools: Compared to tools like Man-
iscope [39] and ManifestInspector [18], which primarily per-
formstraightforwardanalysesofanapp’sAndroidManifest.xml,
PERMEAGRE supports a broader spectrum of bad practices
detection. This includes matching ICC links and performing
static code analysis to identify issues such as RU-NoGrantCheck
and RU-NoDefCheck. Consequently, PERMEAGRE’s analysis
is more comprehensive but also slower relative to these tools
that focus only on manifest ﬁle inspection.

VII. DISCUSSION AND LIMITATIONS

A. Implication and Suggestions

We strongly believe that our efforts can make a positive
contribution to the mobile app ecosystem.

App Markets: Our ﬁndings indicate that most app markets pay
insufﬁcient attention to the security issues stemming from BPCP
issues. Based on our research, we recommend that app markets
take the following actions: (1) Strictly enforce the application
vetting process to identify and address BPCP issues before
releasing apps, thereby preventing the widespread dissemination
of problematic applications. (2) Implement automated tools to
detect and remove problematic applications, as well as identify
apps that exploit these vulnerabilities.

Third-Party Library Providers: Inaccurate or outdated manu-
als contribute to the ease with which developers commit BPCP
issues. To address this, we suggest that third-party library
providers undertake the following measures: (1) Provide correct
and easily understandable developer manuals. (2) Offer an easy-
to-useAPIthatcandetectwhetheritisbeingusedinacompatible
environment. Additionally, prompt developers to design a clear
degradation mechanism, clearly documented within their SDK
materials.

AppDevelopers: Our researchhas uncoveredaprevalent trend
where app developers, particularly those identiﬁed as inexperi-
enced due to their less than two years of industry presence and a
portfolio comprising fewer than three published apps, have been
found to incorrectly position permission-related elements or at-
tributes within their app’s manifest ﬁle. This insight was derived

from an analysis of publicly accessible developer proﬁles and
app information available on various app stores. Our ﬁndings
aim to serve as a valuable resource for these budding developers,
enabling them to recognize and address these common pitfalls.
By doing so, we hope to play a part in enhancing the overall
quality and reliability of apps in the market. Our work not only
provides a diagnostic tool for developers to reﬁne their craft
but also contributes to the collective advancement of the app
development community.

Research Community: Our work serves as a catalyst for
further research within the community on BPCP issues. This
includes investigating other types of BPCP issues, exploring
advanced methods for identifying such issues, and delving into
the automatic exploitation of applications with these issues.
Additionally, future research efforts can focus on developing
techniques to mitigate attacks stemming from BPCP issues.

B. Limitations

To the best of our knowledge, this work represents the ﬁrst
large-scale analysis of BPCP issues. However, our study does
have certain limitations. Firstly, we focused primarily on nine
summarized BPCP patterns, which may not encompass the
complete range of possibilities due to limitations in our available
resources. Thus, we encourage further research to achieve a
more comprehensive understanding of this issue and develop
effective mitigation strategies. Secondly, our measurements and
ﬁndings are conﬁned to the dataset we utilized, which may not
fully capture the extent of global application with these issues.
It is essential to expand the scope of analysis to gain a broader
perspective. Thirdly, our detection method is unable to identify
issues within dynamically loaded code in an app. However, it
is worth noting that our work and existing studies on dynamic
loaded code analysis [1] address distinct aspects of the problem
and are complementary to each other. Additionally, the presence
of obfuscated code can signiﬁcantly impact the performance of
PERMEAGRE, particularly when techniques like packaging are
employed to prevent reverse engineering. However, according to
our evaluation on the app dataset, there are roughly 3.6% of the
apps utilizing packaging for obfuscation. Furthermore, the harm
caused by BPCP issues is related to the speciﬁc design of each
app, and not all BPCP issues necessarily result in harm. For in-
stance, app developers can implement protective measures at the
application level against BPCP issues, such as ﬁltering intents.
However, since the approach to intent judgment and ﬁltering
implementation varies among developers, it is challenging to
accuratelyidentifyappsthathaveimplementedsuchprotections.
As a result, our tool reports all detected BPCP issues, although
not all identiﬁed errors are exploitable. The task of identifying
which apps have implemented intent protection is designated
for future research. We plan to enhance our understanding of
code and its generalization capabilities by leveraging machine
learning techniques or large language models (LLMs) as guides.

C. Ethical Consideration and Vulnerability Disclosure

We conducted manual veriﬁcation of the issues identiﬁed
by PERMEAGRE, speciﬁcally focusing on those that could


---

## Page 17

potentially lead to security vulnerabilities. We also made efforts
to reproduce these issues using the latest versions of the respec-
tive applications and promptly reported the identiﬁed problems
to the developers and vendors. We will continue to monitor the
responses and requests from the developers and vendors. It is
important to note that all experiments were conducted solely in
a local environment to demonstrate the nature of the attacks.

VIII. CONCLUSION

In this work, we conducted a large-scale systematical eval-
uation of Android developers’ misuse of custom permissions.
We ﬁrst summarized nine common permission misuse patterns
through empirical analysis, and then developed an automated
permission misuse detection tool named PERMEAGRE. We an-
alyzed nearly 83,000 applications across seven mainstream app
markets, and the experimental results showed that the custom
permission mechanism is widely less understood and often mis-
used by app developers as well as third-party library providers.
We believe that this work can actively promote developers’
awareness of custom permission misuses, encourage improved
vetting mechanisms across markets, and attract more research
interests from the community.

REFERENCES

[1] M. Alhanahnah et al., “Detecting hidden Android inter-app communica-

tion in dynamic loaded code,” IEEE Trans. Inf. Forensics Secur., vol. 15,
pp. 2782–2797, 2020.
[2] K. Allix, T. F. Bissyandé, J. Klein, and Y. L. Traon, “AndroZoo: Collecting

millions of Android apps for the research community,” in Proc. IEEE/ACM
13th Work. Conf. Mining Softw. Repositories, 2016, pp. 468–471.
[3] K. W. Y. Au, Y. F. Zhou, Z. Huang, and D. Lie, “PScout: Analyzing the

Android permission speciﬁcation,” in Proc. 2012 ACM Conf. Comput.
Commun. Secur., 2012, pp. 217–228.
[4] BAGIPRO, “[mail.ru android] typo in permission name allows to write

contacts without user knowledge,” Accessed: Dec. 16, 2022, 2018. [On-
line]. Available: https://hackerone.com/reports/440749
[5] P. Barros et al., “Static analysis of implicit control ﬂow: Resolving java re-

ﬂection and Android intents (t),” in Proc. IEEE/ACM Int. Conf. Automated
Softw. Eng., 2015, pp. 669–679.
[6] A. Bosu, F. Liu, D. D. Yao, and G. Wang, “Collusive data leak and more:

Large-scale threat analysis of inter-app communications,” in Proc. 2017
ACM Asia Conf. Comput. Commun. Secur., New York, NY, USA, 2017,
pp. 71–85.
[7] P. Calciati, K. Kuznetsov, A. Gorla, and A. Zeller, “Automatically granted

permissions in Android apps: An empirical study on their prevalence and
on the potential threats for privacy,” in Proc. 17th Int. Conf. Mining Softw.
Repositories, New York, NY, USA, 2020, pp. 114–124.
[8] E. Chin, A. P. Felt, K. Greenwood, and D. A. Wagner, “Analyzing inter-

application communication in Android,” in Proc. 9th Int. Conf. Mobile
Syst. Appl. Serv., Bethesda, MD, USA, 2011, pp. 239–252.
[9] J. W. Creswell and C. N. Poth, Qualitative Inquiry and Research Design:

Choosing Among Five Approaches. Thousand Oaks, CA, USA: Sage,
2016.
[10] C. Dennis, D. E. Krutz, and W. Mkaouer, “P-Lint: A permission smell

detector for Android applications,” in Proc. IEEE/ACM 4th Int. Con.
Mobile Softw. Eng. Syst., 2017, pp. 219–220.
[11] W. Enck, M. Ongtang, and P. McDaniel, “On lightweight mobile phone

application certiﬁcation,” in Proc. 16th ACM Conf. Comput. Commun.
Secur., New York, NY, USA, 2009, pp. 235–245.
[12] Z. Fang et al., “Revdroid: Code analysis of the side effects after dynamic

permission revocation of Android apps,” in Proc. 11th ACM Asia Conf.
Comput. Commun. Secur., New York, NY, USA, 2016, pp. 747–758.
[13] A. P. Felt, “Permission re-delegation: Attacks and defenses,” in Proc. 20th

USENIX Secur. Symp., San Francisco, CA, Aug. 2011, Art. no. 22.
[14] FIRST, “Common vulnerability scoring system version 4.0,” Accessed:

May 01, 2024, 2024. [Online]. Available: https://www.ﬁrst.org/cvss/v4-0/

[15] J. Gamba, M. Rashed, A. Razaghpanah, J. Tapiador, and N. Vallina-

Rodriguez, “An analysis of pre-installed Android software,” in Proc. 2020
IEEE Symp. Secur. Privacy, 2020, pp. 1039–1055.
[16] M. I. Gordon, D. Kim, J. H. Perkins, L. Gilham, N. Nguyen, and

M. C. Rinard, “Information ﬂow analysis of Android applications in
droidsafe,” in Proc. Annu. Netw. Distrib. Syst. Secur. Symp., 2015,
Art. no. 110.
[17] F. Idrees, M. Rajarajan, M. Conti, T. M. Chen, and Y. Rahulamathavan,

“PIndroid: A novel Android malware detection system using ensemble
learning methods,” Comput. Secur., vol. 68, pp. 36–46, 2017.
[18] A. K. Jha, S. Lee, and W. J. Lee, “Developer mistakes in writing Android

manifests: An empirical study of conﬁguration errors,” in Proc. IEEE/ACM
14th Int. Conf. Mining Softw. Repositories, 2017, pp. 25–36.
[19] W. Klieber, L. Flynn, W. Snavely, and M. Zheng, “Practical precise

taint-ﬂow static analysis for Android app sets,” in Proc. 13th Int. Conf.
Availability Rel. Secur., 2018, Art. no. 56.
[20] L. Li et al., “IccTA: Detecting inter-component privacy leaks in Android

apps,” in Proc. IEEE/ACM 37th IEEE Int. Conf. Softw. Eng., 2015,
pp. 280–291.
[21] L. Li, T. F. Bissyandé, D. Octeau, and J. Klein, “Droidra: Taming reﬂection

to support whole-program analysis of Android apps,” in Proc. 25th Int.
Symp. Softw. Testing Anal., 2016, pp. 318–329.
[22] R. Li, W. Diao, Z. Li, J. Du, and S. Guo, “Android custom permissions

demystiﬁed: From privilege escalation to design shortcomings,” in 2021
IEEE Symp. Secur. Privacy, 2021, pp. 70–86.
[23] S. Liang and X. Du, “Permission-combination-based scheme for Android

mobile malware detection,” in Proc. 2014 IEEE Int. Conf. Commun., 2014,
pp. 2301–2306.
[24] F. Liu, H. Cai, G. Wang, D. Yao, K. O. Elish, and B. G. Ryder, “MR-Droid:

A scalable and prioritized analysis of inter-app communication risks,” in
Proc. IEEE Secur. Privacy Workshops, 2017, pp. 189–198.
[25] L. Lu, Z. Li, Z. Wu, W. Lee, and G. Jiang, “Chex: Statically vetting

Android apps for component hijacking vulnerabilities,” in Proc. ACM
Conf. Comput. Commun. Secur., New York, NY, USA, 2012, pp. 229–240.
[26] C. Marforio, H. Ritzdorf, A. Francillon, and S. Capkun, “Analysis of the

communication between colluding applications on modern smartphones,”
in Proc. 28th Annu. Comput. Secur. Appl. Conf., New York, NY, USA,
2012, pp. 51–60.
[27] D. Octeau, D. Luchaup, M. Dering, S. Jha, and P. McDaniel, “Composite

constant propagation: Application to Android inter-component commu-
nication analysis,” in Proc. IEEE/ACM 37th IEEE Int. Conf. Softw. Eng.,
2015, pp. 77–88.
[28] D. Octeau et al., “Effective inter-component communication mapping in

Android: An essential step towards holistic security analysis,” in Proc.
22nd USENIX Secur. Symp., Washington, DC, USA, 2013, pp. 543–558.
[29] J. Reardon, Á. Feal, P. Wijesekera, A. E. B. On, N. Vallina-Rodriguez,

and S. Egelman, “50 ways to leak your data: An exploration of apps’
circumvention of the Android permissions system,” in Proc. 28th USENIX
Secur. Symp., Santa Clara, CA, USA, 2019, pp. 603–620.
[30] D. Ö. ¸Sahin, O. E. Kural, S. Akleylek, and E. Kiliç, “A novel permission-

based Android malware detection system using feature selection based on
linear regression,” Neural Comput. Appl., vol. 35, pp. 4903–4918, 2023.
[31] J. Samhi, A. Bartel, T. F. Bissyandé, and J. Klein, “Raicc: Revealing atypi-

cal inter-component communication in Android apps,” in Proc. IEEE/ACM
43rd Int. Conf. Softw. Eng., 2021, pp. 1398–1409.
[32] G. S. Tuncay, S. Demetriou, K. Ganju, and C. A. Gunter, “Resolving the

predicament of Android custom permissions,” in Proc. 25th Annu. Netw.
Distrib. System Secur. Symp., San Diego, CA, USA, 2018, pp. 1–15.
[33] R. Vallée-Rai, P. Co, E. Gagnon, L. Hendren, P. Lam, and V. Sundaresan,

“Soot: A Java bytecode optimization framework,” in Proc. 1999 Conf.
Centre Adv. Stud. Collaborative Res., 2010, pp. 214–224.
[34] H. Wang, H. Liu, and Y. Guo, “Characterizing Android app signing

issues,” in Proc. 34th IEEE/ACM Int. Conf. Automated Softw. Eng., 2019,
pp. 280–292.
[35] S. Wang et al., “Evolution-aware runtime permission misuse detection for

Android apps,” 2022, arXiv:2201.1254.
[36] Y. Wang et al., “Runtime permission issues in Android apps: Taxonomy,

practices, and ways forward,” IEEE Trans. Softw. Eng., vol. 49, no. 1,
pp. 185–210, Jan. 2023.
[37] F. Wei and S. Roy, “Amandroid: A precise and general inter-component

data ﬂow analysis framework for security vetting of Android apps,” ACM
Trans. Privacy Secur., vol. 21, no. 3, pp. 1–32, 2018.
[38] J. Yan, X. Deng, P. Wang, T. Wu, J. Yan, and J. Zhang, “Characterizing

and identifying misexposed activities in Android applications,” in Proc.
33rd ACM/IEEE Int. Conf. Automated Softw. Eng., New York, NY, USA,
2018, pp. 691–701.


---

## Page 18

![Figure 3](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_3.jpeg)

![Figure 4](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_4.jpeg)

![Figure 5](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_5.jpeg)

![Figure 6](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_6.jpeg)

![Figure 7](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_7.jpeg)

![Figure 8](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_8.jpeg)

![Figure 9](../assets/Custom-Permission-Empirical (2024) Understanding Bad Development Practices of Android Custom Permissions in the Wild/fig_p18_9.jpeg)

ZHANG et al.: UNDERSTANDING THE BAD DEVELOPMENT PRACTICES OF ANDROID CUSTOM PERMISSIONS IN THE WILD

[39] Y. Yang, M. Elsabagh, C. Zuo, R. Johnson, A. Stavrou, and Z. Lin,

“Detecting and measuring misconﬁgured manifests in Android apps,” in
Proc. 2022 ACM SIGSAC Conf. Comput. Commun. Secur., New York, NY,
USA, 2022, pp. 3063–3077.
[40] Y. Zhang et al., “Vetting undesirable behaviors in Android apps with

permission use analysis,” in Proc. 2013 ACM SIGSAC Conf. Comput.
Commun. Secur., 2013, pp. 611–622.

Xiaohan Zhang (Student Member, IEEE) received
the BS degree in information security from Xidian
University, in 2017. He is currently working towards
the PhD degree in cyberspace security with Xid-
ian University, China. His research interests include
trusted computing, system security, and privacy pro-
tection.

Zhiyuan Yu (Student Member, IEEE) received
the BS degree in electrical engineering from the
Huazhong University of Science and Technology,
in 2019. He is currently working toward the PhD
degree with the Department of Computer Science
and Engineering, Washington University in St. Louis.
His research interests include IoT security, medical
security, and social privacy.

Xinghua Li (Member, IEEE) received the ME and
PhD degrees in computer science from Xidian Uni-
versity, in 2004 and 2007, respectively. He is cur-
rently a professor with the School of Cyber Engineer-
ing, Xidian University, China. His research interests
include wireless networks security, privacy protec-
tion, cloud computing, and security protocol formal
methodology.

Cen Zhang received the ME degree in computer sci-
ence from the University of Science and Technology
of China, in 2017. He is currently working toward
the PhD degree with Nanyang Technological Univer-
sity. His research interests include center arounds the
software vulnerability including fuzzing, ﬁrmware
rehosting, and program analysis.

Cong Sun (Member, IEEE) received the BS degree
in computer science from Zhejiang University, Zhe-
jiang, China, in 2005, and the PhD degree in computer
science from Peking University, China, in 2011. He
is currently a full professor with the School of Cyber
Engineering, Xidian University, China. His research
interests include information ﬂow security, software
security, and program analysis.

Ning Zhang (Member, IEEE) received the PhD de-
gree from Virginia Tech, in 2016. He is currently
an assistant professor leading with the Laboratory of
Computer Security and Privacy (CSPL), Department
of Computer Science and Engineering, Washington
University in St. Louis. His research interest includes
cyber-physical security.

Robert H. Deng (Fellow, IEEE) is currently AXA
chair professor in cybersecurity and professor in in-
formation systems with the School of Information
Systems, Singapore Management University, since
2004. His research interests include data security and
privacy, multimedia security, network, and system
security.Hehasservedontheeditorialboardsofmany
international journals, including TFIS, IEEE Trans-
actions on Dependable and Secure Computing. He
has received the Distinguished Paper Award (NDSS
2012), Best Paper Award (CMS 2012), Best Journal
Paper Award (IEEE Communications Society 2017).


---

---
title: "40_Zhang_et_al.,_VetDroid_Permission_Use_Analysis"
creator: " TeX output 2013.09.10:1007"
pages: 12
---

# 40_Zhang_et_al.,_VetDroid_Permission_Use_Analysis

> **總頁數**：12 頁

---

## Page 1

Vetting Undesirable Behaviors in Android Apps with

Permission Use Analysis

| 1 | 1 | 1 | 1 |
| --- | --- | --- | --- |
| Yuan Zhang | Min Yang | Bingquan Xu | Zhemin Yang |
| 2 | 3 | 1 | 1 |
| Guofei Gu | Peng Ning | X. Sean Wang | Binyu Zang |

1

School of Computer Science, Fudan University, China

{yuanxzhang, m_yang, xubingquan, yangzhemin, xywangCS, byzang}@fudan.edu.cn

2

SUCCESS Lab, Texas A&M University, USA, guofei@cse.tamu.edu

3

Department of Computer Science, North Carolina State University, USA, pning@ncsu.edu

| Abstract | 1. | INTRODUCTION |  |  |
| --- | --- | --- | --- | --- |
| Android platform adopts permissions to protect sensitive resources | Smartphone platforms are becoming more and more popular |  |  |  |
| from untrusted apps. | However, after permissions are granted by | these days [5]. To protect sensitive resources in the smartphones, |  |  |
| users at install time, apps could use these permissions (sensitive | permission-based isolation mechanism [13] is used by modern |  |  |  |
| resources) with no further restrictions. | Thus, recent years have | smartphone systems to prevent untrusted apps from unauthorized |  |  |
| witnessed the explosion of undesirable behaviors in Android apps. | accesses. | In Android, an app needs to explicitly request a set |  |  |
| An important part in the defense is the accurate analysis of Android | of permissions when it is installed. | However, after permissions |  |  |
| apps. | However, traditional syscall-based analysis techniques are | are granted to an app, there is no way to inspect and restrict |  |  |
| not well-suited for Android, because they could not capture critical | how these permissions are used by the app to utilize sensitive |  |  |  |
| interactions between the application and the Android system. | resources. | Unsurprisingly, Android has attracted a huge number |  |  |
| This paper presents | VetDroid | , a dynamic analysis platform for | of attacks. | According to McAfee threat report of Q3 2012 [6], |
| reconstructing sensitive behaviors in Android apps from a novel | Android remains the largest target for mobile malware and the |  |  |  |
| permission use perspective. | VetDroid | features a systematic frame- | number almost doubled in Q4 2012. | While these malware apps |
| work to effectively construct permission use behaviors, i.e., how | are clear examples containing undesirable behaviors, unfortunately |  |  |  |
| applications use permissions to access (sensitive) system resources, | even in supposedly benign apps, there could also be many hidden |  |  |  |
| and how these acquired permission-sensitive resources are further | undesirable behaviors such as privacy invasion. |  |  |  |
| utilized by the application. With permission use behaviors, security | An important part in the fight against these undesirable behaviors |  |  |  |
| analysts can easily examine the internal sensitive behaviors of an | is the analysis of sensitive behaviors in Android apps. Traditional |  |  |  |
| app. | Using real-world Android malware, we show that | VetDroid | analysis techniques reconstruct program behaviors from collected |  |
| can clearly reconstruct fine-grained malicious behaviors to ease | program execution traces. A rich literature exists (see, e.g., [14, 16, |  |  |  |
| malware analysis. We further apply | VetDroid | to 1,249 top free apps | 21, 22, 33, 40, 49]) that focuses on solutions to construct effective |  |
| in Google Play. | VetDroid | can assist in finding more information | behavior representations. | All these research efforts have mostly |
| leaks than TaintDroid [24], a state-of-the-art technique. In addition, | used system calls to depict software behaviors because system calls |  |  |  |
| we show how we can use | VetDroid | to analyze fine-grained causes of | capture the intrinsic characteristics of the interactions between an |  |
| information leaks that TaintDroid cannot reveal. Finally, we show | application and the underlying system. Previous studies differ from |  |  |  |
| that | VetDroid | can help identify subtle vulnerabilities in some (top | each other only in how to structure the set of system calls made |  |
| free) applications otherwise hard to detect. | by the applications [17]. | However, previous work is not readily |  |  |

applicable due to the following unique features of Android:

Categories and Subject Descriptors Android Framework Managed Resources. Android is an applica-

tion framework on top of Linux kernel [51] where applications do

D.4.6 [ Operating Systems ]: Security and Protection; D.2.1 [ Software not directly use system calls to access system resources. Instead,

Engineering ]: Requirements/Specifications most system resources in Android are managed and protected by

the Android framework, and the application-system interactions

| Keywords | occur at a higher semantic level (such as accessing contacts, call |  |  |  |
| --- | --- | --- | --- | --- |
| Android security; | permission use analysis; | vetting undesirable | history) than system calls at the Linux Kernel level. | Indeed, |
| behaviors; Android behavior representation | Android provides specific APIs for applications to access system |  |  |  |

resources and regulates the access rules. Using system calls to learn

| Permission to make digital or hard copies of all or part of this work for personal or | the interaction behaviors between applications and Android will |  |  |
| --- | --- | --- | --- |
| classroom use is granted without fee provided that copies are not made or distributed | lose a semantic view of accesses to Android resources, degrading |  |  |
| for profit or commercial advantage and that copies bear this notice and the full citation | the quality and precision of the reconstructed behaviors. |  |  |
| on the first page. | Copyrights for components of this work owned by others than | Binder Inter-Process Communication (IPC). | In Android, system |
| ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or | services are provided in separated processes, with a convenient IPC |  |  |

republish, to post on servers or to redistribute to lists, requires prior specific permission

| and/or a fee. Request permissions from permissions@acm.org. | mechanism (Binder) to facilitate the communication among system |  |
| --- | --- | --- |
| CCS’13, | November 4–8, 2013, Berlin, Germany. | services and applications. Binder IPC is heavily used in Android |
| Copyright 2013 ACM 978-1-4503-2477-9/13/11 ...$15.00. | and recommended in the design of applications. | The wide use |

l http://dx.doi.org/10.1145/2508859.2516689.

---

## Page 2

| of IPC also brings problems to traditional syscall-level behavior | To evaluate the effectiveness of permission use behavior and |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reconstruction. First, traditional solutions would only intercept a | VetDroid | , we first use | VetDroid | to analyze real-world Android |  |
| lot of system calls used to interact with the Binder driver, hiding | malware. | The results show that the permission use behaviors |  |  |  |
| the real actions performed by the application. | Second, the use | reconstructed by | VetDroid | can significantly ease the malware |  |
| of IPC in Android apps breaks the execution flow of an app into | analysis. We further apply | VetDroid | to more than one thousand top |  |  |
| chains among multiple processes, making the evasion of traditional | free apps in Google Play Store. | VetDroid | finds more information |  |  |
| syscall-based behavior monitoring easier [42]. | leaks than the state-of-the-art leak detection system TaintDroid |  |  |  |  |
| Event Triggers. | Android employs an event trigger mechanism to | [24], and shows its capability to analyze the fine-grained incentives |  |  |  |
| notify interested applications when certain (hardware) events occur. | of information leaks among the apps. Furthermore, | VetDroid | even |  |  |
| In this model, for example, if an application wants to be notified | detects subtle | Account Hijack Vulnerability | in a top free Android |  |  |
| when the phone’s location changes, it just needs to register a | app. The analysis overhead caused by | VetDroid | is reasonably low |  |  |
| callback for such an event. When Android sniffs a location change | for an offline analysis tool. |  |  |  |  |
| event from the location sensors, it notifies all the interested appli- | This paper makes the following major contributions: |  |  |  |  |
| cations of the latest location by invoking their registered callbacks. | • | We analyze the limitations of existing syscall-based behavior |  |  |  |
| This asynchronous resource access model via system delivery is | analysis methods when applied to Android platform and |  |  |  |  |
| quite different from the synchronous application-request access | propose permission use behavior as a new perspective to |  |  |  |  |
| model. A key observation is that application registered callbacks | analyze Android apps. |  |  |  |  |
| are application code, so they could evade system call interception. | • | We present a systematic framework to reconstruct permission |  |  |  |
| As a result, traditional behavior reconstruction methods will lose | use behaviors. Our automated solution is able to completely |  |  |  |  |
| such important application behaviors. | identify all possible permission use points with accurate |  |  |  |  |
| The above analysis indicates that a general method to reconstruct | permission information. |  |  |  |  |
| sensitive behaviors of Android apps is highly desired. | Since | • | We implement a prototype system, | VetDroid | , and evalu- |
| Android does not use system calls as the main mechanism to | ate its effectiveness in analyzing real-world Android apps. |  |  |  |  |
| isolate applications, system calls do not appear to be a good vehicle | VetDroid | not only greatly eases the analysis of malware |  |  |  |
| for representing behaviors. | Considering the unique permission- | behaviors, but also assists in identifying fine-grained causes |  |  |  |
| based isolation mechanism in Android, we propose to reconstruct | for information leakages and even subtle vulnerabilities in |  |  |  |  |
| sensitive behaviors for Android apps from a novel | permission use | benign Android apps otherwise hard to detect. |  |  |  |
| perspective, i.e., how applications use permissions to interact with | The rest of this paper is organized as follows. §2 introduces some |  |  |  |  |
| the Android system and sensitive resources. | We define a new | background information about Android and defines the permission |  |  |  |
| concept, | permission use behavior | , which captures what and how | use behavior. | §3 describes our overall behavior reconstruction |  |
| permissions are used to access system resources, as well as how | approach. After that, we present our evaluation results in §4 and |  |  |  |  |
| these resources are further utilized by the application internally. | discuss possible limitations & further improvements in §5. Finally, |  |  |  |  |
| Accordingly, we define two kinds of permission use points: | Explicit | we discuss related work in §6 and conclude our paper in §7. |  |  |  |

permission use points (E-PUP) denote those callsites of Android

APIs in applications that explicitly request the permission-sensitive

points of the acquired sensitive resources that are requested with

ACCESS_FINE_LOCATION and INTERNET permissions during

the installation time. Its permission use behavior should track the

explicit points where these two permissions are requested and also

all the implicit points where the location and network resources

are used inside the application. In this case, any point where two

permissions are intertwined is of particular interest because it might

indicate possible location leakage to the network.

In this paper, we design a dynamic analysis system called

VetDroid to automatically construct permission use behaviors for

Android apps. VetDroid features a systematic permission use

analysis to identify a complete set of E-PUP s and I-PUP s with

accurate permission use information during the runtime. Our

proposed permission use analysis is composed of two components:

E-PUP Identifer which intercepts all invocations to Android APIs

and sniffs accurate permission check information from Android’s

permission enforcement system to identifies all the E-PUP s with

accurate permission use information, and I-PUP Tracker which

takes the asynchronous resource delivery model into account to

recognize the exact delivery point in the application for each

resource requested at a E-PUP and locates all the I-PUP s of these

resources by permission-based tainting analysis. VetDroid also

features a driver to enlarge the scope of the dynamic analysis

to cover more application behaviors and a behavior profiler to

generate behavior graphs with highlighted sensitive behaviors for

analysts to examine.

Android is the most popular mobile operating system today. It

is built on top of more than 100 open source projects including

Linux kernel. To enhance the security, Android is designed to be

a privilege-separated operating system, in which each application

runs with a distinct system identity (Linux UID and GID). The

system components are also isolated into distinct identities. With

the help of the identity isolation mechanism in Linux, applications

in Android are isolated from each other and from the system.

Android employs a quite efficient and convenient IPC mecha-

nism, Binder, which is extensively used for interaction between

applications as well as for application-OS interfaces. Binder is

implemented as a kernel driver and user-level applications could

just interact with it through standard system calls, e.g., open(),

ioctl(). Binder is the key infrastructure of Android system and

aggressively used to connect various parts of the system together.

To facilitate resource accessing from isolated applications and

data sharing among applications and the system, Android designs a

permission-based security mechanism [26]. Each application needs

permissions to access system resources. These permissions are

granted from users at install time. At runtime, each application

is checked by Android before accessing sensitive resources. Any

access to resources without granted permissions will be denied.

The permission mechanism in Android is fine-grained [30] which

is different from iOS [11]. In Android 4.2, there are 130 items of

sensitive resources that are protected with permissions [1].

resources; Implicit permission use points (I-PUP) denote the use 2. PROBLEM STATEMENT

permissions. For example, assume an application requests both 2.1 Android Background

---

## Page 3

| The Android application framework forces a component-based | app has been granted the corresponding permissions at install |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| application model [26] to increase the code reusability. | It does | time. Because permission checks explicitly occur during | resource |  |  |  |
| not have a main() function or any single entry point for execution. | request stage | , we denote the callsites in the app that invoke Android |  |  |  |  |
| Instead, Android apps must be developed in terms of components. | APIs to request protected system resources as | explicit permission |  |  |  |  |
| There are four types of components defined in Android’s pro- | use points (E-PUP) | . |  |  |  |  |
| gramming model: | Activity | component has a user interface and | After the | resource request stage | , | system resources may be |
| handles the interactions with user, | Service | component performs | delivered to the app synchronously or asynchronously, depending |  |  |  |
| background processing, | ContentProvider | component stores and | on the API used to request resources. | The | resource delivery |  |
| shares data such as a relational database, and | BroadcastReceiver | point | is the starting point to learn the behaviors of utilizing |  |  |  |
| component handles messages from other components, including | sensitive resources inside an app, and thus is very important for |  |  |  |  |  |
| the system. The primary mechanism for component interactions is | reconstructing permission use behaviors. |  |  |  |  |  |
| through an | Intent | , which is simply a message object encapsulating | Finally, when the requested resources have been delivered to the |  |  |  |
| the information of interest to the component that receives the intent | app, they may be processed by application-specific logic, which |  |  |  |  |  |
| such as the action to be taken and the data to act on, and some | reflects the internal behaviors of utilizing sensitive resources. For |  |  |  |  |  |
| meta data managed by Android system. | A component can be | example, the location resource may be used by an app to suggest the |  |  |  |  |
| protected by permissions and only those applications with granted | restaurants nearby, or may be used by a malicious entity to track the |  |  |  |  |  |
| permissions can interact with the privileged component. | victim. Although the further processing of acquired resources in an |  |  |  |  |  |

app does not cause additional permission checks against the app,

| 2.2 | Motivation | it is still important to track the further use of these resources. In |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Existing work [14, 21, 33, 40, 49] on behavior analysis has | this paper, these internal use points of the protected resources are |  |  |  |  |
| mostly used system calls to depict application’s internal behaviors. | denoted as | implicit permission use points (I-PUP) | . | I-PUP | s make |
| However, previous work has problems when applied to Android | the critical behaviors stand out from other irrelevant application- |  |  |  |  |
| platform due to Android’s new security model. | As explained | specific actions to ease the analysis of the app. |  |  |  |
| in §1, these problems make traditional solutions not well-suited | Permission Use Behavior. | As described above, | E-PUP | s |  |
| for monitoring fine-grained Android behaviors such as accesses | capture what and where permissions are used by the application, |  |  |  |  |
| to Android managed resources, interactions with system services | while | I-PUP | s capture how the application uses permissions to |  |  |
| through Binder IPC, and responses to privileged system events. | implement their specific logic. | However, a single permission |  |  |  |
| TaintDroid [24] alerts information leaks inside an Android app | use point only represents a sensitive action performed by the |  |  |  |  |
| via dynamic taint tracking. | AppIntent [57] redefines the privacy | application, and does not necessarily capture a meaningful behavior |  |  |  |
| leakage as user-unintended sensitive data transmission and designs | for analyzing applications. Based on the | E-PUP | s and | I-PUP | s, we |
| a new technique, event-space constraint symbolic execution, to | now formally define permission use behaviors. |  |  |  |  |

distinguish intended and unintended transmission. However the

| two tools could neither analyze other kinds of undesirable be- | D | EFINITION | 1. | A Permission Use Behavior is a function call |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| haviors such as stealthily sending SMS, nor examine the internal | graph | G | = ( | V, E, α | ) | over a set of permissions | P | where: |  |  |  |  |  |  |  |
| logic of sensitive behaviors. | ProfileDroid [53] is a behavior | • | the set of vertices | V | = | V | E | − | P U P | ∪ | V | I | − | P U P | , and it consists |
| profiling system for Android apps which is also not suitable | of all E-PUPs and I-PUPs, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| for analyzing internal behavior logic. | DroidScope [56] is an | • | the set of edges | E | ⊑ | V | × | V | , and each edge connects nodes |  |  |  |  |  |  |
| analysis platform designed for Android that extends traditional | that use the same permission, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| techniques to cover Java semantics. | However, the problem of | • | the labeling function | α | : | V | → | P | , and it associates each |  |  |  |  |  |  |
| analyzing Android apps is not simple as how to capture behaviors | node with permission(s) it uses. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

from different language implementations. It is hard to conduct

| effective analysis without considering Android’s specific security | With permission use behaviors, the interactions between applica- |  |  |
| --- | --- | --- | --- |
| mechanism. | Permission Event Graph [20], which represents the | tions and the Android system are effectively abstracted because it |  |
| temporal order between Android events and permission requests, is | describes how applications request system resources and internally |  |  |
| proposed to characterize unintended sensitive behaviors. However, | use the acquired system resources. | However, the two kinds of |  |
| this technique could not capture the internal logic of permission | permission use points are hard to identify due to some unique |  |  |
| usage, especially when multiple permissions are intertwined. | features of Android and application-specific logic. We thus design |  |  |
| From the above short analysis of existing work, we find that | an analysis platform called | VetDroid | to automatically reconstruct |
| they do not take full consideration of permission-based isolation | permission use behaviors from Android apps. |  |  |

mechanism in Android [13], which we believe to be important to

| understand behaviors of these applications. | Thus, in this paper | 3. | VETDROID DESIGN |
| --- | --- | --- | --- |
| we propose to reconstruct permission use behaviors as a new and | The overview of | VetDroid | design is shown in Figure 1. Sample |
| complementary aspect in analyzing Android apps. | applications are first loaded into | Application Driver | , which auto- |

matically executes the application in our sandbox (details described

| 2.3 | Definition of Permission Use Behavior | in §3.3). During the execution, | Permission Use Analysis | module |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Permission use behaviors aim to capture apps’ internal sensitive | identifies all the | E-PUP | s, | I-PUP | s and their relationships. | These |
| behaviors on utilizing system resources that are protected by | behaviors are recorded by | Log Tracer | with runtime information |  |  |  |
| some permissions. According to the lifecycle of utilizing system | into a log file. | The log file is offline processed by | Behavior |  |  |  |
| resources inside an app, we define different kinds of permission | Profiler | to automatically construct behavior representations (details |  |  |  |  |
| use points (PUP). First, an app needs to invoke some Android APIs | described in §3.4). |  |  |  |  |  |
| to request system resources, which we call | resource request stage | . | The key challenge in our approach is on the effectiveness |  |  |  |
| If the requested resources are protected by some permissions, | of | permission use analysis | , i.e., how to | completely | identify all |  |
| Android’s permission enforcement system will check whether this | the permission use points with | accurate | permission information |  |  |  |

---

## Page 4

Application Layer System Services

Permission Use Analysis

E-PUP Identifier

Application Driver

Log Tracer

Figure 1: Overview of VetDroid

permission mechanism and programming model. Our systematic

keeps tracking of the resources requested at each E-PUP to trace

3.1 E-PUP Identifier

During the execution, applications may request system resources

that are protected by some permissions. E-PUP s represent such

behaviors in the application. The key feature of an E-PUP is that

it’s a callsite that invokes an Android API, and a permission check

occurs during the execution of this API. To reconstruct effective

permission use behaviors, the E-PUP Identifier should have two

application-system interface , which is a code boundary between

Behavior Profiler

VetDroid Sandbox

I-PUP Tracker

Log File

to reconstruct permission use behaviors for Android apps.

App.getLastLocation() .getLastKnownLocation()

VetDroid.clearPermCheckTags()

.getAllProviders()

Normal Point

No Permission Checked

VetDroid.getPermCheckTags() Ve V V tDroi id.getPe ermCh C C e e eckTa T T gs() ( (

Figure 2: An example of identifying E-PUP s.

huge performance penalty would be introduced. Fortunately, we

| Sample Apps(.apk) | Behavior Report |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and | precisely | track their relationships. | To correctly capture the | Application-System Interface |  |  |  |  |  |  |  |  |  |  |  |  |  |
| behaviors of using permissions inside an app, we analyze the | Application | System |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| execution flow of the application with regards to Android’s special | VetDroid.clearPermCheckTags() | LocationManagerService |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| permission use analysis contains two main components: | E-PUP | Explicit Permission Use Point: | ACCESS_FINE_LOCATION |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Identifier | , which identifies all | E-PUP | s with accurate permission | ACCESS_FINE_LOCATION | Permission Checked |  |  |  |  |  |  |  |  |  |  |  |  |
| information (details described in §3.1); and | I-PUP Tracker | , which | VetDroid.getPermCheckTags() | Ve | V | V tDroi | id.getPe | e | ermCh | C | C e | e | eckTa | T | T gs() | ( | ( |
| all | I-PUP | s (details described in §3.2). | App.getLocationProviders() | LocationManagerService |  |  |  |  |  |  |  |  |  |  |  |  |  |
| properties. First, it should completely identify all the callsites that | permission enforcement system during the execution of an API |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| invoke privileged Android APIs. Second, it should catch accurate | and propagating the exact permission check information to the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| information about the permission checked by Android during the | application side, | E-PUP Identifier | could | completely | identify all the |  |  |  |  |  |  |  |  |  |  |  |  |
| execution of an API; otherwise the correctness and preciseness of | E-PUP | s with | accurate | permission use information, including those |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the reconstructed behaviors cannot be guaranteed. | invoked through Java reflection or Java Native Interface. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Existing work [12,27] has built privileged API lists with required | Figure 2 shows an example of identifying | E-PUP | s at the ap- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| permissions. | It seems that our | E-PUP Identifier | could leverage | plication side. | In this example, | App.getLastLocation() | invokes |  |  |  |  |  |  |  |  |  |  |
| such API-permission lists to identify | E-PUP | s by intercepting all | getLastKnownLocation() | API of | LocationManagerService | to get |  |  |  |  |  |  |  |  |  |  |  |
| APIs during the execution, and then looking up the permissions | the last known location. | Before invoking this API, | VetDroid |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| that would be checked in an API-permission list by matching API | clears the permission check information in the thread-local storage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| signatures. Unfortunately, existing API-permission lists are either | using | VetDroid.clearPermCheckTags() | . | During the execution of |  |  |  |  |  |  |  |  |  |  |  |  |  |
| incomplete [27] or inaccurate [12]. | Stowaway [27] uses Java | this API, Android’s permission enforcement system performs a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| reflection to execute Android APIs and monitors what permissions | permission check on | ACCESS_FINE_LOCATION | permission. At |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| are checked by the system. | To create appropriate arguments for | last, after the execution of | getLastKnownLocation() | API, | VetDroid |  |  |  |  |  |  |  |  |  |  |  |  |
| each API, Stowaway uses API fuzzing to automatically generate | invokes | VetDroid.getPermCheckTags() | to propagate the permission |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| test cases. Although Stowaway’s API-permission list is accurate, | check information from the enforcement system to the application |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| it is quite incomplete due to the fuzzer’s inability to generate | side. | With the propagated permission check information, this |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| complete inputs for all Android APIs. To achieve a good coverage, | callsite in | App.getLastLocation() | is identified as an | E-PUP | of |  |  |  |  |  |  |  |  |  |  |  |  |
| PScout [12] adopts static analysis to extract API-permission lists | ACCESS_FINE_LOCATION | permission. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from Android source code. | Although PScout’s API-permission | The | application-system interface | is recognized at every function |  |  |  |  |  |  |  |  |  |  |  |  |  |
| list is relatively complete, it is not accurate enough, because an | call site by checking whether the caller is application code and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Android API could use different permissions at runtime according | the callee is system code. As Android apps are mostly developed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to its arguments, which is also acknowledged by its authors [12]. | in the Java language and run on the Dalvik virtual machine, we |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To implement a | both | complete and accurate | E-PUP Identifier | , we | instrument Dalvik to monitor all function calls. The algorithm to |  |  |  |  |  |  |  |  |  |  |  |  |
| need to design a new technique, as described below. | perform code origin checks should be very efficient, otherwise a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.1.1 | E-PUP Identification Strategy | find an efficient way to differentiate application code from system |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Based on our definition of | E-PUP | , we propose a straightfor- | code by checking their class loader, because system code is loaded |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ward identification strategy. | First, our technique identifies the | by a distinct class loader in Dalvik to ensure the VM integrity. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| application code and system code. Based on the | application-system | 3.1.2 | Acquire Permission Check Information |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| interface | , | E-PUP Identifier | could intercept all calls to Android | The complete identification of permission checks is the key to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| APIs. Then, by monitoring permission check events in Android’s | identify | E-PUP | s. With the permission check information, it’s easy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

Application System Service the IPC procedure. As all AndPermChk s are finally handled by

| Location | Activity | Package |
| --- | --- | --- |
| File | Binder |  |
| System | IPC |  |

Linux Kernel

to judge whether an application-system interface is an E-PUP or a

illustrates these two kinds of permission checks:

ActivityManagerService , we instrument its permission check logic

can be propagated back to the application side.

signed to every kernel-enforced permission, KerPermChk is en-

forced by the GID isolation mechanism. We instrument the GID

the checked GID to the corresponding permission reversely. To

application-system interface , two system calls are added to access

and clear the checked GID in the kernel thread-local storage.

accurate permission use information.

3.2 I-PUP Tracker

| App_1 | App_2 | Manager | Manager | Manager | ...... | to convey the permission check information to the Binder driver. |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Service | Service | Service | With the extended Binder driver, this permission check information |  |  |  |  |  |  |
| AndPermChk | AndPermChk | AndPermChk | Propagate KerPermChk Information. | With a unique GID as- |  |  |  |  |  |
| ReqSysResource ReqSysResource | ReqSysResource | Android Framework | isolation logic to record the checked GID into a kernel thread-local |  |  |  |  |  |  |
| KerPermChk | KerPermChk | storage. | The checked permission can be recognized by mapping |  |  |  |  |  |  |
| Network | acquire the permission check information from the kernel at the |  |  |  |  |  |  |  |  |
| Figure | 3: | Two | kinds | of | permission | checks | in | Android’s | Thus, with permission check information propagated to the |
| permission enforcement system. | application side, | E-PUP Identifier | could identify all | E-PUP | s with |  |  |  |  |
| normal call site (see | App.getLocationProviders() | in Figure 2). | While | E-PUP | s represent the behaviors of how an application |  |  |  |  |
| Android’s permission system is enforced by two modules: An- | use permissions to request sensitive resources, | I-PUP | s capture |  |  |  |  |  |  |
| droid system services and Linux kernel. According to the different | the internal behaviors of how the application manipulates these |  |  |  |  |  |  |  |  |
| permission enforcing techniques, we differentiate two kinds of | protected resources. | To track the resources use points inside an |  |  |  |  |  |  |  |
| permission checks in Android’s permission enforcement system: | app, | I-PUP Tracker | first needs to recognize the delivery point for |  |  |  |  |  |  |
| Android permission check | and | Kernel permission check | . Figure 3 | each requested resource in the application. |  |  |  |  |  |
| Android Permission Check (AndPermChk). | When an app tries | 3.2.1 | Recognize Resource Delivery Point |  |  |  |  |  |  |
| to access system resources that are protected by Android system | Android’s programming model complicates the identification of |  |  |  |  |  |  |  |  |
| services such as contacts and locations, | AndPermChk | s occurred. | resource delivery points in the application. Callbacks are heavily |  |  |  |  |  |  |
| Figure 3 gives an example of | AndPermChk | . | App_1 | tries to acquire | used in Android to monitor privileged system events, such as |  |  |  |  |
| the current location by invoking an interface of | LocationMan- | location change events and phone state change events. | There |  |  |  |  |  |  |
| agerService | via Binder. | LocationManagerService | first checks | are three types of callbacks in Android that can be registered to |  |  |  |  |  |
| whether | App_1 | has been granted | ACCESS_FINE_LOCATION | deliver system resources: | BroadcastReceiver | , | PendingIntent | , and |  |
| permission by invoking the general permission check interface of | Listener | . | BroadcastReceiver | is one of the four types of components |  |  |  |  |  |
| ActivityManagerService | . | The | AndPermChk | requests are finally | defined in the Android application model, as described in §2. |  |  |  |  |
| redirected to | PackageManagerService | except the permission re- | PendingIntent | [7] is a special Intent that can be sent back from a |  |  |  |  |  |
| quests from the system itself are granted immediately. | PackageM- | separate process on behalf of its creator. According to the ways of |  |  |  |  |  |  |  |
| anagerService | handles the permission check request by looking up | instantiating, a | PendingIntent | can be sent to an Activity, a Service |  |  |  |  |  |
| a table that records all the granted permissions for each application | or a BroadcastReceiver. | Listener | is a specialized class to handle |  |  |  |  |  |  |
| when it is installed. | According to the permission check result, | callbacks that can be triggered remotely. |  |  |  |  |  |  |  |
| LocationManagerService | judges whether to accept or deny the | For most cases, | BroadcastReceivers | are declared in the app’s |  |  |  |  |  |
| request from | App_1 | . | manifest file and registered to the system when the app is installed. |  |  |  |  |  |  |
| Kernel Permission Check (KerPermChk). | The permissions to | Android also provides APIs to register | BroadcastReceivers | at |  |  |  |  |  |
| protect file system and network are enforced by the Linux kernel. | runtime. | PendingIntents | and | Listeners | are registered via specific |  |  |  |  |
| As Figure 3 shows, the accesses to these resources should pass | Android APIs. | Since callbacks are used by a small number of |  |  |  |  |  |  |  |
| KerPermChk | s. | In Android, a unique GID is assigned to each | Android APIs, we choose to recognize the resource delivery point |  |  |  |  |  |  |
| kernel-enforced permission. An app is checked to verify whether it | by monitoring those APIs that may register callbacks. |  |  |  |  |  |  |  |  |
| has the corresponding GID before accessing the protected resource. | Although PScout’s privileged API list [12] is not accurate e- |  |  |  |  |  |  |  |  |
| Our identification of permission checks is implemented in An- | nough for | E-PUP Identifier | , it provides a complete list for picking |  |  |  |  |  |  |
| droid’s permission enforcement system, while | E-PUP Identifier | out APIs that register callbacks. | However, there are more than |  |  |  |  |  |  |
| needs to acquire permission check information at the application | 10,000 distinct APIs in PScout’s API list for every Android version, |  |  |  |  |  |  |  |  |
| side to judge whether a callsite is an | E-PUP | and what permission | so it is hard to manually check every API. Thus, we use an auto- |  |  |  |  |  |  |
| is used by an | E-PUP | . For the two types of permission checks, the | matic method to filter out most APIs that definitely cannot register |  |  |  |  |  |  |
| permission check information is propagated differently: | callbacks, and manually check a small number of remaining APIs. |  |  |  |  |  |  |  |  |
| Propagate AndPermChk Information. | As Figure 3 shows, | And- | Since only one specific API can register | BroadcastReceivers |  |  |  |  |  |
| PermChk | is performed in a separate Android process. | The ap- | at runtime, our automatic filtering method mainly selects APIs |  |  |  |  |  |  |
| plication side has no idea about what permission is checked by | that register | PendingIntents | or | Listeners | . | Our selection strategy |  |  |  |
| what system service. It is difficult to automatically propagate the | is to find all potential APIs whose arguments may contain a |  |  |  |  |  |  |  |  |
| permission check information from a separate service process to the | PendingIntent | or a | Listener | . | We observe that | Listeners | can be |  |  |
| application. Since Android apps employ Binder to invoke remote | invoked from a separate/remote process, so they are Binder objects. |  |  |  |  |  |  |  |  |
| interfaces of a service process and the result is also returned via | Our selection algorithm first finds all the subclasses that extend |  |  |  |  |  |  |  |  |
| Binder, we choose to extend the Binder driver and its communica- | android.os.Binder | . | As an API may declare an interface as the |  |  |  |  |  |  |
| tion protocol to propagate the permission check information during | argument type, our algorithm further collects a list for the interfaces |  |  |  |  |  |  |  |  |

---

## Page 6

| that each Binder subclass implements. At last, our filtering method | parameter values. If the tag is non-zero, the function is an | I-PUP |  |  |  |
| --- | --- | --- | --- | --- | --- |
| looks up PScout’s API list to select those APIs with an argument | for the permission represented by the tag. |  |  |  |  |
| type contained in the subclass list or the interface list. For Android | After identifying resource delivery points and performing the |  |  |  |  |
| 2.3, our filtering method finds 232 APIs that may register | Listeners | . | permission-based taint analysis, | I-PUP Tracker | could trace all the |
| PendingIntent | is easy to handle, because it is defined as a final | use points of resources with accurate permission information. |  |  |  |

class in Android. After a search on PScout’s API list, our method

PUP is also the resource delivery point. Since BroadcastReceiver

After the resource is delivered to the application, it can be used

in different ways with application-specific logic that makes the

identification of I-PUP s quite difficult. To solve this problem, we

use dynamic taint tracking to capture the resource usage inside the

application. However, traditional taint analysis cannot be applied

directly. The key challenge is to automatically taint related data

information. The taint tag is represented as a 32-bit integer. Each

Automatic Data Tainting. After a taint bit is allocated for an

the I-PUP Tracker . It could be performed at the instruction-level,

and compute a taint tag for each function. The tag for a function

each Activity .

permission use behaviors from the application.

It is worth noting that our Application Driver could not guarantee

generally a difficult problem for all dynamic analysis work. This

paper tries to design a better behavior approximation for analyzing

Android apps, and leaves the coverage problem as our future work

(as discussed in §5).

3.4 Behavior Profiler

use graphs for further analysis.

each permission.

| finds 58 APIs whose arguments contain a | PendingIntent | . | Then | 3.3 | Application Driver |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| we manually verify the total 286 APIs (4 APIs register both | Unlike traditional applications, there is no single entry point for |  |  |  |  |  |  |
| PendingIntents | and | Listeners | ), and eventually we confirm 89 APIs | an Android app. | It brings problems to automatically executing |  |  |
| register | PendingIntents | or | Listeners | to acquire protected system | Android apps. Our | Application Driver | adopts a component-based |
| resources. | In this procedure, our automatic API filtering method | testing strategy. | It automatically extracts | Activities | and | Services |  |
| greatly reduces the manual efforts. | from the application and runs each component in the sandbox for |  |  |  |  |  |  |
| For our selected APIs that register callbacks, the resource deliv- | a while (the time depends on the concrete hardware platform). |  |  |  |  |  |  |
| ery point is the registered callback. While for other APIs, the | E- | Additionally, | Monkey | [9] is used to exercise the user interface for |  |  |  |
| can be registered by the manifest file, we parse the manifest file | Furthermore, some behaviors of Android apps are triggered by |  |  |  |  |  |  |
| of each analyzed app to collect declared | BroadcastReceivers | and | events. | Our | Application Driver | also injects fake events (such as |  |
| mark their | onReceive() | functions as the resource delivery points. | the arrival of new SMS, location change) during the monitoring |  |  |  |  |
| After the resource delivery points are recognized, the | I-PUP | s can | when certain callbacks are registered. | With the runtime injected |  |  |  |
| be tracked by following the resource usage inside the app. | events, | Permission Use Analysis | module could reconstruct more |  |  |  |  |
| 3.2.2 | Permission-based Taint Analysis | a complete coverage over all possible behaviors. | In fact, this is |  |  |  |  |
| for each delivered resource with permission information. | Our | During the execution of the application in | VetDroid | sandbox, | Log |  |  |
| permission-based taint analysis works in the following steps. | Tracer | collects the behaviors reported by | Permission Use Analysis |  |  |  |  |
| Tag Allocation. | A taint tag is allocated at each | E-PUP | to | module with runtime information to a log file. | Behavior Profiler |  |  |
| mark the requested resource with corresponding permission check | analyzes the log file offline to automatically generate permission |  |  |  |  |  |  |
| bit of the tag corresponds to a unique | E-PUP | . Our tag allocation | Behavior Profiler | first identifies all the | E-PUP | s from the log |  |
| is context-sensitive, which means the same tag will be assigned to | file. For each | E-PUP | , | Behavior Profiler | further collects all | I-PUP | s |
| E-PUP | s with the same calling context. The reason for this strategy | for the requested permission by tracking the same tag bit. | By |  |  |  |  |
| is to prevent the explosion of tag bits while different | E-PUP | s are | connecting these permission use points according to the execution |  |  |  |  |
| still distinguishable. | orders, | Behavior Profiler | could draw a permission use graph for |  |  |  |  |
| E-PUP | , the corresponding acquired system resource needs to be | As Android adopts a fine-grained permission model [30] to |  |  |  |  |  |
| automatically tainted with the tag. | The automatic data tainting | protect system resources, our insight is that applications usually |  |  |  |  |  |
| occurs at the resource delivery point for each | E-PUP | . For APIs | need to use multiple permissions together to accomplish a mean- |  |  |  |  |
| that register callbacks, a wrapper is added around each registered | ingful behavior. | Based on this observation, | Behavior Profiler |  |  |  |  |
| callback to taint the delivered protected data according to the | searches all the permission use graphs to connect those graphs |  |  |  |  |  |  |
| concrete type of the callback so that the related data gets tainted | with an overlapped node (which uses at least two permissions) |  |  |  |  |  |  |
| only when the callback is triggered. | For other APIs, two kinds | to form a new permission use graph. | The permission use graph |  |  |  |  |
| of data are automatically tainted according to the signature of the | with multiple permissions captures interesting behaviors for anal- |  |  |  |  |  |  |
| API: 1) The return value of the API at each | E-PUP | should be | ysis, as will be demonstrated later in the evaluation. | Behavior |  |  |  |
| tainted with the corresponding tag. 2) As Java is an object-oriented | Profiler | automatically discards permission use graphs that use |  |  |  |  |  |
| language, the state of an object may be modified by instance | only a single (less interesting) permission with the exception of |  |  |  |  |  |  |
| methods. For instance APIs, we also taint the invoked object with | those graphs using a high-risk permission such as | SEND_SMS, |  |  |  |  |  |
| the tag allocated at the | E-PUP | . | CALL_PHONE | . The profiled permission use graphs capture the |  |  |  |
| Identify I-PUPs. | Dynamic taint tracking is employed to follow | behaviors of using permissions inside an application, especially |  |  |  |  |  |
| the propagation of tainted resource data. | I-PUP | is identified by | when multiple permissions are intertwined. With such permission |  |  |  |  |
| recognizing the use point of tainted data. | The granularity of the | use graphs, experts could inspect the internal logic of Android apps |  |  |  |  |  |
| identification is quite important to the quality and efficiency of | to analyze suspicious behaviors, verify programming logic, etc. |  |  |  |  |  |  |
| but a single instruction is too fine-grained to depict a meaningful | 4. | PROTOTYPE & EVALUATION |  |  |  |  |  |
| action. | Thus, we choose to identify | I-PUP | at the function-level. | A prototype of | VetDroid | is implemented based on Gingerbread |  |
| We intercept all function invocations in the Dalvik virtual machine | (Android 2.3). | 1 | This prototype currently supports running on |  |  |  |  |
| is calculated by a bitwise OR operation on the taint tags of its | 1 | Note that our techniques are not limited to this specific version. |  |  |  |  |  |

---

## Page 7

| Samsung Nexus S phones and emulators. | The | Application Driv- | Behaviors | # | Malware Families |  |
| --- | --- | --- | --- | --- | --- | --- |
| er | and | Behavior Profiler | are implemented in Python. | E-PUP | Steal SMS | 46 BaseBridge, SMSReplicator, Zitmo, Gone60 |
| Identifier | instruments the Dalvik virtual machine to intercept all | Steal Phone | ADRD, YZHC, GoldDream, Pjapps, GGTracker |  |  |  |

API invocations, and enhances the Linux kernel as well as the

application side. I-PUP Tracker modifies the Android framework

all, VetDroid modifies and enhances several main components in

virtual machine, to implement a systematic permission use analysis

malicious behaviors with permission use graphs. Next, we report

our findings on vetting more than one thousand top free apps

that we have collected from Malware Genome Project [59]. To

for 120 seconds. Our hardware platform is an AMD server with

4*4 cores (2GHz) and 16GB memory. In all, 5,990 components

are executed, which last totally about 22 hours (i.e., 2.2 minutes per

sample). The reconstructed behaviors are automatically classified

by their E-PUP s and further manually confirmed and categorized.

help reveal undesirable behaviors.

38

Number GingerMaster, DroidDream, DroidKungFu[1-4]

Steal Contact 8 Zitmo, Gone60, Walkinwat

Track Loc. 9

Bgserv, DroidKungFu2, DroidKungFu4

Send SMS 43

X2=0x40520050(type=android.app.ReceiverRestrictedContext),

X3=0x405144f8(android.content.Intent)

RECEIVE_SMS

tag=0x1)

RECEIVE_SMS

X1=" 99735 "(type=java.lang.String, tag=0x1)

It blocks SMS !

RECEIVE_SMS

Figure 4: SMS Blocking behavior in GGTracker .

"33335", "36397", etc.

Auto Reply behavior due to the loss of fine-grained semantic and

context information, while VetDroid can clearly reconstruct such

| Binder driver to acquire accurate permission use information at the | TapSnake, DroidDream, DroidKungFu1 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| to monitor registrations and invocations of application callbacks, | Pjapps, Zsone, Walkinwat, RogueSPPush |  |  |  |  |  |  |
| and extends the taint tracking logic in TaintDroid [24] to implement | GGTracker, FakePlayer, SMSReplicator |  |  |  |  |  |  |
| the permission-based taint analysis (as described before). | In | Block SMS | 22 Zitmo, RogueSPPush, GGTracker, Zsone |  |  |  |  |
| Android including the Linux kernel, the Binder driver, the Dalvik | Table 1: Example behaviors analyzed by | VetDroid |  |  |  |  |  |
| framework. | android.permission.RECEIVE_SMS, Tag: 0x1 |  |  |  |  |  |  |
| We evaluate | VetDroid | from three aspects. | We first apply | Vet- | t4t.power.management.activity.SmsReceiver;onReceive( | X1, X2,X3 | ) |
| Droid | to real-world Android malware and analyze their internal | X1=0x40519b10(type=t4t.power.management.activity.SmsReceiver, tag=0x1), |  |  |  |  |  |
| in Google Play with | VetDroid | . | Finally, we measure the runtime | com.android.internal.telephony.SmsMessageBase;getOriginatingAddress( | X1 | ) |  |
| overhead of | VetDroid | . | X1=0x40521098(type=com.android.internal.telephony.gsm.SmsMessage, |  |  |  |  |
| 4.1 | Real-World Malware Study | java.lang.String;equals(X1, X2) |  |  |  |  |  |
| We have used | VetDroid | to analyze 600 Android malware samples | X2="99735"(type=java.lang.String, tag=0x0) | Dangerous API ! |  |  |  |
| efficiently construct permission use behaviors, | Application Driver | t4t.power.management.activity.SmsReceiver; abortBroadcast( | X1 | ) |  |  |  |
| runs these samples in 10 emulators and each component is executed | X1=0x40519b10(type=t4t.power.management.activity.SmsReceiver, tag=0x1), |  |  |  |  |  |  |
| Table 1 lists six example categories of interesting malicious | provider to sign up a premium-rate service. This behavior is critical |  |  |  |  |  |  |
| behaviors [59] captured by | VetDroid | . | We can find that these | to understand the internal logic of this malware. |  |  |  |
| malware either steals users’ sensitive data or incurs financial | We observe two kinds of behaviors in | GGTracker | with | VetDroid | . |  |  |
| charge. We also compare the analysis results with those reported | Figure 4 shows the | SMS blocking | behavior. | When a new SMS |  |  |  |
| by Malware Genome Project [59]. | Unfortunately, the Command | arrives, | t4t.power.management.activity.SmsReceiver | is triggered. |  |  |  |
| and Control (C&C) servers [58] used by some samples were | Then | getOriginatingAddress | is invoked to get the sender’s number |  |  |  |  |
| not available during the analysis and some malicious behaviors | of this message. | The permission use graph clearly expresses |  |  |  |  |  |
| are only triggered under certain contexts, | so some behaviors | the constraints on the sender’s number in this malware. | If this |  |  |  |  |
| reported in [59] were not observed. In all, | VetDroid | successfully | SMS is sent from "99735", this message is blocked by invoking |  |  |  |  |
| analyzed 21 malware families and more importantly reconstructed | abortBroadcast() | . This function suppresses the broadcasting of the |  |  |  |  |  |
| their detailed behaviors, demonstrating its effectiveness in aiding | event about the arrival of a new SMS. Since | GGTracker | registers |  |  |  |  |
| malware analysis. | More interestingly, | VetDroid | captured some | its BroadcastReceiver with the highest priority, this SMS is hidden |  |  |  |
| previously unreported behaviors in dissected malware samples. For | from the user. By checking the constraints on the sender’s number |  |  |  |  |  |  |
| example, we found 38 BaseBridge samples exhibit | SMS Stealing | from the graph, we can direct the | Application Driver | to inject |  |  |  |
| behavior and 1 Zitmo sample has | SMS Blocking | behavior, which | faked SMS from other numbers (this can be easily implemented |  |  |  |  |
| have not been reported by Malware Genome Project yet. | This | with an emulator [8]) to cover more interested behaviors. At last, |  |  |  |  |  |
| further illustrates the advantages of our new analysis technique to | we confirm | GGTracker | also blocks SMS from "46621", "96512", |  |  |  |  |
| Due to space limit, we can only present some interesting case s- | Besides, we also observe | SMS Auto Reply | behavior by iteratively |  |  |  |  |
| tudies analyzed by | VetDroid | with permission use graphs: | GGTrack- | changing the sender’s number of the faked SMS. From Figure 5, we |  |  |  |
| er | , | SMSReplicator | , | TapSnake | . The permission use graphs capture | could find that when the malware intercepts a SMS from "41001", |  |
| the complete execution flow related to the malicious behaviors. | 2 | it automatically replies an SMS to "41001" with the content "YES" |  |  |  |  |  |
| The nodes with filled colors represent | E-PUP | s, while other nodes | using the | sendTextMessage | API. The | SMS Auto Reply | behavior is |
| represent | I-PUP | s. The edges in the graph depict the flow among | critical in this kind of malware that stealthily signs up infected |  |  |  |  |
| permission use points. | users to premium services. With | VetDroid | , this behavior is clearly |  |  |  |  |
| 1) Analysis of GGTracker. | revealed, enabling the detection and prevention of such attacks. |  |  |  |  |  |  |
| GGTracker | is known for its intent to automatically sign up | System Call Trace. | To have a brief comparison with syscall- |  |  |  |  |
| infected users to premium services. Due to the second-confirmation | based analysis, we use | strace | to collect system call trace during the |  |  |  |  |
| policy required in some countries, | GGTracker | needs to stealthily | execution of | SMS Auto Reply | behavior, as showed in Table 2. From |  |  |
| reply to an acknowledge SMS message sent from the service | the collected 33 system calls, it’s hard to recognize them as | SMS |  |  |  |  |  |
| 2 | In this paper we only present partial permission use graphs. | behavior with the analysis of permission use points and behaviors. |  |  |  |  |  |

---

## Page 8

| android.permission.RECEIVE_SMS, Tag: 0x1 | android.permission.RECEIVE_SMS, Tag: 0x1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| t4t.power.management.activity.SmsReceiver;onReceive( | X1, X2,X3 | ) | com.dlp.SMSReplicatorSecret.SMSReceiver;onReceive( | X1, X2,X3 | ) |
| X1=0x40519b10(type=t4t.power.management.activity.SmsReceiver, tag=0x1), | X1=0x4051bd18(type=com.dlp.SMSReplicatorSecret.SMSReceiver,tag=0x1) | , |  |  |  |
| X2=0x40520050(type=android.app.ReceiverRestrictedContext), | X2=0x405222c0(type=android.app.ReceiverRestrictedContext), |  |  |  |  |

X3=0x405144f8(android.content.Intent)

RECEIVE_SMS

X1=0x40521098(type=com.android.internal.telephony.gsm.SmsMessage,

RECEIVE_SMS

X1="41001"(type=java.lang.String, tag=0x1)

java.lang.String;equals(X1, X2)

RECEIVE_SMS

android.permission.SEND_SMS, Tag: 0x2

t4t.power.management.activity.SmsReceiver;onReceive()VLL---->

getpid,gettid 8 process information

clock_gettime 7 time information

Table 2: System call trace for SMS Auto Reply behavior.

2) Analysis of SMSReplicator.

SMSReplicator [3] is a spyware app targeting infected users’

incoming short messages. This malware protects itself by hiding its

is instantiated using createFromPdu() function of SmsMessage .

body is concatenated to send to a number specified by the attacker

via SMS. This graph clearly shows the permission use points of

three critical permissions ( RECEIVE_SMS, READ_CONTACTS,

SEND_SMS ). It is relatively easy to recognize this behavior as SMS

Forwarding . We can find that SMS Auto Reply behavior and SMS

disguises itself as the classic "snake" video game. During the instal-

X3=0x40519958(type=android.content.Intent)

RECEIVE_SMS

X1=0x405224d8(type=[B,tag=0x1)

android.permission.READ_CONTACTS, Tag: 0x2

android.content.ContentResolver;query( X1,X2,X3,X4,X5 )

RECEIVE_SMS

X2=0x40526a38(type=android.net.Uri$HierarchicalUri),

READ_CONTACTS

X2="***" (tag=0x3, display name queryed from the CONTACTS)

RECEIVE_SMS READ_CONTACTS

android.permission.SEND_SMS, Tag: 0x4

android.location.LocationManager; requestLocationUpdates( X1, X2,X3,X4 )

ake.LocationListener)

LOCATION

X1=0x40528310(type=net.maxicom.android.snake.LocationListener),

X2=0x40527568(type=android.location.Location, tag=0x4)

LOCATION

java.net.URI; <init>( X1, X2 )

X1=0x40529aa0(type=java.net.URI),

X2="?email=%22**%40gmail.com%22&code=%***%22&time=***&lat=*

*&lng=**&pro=gps&acc=0.01"(tag=0x4)

android.permission.INTERNET, Tag: 0x8

net.maxicom.android.snake.SnakeService$1$1; handleMessage()VL---->

X2=0x4053f238(type=org.apache.http.client.methods.HttpPost),

org.apache.harmony.luni.platform.OSNetworkSystem;writeImpl( X1,X2,X3,X4,X5 )

Figure 7: Location Track behavior in TapSnake .

| com.android.internal.telephony.SmsMessageBase;getOriginatingAddress( | X1 | ) | android.telephony.SmsMessage; createFromPdu( | X1 | ) |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tag=0x1) | RECEIVE_SMS |  |  |  |  |  |  |  |  |
| java.lang.String;equals(X1, X2) | com.dlp.SMSReplicatorSecret.SMSReceiver;onReceive()VLL----> |  |  |  |  |  |  |  |  |
| X2="99735"(type=java.lang.String, tag=0x0) | X1=0x4051b8c8(type= | android.app.ContextImpl$ApplicationContentResolver | ), |  |  |  |  |  |  |
| RECEIVE_SMS | X3=0x40526b00(type=Ljava/lang/String,tag=0x1) | ,X4=null,X5="display_name" |  |  |  |  |  |  |  |
| X1="41001"(type=java.lang.String, tag=0x1) | java.lang.StringBuilder; append( | X1,X2 | ) |  |  |  |  |  |  |
| X2="41001"(type=java.lang.String, tag=0x0) | X1=0x40528158(type=java.lang.StringBuilder, tag=0x3) | , |  |  |  |  |  |  |  |
| android.telephony.SmsManager;sendTextMessage( | X1,X2,X3 | ) | com.dlp.SMSReplicatorSecret.SMSReceiver;onReceive()VLL----> |  |  |  |  |  |  |
| X1=0x40526820(type= | android.telephony.SmsManager | ) | android.telephony.SmsManager;sendTextMessage( | X1,X2,X3,X4,X5 | ) |  |  |  |  |
| X2="41001"(type=java.lang.String, tag=0x1) | X1=0x40538068(type=android/telephony/SmsManager), |  |  |  |  |  |  |  |  |
| X3="YES"(type=java.lang.String) | X2="***"(attacker NO.), | X3="***"(tag=0x3, SMS msg.) | ,X4=null,X5=null |  |  |  |  |  |  |
| Figure 5: | SMS Auto Reply | behavior in | GGTracker | . | Figure 6: | SMS Forwarding | behavior in | SMSReplicator | . |
| syscall | # | Comments | android.permission.ACCESS_FINE_LOCATION, Tag: 0x4 |  |  |  |  |  |  |
| ioctl | 8 | Binder communication | net.maxicom.android.snake.SnakeService$1; run()V ----> |  |  |  |  |  |  |
| stat64,access | 9 | app’s resource file | X1="gps",X2=1L,X3=250.0F,X4=0x40528310(type=net.maxicom.android.sn |  |  |  |  |  |  |
| writev | 1 | log operation | net.maxicom.android.snake.LocationListener; onLocationChanged( | X1,X2 | ) |  |  |  |  |
| icon. | SMSReplicator | not only leaks SMS messages, but also incurs | org.apache.http.impl.client.AbstractHttpClient; execute( | X1,X2,X3 | ) |  |  |  |  |
| additional financial charge. As Figure 6 shows, all the incoming | LOCATION | X1=0x4052f008(type=org.apache.http.impl.client.DefaultHttpClient), |  |  |  |  |  |  |  |
| SMS messages are intercepted by this malware using a | Broadcas- | X3=0x400210c8(type=org.apache.http.impl.client.DefaultHttpClient) |  |  |  |  |  |  |  |
| tReceiver | ( | com.dlp.SMSReplicatorSecret.SMSReceiver | ). The SMS | INTERNET |  |  |  |  |  |
| SMSReplicator | further queries the contacts to find the sender of | X1=0x40310548(type=org.apache.harmony.luni.platform.OSNetworkSystem, tag=0x8) | , |  |  |  |  |  |  |
| the intercepted message. The name of the sender and the message | X2=0x4053fd20(type=java.io.FileDescriptor), | X3=0x4056ac88(type=[B, tag=0x4) | ,X4=0x0I,X5=0x140I |  |  |  |  |  |  |
| Forwarding | behavior are similar in intercepting and sending SMS. | event. When location changes, the | onLocationChanged | function is |  |  |  |  |  |
| However, with the reconstructed permission use behaviors which | invoked asynchronously by Android to deliver the latest location. |  |  |  |  |  |  |  |  |
| track the internal application logic (Figure 5 and Figure 6), their | TapSnake | further performs some string operations on the location |  |  |  |  |  |  |  |
| divergent malicious intents get clearly differentiated. | object to encode the location into a URL. The encoded URL is |  |  |  |  |  |  |  |  |
| 3) Analysis of TapSnake. | passed to the | execute() | function of | AbstractHttpClient | . The latest |  |  |  |  |
| TapSnake | [2] tracks the infected user by sending the latest loca- | location that is encoded in the URL is eventually exfiltrated to the |  |  |  |  |  |  |  |
| tion to a remote server. To hide its malicious intent, this malware | server | http://gpsdatapoints.appspot.com | . |  |  |  |  |  |  |
| lation, this malware asks users to grant | ACCESS_FINE_LOCATION | 4.2 | Vetting Market Apps |  |  |  |  |  |  |
| and | INTERNET | permissions. | Considering these permissions are | Next, we use | VetDroid | to vet 1,249 top (benign) apps crawled |  |  |  |
| required by most legitimate advertising libraries [37], most users | from Google Play official store. | These apps are top free apps |  |  |  |  |  |  |  |
| choose to grant these permissions without any idea about how these | crawled from 32 different categories such as games, education, |  |  |  |  |  |  |  |  |
| permissions will be used. | entertainment, finance, social, sports, tools. We also use multiple |  |  |  |  |  |  |  |  |
| As showed in Figure 7, | TapSnake | first registers a callback | emulators to parallelize the process of reconstructing permission |  |  |  |  |  |  |
| ( | net.maxicom.android.snake.LocationListener | ) for the location change | use behaviors for these apps. There are several interesting findings. |  |  |  |  |  |  |

---

## Page 9

| Leak Resource | TaintDroid | VetDroid | Leak Resource | # | Leak Cause |
| --- | --- | --- | --- | --- | --- |
| IMEI | 135 | 135 | Inner-Active Ads |  |  |
| Phone Number | 7 | 7 | Wetter Ads |  |  |
| Location | 17 | 24 | Flurry Ads |  |  |

leaks than TaintDroid. Based on the reconstructed permission

use behaviors, we implement a simple permission-based filter that

selects permission use graphs with at least one permission to read

party. The selected graphs are further classified with regard to E-

same inputs to the Application Driver . The results are also

tracks the behaviors of leaking such kind of sensitive resource by

current implementation does not support detecting leaks of such

sensitive resource. It is worth noting that TaintDroid could be

improved to detect these leaks if we proactively and manually

TaintDroid, VetDroid can automatically track such resources as

long as they are in permission use behaviors. This experiment

Location 12

InMobi Ads

Fortumo Payments

CellLocation 3

Handmark

Phone Number 1 Mobile Public

android.permission.RECEIVE_SMS, Tag: 0x400

com.viber.voip.registration.ActivationSmsReceiver;onReceive( X1, X2,X3 )

tag=0x400),

X2=0x406deb10(type=android.app.ReceiverRestrictedContext),

X1=0x407d9cb8(type=[B, tag=0x400)

tag=0x400)

to activate your account.[CEG]"(type=java.lang.String, tag=0x400)

RECEIVE_SMS

tag=0x400),

X2="8873"(type=java.lang.String, tag=0x400)

| Network State | 0 | 28 | Google Ads |  |  |
| --- | --- | --- | --- | --- | --- |
| Table 3: Information leakage results. | Vserv Ads |  |  |  |  |
| Finding 1: | VetDroid | can assist in finding more information | Table 4: Information leak analysis results. |  |  |
| system resource and one permission to exfiltrate data to a remote | X1=0x407eaf20(type=com.viber.voip.registration.ActivationSmsReceiver, |  |  |  |  |
| PUP | s. We manually check these classified behaviors and confirm | X3=0x407df3a0(android.content.Intent) |  |  |  |
| four kinds of information leaks, as listed in Table 3. | RECEIVE_SMS |  |  |  |  |
| We also use TaintDroid [24] to run these apps with the exact | android.telephony.SmsMessage; createFromPdu( | X1 | ) |  |  |
| presented in Table 3. | We can see that | VetDroid | detects 7 more | RECEIVE_SMS |  |
| location leaks than TaintDroid. | After a further investigation | com.android.internal.telephony.SmsMessageBase;getMessageBody( | X1 | ) |  |
| on these cases, we find that the cell location (acquired through | X1=0x407de1c8(type=com.android.internal.telephony.gsm.SmsMessage, |  |  |  |  |
| TelephonyManager.getCellLocation() | API) is leaked in these cases | RECEIVE_SMS |  |  |  |
| while TaintDroid does not treat this kind of location as sensitive | java.util.regex.Pattern;matcher( | X1, X2 | ) |  |  |
| data. Since an app needs to use | ACCESS_COARSE_LOCATION | X1=0x40792580(type=java.util.regex.Pattern), |  |  |  |
| permission to get the cell location, | VetDroid | could automatically | X2="Your Viber code is: 8873, close this message and enter the code into Viber |  |  |
| following the permission usage. | VetDroid | also detects 28 cases that | com.viber.voip.registration.RegistrationActivity;activationCodeReceived( | X1, X2 | ) |
| leak the device’s network state to a remote party while TaintDroid’s | X1=0x407eaf20(type=com.viber.voip.registration.ActivationSmsReceiver, |  |  |  |  |
| add ad-hoc logic to taint these sources. | However, different from | Figure 8: | SMS Activation | behavior in Viber. |  |
| clearly demonstrates that using permissions to automatically and | carefully examining the permission use behaviors, we find that the |  |  |  |  |
| systematically capture application behaviors is superior to tradi- | Viber application is vulnerable to | Account Hijack attack | . |  |  |
| tional simple taint analysis without permission in consideration. | According to the website of Google Play, Viber is a free VoIP |  |  |  |  |
| Finding 2: | VetDroid | can inspect the fine-grained causes of | app that has been downloaded nearly 100 million times in recent 30 |  |  |
| information leakage. | Our permission use behavior captures the | days worldwide. Viber provides users with free calls and messages |  |  |  |
| internal logic of permission usages inside an app, thus enables | to other Viber users. It also requests its user to bind his/her phone |  |  |  |  |
| us to analyze the fine-grained procedure of information leakage. | number which is used as his/her identity. | When a call/message |  |  |  |
| We manually analyze the permission use behaviors of several | arrives, Viber will look up the sender’s profile in the contact with |  |  |  |  |
| information leaks reported by | VetDroid | to investigate the contexts | the sender’s phone number for a friendly notification. |  |  |
| of reading and leaking sensitive information. In this experiment, | To prevent a user from binding others’ phone numbers, Viber |  |  |  |  |
| we mainly focus on | Phone Number | and | Location | leakage cases | server sends an activation SMS to the phone number. By verifying |
| because they are relatively interesting. | the activation code in the SMS, Viber can confirm whether the |  |  |  |  |
| Based on the context of information leakage, we find that many | user owns the phone number or not. | The activation phase is |  |  |  |
| such information leaks are actually not caused by the app itself. | quite important for a popular communication app such as Viber. |  |  |  |  |
| Table 4 shows our analysis results. From this table, we could find | Otherwise, an attacker could bind a victim’s phone number and |  |  |  |  |
| that 15 out of 24 location leaks are actually caused by mobiles ads | send fake messages/calls to the victim’s friends on behalf of the |  |  |  |  |
| and payments. There is also one case that sends the phone number | victim. This kind of | Account Hijack attack | could cause the same |  |  |
| to a mobile promotion and publishing company (Mobile Public). | damage as | Facebook Account Hijack | [4]. |  |  |
| Cell locations that are not tracked by TaintDroid are also used by | We use | VetDroid | to reconstruct the permission use behavior |  |  |
| Vserv and Handmark for better advertising. | of the activation process, as shown in Figure 8. | As this figure |  |  |  |
| Compared with TaintDroid that could only alert information | shows, Viber intercepts incoming SMS messages in | Activation- |  |  |  |
| leaks, the results show that | VetDroid | is capable of inspecting the | SmsReceiver | , and extracts the activation code from the message |  |
| fine-grained causes of sensitive information leakage by tracing the | body using a regular expression. | Once an activation code is |  |  |  |
| context of permission usage. | matched, the activation process is proceeded in the | Registration- |  |  |  |
| Finding 3: | VetDroid | can help detect subtle application vul- | Activity.activationCodeReceived() | function. |  |
| nerabilities. | Since SMS service is unique and quite important for | By carefully examining the permission use behavior in Figure |  |  |  |
| smartphones, we analyze 33 apps that request both | RECEIVE_SMS | 8, it is easy to find that Viber does not check the origin of an |  |  |  |
| and | SEND_SMS | permissions by running these apps in | VetDroid | . By | activation SMS. Thus, an attacker could pass the activation by |

---

## Page 10

| E-PUP | I-PUP | Log | ALL | [34], Dynodroid [43], or guided analysis technique such as multi- |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Time | 18.124% | 10.385% | 3.785% | 32.294% | path exploration [44], forced/informed execution [54, 55]. |  |  |
| Mem. | 0.100% | 13.573% | 0.637% | 14.110% | Our | I-PUP Tracker | is built upon TaintDroid, thus inheriting |

intercepting the activation SMS from the victim and sending it to

the attacker’s Viber client, causing the victim’s account hijacked.

It is not hard to steal an SMS from a victim, especially when the

Account Hijack attack on the victim could lead to a reasonable

profit. SMS stealing could be possibly implemented by malware

such as SMSReplicator [3], Zitmo [10] or social engineering. To

further confirm this vulnerability, we perform an experiment to

hijack the Viber account of a volunteer in our group. By stealthily

replacing an app in his smartphone into our repackaged version

(which has the similar SMS Blocking and Stealing behavior as

Zitmo ), the activation SMS from Viber server is forwarded by

our repackaged app to the attacker’s device. After binding the

volunteer’s phone number to the attacker’s device, free calls and

messages are successfully initiated to his friends on behalf of his

identity. Interestingly, in a security study [52] that performed

network traffic analysis of nine popular VoIP apps, Viber was

considered to be immune from Account Hijack attacks , because

the activation code was generated in the Viber server and thus

cannot be hijacked by a man-in-the-middle attack. However, our

internal permission use behavior analysis on Viber reveals that the

missing check on the origin of activation SMS actually makes Viber

similar limitations of TaintDroid such as incapable of tracking

taint analysis system that seamlessly tracks Java code and native

code. In addition, implicit flows can also be accurately tracked by

selectively propagating tainted control dependencies as in DTA++

[38]. Furthermore, our E-PUP Identifier relies on the Android

permission system for permission check identification. Thus our

current implementation could not catch those behaviors that do not

cause permission checks [35].

As our evaluation shows, VetDroid is not limited to analyze

malicious apps, but also capable of analyzing benign apps. A

key advantage of our approach is that it captures the application’s

sensitive behaviors with permission use graphs, which can signifi-

cantly reduce irrelevant/uninteresting actions and let analysts focus

on the critical behaviors when inspecting an app’s internal logic.

In practice, analysts can use VetDroid to automatically analyze a

batch of apps and write simple scripts to select interested cases for

further analysis (as demonstrated in our evaluation).

Compared with existing work, Permission Use Behavior pro-

vides a better approximation of sensitive behaviors inside an

Android app. Thus, we believe VetDroid could be integrated with

existing behavior-based malware detection techniques [14, 39] to

extract effective malware signatures for clustering and detection.

Malware Analysis. As mentioned before, syscall-based

designers in determining the most appropriate permission-granting

mechanism for a given permission. Permission-based security rules

| Table 5: | Results of execution time and memory footprint | native code and implicit flows, which we leave as our future work. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| overhead on CaffeineMark benchmark. | One possible way to solve the native code problem is to build a |  |  |  |  |  |
| vulnerable to | Account Hijack attack | . | 6. | RELATED WORK |  |  |
| 4.3 | Performance Overhead Evaluation | solutions (e.g., syscall vector [16], syscall sequence with argu- |  |  |  |  |
| Due to the inline instrumentation on Android, our analysis tool | ments [49], temporal pattern of syscalls [14], resource access |  |  |  |  |  |
| incurs some extra runtime overhead. | We perform experiments | model [40], syscall dependency graph [21, 22, 33]) are not well- |  |  |  |  |
| on our Nexus S to measure the overhead from two aspects: | suited for the Android platform due to the inability of monitoring |  |  |  |  |  |
| execution speed and memory footprint. Table 5 shows the results | Android-specific behaviors. DroidScope [56] seems to notice these |  |  |  |  |  |
| on CaffeineMark, a standard performance benchmark. Compared | problems by seamlessly reconstructing the semantics from system |  |  |  |  |  |
| with the original Android system, | VetDroid | slows down the entire | calls and Java. However, it only refines existing work, leaving the |  |  |  |
| execution of the application by 32.294%, | while increases the | root problems of Android’s special permission mechanism and pro- |  |  |  |  |
| memory footprint by 14.110%. | The main overhead of | I-PUP | gramming model untouched. A survey on current Android malware |  |  |  |
| Tracker | is caused by our permission-based taint analysis which | characteristics was presented in [59] and [29]. DroidRanger [60] |  |  |  |  |
| inherits the overhead of TaintDroid [24]. We believe this is a very | and RiskRanker [36] were two Android malware detectors that |  |  |  |  |  |
| reasonable and acceptable overhead for an offline analysis tool. | relied on existing knowledge about malicious symptoms. Although |  |  |  |  |  |
| To measure the performance penalty in the worst case, we also | they were reported to detect known and unknown malware samples, |  |  |  |  |  |
| write a benchmark app that invokes a privileged Android API | they do not analyze the fine-grained internal behaviors of malware |  |  |  |  |  |
| 10,000 times and opens a socket 10,000 times. This case is used | samples, which is the focus of | VetDroid | . |  |  |  |
| to measure the pure overhead caused by our permission check | To analyze apps at market-scale, Chakradeo et al. [18] proposed |  |  |  |  |  |
| identification module. By measuring the execution time, we find | app triage to efficiently allocate malware analysis resources. | Vet- |  |  |  |  |
| the identification of | AndPermChk | s and | KerPermChk | s incurs an | Droid | can be combined with this technique into a practical market- |
| overhead of 80.108% and 238.870%, respectively. As the execution | scale application analysis solution. |  |  |  |  |  |
| time of privileged calls represent only a small portion of the | Permission Analysis. | Felt et al. [30] studied the effectiveness |  |  |  |  |
| whole execution, | VetDroid | is quite efficient, especially as an offline | of the time-of-use and install-time permission grant mechanism. |  |  |  |
| analysis tool. | This work was extended in [28] to provide guidelines for platform |  |  |  |  |  |
| 5. | DISCUSSION | were used by Kirin [25] to design a lightweight certification frame- |  |  |  |  |
| In this paper we focus on providing a new perspective for | work that could mitigate malware at install time. | Apex [45] and |  |  |  |  |
| analyzing Android apps. | To enlarge the analysis scope, | our | Saint [46] were two extensions to the Android’s permission system |  |  |  |
| Application Driver | utilizes several key features of Android, such | by introducing runtime constraints on the granted permissions. |  |  |  |  |
| as component-based programming model, event triggers. However, | To help end users understand application behaviors at install |  |  |  |  |  |
| our technique alone could not guarantee all possible behaviors | time, AppProfiler [50] devised a two-step translation technique |  |  |  |  |  |
| are captured within the short time an app is executed. | The | which maps API calls to high-level behavior profiles. | While |  |  |  |
| Application Driver | could be enhanced with an automatic input | VetDroid | also tries to provide better behavior understanding, it is |  |  |  |
| generation system such as AppsPlayground [48], AppInspector | a tool provided for different users (security analysts) and it uses |  |  |  |  |  |

---

## Page 11

| a different new technique/perspective (permission use behavior) | [2] Androidos.tapsnake: Watching your every move. | http: |  |  |
| --- | --- | --- | --- | --- |
| to precisely capture application-system interactions and sensitive | //www.symantec.com/connect/blogs/android |  |  |  |
| behaviors inside an app. | ostapsnake-watching-your-every-move | . |  |  |
| Barrera et al. [13] performed an empirical analysis on the expres- | [3] Android.smsreplicator. |  |  |  |
| siveness of Android’s permission sets and discussed some potential | http://www.symantec.com/security_respon |  |  |  |
| improvements for Android’s permission model. | Felt et al. [27] | se/writeup.jsp?docid=2010-110214-1252-99 | . |  |
| proposed the first solution to systematically detect overprivileged | [4] Facebook security phishing attack in the wild. | http://ww |  |  |
| permissions in Android apps and one-third of the applications in | w.securelist.com/en/blog/208193325/Faceb |  |  |  |
| this study were found to be overprivileged. | Probabilistic models | ook_Security_Phishing_Attack_In_The_Wild | . |  |
| of permission request patterns [32] or permission request sets [47] | [5] Idc: Android market share reached 75% worldwide in q3 |  |  |  |
| were also used to indicate the risk of new applications. To extract | 2012. | http://techcrunch.com/2012/11/02/id |  |  |
| permission specifications for Android, Stowaway [27] used API | c-android-market-share-reached-75-world |  |  |  |
| fuzz testing while PScout [12] adopted static analysis on Android | wide-in-q3-2012/ | . |  |  |
| source code. | However, these two permission specifications were | [6] Mcafee threats report: Third quarter 2012. |  |  |
| limited in either completeness or preciseness, making them not | http://www.mcafee.com/ca/resources/repo |  |  |  |
| well-suited for implementing | E-PUP Identifier | . | rts/rp-quarterly-threat-q3-2012.pdf | . |

Permission re-delegation attack in Android was first introduced

in [23, 31]. Grace et al. [35] empirically evaluated the re-delegated

permission leaks in pre-installed apps of stock Android smart-

phones. CHEX [41] and DroidChecker [19] were two tools that

could detect such kind of capability leaks. Bugiel et al. [15]

proposed system-centric and policy-driven runtime monitoring of

first systematic framework to analyze permission use behaviors.

plicit permission use points with accurate permission information.

and examining Android apps, which brings benefits to malware

We would like to thank the anonymous reviewers for their

61300027), Science and Technology Commission of Shanghai

Education and Intel numbered MOE-INTEL201202, Fundamental

[1] Android permissions.

http://developer.android.com/reference/

android/Manifest.permission.html .

[7] Pendingintent. http://developer.android.com/

reference/android/app/PendingIntent.html .

[8] Sms emulation using the android emulator.

http://developer.android.com/tools/devi

ces/emulator.html#sms .

ACM CCS’12 , 2012.

[13] D. Barrera, H. G. Kayacik, P. C. van Oorschot, and

MobiSys’08 , 2008.

Proc. of SPSM’11 , 2011.

M. Christodorescu, and E. Kirda. A quantitative study of

ISSTA’12 , 2012.

WiSec’13 , 2013.

WiSec’12 , 2012.

[21] M. Christodorescu, S. Jha, and C. Kruegel. Mining

ESEC-FSE’07 , 2007.

| communication channels between applications at both Android- | [9] Ui/application exerciser monkey. | http://developer. |  |  |
| --- | --- | --- | --- | --- |
| level and kernel-level, which could prevent not only re-delegation | android.com/tools/help/monkey.html | . |  |  |
| attacks but also collusion attacks. Chen et al. [20] adopted static | [10] Zeus-in-the-mobile - facts and theories. | http: |  |  |
| analysis to extract permission event graphs and examined the | //www.securelist.com/en/analysis/2047921 |  |  |  |
| constraint conditions on events for each privileged API using model | 94/ZeuS_in_the_Mobile_Facts_and_Theories | . |  |  |
| checking. However, it could not capture the internal logic of using | [11] Apple: ios 4. | http://www.apple.com/iphone | , 2011. |  |
| permissions, especially when multiple permissions are intertwined. | [12] K. W. Y. Au, Y. F. Zhou, Z. Huang, and D. Lie. Pscout: |  |  |  |
| Our | VetDroid | differs from all existing work in that it provides the | analyzing the android permission specification. In | Proc. of |
| 7. | CONCLUSION | A. Somayaji. A methodology for empirical analysis of |  |  |
| This paper presents | VetDroid | , the first approach to perform | permission-based security models and its application to |  |
| accurate permission use analysis to vet undesirable behaviors. | android. In | Proc. of ACM CCS’10 | , 2010. |  |
| To construct permission use behaviors, | this paper proposes a | [14] A. Bose, X. Hu, K. G. Shin, and T. Park. Behavioral |  |  |
| systematic framework that completely identifies explicit and im- | detection of malware on mobile handsets. In | Proc. of |  |  |
| VetDroid | is shown to be able to clearly reconstruct malicious | [15] S. Bugiel, L. Davi, A. Dmitrienko, T. Fischer, A.-R. Sadeghi, |  |  |
| behaviors of real-world apps to ease malware analysis. It can also | and B. Shastry. Towards taming privilege-escalation attacks |  |  |  |
| assist in finding information leaks, analyzing fine-grained causes | on Android. In | Proc. of NDSS’12 | , Feb. 2012. |  |
| of information leaks, and detecting subtle vulnerabilities in regular | [16] I. Burguera, U. Zurutuza, and S. Nadjm-Tehrani. Crowdroid: |  |  |  |
| apps. | In all, | VetDroid | provides a better vehicle for analyzing | behavior-based malware detection system for android. In |
| analysis/detection, vulnerability analysis, and other related fields. | [17] D. Canali, A. Lanzi, D. Balzarotti, C. Kruegel, |  |  |  |
| 8. | ACKNOWLEDGEMENTS | accuracy in system call-based malware detection. In | Proc. of |  |
| insightful comments and feedback. | This work is funded by | [18] S. Chakradeo, B. Reaves, P. Traynor, and W. Enck. Mast: |  |  |
| National Natural Science Foundation of China (NO. 61103078, | triage for market-scale mobile malware analysis. In | Proc. of |  |  |
| Municipality (NO. 11DZ2281500, 11511504404, 13511504402 | [19] P. P. Chan, L. C. Hui, and S. M. Yiu. Droidchecker: |  |  |  |
| and 13JC1400800), a joint program between China Ministry of | analyzing android applications for capability leak. In | Proc. of |  |  |
| Research Funds for the Central Universities in China and Shanghai | [20] K. Z. Chen, N. Johnson, V. D’Silva, S. Dai, K. MacNamara, |  |  |  |
| Leading Academic Discipline Project numbered B114. This work | T. Magrino, E. X. Wu, M. Rinard, and D. Song. Contextual |  |  |  |
| is also partially supported by the National Science Foundation | policy enforcement in android applications with permission |  |  |  |
| under Grant no. CNS-0954096. | event graphs. In | Proc. of NDSS’13 | , February 2013. |  |
| 9. | REFERENCES | specifications of malicious behavior. In | Proc. of |  |

---

## Page 12

| [22] P. M. Comparetti, G. Salvaneschi, E. Kirda, C. Kolbitsch, | [42] W. Ma, P. Duan, S. Liu, G. Gu, and J.-C. Liu. Shadow |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| C. Kruegel, and S. Zanero. Identifying dormant functionality | attacks: Automatically evading system-call-behavior based |  |  |  |  |
| in malware programs. In | Proc. of IEEE S&P’10 | , 2010. | malware detection. | Springer Journal in Computer Virology | , |
| [23] M. Dietz, S. Shekhar, Y. Pisetsky, A. Shu, and D. S. Wallach. | 2012. |  |  |  |  |
| Quire: lightweight provenance for smart phone operating | [43] A. MacHiry, R. Tahiliani, and M. Naik. Dynodroid: An input |  |  |  |  |
| systems. In | Proc. of USENIX Security’11 | , 2011. | generation system for android apps. Technical report, |  |  |
| [24] W. Enck, P. Gilbert, B.-G. Chun, L. P. Cox, J. Jung, | Program Analysis Group, Georgia Tech, 2012. |  |  |  |  |
| P. McDaniel, and A. N. Sheth. Taintdroid: an | [44] A. Moser, C. Kruegel, and E. Kirda. Exploring multiple |  |  |  |  |
| information-flow tracking system for realtime privacy | execution paths for malware analysis. In | Proc. of IEEE |  |  |  |
| monitoring on smartphones. In | Proc. of OSDI’10 | , 2010. | S&P’07 | , 2007. |  |
| [25] W. Enck, M. Ongtang, and P. McDaniel. On lightweight | [45] M. Nauman, S. Khan, and X. Zhang. Apex: extending |  |  |  |  |
| mobile phone application certification. In | Proc. of ACM | android permission model and enforcement with user-defined |  |  |  |
| CCS’09 | , 2009. | runtime constraints. In | Proc. of AsiaCCS’10 | , 2010. |  |
| [26] W. Enck, M. Ongtang, and P. McDaniel. Understanding | [46] M. Ongtang, S. McLaughlin, W. Enck, and P. McDaniel. |  |  |  |  |
| android security. | IEEE Security and Privacy | , 7(1):50–57, | Semantically rich application-centric security in android. In |  |  |
| Jan. 2009. | Proc. of ACSAC’09 | , 2009. |  |  |  |
| [27] A. P. Felt, E. Chin, S. Hanna, D. Song, and D. Wagner. | [47] H. Peng, C. Gates, B. Sarma, N. Li, Y. Qi, R. Potharaju, |  |  |  |  |
| Android permissions demystified. In | Proc. of ACM CCS’11 | , | C. Nita-Rotaru, and I. Molloy. Using probabilistic generative |  |  |
| 2011. | models for ranking risks of android apps. In | Proc. of ACM |  |  |  |
| [28] A. P. Felt, S. Egelman, M. Finifter, D. Akhawe, and | CCS’12 | , 2012. |  |  |  |
| D. Wagner. How to ask for permission. In | Proc. of | [48] V. Rastogi, Y. Chen, and W. Enck. Appsplayground: |  |  |  |
| HotSec’12 | , 2012. | Automatic security analysis of smartphone applications. In |  |  |  |
| [29] A. P. Felt, M. Finifter, E. Chin, S. Hanna, and D. Wagner. A | Proc. of CODASPY’13 | , 2013. |  |  |  |
| survey of mobile malware in the wild. In | Proc. of SPSM’11 | , | [49] K. Rieck, T. Holz, C. Willems, P. Düssel, and P. Laskov. |  |  |
| 2011. | Learning and classification of malware behavior. In | Proc. of |  |  |  |
| [30] A. P. Felt, K. Greenwood, and D. Wagner. The effectiveness | DIMVA’08 | , 2008. |  |  |  |
| of application permissions. In | Proc. of WebApps’11 | , 2011. | [50] S. Rosen, Z. Qian, and Z. M. Mao. Appprofiler: a flexible |  |  |
| [31] A. P. Felt, H. J. Wang, A. Moshchuk, S. Hanna, and E. Chin. | method of exposing privacy-related behavior in android |  |  |  |  |
| Permission re-delegation: attacks and defenses. In | Proc. of | applications to end users. In | Proc. of CODASPY’13 | , 2013. |  |
| USENIX Security’11 | , 2011. | [51] H.-G. Schmidt, K. Raddatz, A.-D. Schmidt, A. Camtepe, and |  |  |  |
| [32] M. Frank, B. Dong, A. P. Felt, and D. Song. Mining | S. Albayrak. Google android: A comprehensive introduction. |  |  |  |  |
| permission request patterns from android and facebook | Technical report, DAI-Labor, TU Berlin, 2009. |  |  |  |  |
| applications. In | Proc. of ICDM’12 | , 2012. | [52] S. Schrittwieser, P. Fruehwirt, P. Kieseberg, M. Leithner, |  |  |
| [33] M. Fredrikson, S. Jha, M. Christodorescu, R. Sailer, and | M. Mulazzani, M. Huber, and E. R. Weippl. Guess who is |  |  |  |  |
| X. Yan. Synthesizing near-optimal malware specifications | texting you? evaluating the security of smartphone |  |  |  |  |
| from suspicious behaviors. In | Proc. of IEEE S&P’10 | , 2010. | messaging applications. In | Prof. of NDSS’12 | , Feb 2012. |
| [34] P. Gilbert, B.-G. Chun, L. P. Cox, and J. Jung. Vision: | [53] X. Wei, L. Gomez, I. Neamtiu, and M. Faloutsos. |  |  |  |  |
| automated security validation of mobile apps at app markets. | Profiledroid: multi-layer profiling of android applications. In |  |  |  |  |
| In | Proc. of 2nd international workshop on Mobile cloud | Proc. of Mobicom’12 | , 2012. |  |  |
| computing and services (MCS’11) | , 2011. | [54] J. Wilhelm and T.-c. Chiueh. A forced sampled execution |  |  |  |
| [35] M. Grace, Y. Zhou, Z. Wang, and X. Jiang. Systematic | approach to kernel rootkit identification. In | Proc. of |  |  |  |
| detection of capability leaks in stock android smartphones. In | RAID’07 | , 2007. |  |  |  |
| Proc. of NDSS’12 | , 2012. | [55] Z. Xu, L. Chen, G. Gu, and C. Kruegel. Peerpress: utilizing |  |  |  |
| [36] M. Grace, Y. Zhou, Q. Zhang, S. Zou, and X. Jiang. | enemies’ p2p strength against them. In | Proc. of ACM |  |  |  |
| Riskranker: scalable and accurate zero-day android malware | CCS’12 | , 2012. |  |  |  |
| detection. In | Proc. of MobiSys’12 | , 2012. | [56] L. K. Yan and H. Yin. Droidscope: seamlessly reconstructing |  |  |
| [37] M. C. Grace, W. Zhou, X. Jiang, and A.-R. Sadeghi. Unsafe | the os and dalvik semantic views for dynamic android |  |  |  |  |
| exposure analysis of mobile in-app advertisements. In | Proc. | malware analysis. In | Proc. of USENIX Security’12 | , 2012. |  |
| of WiSec’12 | , 2012. | [57] Z. Yang, M. Yang, Y. Zhang, G. Gu, P. Ning, and X. S. |  |  |  |
| [38] M. G. Kang, S. McCamant, P. Poosankam, and D. Song. | Wang. Appintent: Analyzing sensitive data transmission in |  |  |  |  |
| DTA++: Dynamic taint analysis with targeted control-flow | android for privacy leakage detection. In | Proc. of ACM |  |  |  |
| propagation. In | Proc. of NDSS’11 | , Feb. 2011. | CCS’13 | , 2013. |  |
| [39] C. Kolbitsch, P. M. Comparetti, C. Kruegel, E. Kirda, | [58] H. R. Zeidanloo and A. A. Manaf. Botnet command and |  |  |  |  |
| X. Zhou, and X. Wang. Effective and efficient malware | control mechanisms. In | Proc. of ICCEE’09 | , 2009. |  |  |
| detection at the end host. In | Proc. of USENIX Security’09 | , | [59] Y. Zhou and X. Jiang. Dissecting android malware: |  |  |
| 2009. | Characterization and evolution. In | Proc. of IEEE S&P’12 | , |  |  |
| [40] A. Lanzi, D. Balzarotti, C. Kruegel, M. Christodorescu, and | 2012. |  |  |  |  |
| E. Kirda. Accessminer: using system-centric models for | [60] Y. Zhou, Z. Wang, W. Zhou, and X. Jiang. Hey, you, get off |  |  |  |  |
| malware protection. In | Proc. of ACM CCS’10 | , 2010. | of my market: Detecting malicious apps in official and |  |  |
| [41] L. Lu, Z. Li, Z. Wu, W. Lee, and G. Jiang. Chex: statically | alternative Android markets. In | Proc. of NDSS’12 | , 2012. |  |  |

vetting android apps for component hijacking vulnerabilities.

In Prof. of ACM CCS’12 , 2012.

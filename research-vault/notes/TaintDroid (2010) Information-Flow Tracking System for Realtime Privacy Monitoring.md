---year: 2010

secverify_category: "Legacy"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "24_Enck_et_al.,_TaintDroid_Information-Flow_Tracking"
creator: "LaTeX with hyperref package"
pages: 15
source: "TaintDroid (2010) Information-Flow Tracking System for Realtime Privacy Monitoring.pdf"
---

# TaintDroid (2010) Information-Flow Tracking System for Realtime Privacy Monitoring

> **文獻存檔**：[PDF 原文](<../../raw-papers/2010-2019/TaintDroid (2010) Information-Flow Tracking System for Realtime Privacy Monitoring.pdf>) | [Markdown 原文](<../../raw-papers/2010-2019/TaintDroid (2010) Information-Flow Tracking System for Realtime Privacy Monitoring (Raw).md>)

> **總頁數**：15 頁

---

## Page 1

TaintDroid: An Information-Flow Tracking System for Realtime Privacy

Monitoring on Smartphones

| William Enck | Peter Gilbert | Byung-Gon Chun |  |
| --- | --- | --- | --- |
| The Pennsylvania State University | Duke University | Intel Labs |  |
| Landon P. Cox | Jaeyeon Jung | Patrick McDaniel | Anmol N. Sheth |
| Duke University | Intel Labs | The Pennsylvania State University | Intel Labs |
| Abstract | Resolving the tension between the fun and utility of |  |  |

Today’s smartphone operating systems frequently fail

to provide users with adequate control over and visibility

into how third-party applications use their private data.

We address these shortcomings with TaintDroid, an ef-

ficient, system-wide dynamic taint tracking and analy-

sis system capable of simultaneously tracking multiple

sources of sensitive data. TaintDroid provides realtime

analysis by leveraging Android’s virtualized execution

environment. TaintDroid incurs only 14% performance

overhead on a CPU-bound micro-benchmark and im-

poses negligible overhead on interactive third-party ap-

plications. Using TaintDroid to monitor the behavior of

30 popular third-party Android applications, we found

68 instances of potential misuse of users’ private infor-

mation across 20 applications. Monitoring sensitive data

with TaintDroid provides informed use of third-party ap-

plications for phone users and valuable input for smart-

phone security service firms seeking to identify misbe-

having applications.

1 Introduction

A key feature of modern smartphone platforms is a

running third-party mobile applications and the privacy

risks they pose is a critical challenge for smartphone plat-

forms. Mobile-phone operating systems currently pro-

vide only coarse-grained controls for regulating whether

an application can access private information, but pro-

vide little insight into how private information is actu-

ally used. For example, if a user allows an application

to access her location information, she has no way of

knowing if the application will send her location to a

location-based service, to advertisers, to the application

developer, or to any other entity. As a result, users must

blindly trust that applications will properly handle their

private data.

This paper describes TaintDroid , an extension to the

Android mobile-phone platform that tracks the flow of

privacy sensitive data through third-party applications.

TaintDroid assumes that downloaded, third-party appli-

cations are not trusted, and monitors–in realtime–how

these applications access and manipulate users’ personal

data. Our primary goals are to detect when sensitive data

leaves the system via untrusted applications and to facil-

itate analysis of applications by phone users or external

security services [33, 55].

| centralized service for downloading third-party applica- | Analysis of applications’ behavior requires sufficient |  |
| --- | --- | --- |
| tions. The convenience to users and developers of such | contextual information about what data leaves a device |  |
| “app stores” has made mobile devices more fun and use- | and where it is sent. | Thus, TaintDroid automatically |
| ful, and has led to an explosion of development. Apple’s | labels (taints) data from privacy-sensitive sources and |  |
| App Store alone served nearly 3 billion applications af- | transitively applies labels as sensitive data propagates |  |
| ter only 18 months [4]. Many of these applications com- | through program variables, files, and interprocess mes- |  |
| bine data from remote cloud services with information | sages. | When tainted data are transmitted over the net- |
| from local sensors such as a GPS receiver, camera, mi- | work, or otherwise leave the system, TaintDroid logs the |  |
| crophone, and accelerometer. Applications often have le- | data’s labels, the application responsible for transmitting |  |
| gitimate reasons for accessing this privacy sensitive data, | the data, and the data’s destination. Such realtime feed- |  |
| but users would also like assurances that their data is used | back gives users and security services greater insight into |  |
| properly. Incidents of developers relaying private infor- | what mobile applications are doing, and can potentially |  |
| mation back to the cloud [35, 12] and the privacy risks | identify misbehaving applications. |  |
| posed by seemingly innocent sensors like accelerome- | To be practical, the performance overhead of the Taint- |  |
| ters [19] illustrate the danger. | Droid runtime must be minimal. | Unlike existing so- |

---

## Page 2

| lutions that rely on heavy-weight whole-system emula- | Monitoring network disclosure of privacy sensitive in- |
| --- | --- |
| tion [7, 57], we leveraged Android’s virtualized archi- | formation on smartphones presents several challenges: |

tecture to integrate four granularities of taint propaga-

techniques and in identifying an appropriate trade-off

mark. More importantly, interactive third-party applica-

tions can be monitored with negligible perceived latency.

mitted tainted data; of the 105, we determined that 37

were clearly legitimate. TaintDroid also revealed that 15

of the 30 applications reported users’ locations to remote

advertising servers. Seven applications collected the de-

vice ID and, in some cases, the phone number and the

SIM card serial number. In all, two-thirds of the applica-

2 Approach Overview

their private data in realtime. Many smartphone appli-

as Panorama [57].

and storage.

• Context-based privacy sensitive information is dy-

• Applications can share information. Limiting the

monitoring system to a single application does not

account for flows via files and IPC between applica-

tions, including core system applications designed

to disseminate privacy sensitive information.

ence taint explosion if the stack pointer becomes falsely

tainted [49] and taint loss if complicated instructions

such as CMPXCHG, REP MOV are not instrumented

could arise.

| tion: | variable-level, method-level, message-level, and | • | Smartphones are resource constrained. | The re- |  |
| --- | --- | --- | --- | --- | --- |
| file-level. | Though the individual techniques are not | source limitations of smartphones precludes the use |  |  |  |
| new, our contributions lie in the integration of these | of heavyweight information tracking systems such |  |  |  |  |
| between performance and accuracy for resource con- | • | Third-party applications are entrusted with several |  |  |  |
| strained smartphones. | Experiments with our prototype | types of privacy sensitive information. | The mon- |  |  |
| for Android show that tracking incurs a runtime over- | itoring system must distinguish multiple informa- |  |  |  |  |
| head of less than 14% for a CPU-bound microbench- | tion types, which requires additional computation |  |  |  |  |
| We evaluated the accuracy of TaintDroid using 30 ran- | namic and can be difficult to identify even when |  |  |  |  |
| domly selected, popular Android applications that use lo- | sent in the clear. | For example, geographic locations |  |  |  |
| cation, camera, or microphone data. TaintDroid correctly | are pairs of floating point numbers that frequently |  |  |  |  |
| flagged 105 instances in which these applications trans- | change and are hard to predict. |  |  |  |  |
| tions in our study used sensitive data suspiciously. Our | We use dynamic taint analysis [57, 44, 8, 61, 39] (also |  |  |  |  |
| findings demonstrate that TaintDroid can help expose po- | called “taint tracking”) to monitor privacy sensitive in- |  |  |  |  |
| tential misbehavior by third-party applications. | formation on smartphones. Sensitive information is first |  |  |  |  |
| Like similar information-flow tracking systems [7, | identified at a | taint source | , where a | taint marking | indi- |
| 57], a fundamental limitation of TaintDroid is that it can | cating the information type is assigned. Dynamic taint |  |  |  |  |
| be circumvented through leaks via implicit flows. | The | analysis tracks how labeled data impacts other data in a |  |  |  |
| use of implicit flows to avoid taint detection is, in and of | way that might leak the original sensitive information. |  |  |  |  |
| itself, an indicator of malicious intent, and may well be | This tracking is often performed at the instruction level. |  |  |  |  |
| detectable through other techniques such as automated | Finally, the impacted data is identified before it leaves |  |  |  |  |
| static code analysis [14, 46] as we discuss in Section 8. | the system at a | taint sink | (usually the network interface). |  |  |
| The rest of this paper is organized as follows: Sec- | Existing taint tracking approaches have several lim- |  |  |  |  |
| tion 2 provides a high-level overview of TaintDroid, Sec- | itations. | First and foremost, approaches that rely on |  |  |  |
| tion 3 describes background information on the Android | instruction-level dynamic taint analysis using whole sys- |  |  |  |  |
| platform, Section 4 describes our TaintDroid design, | tem emulation [57, 7, 26] incur high performance penal- |  |  |  |  |
| Section 5 describes the taint sources tracked by Taint- | ties. Instruction-level instrumentation incurs 2-20 times |  |  |  |  |
| Droid, Section 6 presents results from our Android ap- | slowdown [57, 7] in addition to the slowdown introduced |  |  |  |  |
| plication study, Section 7 characterizes the performance | by emulation, which is not suitable for realtime analysis. |  |  |  |  |
| of our prototype implementation, Section 8 discusses the | Second, developing accurate taint propagation logic has |  |  |  |  |
| limitations of our approach, Section 9 describes related | proven challenging for the x86 instruction set [40, 48]. |  |  |  |  |
| work, and Section 10 summarizes our conclusions. | Implementations of instruction-level tracking can experi- |  |  |  |  |
| We seek to design a framework that allows users to | properly [61]. | While most smartphones use the ARM |  |  |  |
| monitor how third-party smartphone applications handle | instruction set, similar false positives and false negatives |  |  |  |  |
| cations are closed-source, therefore, static source code | Figure 1 presents our approach to taint tracking on |  |  |  |  |
| analysis is infeasible. Even if source code is available, | smartphones. We leverage architectural features of vir- |  |  |  |  |
| runtime events and configuration often dictate informa- | tual machine-based smartphones (e.g., Android, Black- |  |  |  |  |
| tion use; realtime monitoring accounts for these environ- | Berry, | and J2ME-based phones) to enable efficient, |  |  |  |
| ment specific dependencies. | system-wide taint tracking using fine-grained labels with |  |  |  |  |

---

## Page 3

Message-level tracking

| Application Code | Msg | Application Code |
| --- | --- | --- |
| Machine | Machine | tracking |
| Native System Libraries | Method-level |  |

tracking

tracking

the interpreter provides valuable context for avoiding

the taint explosion observed in the x86 instruction set.

defined interfaces through which applications access sen-

plications using native third-party libraries, but that the

number of affected applications remains small.

In summary, we provide a novel, efficient, system-

bining multiple granularities of information tracking.

While some techniques such as variable tracking within

tion 9), to our knowledge, our approach is the first to

extend such tracking system-wide. By choosing a mul-

wide approach is both highly efficient ( ∼ 14% CPU over-

3 Background: Android

our tracking system.

| Virtual | Virtual | Variable-level | wide, multiple-marking, taint tracking design by com- |
| --- | --- | --- | --- |
| Network Interface | Secondary Storage | File-level | an interpreter have been previously proposed (see Sec- |
| Figure 1: Multi-level approach for performance efficient | tiple granularity approach, we balance performance and |  |  |
| taint tracking within a common smartphone architecture. | accuracy. As we show in Sections 6 and 7, our system- |  |  |
| clear semantics. First, we instrument the VM interpreter | head and | ∼ | 4.4% memory overhead for simultaneously |
| to provide | variable-level tracking | within untrusted ap- | tracking 32 taint markings per data unit) and accurately |
| plication code. | 1 | Using variable semantics provided by | detects many suspicious network packets. |
| Additionally, by tracking variables, we maintain taint | Android [1] is a Linux-based, open source, mobile |  |  |
| markings only for data and not code. | Second, we use | phone platform. Most core phone functionality is imple- |  |
| message-level tracking | between applications. | Tracking | mented as applications running on top of a customized |
| taint on messages instead of data within messages mini- | middleware. | The middleware itself is written in Java |  |
| mizes IPC overhead while extending the analysis system- | and C/C++. Applications are written in Java and com- |  |  |
| wide. Third, for system-provided native libraries, we use | piled to a custom byte-code known as the Dalvik EXe- |  |  |
| method-level tracking | . | Here, we run native code with- | cutable (DEX) byte-code format. Each application exe- |
| out instrumentation and patch the taint propagation on | cutes within its Dalvik VM interpreter instance. Each in- |  |  |
| return. These methods accompany the system and have | stance executes as unique UNIX user identities to isolate |  |  |
| known information flow semantics. Finally, we use | file- | applications within the Linux platform subsystem. Ap- |  |
| level | tracking to ensure persistent information conserva- | plications communicate via the binder IPC mechanism. |  |
| tively retains its taint markings. | Binder provides transparent message passing based on |  |  |
| To assign labels, | we take advantage of the well- | parcels. We now discuss topics necessary to understand |  |
| sitive data. For example, all information retrieved from | Dalvik VM Interpreter: | DEX is a register-based ma- |  |
| GPS hardware is location-sensitive, and all informa- | chine language, as opposed to Java byte-code, which is |  |  |
| tion retrieved from an address book database is contact- | stack-based. Each DEX method has its own predefined |  |  |
| sensitive. This avoids relying on heuristics [10] or man- | number of virtual registers (which we frequently refer to |  |  |
| ual specification [61] for labels. We expand on informa- | as simply “registers”). The Dalvik VM interpreter man- |  |  |
| tion sources in Section 5. | ages method registers with an internal execution state |  |  |
| In order to achieve this tracking at multiple granulari- | stack; the current method’s registers are always on the |  |  |
| ties, our approach relies on the firmware’s integrity. The | top stack frame. | These registers loosely correspond to |  |
| taint tracking system’s trusted computing base includes | local variables in the Java method and store primitive |  |  |
| the virtual machine executing in userspace and any na- | types and object references. | All computation occurs |  |
| tive system libraries loaded by the untrusted interpreted | on registers, therefore values must be loaded from and |  |  |
| application. However, this code is part of the firmware, | stored to class fields before use and after use. Note that |  |  |
| and is therefore trusted. | Applications can only escape | DEX uses class fields for all long term storage, unlike |  |
| the virtual machine by executing native methods. In our | hardware register-based machine languages (e.g., x86), |  |  |
| target platform (Android), we modified the native library | which store values in arbitrary memory locations. |  |  |
| loader to ensure that applications can only load native li- | Native Methods: | The Android middleware provides ac- |  |
| braries from the firmware and not those downloaded by | cess to native libraries for performance optimization and |  |  |
| the application. Note that an early 2010 survey of the top | third-party libraries such as OpenGL and Webkit. | An- |  |
| 50 most popular free applications in each category of the | droid also uses Apache Harmony Java [3], which fre- |  |  |
| Android Market [2] (1100 applications in total) revealed | quently uses system libraries (e.g., math routines). Na- |  |  |
| that less than 4% included a | .so | file. A similar survey | tive methods are written in C/C++ and expose function- |
| conducted in mid 2010 revealed this fraction increased to | ality provided by the underlying Linux kernel and ser- |  |  |
| 5%, which indicates there is growth in the number of ap- | vices. They can also access Java internals, and hence are |  |  |

---

## Page 4



 

  

| alvik | alvik |  |  |  |  |  | Trusted Application | Trusted Application |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Trusted Application | Untrusted Application | Untrusted Application |  |  |  |  |  |
|  |  | Untrusted Application |  |  |  |  |  |  |
| nal | l | al |  | (8) |  |  |  |  |

  



ore    Taint Source Taint Source Taint Source (1)

ore       (1) (1) (1) Trusted Library Trusted Library Trusted Library Trusted Library

Taint Sink

Interpreted Code Interpreted Code 

] ] ]  



   

|  |  | JNI Hook | Binder Hook | Binder Hook |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | JNI Hook | Binder Hook |  |  |
|  | JNI Hook |  |  |  |  |  |  |
|  | (2) | Binder Hook | (3) | Binder Hook | Binder Hook | (7) | (9) |
| l |  |  |  |  |  |  |  |

   

|  |  |  |  |  | (3) |
| --- | --- | --- | --- | --- | --- |
| ds |  |  |  | (3) | (3) |
| ods | (2) | (4) | (4) | (6) |  |
|  | (5) | (6) |  |  |  |

(2)

| as |  |  | Dalvik VM | (2) | (5) |
| --- | --- | --- | --- | --- | --- |
| Userspace |  |  |  | (5) |  |
| as | Userspace |  |  |  |  |

Userspace Userspace   

   Virtual Taint Map



  

  Virtual Taint Map

s   

￿ Binder IPC Library DVM Intepreter Binder Hook

| ing Java | DVM Intepreter | (5) |  |
| --- | --- | --- | --- |
| g Java | ￿ |  |  |
| is | Kernel | Binder Kernel Module | Binder Kernel Module |
| s | Binder Kernel Module |  |  |
| h is | Kernel |  |  |
| ernal | Kernel |  |  |
| ernal | nal | Figure 2. | TaintDroid Architecture |
| e | Figure 2: TaintDroid architecture within Android. |  |  |

Figure 2. TaintDroid Architecture

Figure 2. TaintDroid Architecture

| se | Dalvik VM interpreter, storing the specified taint marking(s) |  |  |  |
| --- | --- | --- | --- | --- |
| are | in the virtual taint map. As the trusted application uses the |  |  |  |
| ity | e | in the virtual taint map. As the trusted application uses the | tainted information, the Dalvik VM propagates taint tags |  |
| y | An- | tainted information, the Dalvik VM propagates taint tags | (3) according to our data flow rules. When the trusted ap- | JNI methods conform to Java native interface standards |

specifications [32], which requires Dalvik to separate

| va [ | n- | 12] | (3) according to our data flow rules. When the trusted ap- | plication uses the tainted information in an IPC transaction, |
| --- | --- | --- | --- | --- |
| An- | (3) according to our data flow rules. When the trusted ap- | Java arguments into variables using a JNI call bridge. |  |  |
| [ | 12] | plication uses the tainted information in an IPC transaction, |  |  |
| braries | carries a taint tag reflecting the combined taint markings |  |  |  |

the modified binder library (4) ensures the parcel message

| roid | of all contained data. The parcel is passed transparently |
| --- | --- |
| raries | carries a taint tag reflecting the combined taint markings |

through the kernel (5) and received by the remote untrusted

to roid application. Note that the third-party interpreted code is of all contained data. The parcel is passed transparently

through the kernel (5) and received by the remote untrusted

ly, untrusted. The modified binder library retrieves the taint tag through the kernel (5) and received by the remote untrusted

application. Note that the third-party interpreted code is

| s to | DK) | from the parcel and assigns it to all values read from the | application. Note that the third-party interpreted code is |
| --- | --- | --- | --- |
| , | untrusted. The modified binder library retrieves the taint tag |  |  |
| tions. | K) | from the parcel and assigns it to all values read from the | tags (7) identically for the untrusted application. When the |
| nt | parcel (6). The remote Dalvik VM instance propagates taint |  |  |
| ons. | ent | tags (7) identically for the untrusted application. When the | sink (8), e.g., sending a data buffer over the network, the |
| tions. | tags (7) identically for the untrusted application. When the |  |  |
| The | s | untrusted application invokes a library specified as a taint | library retrieves the taint tag for the data in question (9-11) |
| des | untrusted application invokes a library specified as a taint | 4 | TaintDroid |

and makes a policy decision.

t sink (8), e.g., sending a data buffer over the network, the

At a high level, TaintDroid architecture enables system-

he library retrieves the taint tag for the data in question (9-11)

wide tracking by combining execution taint tracking, IPC

and makes a policy decision. variable-level tracking within the VM interpreter. Mul-

At a high level, TaintDroid architecture enables system-

int storage taint tracking. applications execute native methods, variable taint tags At a high level, TaintDroid architecture enables system-

wide tracking by combining execution taint tracking, IPC

| intDroid | to | aintDroid | Variable-level taint tracking | taint propagation, performance is sacrificed. On the other | Variable-level taint tracking |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| an | ations. | such as Panorama | end of the spectrum, approaches such as PRECIP | such as Panorama | tion is tainted (1) in a trusted application with sufficient | [panorama] | [panorama] | and TaintBochs | and TaintBochs |
| a- | off accuracy for performance; thus, they provide only nomi- |  |  |  |  |  |  |  |  |
| bu- | nal advantage over OS permissions (e.g., those implemented |  |  |  |  |  |  |  |  |
| cations. | end of the spectrum, approaches such as PRECIP |  |  |  |  |  |  |  |  |
| ng | ting | consider only high-level system calls into the kernel, trading | consider only high-level system calls into the kernel, trading |  |  |  |  |  |  |
| ca- | - | off accuracy for performance; thus, they provide only nomi- | off accuracy for performance; thus, they provide only nomi- |  |  |  |  |  |  |

type variables (e.g., int , float

| odify | sink libraries (Section VI) provide an easy interface to set |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | e all | and check the taint markings on primitive types. However, | In TaintDroid, we choose a middle ground, | In TaintDroid, we choose a middle ground, |  |  |  |  |  |  |  |  |
| alvik | tDroid. | Dalvik | level taint tracking | there are cases when object references must become tainted | level taint tracking | . TaintDroid is designed to taint | . TaintDroid is designed to taint |  |  |  |  |  |
| code, | de, | type | to ensure taint propagation operates correctly. Applications | type | variables (e.g., | variables (e.g., | int | int | , | float | , | float |
| dify | odify | t | sink libraries (Section VI) provide an easy interface to set | are compiled into the Dalvik EXecutable (DEX) byte-code | sink libraries (Section VI) provide an easy interface to set |  |  |  |  |  |  |  |

(8)

(8)

Taint Sink Taint Sink Taint Sink

(9) (11)

(9) (9)

untrusted application. Note that only the interpreted code (11) (11)

JNI Hook

JNI Hook JNI Hook

(7)

(7)

(10) (10)

Virtual Taint Map Interpreter

Virtual Taint Map

DVM Interpreter

DVM Interpreter

ports the event.

Implementing this architecture requires addressing

we store a 32-bit bitvector with each variable to encode

the taint tag, allowing 32 different taint markings.

stack. Before calling a method, the callee places the ar-

While previous approaches While previous approaches

[taintbochs] [taintbochs] [precip]

accessed as f p [2 · i ] after modification. Note that Dalvik

[precip] [precip]

, etc). Our taint source and

variable- variable-

primitive primitive

, etc). Our taint source and , etc). Our taint source and

| vik |  |  |  |  | Trusted Application | Untrusted Application | transaction, the modified binder library (4) ensures the |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | parcel has a taint tag reflecting the combined taint mark- |  |  |  |  |  |  |
| e |  |  |  |  | Taint Source | (8) | ings of all contained data. The parcel is passed transpar- |  |  |
| Interpreted Code | Interpreted Code | ently through the kernel (5) and received by the remote |  |  |  |  |  |  |  |
| l |  |  |  | is untrusted. | The modified binder library retrieves the |  |  |  |  |
| s | (4) | (4) | (6) | (6) | (7) | (10) | taint tag from the parcel and assigns it to all values read |  |  |
|  |  |  |  | Interpreter | Virtual Taint Map | Virtual Taint Map | Dalvik VM | from it (6). The remote Dalvik VM instance propagates |  |
| s |  |  |  | Virtual Taint Map | Virtual Taint Map | taint tags (7) identically for the untrusted application. |  |  |  |
| DVM Intepreter | Binder Hook | Binder IPC Library | DVM Interpreter | When the untrusted application invokes a library spec- |  |  |  |  |  |
| ing Java | ￿ | Binder Kernel Module | ified as a taint sink (8), e.g., network send, the library |  |  |  |  |  |  |
| Kernel | retrieves the taint tag for the data in question (9) and re- |  |  |  |  |  |  |  |  |
| e | e | several system challenges, including: | a | ) | taint tag stor- |  |  |  |  |
| e | included in our trusted computing base (see Section 2). | age, | b | ) | interpreted code taint propagation, | c | ) | native code |  |
| t use | Dalvik VM interpreter, storing the specified taint marking(s) | Android contains two types of native methods: inter- | taint propagation, | d | ) | IPC taint propagation, and | e | ) | sec- |
| t use | Dalvik VM interpreter, storing the specified taint marking(s) | nal VM methods and JNI methods. | The internal VM | ondary storage taint propagation. The remainder of this |  |  |  |  |  |
| are | in the virtual taint map. As the trusted application uses the | methods access interpreter-specific structures and APIs. | section describes our design. |  |  |  |  |  |  |
| ity | tainted information, the Dalvik VM propagates taint tags | 4.1 | Taint Tag Storage |  |  |  |  |  |  |
| f | the modified binder library (4) ensures the parcel message | The choice of how to store taint tags influences per- |  |  |  |  |  |  |  |
| va [ | 12] | plication uses the tainted information in an IPC transaction, | Conversely, internal VM methods must manually parse | formance and memory overhead. | Dynamic taint track- |  |  |  |  |
| of | the modified binder library (4) ensures the parcel message | arguments from the interpreter’s byte array of arguments. | ing systems commonly store tags for every data byte or |  |  |  |  |  |  |
| ibraries | carries a taint tag reflecting the combined taint markings | Binder IPC: | All Android IPC occurs through binder. | word [57, 7]. Tracked memory is unstructured and with- |  |  |  |  |  |
| id | of all contained data. The parcel is passed transparently | Binder is a component-based processing and IPC frame- | out content semantics. | Frequently taint tags are stored |  |  |  |  |  |
| work designed for BeOS, extended by Palm Inc., and | in non-adjacent shadow memory [57] and tag maps [61]. |  |  |  |  |  |  |  |  |
| customized for Android by Google. | Fundamental to | TaintDroid uses variable semantics within the Dalvik in- |  |  |  |  |  |  |  |
| binder are | parcels | , which serialize both active and stan- | terpreter. | We store taint tags adjacent to variables in |  |  |  |  |  |

lly, nt parcel (6). The remote Dalvik VM instance propagates taint untrusted. The modified binder library retrieves the taint tag dard data objects. The former includes references to memory, providing spatial locality.

DK) from the parcel and assigns it to all values read from the binder objects, which allows the framework to manage Dalvik has five variable types that require taint stor-

des t parcel (6). The remote Dalvik VM instance propagates taint untrusted application invokes a library specified as a taint shared data objects between processes. A binder kernel age: method local variables, method arguments, class

| module passes parcel messages between processes. | static fields, class instance fields, and arrays. In all cases, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ent | sink (8), e.g., sending a data buffer over the network, the | TaintDroid is a realization of our multiple granularity | Dalvik stores method local variables and arguments |  |  |
| . The | library retrieves the taint tag for the data in question (9-11) | taint tracking approach within Android. TaintDroid uses | on an internal stack. | When an application invokes a |  |
| and makes a policy decision. | method, a new stack frame is allocated for all local vari- |  |  |  |  |
| taint tracking, native interface taint tracking, and secondary | tiple taint markings are stored as one | taint tag | . | When | ables. Method arguments are also passed via the internal |

aintDroid Variable-level taint tracking wide tracking by combining execution taint tracking, IPC are patched on return. Finally, taint tags are assigned While previous approaches guments on the top of the stack such that they become

n taint tracking, native interface taint tracking, and secondary such as Panorama taint tracking, native interface taint tracking, and secondary to parcels and propagated through binder. [panorama] and TaintBochs Note that [taintbochs] high numbered registers in the callee’s stack frame. We

nt aint storage taint tracking. provide high-accuracy taint tracking via instruction-level storage taint tracking. the Technical Report [17] version of this paper contains allocate taint tag storage by doubling the size of the stack

more implementation details. frame allocation. Taint tags are interleaved between val-

Figure 2 depicts TaintDroid’s architecture. Informa- ues such that register v i originally accessed via f p [ i ] is

ting provide high-accuracy taint tracking via instruction-level consider only high-level system calls into the kernel, trading provide high-accuracy taint tracking via instruction-level context (e.g., the location provider). The taint inter- stores 64-bit variables as two adjacent 32-bit registers on

to taint propagation, performance is sacrificed. On the other taint propagation, performance is sacrificed. On the other face invokes a native method (2) that interfaces with the the internal stack. While the byte-code interprets these

| tions. | end of the spectrum, approaches such as PRECIP | Dalvik VM interpreter, storing specified taint markings | adjacent registers as a single 64-bit value, the interpreter |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing | in Android). | in the virtual taint map. The Dalvik VM propagates taint | manages these registers as separate values. | Therefore, |  |  |  |  |  |  |
| e all | tags (3) according to data flow rules as the trusted ap- | In TaintDroid, we choose a middle ground, | variable- | our modified stack transparently stores and retrieves 64- |  |  |  |  |  |  |
| Dalvik | level taint tracking | plication uses the tainted information. Every interpreter | . TaintDroid is designed to taint | primitive | bit values to and from separate 32-bit registers (at | f p | [2 | · | i | ] |

code, bu- - nal advantage over OS permissions (e.g., those implemented nal advantage over OS permissions (e.g., those implemented instance simultaneously propagates taint tags. When the and f p [2 · i + 2] ). Finally, native method targets require

ing g in Android). in Android). trusted application uses the tainted information in an IPC a slightly different stack frame organization for reasons

---

## Page 5

Low Addresses ( 0x00000000 ) Interpreted Targets Native Targets propriate propagation logic. We use a data flow logic, as

out0

VM goop

frame pointer (current)

out0 v1 == in0 arg0

out0 taint tag v1 taint tag arg1

VM goop

frame pointer (previous)

v1 == local1

represent taint tags.

discussed in Section 4.3. The modified stack format is

shown in Figure 3.

Taint tags are stored adjacent to class fields and ar-

rays inside the VM interpreter’s internal data structures.

TaintDroid stores only one taint tag per array to minimize

storage overhead. Per-value taint tag storage is severely

inefficient for Java String objects, as all characters have

terpreter. Variables provide valuable semantics for taint

4.2.1 Taint Propagation Logic

significant performance overhead and overestimation in

then present our logic rules for DEX.

instance of one of the five types described in Section 4.1.

denoted v

require an instance object and are denoted v y ( f x ) , where

variable.

Our virtual taint map function is τ ( · ) . τ ( v ) returns the

taint tag t for variable v . τ ( v ) is also used to assign a

taint tag to a variable. Retrieval and assignment are dis-

tinguished by the position of τ ( · ) w.r.t. the ← symbol.

When τ ( v ) appears on the right hand side of ← , τ ( v ) re-

trieves the taint tag for v . When τ ( v ) appears on the left

hand side, τ ( v ) assigns the taint tag for v . For example,

τ ( v

ister. For example, we do not consider the array-length

the resulting “A” value should be tainted even though the

“A” value in the array is not. Hence, the taint logic for

| stack pointer (top) | tracking implicit flows requires static analysis and causes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v0 | == | local0 | tracking [29] (see Section 8). We begin by defining taint |  |  |  |  |  |  |  |  |  |  |  |  |  |
| v0 | taint | tag | markings, taint tags, variables, and taint propagation. We |  |  |  |  |  |  |  |  |  |  |  |  |  |
| out1 | v2 | == | in1 | return | taint | Let | L | be the universe of taint markings for a particular |  |  |  |  |  |  |  |  |
| out1 | taint | tag | v2 | taint | tag | arg0 | taint | tag | system. A taint tag | t | is a set of taint markings, | t | ⊆ L | . |  |  |
| (unused) | arg1 | taint | tag | Each variable has an associated taint tag. A variable is an |  |  |  |  |  |  |  |  |  |  |  |  |
| v0 | == | local0 | variable | We use a different representation for each type. The local |  |  |  |  |  |  |  |  |  |  |  |  |
| v0 | taint | tag | variable taint tag | and argument variables correspond to virtual registers, |  |  |  |  |  |  |  |  |  |  |  |  |
| v1 | taint | tag | x | . Class field variables are denoted as | f | x | to in- |  |  |  |  |  |  |  |  |  |
| v2 | == | in0 | dicate a field variable with class index | x | . Instance fields |  |  |  |  |  |  |  |  |  |  |  |
| v4 | taint | tag | v | y | is the instance object reference (note that both the ob- |  |  |  |  |  |  |  |  |  |  |  |
| High Addresses ( | 0xffffffff | ) | ject reference and the dereferenced value are variables). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Figure 3: Modified Stack Format. Taint tags are inter- | Static fields are denoted as | f | x | alone, which is shorthand |  |  |  |  |  |  |  |  |  |  |  |  |
| leaved between registers for interpreted method targets | for | S | ( | f | x | ) | , where | S | () | is the static scope. | Finally, | v | x | [ | · | ] |
| and appended for native methods. | Dark grayed boxes | denotes an array, where | v | x | is an array object reference |  |  |  |  |  |  |  |  |  |  |  |
| the same tag. Unfortunately, storing one taint tag per ar- | 1 | ) | ← | τ | ( | v | 2 | ) | copies the taint tag from | v | 2 | to | v | 1 | . |  |
| ray may result in false positives during taint propagation. | Table 1 captures our propagation logic. The table enu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For example, if untainted variable | u | is stored into array | A | merates abstracted versions of the byte-code instructions |  |  |  |  |  |  |  |  |  |  |  |  |
| at index | 0 | ( | A | [0] | ) and tainted variable | t | is stored into | A | [1] | , | specified in the DEX documentation. Register variables |  |  |  |  |  |
| then array | A | is tainted. Later, if variable | v | is assigned | and class fields are referenced by | v | X | and | f | X | , respec- |  |  |  |  |  |
| to | A | [0] | , | v | will be tainted, even though | u | was untainted. | tively. | R | and | E | are the return and exception variables |  |  |  |  |
| Fortunately, Java frequently uses objects, and object ref- | maintained within the interpreter, respectively. | A | , | B | , and |  |  |  |  |  |  |  |  |  |  |  |
| erences are infrequently tainted (see Section 4.2), there- | C | are constants in the byte-code. The table does not list |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| fore this coding practice leads to less false positives. | instructions that clear the taint tag of the destination reg- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4.2 | Interpreted Code Taint Propagation | instruction to return a tainted value even if the array is |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Taint tracking granularity and flow semantics influ- | tainted. Note that the array length is sometimes used to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ence performance and accuracy. TaintDroid implements | aid direct control flow propagation (e.g., Vogt et al. [53]). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| variable-level taint tracking within the Dalvik VM in- | 4.2.2 | Tainting Object References |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| propagation, distinguishing data pointers from scalar val- | The propagation rules in Table 1 are straightforward |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ues. TaintDroid primarily tracks primitive type variables | with two exceptions. First, taint propagation logics com- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (e.g., | int | , | float | , etc); however, there are cases when object | monly include the taint tag of an array index during |  |  |  |  |  |  |  |  |  |  |  |
| references must become tainted to ensure taint propaga- | lookup to handle translation tables (e.g., ASCII/UNI- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tion operates correctly; this section addresses why these | CODE or character case conversion). For example, con- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cases exist. | However, first we present taint tracking in | sider a translation table from lowercase to upper case |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the Dalvik machine language as a formal logic. | characters: if a tainted value “a” is used as an array index, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The Dalvik VM operates on the unique DEX machine | aget-op | uses both the array and array index taint. Sec- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| language instruction set, therefore we must design an ap- | ond, when the array contains object references (e.g., an |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

Table 1: DEX Taint Propagation Logic. Register variables and class fields are referenced by v X and f X , respectively.

R and E are the return and exception variables maintained within the interpreter. A , B , and C are byte-code constants.

| Op Format | Op Semantics | Taint Propagation | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| const-op | v | A | C | v | A | ← | C | τ | ( | v | A | ) | ← ∅ | Clear | v | A | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| move-op | v | A | v | B | v | A | ← | v | B | τ | ( | v | A | ) | ← | τ | ( | v | B | ) | Set | v | A | taint to | v | B | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| move-op-R | v | A | v | A | ← | R | τ | ( | v | A | ) | ← | τ | ( | R | ) | Set | v | A | taint to return taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| return-op | v | A | R | ← | v | A | τ | ( | R | ) | ← | τ | ( | v | A | ) | Set return taint ( | ∅ | if void) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| move-op-E | v | A | v | A | ← | E | τ | ( | v | A | ) | ← | τ | ( | E | ) | Set | v | A | taint to exception taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| throw-op | v | A | E | ← | v | A | τ | ( | E | ) | ← | τ | ( | v | A | ) | Set exception taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| unary-op | v | A | v | B | v | A | ← ⊗ | v | B | τ | ( | v | A | ) | ← | τ | ( | v | B | ) | Set | v | A | taint to | v | B | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| binary-op | v | A | v | B | v | C | v | A | ← | v | B | ⊗ | v | C | τ | ( | v | A | ) | ← | τ | ( | v | B | ) | ∪ | τ | ( | v | C | ) | Set | v | A | taint to | v | B | taint | ∪ | v | C | taint |  |
| binary-op | v | A | v | B | v | A | ← | v | A | ⊗ | v | B | τ | ( | v | A | ) | ← | τ | ( | v | A | ) | ∪ | τ | ( | v | B | ) | Update | v | A | taint with | v | B | taint |  |  |  |  |  |  |  |
| binary-op | v | A | v | B | C | v | A | ← | v | B | ⊗ | C | τ | ( | v | A | ) | ← | τ | ( | v | B | ) | Set | v | A | taint to | v | B | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |
| aput-op | v | A | v | B | v | C | v | B | [ | v | C | ] | ← | v | A | τ | ( | v | B | [ | · | ]) | ← | τ | ( | v | B | [ | · | ]) | ∪ | τ | ( | v | A | ) | Update array | v | B | taint with | v | A | taint |
| aget-op | v | A | v | B | v | C | v | A | ← | v | B | [ | v | C | ] | τ | ( | v | A | ) | ← | τ | ( | v | B | [ | · | ]) | ∪ | τ | ( | v | C | ) | Set | v | A | taint to array and index taint |  |  |  |  |  |
| sput-op | v | A | f | B | f | B | ← | v | A | τ | ( | f | B | ) | ← | τ | ( | v | A | ) | Set field | f | B | taint to | v | A | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sget-op | v | A | f | B | v | A | ← | f | B | τ | ( | v | A | ) | ← | τ | ( | f | B | ) | Set | v | A | taint to field | f | B | taint |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| iput-op | v | A | v | B | f | C | v | B | ( | f | C | ) | ← | v | A | τ | ( | v | B | ( | f | C | )) | ← | τ | ( | v | A | ) | Set field | f | C | taint to | v | A | taint |  |  |  |  |  |  |  |
| iget-op | v | A | v | B | f | C | v | A | ← | v | B | ( | f | C | ) | τ | ( | v | A | ) | ← | τ | ( | v | B | ( | f | C | )) | ∪ | τ | ( | v | B | ) | Set | v | A | taint to field | f | C | and object reference taint |  |
| public | static | Integer | valueOf(int | i) | { | only by including the object reference taint tag when the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| if | (i | < | -128 | \|\| | i | > | 127) | { | value | field is read from the Integer (i.e., the | iget-op | prop- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

return new Integer(i); }

return valueOfCache.CACHE [i+128];

}

static class valueOfCache {

static {

Figure 4: Excerpt from Android’s Integer class illustrat-

ing the need for object reference taint propagation.

The code listed in Figure 4 demonstrates a real in-

stance of where object reference tainting is needed. Here,

valueOf() returns an Integer object for a passed int . If the

int argument is between − 128 and 127 , valueOf() returns

reference to a statically defined Integer object. valueOf()

is implicitly called for conversion to an object. Consider

the following definition and use of a method intProxy() .

Consider the case where tVal is an int with value 1

and taint tag TAG . When intProxy() is passed tVal , TAG

is propagated to val . When intProxy() returns val , it

calls Integer.valueOf() to obtain an Integer instance cor-

agation rule), will the correct taint tag of TAG be assigned

to out .

postconditions for accurate taint tracking in the Java-

like environment: 1) all accessed external variables (i.e.,

class fields referenced by other methods) are assigned

taint tags according to data flow rules; and 2) the re-

Internal VM Methods: Internal VM methods are called

directly by interpreted code, passing a pointer to an ar-

ray of 32-bit register arguments and a pointer to a return

value. The stack augmentation shown in Figure 3 pro-

vides access to taint tags for both Java arguments and

the return value. As there are a relatively small number

of internal VM methods which are infrequently added

internal VM methods in Android version 2.1; however,

only 5 required patching: the System.arraycopy() native

method for copying array contents, and several native

methods implementing Java reflection.

static final Integer[] CACHE = new Integer[256]; 4.3 Native Code Taint Propagation

| for(int i=-128; | i<=127; | i++) | { | Native code is unmonitored in TaintDroid. | Ideally, |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CACHE[i+128] | = | new | Integer(i); | } | } | we achieve the same propagation semantics as the in- |  |  |  |
| } | terpreted counterpart. | Hence, we define two | necessary |  |  |  |  |  |  |
| Integer | array), the index taint tag is propagated to the ob- | turn value is assigned a taint tag according to data flow |  |  |  |  |  |  |  |
| ject reference and not the object value. | Therefore, we | rules. TaintDroid achieves these postconditions through |  |  |  |  |  |  |  |
| include the object reference taint tag in the instance | get | an assortment of manual instrumentation, heuristics, and |  |  |  |  |  |  |  |
| ( | iget-op | ) rule. | method profiles, depending on situational requirements. |  |  |  |  |  |  |
| Object | intProxy(int | val) | { | return | val; | } | between versions, | 2 | we manually inspected and patched |
| int | out | = | (Integer) | intProxy(tVal); | them for taint propagation as needed. We identified 185 |  |  |  |  |
| responding to the scalar variable | val | . In this case, | Inte- | JNI Methods: | JNI methods are invoked through the |  |  |  |  |
| ger.valueOf() | returns a reference to the static Integer ob- | JNI call bridge. The call bridge parses Java arguments |  |  |  |  |  |  |  |
| ject with value | 1 | . The | value | field (of the | Integer | class) in | and assigns a return value using the method’s descriptor |  |  |
| the object has taint tag of | ∅ | ; however, since the | aget-op | string. We patched the call bridge to provide taint propa- |  |  |  |  |  |
| propagation rule includes the taint of the index register, | gation for all JNI methods. When a JNI method returns, |  |  |  |  |  |  |  |  |
| the object reference has a taint tag of | TAG | . Therefore, | TaintDroid consults a method profile table for tag propa- |  |  |  |  |  |  |

---

## Page 7

gation updates. A method profile is a list of ( f rom, to ) However, this additional complexity will negatively im-

pairs indicating flows between variables, which may be pact IPC performance.

method parameters, class variables, or return values.

Enumerating the information flows for all JNI methods

ods with a Java interface and C or C++ implementation. 3

Of these methods, 913 did not reference objects (as argu-

ments, return value, or method body) and hence are auto-

4.4 IPC Taint Propagation

ues without taint propagation. For example, if an IPC

parcel message contains a sequence of scalar values, the

passing as portions the value as configuration parameters

4.5 Secondary Storage Taint Propagation

performance overhead.

4.6 Taint Interface Library

only provides the ability to add and not set or clear taint

tags, as such functionality could be used by untrusted

5 Privacy Hook Placement

defining the taint source.

| is a time consuming task best completed automatically | Taint tags may be lost when data is written to a file. |  |  |
| --- | --- | --- | --- |
| using source code analysis (a task we leave for future | Our design stores one taint tag per file. | The taint tag |  |
| work). | We currently include an additional propagation | is updated on file write and propagated to data on file |  |
| heuristic patch. | The heuristic is conservative for JNI | read. | TaintDroid stores file taint tags in the file sys- |
| methods that only operate on primitive and String ar- | tem’s extended attributes. | To do this, we implemented |  |
| guments and return values. | It assigns the union of the | extended attribute support for Android’s host file system |  |
| method argument taint tags to the taint tag of the return | (YAFFS2) and formatted the removable SDcard with the |  |  |
| value. While the heuristic has false negatives for meth- | ext2 file system. | As with arrays and IPC, storing one |  |
| ods using objects, it covers many existing methods. | taint tag per file leads to false positives and limits the |  |  |
| We performed a survey of the JNI methods included | granularity of taint markings for information databases |  |  |
| in the official Android source code (version 2.1) to de- | (see Section 5). Alternatively, we could track taint tags |  |  |
| termine specific properties. We found 2,844 JNI meth- | at a finer granularity at the expense of added memory and |  |  |
| matically covered by our heuristic. The remaining meth- | Taint sources and sinks defined within the virtualized |  |  |
| ods may or may not have information flows that produce | environment must communicate taint tags with the track- |  |  |
| false negatives. Currently, we define method profiles as | ing system. We abstract the taint source and sink logic |  |  |
| needed. For example, methods in the IBM | NativeCon- | into a single taint interface library. | The interface per- |
| verter | class require propagation for conversion between | forms two functions: 1) add taint markings to variables; |  |
| character and byte arrays. | and 2) retrieve taint markings from variables. The library |  |  |
| Taint tags must propagate between applications when | Java code to remove taint markings. |  |  |
| they exchange data. | The tracking granularity affects | Adding taint tags to arrays and strings via internal VM |  |
| performance and memory overhead. | TaintDroid uses | methods is straightforward, as both are stored in data ob- |  |
| message-level taint tracking. A message taint tag repre- | jects. | Primitive type variables, on the other hand, are |  |
| sents the upper bound of taint markings assigned to vari- | stored on the interpreter’s internal stack and disappear |  |  |
| ables contained in the message. | We use message-level | after a method is called. Therefore, the taint library uses |  |
| granularity to minimize performance and storage over- | the method return value as a means of tainting primitive |  |  |
| head during IPC. | type variables. The developer passes a value or variable |  |  |
| We chose to implement message-level over variable- | into the appropriate add taint method (e.g., | addTaintInt() | ) |
| level taint propagation, because in a variable-level sys- | and the returned variable has the same value but addition- |  |  |
| tem, a devious receiver could game the monitoring by | ally has the specified taint tag. Note that the stack storage |  |  |
| unpacking variables in a different way to acquire val- | does not pose complications for taint tag retrieval. |  |  |
| receiver may unpack a string instead, thereby acquiring | Using TaintDroid for privacy analysis requires iden- |  |  |
| values without propagating all the taint tags on scalar val- | tifying privacy sensitive sources and instrumenting taint |  |  |
| ues in the sequence. Hence, to prevent applications from | sources within the operating system. | Historically, dy- |  |
| removing taint tags in this way, the current implementa- | namic taint analysis systems assume taint source and sink |  |  |
| tion protects taint tags at the message-level. | placement is trivial. | However, complex operating sys- |  |
| Message-level taint propagation for IPC leads to false | tems such as Android provide applications information |  |  |
| positives. | Similar to arrays, all data items in a parcel | in a variety of ways, e.g., direct access, and service inter- |  |
| share the same taint tag. | For example, Section 8 dis- | face. Each potential type of privacy sensitive information |  |
| cusses limitations for tracking the IMSI that results from | must be studied carefully to determine the best method of |  |  |
| in parcels. Future implementations will consider word- | Taint sources can only add taint tags to memory for |  |  |
| level taint tags along with additional consistency checks | which TaintDroid provides tag storage. Currently, taint |  |  |
| to ensure accurate propagation for unpacked variables. | source and sink placement is limited to variables in in- |  |  |

---

## Page 8

terpreted code, IPC messages, and files. This section 6 Application Study

discusses how valuable taint sources and sinks can be im-

plemented within these restrictions. We generalize such

taint sources based on information characteristics.

ager and SensorManager applications.

Information Databases: Shared information such as ad-

dress books and SMS messages are often stored in file-

based databases. This organization provides a useful un-

ambiguous taint source similar to hardware sensors. By

adding a taint tag to such database files, all informa-

tion read from the file will be automatically tainted. We

used this technique for tracking address book informa-

tion. Note that while TaintDroid’s file-level granularity

was appropriate for these valuable information sources,

others may exist for which files are too coarse grained.

However, we have not yet encountered such sources.

Device Identifiers: Information that uniquely identifies

the phone or the user is privacy sensitive. Not all per-

sonally identifiable information can be easily tainted.

However, the phone contains several easily tainted iden-

tifiers: the phone number, SIM card identifiers (IMSI,

ICC-ID), and device identifier (IMEI) are all accessed

through well-defined APIs. We instrumented the APIs

for the phone number, ICC-ID, and IMEI. An IMSI taint

the native socket library is invoked.

This section reports on an application study that uses

TaintDroid to analyze how 30 popular third-party An-

droid applications use privacy sensitive user data. Exist-

6.1 Experimental Setup

tual access or use of sensitive data.

We studied each of the thirty downloaded applica-

tions by starting the application, performing any initial-

ization or registration that was required, and then man-

ually exercising the functionality offered by the appli-

cation. We recorded system logs including detailed in-

formation from TaintDroid: tainted binder messages,

tainted file output, and tainted network messages with

the remote address. The overall experiment (conducted

in May 2010) lasted slightly over 100 minutes, generat-

ing 22,594 packets (8.6MB) and 1,130 TCP connections.

To verify our results, we also logged the network traffic

using tcpdump on the WiFi interface and repeated exper-

iments on multiple Nexus One phones, running the same

version of TaintDroid built on Android 2.1. Though the

phones used for experiments had a valid SIM card in-

stalled, the SIM card was inactivate, forcing all the pack-

ets to be transmitted via the WiFi interface. The packet

trace was used only to verify the exposure of tainted data

flagged by TaintDroid.

applications acquired user consent (either explicit or im-

the weather server.

| Low-bandwidth Sensors: | A variety of privacy sensitive | ing applications acquire a variety of user data along with |  |
| --- | --- | --- | --- |
| information types are acquired through low-bandwidth | permissions to access the Internet. Our study finds that |  |  |
| sensors, e.g., location and accelerometer. Such informa- | two thirds of these applications expose detailed location |  |  |
| tion often changes frequently and is simultaneously used | data, the phone’s unique ID, and the phone number using |  |  |
| by multiple applications. | Therefore, it is common for | the combination of the seemingly innocuous access per- |  |
| a smartphone OS to multiplex access to low-bandwidth | missions granted at install. This finding was made possi- |  |  |
| sensors using a manager. This sensor manager represents | ble by TaintDroid’s ability to monitor runtime | access | of |
| an ideal point for taint source hook placement. For our | sensitive user data and to precisely relate the monitored |  |  |
| analysis, we placed hooks in Android’s LocationMan- | accesses with the | data exposure | by applications. |
| High-bandwidth Sensors: | Privacy sensitive informa- | An early 2010 survey of the 50 most popular free ap- |  |
| tion sources such as the microphone and camera are | plications in each category of the Android Market [2] |  |  |
| high-bandwidth. Each request from the sensor frequently | (1,100 applications, in total) revealed that roughly a third |  |  |
| returns a large amount of data that is only used by one | of the applications (358 of the 1,100 applications) re- |  |  |
| application. | Therefore, the smartphone OS may share | quire Internet permissions along with permissions to ac- |  |
| sensor information via large data buffers, files, or both. | cess either location, camera, or audio data. From this set, |  |  |
| When sensor information is shared via files, the file must | we randomly selected 30 popular applications (an 8.4% |  |  |
| be tainted with the appropriate tag. Due to flexible APIs, | sample size), which span twelve categories. Table 2 enu- |  |  |
| we placed hooks for both data buffer and file tainting for | merates these applications along with permissions they |  |  |
| tracking microphone and camera information. | request at install time. Note that this does not reflect ac- |  |  |
| source has inherent limitations discussed in Section 8. | In addition to the network trace, we also noted whether |  |  |
| Network Taint Sink: | Our privacy analysis identifies | plicit) for exporting sensitive information. This provides |  |
| when tainted information transmits out the network in- | additional context information to identify possible pri- |  |  |
| terface. The VM interpreter-based approach requires the | vacy violations. For example, by selecting the “use my |  |  |
| taint sink to be placed within interpreted code. Hence, | location” option in a weather application, the user im- |  |  |
| we instrumented the Java framework libraries at the point | plicitly consents to disclosing geographic coordinates to |  |  |

---

## Page 9

Table 2: Applications grouped by the requested permissions (L: location, C: camera, A: audio, P: phone state). Android

Market categories are indicated in parenthesis, showing the diversity of the studied applications.

Babble (Social); Manga Browser (Comics)

Blackjack, (Games); Horoscope (Lifestyle); Yellow Pages (Reference); 3001 Wisdom Quotes

Lite, Dastelefonbuch, Astrid (Productivity), BBC News Live Stream (News & Weather); Ring-

tones (Entertainment)

(Game); ProBasketBall (Sports)

† All listed applications also require access to the Internet.

violations, one of which had a violation in all three categories.

Observed Behavior (# of apps) Details

Table 3 summarizes our findings. TaintDroid flagged

105 TCP connections as containing tainted privacy sen-

sitive information. We manually labeled each mes-

sage based on available context, including remote server

names and temporally relevant application log messages.

We used remote hostnames as an indication of whether

transmissions immediately after the application received

a tainted parcel from the system location manager. We

now expand on our findings for each category and reflect

on potential privacy violations.

Permissions †

L C A P

geo-coordinates to the app’s content server.

the IMEI number to the app’s content server.

2 apps to ads.mobclix.com (1 sent location both to admob.com and

ads.mobclix.com) and 4 apps sent location † to data.flurry.com.

identify an individual user on a GSM network, and (3)

the ICC-ID number which is a unique SIM card serial

number. We verified messages were flagged correctly by

inspecting the plaintext payload. 4  In neither case was the

user informed that this information was transmitted off

the phone.

Device Unique ID: The device’s IMEI was also exposed

by applications. The IMEI uniquely identifies a specific

mobile phone and is used to prevent a stolen handset

from accessing the cellular network. TaintDroid flags

| Applications | ∗ | # |  |  |
| --- | --- | --- | --- | --- |
| The Weather Channel (News & Weather); Cestos, Solitaire (Game); Movies (Entertainment); | 6 | x |  |  |
| Bump, Wertago (Social); Antivirus (Communication); ABC — Animals, Traffic Jam, Hearts, | 14 | x | x |  |
| Layar (Lifestyle); Knocking (Social); Coupons (Shopping); Trapster (Travel); Spongebob Slide | 6 | x | x | x |
| MySpace (Social); Barcode Scanner, ixMAT (Shopping) | 3 | x |  |  |
| Evernote (Productivity) | 1 | x | x | x |

∗ Listed names correspond to the name displayed on the phone and not necessarily the name listed in the Android Market.

Table 3: Potential privacy violations by 20 of the studied applications. Note that three applications had multiple

Phone Information to Content Servers (2) 2 apps sent out the phone number, IMSI, and ICC-ID along with the

Device ID to Content Servers (7) ∗ 2 Social, 1 Shopping, 1 Reference and three other apps transmitted

Location to Advertisement Servers (15) 5 apps sent geo-coordinates to ad.qwapi.com, 5 apps to admob.com,

∗ TaintDroid flagged nine applications in this category, but only seven transmitted the raw IMEI without mentioning such practice in the EULA.

† To the best of our knowledge, the binary messages contained tainted location data (see the discussion below).

| 6.2 | Findings | ber, (2) the IMSI which is a unique 15-digit code used to |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| data was being sent to a server providing application | This | finding | demonstrates | that | Android’s | coarse- |
| functionality or to a third party. | Frequently, messages | grained access control provides insufficient protection |  |  |  |  |
| contained plaintext that aided categorization, e.g., an | against third-party applications seeking to collect sensi- |  |  |  |  |  |
| HTTP GET request containing geographic coordinates. | tive data. Moreover, we found that one application trans- |  |  |  |  |  |
| However, 21 flagged messages contained binary data. | mits the phone information | every time | the phone boots. |  |  |  |
| Our investigation indicates these messages were gen- | While this application displays a terms of use on first use, |  |  |  |  |  |
| erated by the Google Maps for Mobile [21] and Flur- | the terms of use does not specify collection of this highly |  |  |  |  |  |
| ryAgent [20] APIs and contained tainted privacy sensi- | sensitive data. Surprisingly, this application transmits the |  |  |  |  |  |
| tive data. These conclusions are supported by message | phone data immediately after install, before first use. |  |  |  |  |  |
| Phone Information: | Table 2 shows that 21 out of the | indicated that nine applications transmitted the IMEI. |  |  |  |  |
| 30 applications require permissions to read phone state | Seven out of the nine applications either do not present |  |  |  |  |  |
| and the Internet. We found that 2 of the 21 applications | an End User License Agreement (EULA) or do not spec- |  |  |  |  |  |
| transmitted to their server (1) the device’s phone num- | ify IMEI collection in the EULA. One of the seven ap- |  |  |  |  |  |

---

## Page 10

| plications is a popular social networking application and | TaintDroid, 37 were deemed clearly legitimate use. The |  |  |
| --- | --- | --- | --- |
| another is a location-based search application. Further- | flags resulted from four applications and the OS itself |  |  |
| more, we found two of the seven applications include the | while using the Google Maps for Mobile (GMM) API. |  |  |
| IMEI when transmitting the device’s geographic coordi- | The TaintDroid logs indicate an HTTP request with the |  |  |
| nates to their content server, potentially repurposing the | “User-Agent: | GMM . . . ” | header, but a binary pay- |
| IMEI as a client ID. | load. Given that GMM functionality includes download- |  |  |
| In comparison, two of the nine applications treat the | ing maps based on geographic coordinates, it is obvious |  |  |
| IMEI with more care, thus we do not classify them as | that TaintDroid correctly identified location information |  |  |
| potential privacy violators. | One application displays a | in the payload. Our manual inspection of each message |  |
| privacy statement that clearly indicates that the applica- | along with the network packet trace confirmed that there |  |  |
| tion collects the device ID. The other uses the hash of | were no false positives. We note that there is a possibil- |  |  |
| the IMEI instead of the number itself. We verified this | ity of false negatives, which is difficult to verify with the |  |  |
| practice by comparing results from two different phones. | lack of the source code of the third-party applications. |  |  |
| Location Data to Advertisement Servers: | Half of the | Summary: | Our study of 30 popular applications shows |
| studied applications exposed location data to third-party | the effectiveness of the TaintDroid system in accu- |  |  |
| advertisement servers without requiring implicit or ex- | rately tracking applications’ use of privacy sensitive data. |  |  |
| plicit user consent. Of the fifteen applications, only two | While monitoring these applications, TaintDroid gener- |  |  |
| presented a EULA on first run; however neither EULA | ated no false positives (with the exception of the IMSI |  |  |
| indicated this practice. | Exposure of location informa- | taint source which we disabled for experiments, see Sec- |  |
| tion occurred both in plaintext and in binary format. | tion 8). The flags raised by TaintDroid helped to identify |  |  |
| The latter highlights TaintDroid’s advantages over sim- | potential privacy violations by the tested applications. |  |  |
| ple pattern-based packet scanning. Applications sent lo- | Half of the studied applications share location data with |  |  |
| cation data in plaintext to admob.com, ad.qwapi.com, | advertisement servers. | Approximately one third of the |  |
| ads.mobclix.com (11 applications) and in binary format | applications expose the device ID, sometimes with the |  |  |
| to FlurryAgent (4 applications). | The plaintext location | phone number and the SIM card serial number. The anal- |  |
| exposure to AdMob occurred in the HTTP GET string: | ysis was simplified by the taint tag provided by Taint- |  |  |

Droid that precisely describes which privacy relevant

...&s=a14a4a93f1e4c68&..&t=062A1CB1D476DE85

B717D9195A6722A9&d%5Bcoord%5D=47.6612278900 data is included in the payload, especially for binary pay-

00006%2C-122.31589477&... loads. We also note that there was almost no perceived

latency while running experiments with TaintDroid.

Investigating the AdMob SDK revealed the s= parameter

| is an identifier unique to an application publisher, and the | 7 | Performance Evaluation |
| --- | --- | --- |
| coord= | parameter provides the geographic coordinates. | We now study TaintDroid’s taint tracking overhead. |
| For FlurryAgent, we confirmed location exposure by | Experiments were performed on a Google Nexus One |  |
| the following sequence of events. | First, a component | running Android OS version 2.1 modified for TaintDroid. |
| named “FlurryAgent” registers with the location man- | Within the interpreted environment, TaintDroid incurs |  |
| ager to receive location updates. | Then, TaintDroid log | the same performance and memory overhead regardless |
| messages show the application receiving a tainted par- | of the existence of taint markings. Hence, we only need |  |
| cel from the location manager. | Finally, the application | to ensure file access includes appropriate taint tags. |

reports “sending report to http://data.flurry.

| com/aar.do | ” after receiving the tainted parcel. | 7.1 | Macrobenchmarks |
| --- | --- | --- | --- |
| Our experimentation indicates these fifteen applica- | During the application study, we anecdotally observed |  |  |
| tions collect location data and send it to advertisement | limited performance overhead. We hypothesize that this |  |  |
| servers. | In some cases, location data was transmitted | is because: 1) most applications are primarily in a “wait |  |
| to advertisement servers even when no advertisement | state,” and 2) heavyweight operations (e.g., screen up- |  |  |
| was displayed in the application. However, we note that | dates and webpage rendering) occur in unmonitored na- |  |  |
| TaintDroid helped us verify that three of the studied ap- | tive libraries. |  |  |
| plications (not included in the Table 3) only transmitted | To gain further insight into perceived overhead, we |  |  |
| location data per user’s request to pull localized content | devised five macrobenchmarks for common high-level |  |  |
| from their servers. This finding demonstrates the impor- | smartphone operations. Each experiment was measured |  |  |
| tance of monitoring exercised functionality of an appli- | 50 times and observed 95% confidence intervals at least |  |  |
| cation that reflects how the application | actually | uses or | an order of magnitude less than the mean. In each case, |
| abuses the granted permissions. | we excluded the first run to remove unrelated initializa- |  |  |
| Legitimate Flags: | Out of 105 connections flagged by | tion costs. Experimental results are shown in Table 4. |  |

---

## Page 11

Android TaintDroid

| App Load Time | 63 | ms | 65 | ms |
| --- | --- | --- | --- | --- |
| Address Book (create) | 348 | ms | 367 | ms |
| Address Book (read) | 101 | ms | 119 | ms |
| Phone Call | 96 | ms | 106 | ms |
| Take Picture | 1718 | ms | 2216 | ms |

Application Load Time: The application load time

measures from when Android’s Activity Manager re-

ceives a command to start an activity component to the

time the activity thread is displayed. This time includes

application resolution by the Activity Manager, IPC, and

graphical display. TaintDroid adds only 3% overhead, as

read, and delete entries for the phone’s address book, ex-

be propagated. For example, the current taint tag could

be associated with the file descriptor.

7.2 Java Microbenchmark

2000

Android

1600

1400

1200

1000

800

CaffeineMark 3.0 Score 600

400

200

sieve loop logic string float method Overall

CaffeineMark 3.0 Benchmark

overhead is expected.

7.3 IPC Microbenchmark

The IPC benchmark considers overhead due to the par-

| Table 4: Macrobenchmark Results | 1800 | TaintDroid |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| the operation is dominated by native graphics libraries. | Figure 5: Microbenchmark of Java overhead. Error bars |  |  |  |  |  |
| Address Book: | We built a custom application to create, | indicate 95% confidence intervals. |  |  |  |  |
| ercising both file read and write. Create used three SQL | scoring metric only useful for relative comparisons. |  |  |  |  |  |
| transactions while read used two SQL transactions. The | The | results | are | consistent | with | implementation- |
| subsequent delete operation was lazy, returning in 0 ms, | specific expectations. | The overhead incurred by Taint- |  |  |  |  |
| and hence was excluded from our results. | TaintDroid | Droid is smallest for the benchmarks dominated by arith- |  |  |  |  |
| adds approximately 5.5% and 18% overhead for address | metic and logic operations. | The taint propagation for |  |  |  |  |
| book entry creates and reads, respectively. | The addi- | these operations is simple, consisting of an additional |  |  |  |  |
| tional overhead for reads can be attributed to file taint | copy of spatially local memory. The string benchmark, |  |  |  |  |  |
| propagation. The data is not tainted before create, hence | on the other hand, experiences the greatest overhead. |  |  |  |  |  |
| no file propagation is needed. Note that the user experi- | This is most likely due to the additional memory com- |  |  |  |  |  |
| ences less than 20 ms overhead when creating or viewing | parisons that occur when the JNI propagation heuristic |  |  |  |  |  |
| a contact. | checks for string objects in method prototypes. |  |  |  |  |  |
| Phone Call: | The phone call benchmark measured the | The “overall” results indicate cumulative score across |  |  |  |  |
| time from pressing “dial” to the point at which the audio | individual benchmarks. | CaffeineMark documentation |  |  |  |  |
| hardware was reconfigured to “in call” mode. TaintDroid | states that scores roughly correspond to the number of |  |  |  |  |  |
| only adds 10 ms per phone call setup ( | ∼ | 10% overhead), | Java instructions executed per second. Here, the unmod- |  |  |  |
| which is significantly less than call setup in the network, | ified Android system had an average score of 1121, and |  |  |  |  |  |
| which takes on the order of seconds. | TaintDroid measured 967. TaintDroid has a 14% over- |  |  |  |  |  |
| Take Picture: | The picture benchmark measures from | head with respect to the unmodified system. |  |  |  |  |
| the time the user presses the “take picture” button un- | We also measured memory consumption during the |  |  |  |  |  |
| til the preview display is re-enabled. This measurement | CaffeineMark benchmark. | The benchmark consumed |  |  |  |  |
| includes the time to capture a picture from the camera | 21.28 MB on the unmodified system and 22.21 MB while |  |  |  |  |  |
| and save the file to the SDcard. TaintDroid adds 498 ms | running on TaintDroid, indicating a 4.4% memory over- |  |  |  |  |  |
| to the 1718 ms needed by Android to take a picture (an | head. Note that much of an Android process’s memory |  |  |  |  |  |
| overhead of 29%). A portion of this overhead can be at- | is used by the zygote runtime environment. | These na- |  |  |  |  |
| tributed to to additional file operations required for taint | tive library memory pages are shared between applica- |  |  |  |  |  |
| propagation (one | getxattr | / | setxattr | pair per written data | tions to reduce the overall system memory footprint and |  |
| buffer). Note that some of this overhead can be reduced | require taint tracking. | Given that TaintDroid stores 32 |  |  |  |  |
| by eliminating redundant taint propagation. That is, only | taint markings (4 bytes) for each 32-bit variable in the |  |  |  |  |  |
| the taint tag for the first data buffer written to file needs to | interpreted environment (regardless of taint state), this |  |  |  |  |  |
| Figure 5 shows the execution time results of a Java mi- | cel modifications. | For this experiment, we developed |  |  |  |  |
| crobenchmark. We used an Android port of the standard | client and service applications that perform binder trans- |  |  |  |  |  |
| CaffeineMark 3.0 [43]. | CaffeineMark uses an internal | actions as fast as possible. The service manipulates ac- |  |  |  |  |

---

## Page 12

Table 5: IPC Throughput Test (10,000 msgs).

| Time (s) | 8.58 | 10.89 |
| --- | --- | --- |
| Memory (client) | 21.06MB | 21.88MB |

count objects (a username string and a balance integer)

and provides two interfaces: setAccount() and getAc-

count() . The experiment measures the time for the client

to invoke each interface pair 10,000 times.

Table 5 summarizes the results of the IPC benchmark.

TaintDroid was 27% slower than Android. TaintDroid

only adds four bytes to each IPC object, therefore over-

head due to data size is unlikely. The more likely cause of

the overhead is the continual copying of taint tags as val-

ues are marshalled into and out of the parcel byte buffer.

Finally, TaintDroid used 3.5% more memory than An-

droid, which is comparable to the consumption observed

during the CaffeineMark benchmarks.

8 Discussion

or write “direct” variant is used, which anecdotally oc-

curred with minimal frequency. Similar implementation

also operates on native addresses.

fective for tracking sensitive information, it causes sig-

nificant false positives when the tracked information con-

tains configuration identifiers. For example, the IMSI nu-

meric string consists of a Mobile Country Code (MCC),

Mobile Network Code (MNC), and Mobile Station Iden-

tifier Number (MSIN), which are all tainted together. 5

Android uses the MCC and MNC extensively as con-

figuration parameters when communicating other data.

This causes all information in a parcel to become tainted,

eventually resulting in an explosion of tainted informa-

tion. Thus, for taint sources that contain configuration

parameters, tainting individual variables within parcels

is more appropriate. However, as our analysis results in

Section 6 show, message-level taint tracking is effective

for the majority of our taint sources.

9 Related Work

| Android | TaintDroid | limitations exist with the | sun.misc.Unsafe | class, which |
| --- | --- | --- | --- | --- |
| Memory (service) | 18.92MB | 19.48MB | Taint Source Limitations: | While TaintDroid is very ef- |
| Approach Limitations: | TaintDroid only tracks data | Mobile phone host security is a growing concern. |  |  |
| flows (i.e., explicit flows) and does not track control | OS-level protections such as Kirin [18], | Saint [42], |  |  |
| flows (i.e., implicit flows) to minimize performance over- | and Security-by-Contract [15] provide enhanced security |  |  |  |
| head. Section 6 shows that TaintDroid can track applica- | mechanisms for Android and Windows Mobile. | These |  |  |
| tions’ expected data exposure and also reveal suspicious | approaches prevent access to sensitive information; how- |  |  |  |
| actions. | However, applications that are truly malicious | ever, once information enters the application, no addi- |  |  |
| can game our system and exfiltrate privacy sensitive in- | tional mediation occurs. In systems with larger displays, |  |  |  |
| formation through control flows. Fully tracking control | a graphical widget [27] can help users visualize sensor |  |  |  |
| flow requires static analysis [14, 37], which is not appli- | access policies. Mulliner et al. [36] provide information |  |  |  |
| cable to analyzing third-party applications whose source | tracking by labeling smartphone processes based on the |  |  |  |
| code is unavailable. Direct control flows can be tracked | interfaces they access, effectively limiting access to fu- |  |  |  |
| dynamically if a taint scope can be determined [53]; | ture interfaces based on acquired labels. |  |  |  |
| however, DEX does not maintain branch structures that | Decentralized information flow control (DIFC) en- |  |  |  |
| TaintDroid can leverage. | On-demand static analysis to | hanced operating systems such as Asbestos [52] and HiS- |  |  |
| determine method control flow graphs (CFGs) provides | tar [60] label processes and enforce access control based |  |  |  |
| this context [39]; however, TaintDroid does not currently | on Denning’s lattice model for information flow secu- |  |  |  |
| perform such analysis in order to avoid false positives | rity [13]. Flume [30] provides similar enhancements for |  |  |  |
| and significant performance overhead. | Our data flow | legacy OS abstractions. DEFCon [34] uses a logic simi- |  |  |
| taint propagation logic is consistent with existing, well | lar to these DIFC OSes, but focuses on events and modi- |  |  |  |
| known, taint tracking systems [7, 57]. Finally, once in- | fies a Java runtime with lightweight isolation. Related to |  |  |  |
| formation leaves the phone, it may return in a network | these system-level approaches, PRECIP [54] labels both |  |  |  |
| reply. TaintDroid cannot track such information. | processes and shared kernel objects such as the clipboard |  |  |  |
| Implementation Limitations: | Android uses the Apache | and display buffer. However, these process-level infor- |  |  |
| Harmony [3] implementation of Java with a few custom | mation flow models are coarse grained and cannot track |  |  |  |
| modifications. This implementation includes support for | sensitive information | within | untrusted applications. |  |
| the | PlatformAddress | class, which contains a native ad- | Tools that analyze applications for privacy sensi- |  |
| dress and is used by | DirectBuffer | objects. The file and | tive information leaks include Privacy Oracle [28] and |  |
| network IO APIs include write and read “direct” vari- | TightLip [59]. These tools investigate applications while |  |  |  |
| ants that consume the native address from a | DirectBuffer | . | treating them as a black box, thus enabling analysis of |  |
| TaintDroid does not currently track taint tags on | Direct- | off-the-shelf applications. However, this black-box anal- |  |  |
| Buffer | objects, because the data is stored in opaque native | ysis tool becomes ineffective when applications use en- |  |  |
| data structures. Currently, TaintDroid logs when a read | cryption prior to releasing sensitive information. |  |  |  |

---

## Page 13

| Language-based information flow security [46] ex- | for files and SQL databases to serialize and de-serialize |  |
| --- | --- | --- |
| tends existing programming languages by labeling vari- | objects and policy with byte-level granularity. | Taint- |
| ables with security attributes. | Compilers use the secu- | Droid’s interpreted code taint propagation bears similar- |
| rity labels to generate security proofs, e.g., Jif [37, 38] | ity to some of these works. | However, TaintDroid im- |
| and SLam [24]. Laminar [45] provides DIFC guarantees | plements system-wide information flow tracking, seam- |  |
| based on programmer defined security regions. However, | lessly connecting interpreter taint tracking with a range |  |
| these languages require careful development and are of- | of operating system sharing mechanisms. |  |

ten incompatible with legacy software designs [25].

Dynamic taint analysis provides information track-

ing for legacy programs. The approach has been used

to enhance system integrity (e.g., defend against soft-

ware attacks [41, 44, 8]) and confidentiality (e.g., dis-

cover privacy exposure [57, 16, 61]), as well as track

Internet worms [9]. Dynamic tracking approaches

range from whole-system analysis using hardware exten-

sions [51, 11, 50] and emulation environments [7, 57]

to per-process tracking using dynamic binary transla-

tion (DBT) [6, 44, 8, 61]. The performance and mem-

ory overhead associated with dynamic tracking has re-

sulted in an array of optimizations, including optimizing

context switches [44], on-demand tracking [26] based

on hypervisor introspection, and function summaries for

code with known information flow properties [61]. If

source code is available, significant performance im-

provements can be achieved by automatically instru-

menting legacy programs with dynamic tracking func-

tionality [56, 31]. Automatic instrumentation has also

been performed on x86 binaries [47], providing a com-

promise between source code translation and DBT. Our

TaintDroid design was inspired by these prior works, but

addressed different challenges unique to mobile phones.

To our knowledge, TaintDroid is the first taint tracking

system for a mobile phone and is the first dynamic taint

analysis system to achieve practical system-wide analy-

sis through the integration of tracking multiple data ob-

ject granularities.

to prevent cross-site scripting attacks. Xu et al. [56] au-

tomatically instrument the PHP interpreter source code

with dynamic information tracking to prevent SQL in-

the interpreted environment, Resin implements filters

10 Conclusions

While some mobile phone operating systems allow

users to control applications’ access to sensitive informa-

tion, such as location sensors, camera images, and con-

tact lists, users lack visibility into how applications use

their private data. To address this, we present TaintDroid,

an efficient, system-wide information flow tracking tool

that can simultaneously track multiple sources of sensi-

tive data. A key design goal of TaintDroid is efficiency,

and TaintDroid achieves this by integrating four gran-

ularities of taint propagation (variable-level, message-

level, method-level, and file-level) to achieve a 14% per-

formance overhead on a CPU-bound microbenchmark.

We also used our TaintDroid implementation to study

the behavior of 30 popular third-party applications, cho-

sen at random from the Android Marketplace. Our study

revealed that two-thirds of the applications in our study

exhibit suspicious handling of sensitive data, and that 15

of the 30 applications reported users’ locations to remote

advertising servers. Our findings demonstrate the effec-

tiveness and value of enhancing smartphone platforms

with monitoring tools such as TaintDroid.

Acknowledgments

We would like to thank Intel Labs, Berkeley and

Seattle for its support and feedback during the design

and prototype implementation of this work. We thank

Jayanth Kannon, Stuart Schechter, and Ben Greenstein

for their feedback during the writing of this paper. We

dation.

References

harmony.apache.org .

| Finally, dynamic taint analysis has been applied to vir- | also thank Kevin Butler, Stephen McLaughlin, Machigar |  |  |  |
| --- | --- | --- | --- | --- |
| tual machines and interpreters. | Haldar et al. [22] in- | Ongtang, and the SIIS lab as a whole for their helpful |  |  |
| strument the Java String class with taint tracking to pre- | comments. This material is based upon work supported |  |  |  |
| vent SQL injection attacks. WASP [23] has similar mo- | by the National Science Foundation. William Enck and |  |  |  |
| tivations; however, it uses positive tainting of individ- | Patrick McDaniel were partially supported by NSF Grant |  |  |  |
| ual characters to ensure the SQL query contains only | No. | CNS-0905447, CNS-0721579 and CNS-0643907. |  |  |
| high-integrity substrings. | Chandra and Franz [5] pro- | Landon Cox and Peter Gilbert were partially supported |  |  |
| pose fine-grained information flow tracking within the | by NSF CAREER Award CNS-0747283. Any opinions, |  |  |  |
| JVM and instrument Java byte-code to aid control flow | findings, and conclusions or recommendations expressed |  |  |  |
| analysis. Similarly, Nair et al. [39] instrument the Kaffe | in this material are those of the author(s) and do not nec- |  |  |  |
| JVM. Vogt et al. [53] instrument a Javascript interpreter | essarily reflect the views of the National Science Foun- |  |  |  |
| jection attacks. Finally, the Resin [58] environment for | [1] | Android. | http://www.android.com | . |
| PHP and Python uses data flow tracking to prevent an as- | [2] | Android Market. | http://market.android.com | . |
| sortment of Web application attacks. When data leaves | [3] | Apache Harmony – Open Source Java Platform. | http:// |  |

---

## Page 14

| [4] | APPLE, | INC. | Apples | App | Store | Downloads | Top | Three | [21] | Google Maps for Mobile. | http://www.google.com/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Billion. | http://www.apple.com/pr/library/2010/ | mobile/products/maps.html | . |  |  |  |  |  |  |  |  |
| 01/05appstore.html | , January 2010. | [22] | HALDAR, | V., | CHANDRA, | D., | AND FRANZ, | M. | Dynamic |  |  |
| [5] | CHANDRA, D., | AND FRANZ, M. | Fine-Grained Information | Taint Propagation for Java. | In | Proceedings of the 21st Annual |  |  |  |  |  |
| Flow Analysis and Enforcement in a Java Virtual Machine. | In | Computer Security Applications Conference (ACSAC) | (Decem- |  |  |  |  |  |  |  |  |
| Proceedings of the 23rd Annual Computer Security Applications | ber 2005), pp. 303–311. |  |  |  |  |  |  |  |  |  |  |
| Conference (ACSAC) | (December 2007). | [23] | HALFOND, W. G., ORSO, A., | AND MANOLIOS, P. | WASP: |  |  |  |  |  |  |
| [6] | CHENG, W., ZHAO, Q., YU, B., AND HIROSHIGE, S. | Taint- | Protecting Web Applications Using Positive Tainting and Syntax- |  |  |  |  |  |  |  |  |
| Trace: Efficient Flow Tracing with Dyanmic Binary Rewriting. | Aware Evaluation. | IEEE Transactions on Software Engineering |  |  |  |  |  |  |  |  |  |
| In | Proceedings of the IEEE Symposium on Computers and Com- | 34 | , 1 (2008), 65–81. |  |  |  |  |  |  |  |  |
| munications (ISCC) | (June 2006), pp. 749–754. | [24] | HEINTZE, N., AND RIECKE, J. G. | The SLam Calculus: Pro- |  |  |  |  |  |  |  |
| [7] | CHOW, J., PFAFF, B., GARFINKEL, T., CHRISTOPHER, K., | gramming with Secrecy and Integrity. | In | Proceedings of the |  |  |  |  |  |  |  |
| AND ROSENBLUM, M. Understanding Data Lifetime via Whole | Symposium on Principles of Programming Languages (POPL) |  |  |  |  |  |  |  |  |  |  |
| System Simulation. In | Proceedings of the 13th USENIX Security | (1998), pp. 365–377. |  |  |  |  |  |  |  |  |  |
| Symposium | (August 2004). | [25] | HICKS, B., AHMADIZADEH, K., AND MCDANIEL, P. Under- |  |  |  |  |  |  |  |  |
| [8] | CLAUSE, J., LI, W., AND ORSO, A. | Dytan: A Generic Dy- | standing practical application development in security-typed lan- |  |  |  |  |  |  |  |  |
| namic Taint Analysis Framework. In | Proceedings of the 2007 in- | guages. In | 22st Annual Computer Security Applications Confer- |  |  |  |  |  |  |  |  |
| ternational symposium on Software testing and analysis | (2007), | ence (ACSAC) | (2006), pp. 153–164. |  |  |  |  |  |  |  |  |
| pp. 196–206. | [26] | HO, A., FETTERMAN, M., CLARK, C., WARFIELD, A., AND |  |  |  |  |  |  |  |  |  |
| [9] | COSTA, M., CROWCROFT, J., CASTRO, M., ROWSTRON, A., | HAND, S. Practical Taint-Based Protection using Demand Emu- |  |  |  |  |  |  |  |  |  |
| ZHOU, L., ZHANG, L., AND BARHAM, P. | Vigilante: End-to- | lation. In | Proceedings of the European Conference on Computer |  |  |  |  |  |  |  |  |
| End Containment of Internet Worms. In | Proceedings of the ACM | Systems (EuroSys) | (2006), pp. 29–41. |  |  |  |  |  |  |  |  |
| Symposium on Operating Systems Principles | (2005). | [27] | HOWELL, J., AND SCHECHTER, S. What You See is What they |  |  |  |  |  |  |  |  |
| [10] | COX, L. P., AND GILBERT, P. RedFlag: Reducing Inadvertent | Get: Protecting users from unwanted use of microphones, cam- |  |  |  |  |  |  |  |  |  |
| Leaks by Personal Machines. Tech. Rep. TR-2009-02, Duke Uni- | era, and other sensors. In | Proceedings of Web 2.0 Security and |  |  |  |  |  |  |  |  |  |
| versity, 2009. | Privacy Workshop | (2010). |  |  |  |  |  |  |  |  |  |

[11] CRANDALL, J. R., AND CHONG, F. T. Minos: Control Data

Attack Prevention Orthogonal to Memory Model. In Proceedings

of the International Symposium on Microarchitecture (December

2004), pp. 221–232.

[12] DAVIES, C. iPhone spyware debated as app li-

brary “phones home”. http://www.slashgear.

com/iphone-spyware-debated-as-app-

library-phones-home-1752491/ , August 17, 2009.

[13] DENNING, D. E. A Lattice Model of Secure Information Flow.

Communications of the ACM 19 , 5 (May 1976), 236–243.

P., PIESSENS, F., SIAHAAN, I., AND VANOVERBERGHE, D.

[17] ENCK, W., GILBERT, P., CHUN, B.-G., COX, L. P., JUNG,

Science and Engineering, Pennsylvania State University, Univer-

sity Park, PA, USA, August 2010.

Lightweight Mobile Phone Application Certification. In Proceed-

ings of the 16th ACM Conference on Computer and Communica-

tions Security (CCS) (November 2009).

[28] JUNG, J., SHETH, A., GREENSTEIN, B., WETHERALL, D.,

MAGANIS, G., AND KOHNO, T. Privacy Oracle: A System for

Finding Application Leaks with Black Box Differential Testing.

In Proceedings of ACM CCS (2008).

[29] KING, D., HICKS, B., HICKS, M., AND JAEGER, T. Implicit

Flows: Can’t Live with ’Em, Can’t Live without ’Em. In Pro-

ceedings of the International Conference on Information Systems

Security (2008).

[30] KROHN, M., YIP, A., BRODSKY, M., CLIFFER, N.,

KAASHOEK, M. F., KOHLER, E., AND MORRIS, R. Informa-

tion Flow Control for Standard OS Abstractions. In Proceedings

ference (ACSAC) (2006).

2010.

[35] MOREN, D. Retrievable iPhone numbers mean potential

privacy issues. http://www.macworld.com/article/

2009.

[36] MULLINER, C., VIGNA, G., DAGON, D., AND LEE, W. Us-

ing Labeling to Prevent Cross-Service Attacks Against Smart

| [14] | DENNING, D. E., AND DENNING, P. J. | Certification of Pro- | of ACM Symposium on Operating Systems Principles | (2007). |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grams for Secure Information Flow. | Communications of the ACM | [31] | LAM, L. C., AND CKER CHIUEH, T. A General Dynamic Infor- |  |  |  |  |  |  |  |  |  |
| 20 | , 7 (July 1977). | mation Flow Tracking Framework for Security Applications. In |  |  |  |  |  |  |  |  |  |  |
| [15] | DESMET, L., JOOSEN, W., MASSACCI, F., PHILIPPAERTS, | Proceedings of the Annual Computer Security Applications Con- |  |  |  |  |  |  |  |  |  |  |
| Security-by-contract on the .NET platform. | Information Security | [32] | LIANG, S. | Java Native Interface: | Programmer’s Guide and |  |  |  |  |  |  |  |
| Technical Report 13 | , 1 (January 2008), 25–32. | Specification | . Prentice Hall PTR, 1999. |  |  |  |  |  |  |  |  |  |
| [16] | EGELE, M., KRUEGEL, C., KIRDA, E., YIN, H., AND SONG, | [33] | LOOKOUT. | Introducing | the | App | Genome | Project. |  |  |  |  |
| D. Dyanmic Spyware Analysis. In | Proceedings of the USENIX | http://blog.mylookout.com/2010/07/ |  |  |  |  |  |  |  |  |  |  |
| Annual Technical Conference | (June 2007), pp. 233–246. | introducing-the-app-genome-project/ | , | July |  |  |  |  |  |  |  |  |
| J., | MCDANIEL, | P., | AND SHETH, | A. N. | TaintDroid: | An | [34] | MIGLIAVACCA, M., PAPAGIANNIS, I., EYERS, D. M., SHAND, |  |  |  |  |
| Information-Flow Tracking System for Realtime Privacy Mon- | B., BACON, J., AND PIETZUCH, P. DEFCon: High-Performance |  |  |  |  |  |  |  |  |  |  |  |
| itoring on Smartphones. | Tech. Rep. NAS-TR-0120-2010, Net- | Event Processing with Information Security. In | PROCEEDINGS |  |  |  |  |  |  |  |  |  |
| work and Security Research Center, Department of Computer | of the USENIX Annual Technical Conference | (2010). |  |  |  |  |  |  |  |  |  |  |
| [18] | ENCK, | W., | ONGTANG, | M., | AND | MCDANIEL, | P. | On | 143047/2009/09/phone_hole.html | , | September | 29, |
| [19] | FITZPATRICK, M. | Mobile that allows bosses to snoop on staff | Phones. In | Proceedings of Detection of Intrusions and Malware |  |  |  |  |  |  |  |  |
| developed. | BBC News, March 2010. | http://news.bbc. | & Vulnerability Assessment (DIMVA) | (2006). |  |  |  |  |  |  |  |  |
| co.uk/2/hi/technology/8559683.stm | . | [37] | MYERS, A. C. JFlow: Practical Mostly-Static Information Flow |  |  |  |  |  |  |  |  |  |
| [20] | Flurry Mobile Application Analytics. | http://www.flurry. | Control. In | Proceedings of the ACM Symposium on Principles of |  |  |  |  |  |  |  |  |
| com/product/technical-info.html | . | Programming Langauges (POPL) | (January 1999). |  |  |  |  |  |  |  |  |  |

---

## Page 15

| [38] | MYERS, A. C., AND LISKOV, B. Protecting Privacy Using the | [53] | VOGT, | P., | NENTWICH, | F., | JOVANOVIC, | N., | KIRDA, | E., |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Decentralized Label Model. | ACM Transactions on Software En- | KRUEGEL, C., AND VIGNA, G. | Cross-Site Scripting Preven- |  |  |  |  |  |  |  |
| gineering and Methodology 9 | , 4 (October 2000), 410–442. | tion with Dynamic Data Tainting and Static Analysis. In | Proc. of |  |  |  |  |  |  |  |

[39] NAIR, S. K., SIMPSON, P. N., CRISPO, B., AND TANENBAUM,

(REM) (2007).

channel capacity to distinguish undue influence. In ACM SIG-

Automatic Detection, Analysis, and Signature Generation of Ex-

[42] ONGTANG, M., MCLAUGHLIN, S., ENCK, W., AND MC-

DANIEL, P. Semantically Rich Application-Centric Security in

[43] PENDRAGON SOFTWARE CORPORATION. CaffeineMark 3.0.

http://www.benchmarkhq.ru/cm30/ .

Tracking System for Detecting Security Attacks. In Proceedings

of the 39th Annual IEEE/ACM International Symposium on Mi-

ized Information Flow Control. In Proceedings of Programming

Communication 21 , 1 (January 2003), 5–19.

[47] SAXENA, P., SEKAR, R., AND PURANIK, V. Efficient Fine-

You Ever Wanted to Know about Dynamic Taint Analysis and

Forward Symbolic Execution (but might have been afraid to ask).

[50] SUH, G. E., LEE, J. W., ZHANG, D., AND DEVADAS, S. Se-

cure Program Execution via Dynamic Information Flow Track-

ing. In Proceedings of Architectural Support for Programming

Languages and Operating Systems (2004).

[51] VACHHARAJANI, N., BRIDGES, M. J., CHANG, J., RANGAN,

R., OTTONI, G., BLOME, J. A., REIS, G. A., VACHHARA-

JANI, M., AND AUGUST, D. I. RIFLE: An Architectural Frame-

work for User-Centric Information-Flow Security. In Proceed-

ings of the 37th annual IEEE/ACM International Symposium on

Microarchitecture (2004), pp. 243–254.

[52] VANDEBOGART, S., EFSTATHOPOULOS, P., KOHLER, E.,

KROHN, M., FREY, C., ZIEGLER, D., KAASHOEK, F., MOR-

RIS, R., AND MAZI ` ERES, D. Labels and Event Processes in

the Asbestos Operating System. ACM Transactions on Computer

Systems (TOCS) 25 , 4 (December 2007).

Network & Distributed System Security (2007).

Symposium (NDSS) (2008).

2010.

(August 2006), pp. 121–136.

ware Detection and Analysis. In Proceedings of ACM Computer

and Communications Security (2007).

Proceedings of the ACM Symposium on Operating Systems Prin-

ciples (Oct. 2009).

[59] YUMEREFENDI, A. R., MICKLE, B., AND COX, L. P. TightLip:

Implementation (NSDI) (2007).

MAZI ` ERES, D. Making Information Flow Explicit in HiStar. In

D. Privacy Scope: A Precise Information Flow Tracking Sys-

Notes

and 2.1 (primarily for debugging and profiling)

either have a Java interface or C/C++ implementation. These unusable

methods were excluded from our survey.

fiers that warrant taint sources.

| A. S. A Virtual Machine Based Information Flow Control Sys- | [54] | WANG, X., LI, Z., LI, N., AND CHOI, J. Y. PRECIP: Towards |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tem for Policy Enforcement. In | the 1st International Workshop | Practical and Retrofittable Confidential Information Protection. |  |  |  |  |  |  |
| on Run Time Enforcement for Mobile and Distributed Systems | In | Proceedings of 15th Network and Distributed System Security |  |  |  |  |  |  |
| [40] | NEWSOME, J., MCCAMANT, S., AND SONG, D. | Measuring | [55] | WhatApp. | http://www.whatapp.org | . | Accessed April |  |
| PLAN Workshop on Programming Languages and Analysis for | [56] | XU, W., BHATKAR, S., AND SEKAR, R. Taint-Enhanced Pol- |  |  |  |  |  |  |
| Security | (2009). | icy Enforcement: A Practical Approach to Defeat a Wide Range |  |  |  |  |  |  |
| [41] | NEWSOME, J., | AND SONG, D. | Dynamic Taint Analysis for | of Attacks. In | Proceedings of the USENIX Security Symposium |  |  |  |
| ploits on Commodity Software. | In | Proc. of Network and Dis- | [57] | YIN, H., SONG, D., EGELE, M., KRUEGEL, C., AND KIRDA, |  |  |  |  |
| tributed System Security Symposium | (2005). | E. Panorama: Capturing System-wide Information Flow for Mal- |  |  |  |  |  |  |
| Android. In | Proceedings of the 25th Annual Computer Security | [58] | YIP, A., WANG, X., ZELDOVICH, N., AND KAASHOEK, M. F. |  |  |  |  |  |
| Applications Conference (ACSAC) | (2009). | Improving Application Security with Data Flow Assertions. | In |  |  |  |  |  |
| [44] | QIN, F., WANG, C., LI, Z., SEOP KIM, H., ZHOU, Y., AND | Keeping Applications from Spilling the Beans. | In | Proceedings |  |  |  |  |
| WU, Y. | LIFT: A Low-Overhead Practical Information Flow | of the 4th USENIX Symposium on Network Systems Design & |  |  |  |  |  |  |
| croarchitecture | (2006), pp. 135–148. | [60] | ZELDOVICH, N., BOYD-WICKIZER, S., KOHLER, E., | AND |  |  |  |  |
| [45] | ROY, I., PORTER, D. E., BOND, M. D., MCKINLEY, K. S., | Proceedings of the 7th symposium on Operating Systems Design |  |  |  |  |  |  |
| AND WITCHEL, E. Laminar: Practical Fine-Grained Decentral- | and Implementation (OSDI) | (2006). |  |  |  |  |  |  |
| Language Design and Implementation | (2009). | [61] | ZHU, D., JUNG, J., SONG, D., KOHNO, T., AND WETHERALL, |  |  |  |  |  |
| [46] | SABELFELD, | A., | AND | MYERS, | A. | C. | Language-based | tem For Finding Application Leaks. Tech. Rep. EECS-2009-145, |
| information-flow security. | IEEE Journal on Selected Areas in | Department of Computer Science, UC Berkeley, 2009. |  |  |  |  |  |  |
| Grained | Binary | Instrumentation | with | Applications | to | Taint- | 1 | A similar approach can be applied to just-in-time compilation by |
| Tracking. In | Proceedings of the IEEE/ACM symposium on Code | inserting tracking code within the generated binary. |  |  |  |  |  |  |
| Generation and Optimization (CGO) | (2008). | 2 | Only 11 internal VM methods were added between versions 1.5 |  |  |  |  |  |
| [48] | SCHWARTZ, E. J., AVGERINOS, T., AND BRUMLEY, D. | All | 3 | There was a relatively small number of JNI methods that did not |  |  |  |  |
| In | IEEE Symposium on Security and Privacy | (2010). | 4 | Because of the limitation of the IMSI taint source as discussed in |  |  |  |  |
| [49] | SLOWINSKA, A., AND BOS, H. Pointless Tainting? Evaluating | Section 8, we disabled the IMSI taint source for experiments. Nonethe- |  |  |  |  |  |  |
| the Practicality of Pointer Tainting. In | Proceedings of the Euro- | less, TaintDroid’s flag of the ICC-ID and the phone number led us to |  |  |  |  |  |  |
| pean Conference on Computer Systems (EuroSys) | (April 2009), | find the IMSI contained in the same payload. |  |  |  |  |  |  |
| pp. 61–74. | 5 | Regardless of the string separation, the MCC and MNC are identi- |  |  |  |  |  |  |

---
title: "FANS: Fuzzing Android Native System Services via Automated Interface Analysis"
pages: 18
---

# sec20-liu

> **總頁數**：18 頁

---

## Page 1

FANS: Fuzzing Android Native System Services

via Automated Interface Analysis

Baozheng Liu and Chao Zhang, Institute of Network Science and Cyberspace,

Tsinghua University; Beijing National Research Center for Information Science

and Technology; Guang Gong, Alpha Lab, 360 Internet Security Center; Yishun

Zeng, Institute of Network Science and Cyberspace, Tsinghua University; Beijing

National Research Center for Information Science and Technology; Haifeng Ruan,

Department of Computer Science and Technology, Tsinghua University; Jianwei

Zhuge, Institute of Network Science and Cyberspace, Tsinghua University; Beijing

National Research Center for Information Science and Technology

https://www.usenix.org/conference/usenixsecurity20/presentation/liu

This paper is included in the Proceedings of the

29th USENIX Security Symposium.

August 12–14, 2020

978-1-939133-17-5

Open access to the Proceedings of the

29th USENIX Security Symposium

is sponsored by USENIX.

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

FANS: Fuzzing Android Native System Services

via Automated Interface Analysis

| 1 | , | 2 | ∗ | 1 | , | 2 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baozheng Liu | , Chao Zhang | , Guang Gong | , |  |  |  |  |
| 1 | , | 2 | 4 | 1 | , | 2 |  |

Yishun Zeng , Haifeng Ruan , Jianwei Zhuge

1 Institute of Network Science and Cyberspace, Tsinghua University chaoz@tsinghua.edu.cn

2 Beijing National Research Center for Information Science and Technology zhugejw@tsinghua.edu.cn

3 Alpha Lab, 360 Internet Security Center 4 Department of Computer Science and Technology, Tsinghua University

Abstract 1 Introduction

In this paper, we propose an automated generation-based

fuzzing solution FANS to find vulnerabilities in Android na-

tive system services. It first collects all interfaces in target

services and uncovers deep nested multi-level interfaces to

test. Then, it automatically extracts interface models, includ-

ing feasible transaction code, variable names and types in the

transaction data, from the abstract syntax tree (AST) of target

interfaces. Further, it infers variable dependencies in transac-

tions via the variable name and type knowledge, and infers

interface dependencies via the generation and use relation-

ship. Finally, it employs the interface models and dependency

knowledge to generate sequences of transactions, which have

valid formats and semantics, to test interfaces of target ser-

vices. We implemented a prototype of FANS from scratch and

evaluated it on six smartphones equipped with a recent ver-

sion of Android, i.e., android-9.0.0_r46 , and found 30 unique

vulnerabilities deduplicated from thousands of crashes, of

which 20 have been confirmed by Google. Surprisingly, we

also discovered 138 unique Java exceptions during fuzzing.

∗ Part of this work was done during Baozheng Liu’s research internship at

Android has become the most popular mobile operating sys-

thus crucial for Android security.

However, to the best of our knowledge, existing researches

paid little attention to Android native system services. Apart

from a non-scalable manual approach [7], two automated

fuzzing solutions have been proposed to discover vulnera-

bilities in Android system services. The first one is Binder-

Cracker [6], which captures input models of target services

by recording requests made by 30 popular applications. An

inherent disadvantage of this approach is that it cannot re-

cover precise input semantics, e.g., variable names and types.

Also, it will miss rarely-used or deeply-nested interfaces, due

to the incomplete testing. The other one is Chizpurfle [10],

which utilizes Java reflection to acquire parameter types of

interfaces to test vendor-implemented Java services. However,

such a method cannot be used to retrieve the input model of

Android native system services.

In Android, system services are registered to the Service

Manager . User apps query the manager to get the target

service’s interface (encapsulated in a proxy Binder object),

then invoke different transactions provided by this interface

via a unified remote procedure call (RPC) interface named

IBinder::transact(code,data,reply,flags) , where,

| Android native system services provide essential supports and | tem, taking over 85% markets according to International Data |  |  |
| --- | --- | --- | --- |
| fundamental functionalities for user apps. Finding vulnerabil- | Corporation | 1 | . The most fundamental functions of Android |
| ities in them is crucial for Android security. Fuzzing is one of | are provided by Android system services, e.g., the camera |  |  |
| the most popular vulnerability discovery solutions, yet faces | service. Until October 2019, hundreds of vulnerabilities re- |  |  |
| several challenges when applied to Android native system | lated to Android system services had been reported to Google, |  |  |
| services. First, such services are invoked via a special inter- | revealing that Android system services are still vulnerable and |  |  |
| process communication (IPC) mechanism, namely | binder | , | attractive for attackers. A large portion of these vulnerabilities |
| via service-specific interfaces. Thus, the fuzzer has to recog- | reside in native system services, i.e., those mainly written in |  |  |
| nize all interfaces and generate interface-specific test cases | C++. Vulnerabilities in Android native system services could |  |  |
| automatically. Second, effective test cases should satisfy the | allow remote attackers to compromise the Android system, |  |  |
| interface model of each interface. Third, the test cases should | e.g., performing privilege escalation, by means of launching |  |  |
| also satisfy the semantic requirements, including variable | IPC requests with crafted inputs from third-party applications. |  |  |
| dependencies and interface dependencies. | Finding vulnerabilities in Android native system services is |  |  |
| Alpha Lab of 360. | 1 | https://www.idc.com/promo/smartphone-market-share/os |  |
| USENIX Association | 29th USENIX Security Symposium | 307 |  |

---

## Page 3

| (1) | code | determines the target transaction to invoke, and (2) | ated by invoking the special method | writeStrongBinder | to |
| --- | --- | --- | --- | --- | --- |
| inputs of the transaction are marshalled into the serialized | identify multi-level interfaces. For | C2 | , we notice that, Android |  |  |
| parcel | object | data | . Thus, we could utilize this unified | system services always use a set of specific deserialization |  |
| IPC method to test all system services. | To thoroughly | methods (e.g., | readInt32 | ) to parse input data. By recogniz- |  |
| test target services, we could first find all interfaces and | ing the invocation sequence of such methods, we could infer |  |  |  |  |
| available transactions, and then invoke them with input | data | the grammar of a valid input. To preserve the knowledge of |  |  |  |
| satisfying service-specific formats and semantic requirements. | variables’ names and types, we choose to extract the deserial- |  |  |  |  |
| Specifically, there are three challenges to address: | ization sequence (i.e., the input grammar) from abstract syntax |  |  |  |  |
| C1: Multi-Level Interface Recognition. | In addition to the | tree (AST). For | C3 | , we will utilize the variable name and type |  |
| (top-level) interfaces registered in the | Service Manager | , | knowledge extracted from the AST to generate proper inputs |  |  |
| there are nested multi-level interfaces, which could be re- | and recognize intra-transaction variable dependency. Further, |  |  |  |  |
| trieved via the top-level interface and invoked by user apps. | we rely on the fact that a dependent transaction will deserial- |  |  |  |  |
| For example, the | IMeoryHeap | interface is buried at the fifth- | ize data serialized by the depended transaction, to recognize |  |  |
| level (i.e., invoked via four layers of interfaces). Therefore, | inter-transaction variable dependency. Moreover, we rely on |  |  |  |  |
| we need to recognize all top-level interfaces and nested multi- | the generation and use relationship between interfaces to infer |  |  |  |  |
| layer interfaces, in order to systematically test Android system | their dependencies. |  |  |  |  |
| services. Given that many interfaces are defined in Android | We implemented a prototype of FANS from scratch, inter- |  |  |  |  |
| Interface Definition Language (AIDL) rather than C++ and | mittently examined it on six mobile phones equipped with the |  |  |  |  |
| dynamically generated during compilation, we have to take | recent Android version android-9.0.0_r46 for about 30 days. |  |  |  |  |
| them into consideration as well. | FANS has discovered 30 unique vulnerabilities deduplicated |  |  |  |  |
| C2: Interface Model Extraction. | For each interface, we | from thousands of crashes. To our surprise, FANS also found |  |  |  |
| need to get the list of supported transactions (i.e., | code | ) to | 138 unique Java exceptions, yielded by Java applications that |  |  |
| test, and then provide input | data | to invoke each transaction. | might depend on Android native system services. Besides, |  |  |
| To improve the fuzzing effectiveness, the input | data | should | we dig into the code and observe that some Android native |  |  |
| follow grammatical requirements of target interfaces. Manu- | system services would also invoke Java methods. We have |  |  |  |  |
| ally providing the grammar knowledge is not scalable. Auto- | submitted all native bugs to Google, and received 20 con- |  |  |  |  |
| matically extracting such knowledge from the large volume | firmations. As for the Java exceptions, we are working on |  |  |  |  |
| of Android source code is also challenging. First, the gram- | examining them manually and submitting them to Google. |  |  |  |  |
| mar is specific to an individual transaction, and thus we have | To facilitate future research, we open source the prototype of |  |  |  |  |
| to recognize all available transactions and extract grammars | FANS at | https://github.com/iromise/fans | . |  |  |

for each of them. Second, the grammar requirements co-exist

with the path constraints, e.g., branch conditions, loop condi-

| tions and even nested loops, making it hard to be extracted | Contributions. | In summary, this paper makes the following |  |
| --- | --- | --- | --- |
| and represented. | contributions: |  |  |
| C3: Semantically-correct Input Generation. | Android it- | • | We systematically investigated the dependency between |
| self performs many sanity checks (e.g., size check) on the | interfaces in Android native system services, and un- |  |  |
| input | data | . Therefore, inputs that do not meet semantic re- | earthed deeper multi-level interfaces. |
| quirements can hardly explore deep states or trigger vulner- | • | We proposed a solution to automatically extract input |  |
| abilities. There are many types of semantic requirements, | interface model and semantics from AST. This method |  |  |
| including variable names and types, and even dependencies | can be applied to other interface-based programs. |  |  |
| between variables or interfaces. For instance, a variable named | • | We proposed a solution to infer inter-transaction depen- |  |
| packageName | indicates an existing package’s name is re- | dencies, by utilizing variable name and type knowledge |  |
| quired; a variable of an enumeration type can only have a | in serialization and deserialization pairs in different trans- |  |  |
| limited set of candidate values; a variable in current transac- | actions. |  |  |
| tion may depend on another variable in either the current or | • | We implemented a prototype of FANS to systematically |  |
| previous transaction, and even an interface may depend on an- | fuzz Android native system services, and have found |  |  |
| other interface. Recognizing such semantic requirements and | 30 unique native vulnerabilities and 138 unique Java |  |  |
| generating inputs accordingly are important but challenging. | exceptions. |  |  |

Our Approach. In this paper, we propose a generation-

based fuzzing solution FANS to address the aforementioned 2 Background

challenges. To address the challenge C1 , FANS first recog-

| nizes all top-level interfaces by scanning service registration | In this section, we start by introducing the Android system |  |
| --- | --- | --- |
| operations, and utilizes the fact that deep interfaces are gener- | service. Then we provide the research scope of this paper. |  |
| 308 | 29th USENIX Security Symposium | USENIX Association |

---

## Page 4

Application Service Service Manager

Request a multi-level interface, e.g.,

IMediaExtractor , or call other transactions

Return the interface,

or the transaction results

Figure 1: Application-Service Communication Model

System services are essential parts of Android, providing the

most fundamental and core functionalities.

Systematization of Android System Services. Depend-

ing on the programming language, Android system services

can be divided into two categories: (1) Java system ser-

vices , which are implemented mainly using Java, e.g., activity

From another perspective, the services are divided into

three domains since Android 8, including normal domain,

tively.

Application-Service Communication Model. Figure 1 il-

lustrates the workflow of the application-service communi-

the application could retrieve deeper multi-level interfaces

and invoke corresponding transactions. Apart from the enti-

ties illustrated in the figure, there is another important entity,

i.e., binder driver , which bridges the communication between

applications and services. However, as the binder driver is not

strictly relevant to our research, we omit it in the figure.

Interfaces in Android System Services. As mentioned

earlier, apps invoke target transactions in top-level interfaces

via a unified RPC interface IBinder::transact(code,

Register service, e.g., MediaExtractor Service

Request service, e.g., MediaExtractor Service

Return the service interface, i.e., a top-level interface

reply, flags) . This dispatcher (or the target transaction)

will then deserialize the input data and perform the action

requested by the client. In general, every service has a set of

methods that can be called through RPC. They are declared

in a base class, but implemented in the client-side proxy and

the server-side stub separately. The binder driver bridges the

proxy and stub objects to communicate.

available in the service manager , and could only be retrieved

via top-level interfaces.

code for further compilation.

2.2 Research Scope

3 Design

To find vulnerabilities in Android native system services,

we propose a generation-based fuzzing solution FANS, and

present its design in this section.

3.1 Design Choices

| 2.1 | Android System Services | is defined in a unified method | onTransact(code, data, |
| --- | --- | --- | --- |
| manager. (2) | native system services | , which are implemented | This mechanism also applies to multi-level interfaces, as |
| mainly using C++, e.g., camera service. Some Android native | multi-level interfaces share the same architecture with top- |  |  |
| system services run as daemons, e.g., | netd | . Note that a native | level interfaces. However, unlike top-level interfaces, the |
| service might sometimes call java code and vice versa. | Binder objects corresponding to multi-level interfaces are not |  |  |
| vendor domain and hardware domain. Services in normal do- | Besides, not all interfaces are statically defined in C++, and |  |  |
| main are services directly located in Android Open Source | some of them are defined in the Android Interface Definition |  |  |
| Project (AOSP), while services inside vendor domain and | Language (AIDL). When building an Android image, AIDL |  |  |
| hardware domain are related to vendors and hardware respec- | tools will be invoked to dynamically generate proper C++ |  |  |
| cation | in Android. A service will first register itself into the | In this paper, we focus on discovering vulnerabilities in the |  |
| service manager, and then listen to and handle requests from | Android | native | system services, which are registered in the |
| applications. On the other hand, an application will query the | service manager | and belong to the normal domain. To the |  |
| service manager to obtain the interface (encapsulated in a | best of our knowledge, existing researches have paid little |  |  |
| proxy Binder object) of the target service, which is denoted | attention to them. Meanwhile, as all Android system services |  |  |
| as a | top-level interface | . Then, it can utilize the top-level inter- | share the same architecture in the aspect of communication |
| face to retrieve a multi-level interface or to call transactions | and interface implementation, the scheme proposed in this |  |  |
| provided by the interface to perform certain actions. Further, | paper can be applied to other types of services as well. |  |  |
| data,reply,flags) | . Therefore, it implies that on the ser- | RPC-centric testing: | There are several alternative solutions |
| vice side there is a dispatcher responsible for handling | to testing Android native system services. A straightforward |  |  |
| the request based on the transaction | code | . This dispatcher | solution is to test target transactions by directly injecting |
| USENIX Association | 29th USENIX Security Symposium | 309 |  |

---

## Page 5

onTransact

Compile

| tx1 | tx n |
| --- | --- |
| ... | ... |

...

>

status_t XXX::onTransact(...)

Figure 2: Overview of FANS.

cannot generate arbitrary events. Instead, the adversary has to

interact with target services via the IPC interface, and could

only produce a limited number of events for the following two

reasons: (1) the binder IPC mechanism will perform some

Learn input model from code: Generation-based fuzzers

rely on input model knowledge to generate valid and effec-

including PEACH [5], Skyfire [20] and Syzkaller [19], rely

diversity of test cases.

push corpus

push fuzzer

pull logs

fetch corpus

store logs

3.2 Overview

tested.

compilation commands, so that we can collect interfaces that

which will be overlooked otherwise.

| service-specific events to the system, without calling the uni- | will probably overlook rarely-used transactions. Moreover, |  |  |  |
| --- | --- | --- | --- | --- |
| fied binder communication interface | transact | . However, | the input model learned in this way is in general inaccurate, |  |
| there are a lot of engineering challenges to address in order | since only transaction data is given. On the other hand, we |  |  |  |
| to inject events to different services located in different pro- | notice that the input model knowledge is buried in the source |  |  |  |
| cesses. More importantly, vulnerabilities found in this way | code, and choose to analyze Android source code to automat- |  |  |  |
| are likely to be false alarms, because the adversary in practice | ically retrieve the input model. |  |  |  |
| sanity checks, e.g., on packet size; and (2) the data marshalled | Figure 2 illustrates the design overview of our solution FANS. |  |  |  |
| into a parcel might depend on some dynamic system states | First, the | interface collector | (Section 3.3) collects all inter- |  |
| and are thus not arbitrary. To reduce false positives, we choose | faces in target services, including top-level interfaces and |  |  |  |
| to test target services via the RPC interface, as could be done | multi-level interfaces. Then | interface model extractor | (Sec- |  |
| by an adversary. | tion 3.4) extracts input and output formats as well as vari- |  |  |  |
| Generation-based fuzzing: | In general, there are two types | able semantics, i.e., variable names and types, for each can- |  |  |
| of fuzzers: mutation-based [4, 25], which generates new | didate transaction in each collected interface. The extractor |  |  |  |
| test cases by mutating existing test cases, and generation- | also collects definitions of structures, enumerations and type |  |  |  |
| based [5,19] | 2 | , which generate test cases according to an input | aliases that are relevant to variables. Next, the | dependency |
| specification. Mutation-based fuzzers are likely to generate | inferer | (Section 3.5) infers interface dependencies, as well as |  |  |
| test cases of invalid formats or semantics, which cannot be | intra-transaction and inter-transaction variable dependencies. |  |  |  |
| correctly deserialized or processed by target services. There- | Finally, based on the above information, the | fuzzer engine |  |  |
| fore, such fuzzers tend to have low code coverage of target | (Section 3.6) randomly generates transactions and invokes |  |  |  |
| services and may miss many potential vulnerabilities. To re- | corresponding interfaces to fuzz native system services. The |  |  |  |
| duce false negatives, we choose to test target services with | fuzzer engine also has a | manager | responsible for synchro- |  |
| generation-based fuzzing. | nizing data between the host and the mobile phone being |  |  |  |
| tive test cases. A large number of generation-based fuzzers, | 3.3 | Interface Collector |  |  |
| on grammar files produced by human to generate test cases, | As demonstrated in Section 2.1, top-level or multi-level in- |  |  |  |
| which generally require huge manual efforts and are currently | terfaces both have the | onTransact | method to dispatch trans- |  |
| unavailable for Android services. Another line of works, e.g., | actions. Thus, we could utilize this feature to recognize in- |  |  |  |
| BinderCracker [6], learn from existing transactions to gener- | terfaces. We do not directly scan C/C++ files in the AOSP |  |  |  |
| ate new inputs. This type of solutions is in general incomplete, | codebase for the | onTransact | method, though. Instead, we |  |
| since it relies on the completeness of example transactions and | examine every C/C++ file that appears as a source in AOSP |  |  |  |
| 2 | Some generation-based fuzzers also utilize mutations to increase the | are dynamically generated by AIDL tools during compilation, |  |  |
| 310 | 29th USENIX Security Symposium | USENIX Association |  |  |

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

---

## Page 6

3.4 Interface Model Extractor in AIDL, a candidate solution is to extract the interface model

To effectively generate test cases, FANS will extract inter-

face models of target services. Here, we briefly introduce

the design principles and design choices of interface model

extraction, then detail how to extract the interface model, in-

cluding transaction code, input and output variables, as well

as type definitions.

Three principles are recommended when designing the inter-

face model extractor:

Precise: Since the target interfaces will fall back on ex-

ception handling when invalid random inputs are given in

the transaction request, we need a precise interface model to

generate valid inputs that pass sanity checks. We handle the

precision of the model from the following aspects: variable

patterns , variable names and variable types . The variable

pattern implies input formats, as will be discussed later. The

other two aspects help generate semantically correct inputs.

3.4.2 Design Choices of Extractor

With the above principles in mind, we have made the follow-

ing design choices for the extractor:

is service that we are to fuzz, and directly dealing with the

server side will give us a more accurate view of what inputs

puts deserialized from data and outputs serialized into reply .

(2) An interface has multiple transactions, whose definitions

and implementations are in general closely distributed in the

server-side code. On the other hand, client-side code may

invoke them in a scattered way, causing trouble for interface

model extraction.

Extract from the AST Representation: There are many

base the analysis on. First, since some interfaces are defined

from AIDL files. However, this method will miss a wide range

interfaces directly implemented in C++ in the Android source

code. We can convert files of one format to another format to

address this issue. Here we choose to convert AIDL files to

C++ files because: (1) Existing AIDL tools can generate C++

implementations of interfaces defined in AIDL files without

losing information. (2) Converting C++ implementations to

AIDL files is not trivial and might decrease the precision of

when, for example, a variable is available under a specific

path condition.

After converting AIDL files to C++ files, another choice

information.

On the other hand, the AST is a good representation for

interface model extraction. In the AST, variable names and

variable types are kept intact. Also, every type cast expression

is recorded in AST. In addition, the compiler resolves all

header file dependencies and provide types in correct order

in the AST. Thus, we can process the AST sequentially to

resolve the original type of a typedef type. Besides, the AST

provides a clear view of all transaction codes of each interface

representation.

3.4.3 Transaction Code Identification

As described in Section 2.1, the onTransact function in a tar-

get interface dispatches the control flow to target transactions

constant transaction code .

After identifying transaction codes, we need to extract inputs

deserialized from the data parcel in each transaction. Besides,

as we would like to infer inter-transaction dependencies, we

also need to extract transactions’ outputs which are serialized

into the reply parcel.

Specifically, there are three possible classes of variables

used in a transaction:

out any preconditions.

| 3.4.1 | Principles of Extraction | the interface model. It may lose some important information, |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Complete: | As we want to fuzz Android native system ser- | is to extract the interface model from an intermediate rep- |  |  |  |  |  |  |
| vices systematically, we need to obtain a complete set of | resentation (IR), e.g., the LLVM IR provided by the Clang |  |  |  |  |  |  |  |
| interfaces, together with all transactions of them. All of the | compiler. But IRs usually optimize out some information, |  |  |  |  |  |  |  |
| interfaces have been collected by interface collector. | e.g., type aliases, making it harder to extract precise interface |  |  |  |  |  |  |  |
| Convenient: | Ideally, a | convenient | method | should | be | in the | onTransact | dispatcher, as shown in Figure 2. Lastly, |
| adopted for interface model extraction. Besides, we had better | each statement (e.g., sequential statement and conditional |  |  |  |  |  |  |  |
| find a unified approach to handle both the interfaces defined | statement) is separated in the AST. These characteristics make |  |  |  |  |  |  |  |
| in C++ and those defined in AIDL. | it convenient to extract the interface model from the AST |  |  |  |  |  |  |  |
| Extract from Server Side Code: | In Android, client apps | according to the transaction | code | . This dispatch process is |  |  |  |  |
| call target transactions with the RPC interface | transact | . | usually implemented as a | switch | statement in the C++ source, |  |  |  |
| The service, i.e., the server side, handles the RPC with the | and converted to multiple | case | nodes in the AST, where each |  |  |  |  |  |
| onTransact | method. This correlation means that we can ex- | case | represents a transaction to invoke. Therefore, we can |  |  |  |  |  |
| tract all possible transactions on either side. We prefer to | readily identify all transactions of a target interface by ana- |  |  |  |  |  |  |  |
| analyze the server side for the following two reasons: (1) It | lyzing | case | nodes in the AST and recognize the associated |  |  |  |  |  |
| the server-side code expect, as well as how services use in- | 3.4.4 | Input and Output Variable Extraction |  |  |  |  |  |  |
| representations of the code. We have to choose a proper one to | • | Sequential Variables. | This type of variables exists with- |  |  |  |  |  |
| USENIX Association | 29th USENIX Security Symposium | 311 |  |  |  |  |  |  |

---

## Page 7

| 1 | / / | c h e c k I n t e r f a c e | 1 | i n t 3 2 _ t | i s F d V a l i d | = | d a t a . r e a d I n t 3 2 ( ) ; |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CHECK_INTERFACE ( I M e d i a E x t r a c t o r S e r v i c e , | d a t a , | 2 | i n t | f d | = | − | 1; |
| r e p l y ) ; | 3 | i f | ( i s F d V a l i d ) | { |  |  |  |  |
| 3 | / / | readXXX | 4 | f d | = | d a t a . r e a d F i l e D e s c r i p t o r ( ) ; |  |  |
| 4 | S t r i n g 1 6 | opPackageName= d a t a . r e a d S t r i n g 1 6 ( ) ; | 5 | } |  |  |  |  |

5 p i d _ t p i d = d a t a . r e a d I n t 3 2 ( ) ;

7 e f f e c t _ d e s c r i p t o r _ t d e s c = { } ;

8 d a t a . r e a d (& d e s c , s i z e o f ( d e s c ) ) ;

9 / / r e a d ( a )

11 d a t a . r e a d ( s o u r c e C r o p ) ;

12 / / r e a d F r o m P a r c e l

15 / / c a l l L o c a l

17 / / f u n c t i o n c a l l

Listing 1: Sequential Statement Example

on some conditions. If these conditions are not satisfied,

A. Sequential Statement: As shown in Listing 1, there are

(2) readXXX. In Line 4, readString16 deserializes a com-

mon type, i.e., String16 , from the data parcel. The vari-

able name also holds some semantics. In this case, the

Line 5, readInt32 reads a int32_t variable, while the

will always choose the type with richer semantics as the

variable type, i.e., pid_t . We will also apply this strategy

to type cast expressions.

(3) read(a, sizeof(a) * num). In this circumstance, the server

will directly copy a raw structure or an array from the

data parcel. In Line 8, the server reads a structure whose

(4) read(a). Here, the server will read a Flattenable or Light-

Flattenable structure Rect .

(6) callLocal. Taking Line 16 as an example, callLocal

method will process the arguments of createSurface

one by one. If the variable type is not a pointer, it is con-

as an output variable.

condition for fd to get a more precise interface model.

1 c o n s t i n t s i z e = d a t a . r e a d I n t 3 2 ( ) ;

| 3 | . . . |  |  |  |
| --- | --- | --- | --- | --- |
| 4 | c o n s t | S t r i n g 8 | key ( d a t a . r e a d S t r i n g 8 ( ) ) ; |  |
| 6 | . . . |  |  |  |
| 7 | i n t | f d | = | d a t a . r e a d F i l e D e s c r i p t o r ( ) ; |
| 8 | . . . |  |  |  |
| 9 | } | e l s e | { |  |
| 10 | c o n s t | S t r i n g 8 | v a l u e ( d a t a . r e a d S t r i n g 8 ( ) ) ; |  |
| 11 | . . . |  |  |  |
| 12 | } |  |  |  |

13 }

| 6 | / / | r e a d ( a , s i z e o f ( a ) | ∗ | num ) | Listing 2: Conditional Statement Example |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | R e c t | s o u r c e C r o p ( R e c t : : EMPTY_RECT) ; | Flattenable structure. In Line 11, the server reads a Light- |  |  |  |  |  |  |  |
| 13 | a a u d i o : : A A u d i o S t r e a m R e q u e s t | r e q u e s t ; | (5) | readFromParcel. | This kind of sequential statement |  |  |  |  |  |
| 14 | r e q u e s t . r e a d F r o m P a r c e l (& d a t a ) ; | is special in that the deserializtion process happens |  |  |  |  |  |  |  |  |
| 16 | c a l l L o c a l ( d a t a , | r e p l y , | &I S u r f a c e C o m p o s e r C l i e n t : : | in another class or structure which implements the |  |  |  |  |  |  |
| c r e a t e S u r f a c e ) ; | Parcelable | interface. In Line 14, the server reads a class |  |  |  |  |  |  |  |  |
| 18 | s e t S c h e d P o l i c y ( d a t a ) ; | whose type is | aaudio::AAudioStreamRequest | . |  |  |  |  |  |  |
| • | Conditional Variables. | This type of variables depends | sidered as an input variable. Otherwise, it is considered |  |  |  |  |  |  |  |
| the variables could be | NULL | or do not appear in the data, | (7) | Misc Function. | For those special input formats, the | data |  |  |  |  |
| or even have a different type than when the conditions | parcel will be passed into a function. In Line 18, the | data |  |  |  |  |  |  |  |  |
| are satisfied. | parcel is passed into the function | setShedPolicy | . For |  |  |  |  |  |  |  |
| • | Loop Variables. | This type of variables are deserialized | such a case, we will mark this input as a function and |  |  |  |  |  |  |  |
| in loops, and even nested loops. | recursively handle the data. Moreover, this indicates we |  |  |  |  |  |  |  |  |  |
| These three types of variables correspond to three types | should also collect the file which includes the correspond- |  |  |  |  |  |  |  |  |  |
| of statements in the program exactly, i.e., sequential state- | ing function, e.g., | setSchedPolicy | in this case. |  |  |  |  |  |  |  |
| ment, conditional statement and loop statement. As a result, | B. Conditional Statement: | There are several kinds of con- |  |  |  |  |  |  |  |  |
| we will mainly process these kinds of statements in the AST. | ditional statements, e.g., | if | statement and | switch | statement. |  |  |  |  |  |
| Besides, we will also consider the return statement. The rea- | Here we demonstrate our approach to the | if | statement. As |  |  |  |  |  |  |  |
| son will be detailed in the corresponding part. Moreover, as | shown in Listing 2, whether Line 4 will be executed or not |  |  |  |  |  |  |  |  |  |
| onTransact | function processes inputs and outputs similarly, | is decided by the | isFDValid | variable. In such a case, we |  |  |  |  |  |  |
| we only demonstrate the details with input variables. | consider | fd | as a | conditional input | . Besides, we record the |  |  |  |  |  |
| mainly seven kinds of sequential statements: | C. Loop Statement: | There are several forms of | loop | state- |  |  |  |  |  |  |
| (1) | checkInterface. | The server will check the interface to- | ments, e.g., | for | statement and | while | statement. Here we |  |  |  |
| ken (unique for every interface) given by the client at | demonstrate our approach to the | for | statement. As shown |  |  |  |  |  |  |  |
| the beginning of each transaction. If the interface token | in Listing 3, we record the number of times | key | is read, |  |  |  |  |  |  |  |
| does not match, it will just return, which suggests that we | i.e., | size | . We consider | key | , | fd | and | value | as | loop vari- |
| cannot fill random bytes into | data | parcel. | ables | . Moreover, there might be a kind of | for | statement, |  |  |  |  |
| opPackageName | should be a package name. Besides, in | 2 | f o r | ( i n t | i n d e x | = | 0 ; i n d e x < s i z e ; | ++ i n d e x ) { |  |  |
| left-hand-side variable type is | pid_t | . In such a case, we | 5 | i f ( key | == | S t r i n g 8 ( " F i l e D e s c r i p t o r K e y " ) ) { |  |  |  |  |
| type is | effect_descriptor_t | . | Listing 3: Loop Statement Example |  |  |  |  |  |  |  |
| 312 | 29th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |

---

## Page 8

2 i f ( numBytes >MAX_BINDER_TRANSACTION_SIZE ) {

5 }

types of statements can be nested together.

D. Return Statement: Return statement is special among

numBytes is larger than MAX_BINDER_TRANSACTION_SIZE ,

the function will simply return an error code DRM_NO_ERROR .

ing numBytes . Besides, it will also help us generate explicit

Apart from extracting input and output variables in trans-

actions, we also extract type definitions. It helps enrich the

variable semantics so as to generate better inputs. There are

three kinds of types to analyze:

1 t y p e d e f i n t _ _ k e r n e l _ p i d _ t ;

2 t y p e d e f _ _ k e r n e l _ p i d _ t _ _ p i d _ t ;

| 5 | e f f e c t _ u u i d _ t | t y p e ; |
| --- | --- | --- |
| 7 | u i n t 3 2 _ t | a p i V e r s i o n ; |
| 9 | u i n t 1 6 _ t | cpuLoad ; |
| 12 | c h a r | i m p l e m e n t o r [ EFFECT_STRING_LEN_MAX ] ; |

• Type Alias: There are many typedef statements in

effect_descriptor_t in Listing 1 is actually struct

edge, we could not generate semantics-rich inputs.

Also, as AOSP is a monolithic project, we need to add

3.5 Dependency Inferer

3.5.1 Interface Dependency

dency between these two interfaces. As introduced in Section

2.1, we can get Android native system service interfaces, i.e.,

gards multi-level interfaces, we find that upper-level interface

will call writeStrongBinder to serialize a deep interface

into reply . In this way, we can easily collect all generation

dependencies of interfaces.

the use dependency.

3.5.2 Variable Dependency

transaction. Conditional dependency refers to the case where

| 1 | c o n s t | u i n t 3 2 _ t | numBytes= d a t a . r e a d I n t 3 2 ( ) ; | AOSP. | As shown | in | Listing 5, | pid_t | is actually |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | r e p l y | − | > w r i t e I n t 3 2 (BAD_VALUE) ; | an | int | type. | As a result, we could generate vari- |  |  |
| 4 | r e t u r n | DRM_NO_ERROR; | ables of type | pid_t | with random integers. Besides, |  |  |  |  |
| Listing 4: Return Statement Example | effect_descriptor_s | . Without such typedef knowl- |  |  |  |  |  |  |  |
| for(auto i: vector) | , which does not explicitly declare | the namespace to variable types so as to avoid conflicts when |  |  |  |  |  |  |  |
| the cycle count. We heuristically guess that the cycle count is | extracting these kinds of type knowledge. Besides, guaranteed |  |  |  |  |  |  |  |  |
| the previous value read from the parcel before the | for | state- | by the compiler, all headers used by the C/C++ files will |  |  |  |  |  |  |
| ment, e.g., | size | in Line 1. Furthermore, we can observe that | be included in AST in order. As a result, we can collect |  |  |  |  |  |  |
| there is also a conditional statement, which implies that these | definitions of all related types. |  |  |  |  |  |  |  |  |
| these statements. During a transaction, several | return | state- | After extracting interface models, we infer two kinds of depen- |  |  |  |  |  |  |
| ments might appear, which lead to different execution paths. | dencies: (1) | interface dependency | . That is, how a multi-level |  |  |  |  |  |  |
| If a path returns an error code, it implies that this path is | interface is recognized and generated. It also implies how an |  |  |  |  |  |  |  |  |
| less likely to have vulnerabilities. Thus, we will assign this | interface is used by other interfaces. (2) | variable dependency. |  |  |  |  |  |  |  |
| path a low probability, which means that fewer test cases | There are dependencies between variables in transactions. |  |  |  |  |  |  |  |  |
| taking this path will be generated. As Listing 4 shows, if | Previous researches rarely consider these dependencies. |  |  |  |  |  |  |  |  |
| In such a case, we should try not to generate a value | In general, there are two types of dependencies between inter- |  |  |  |  |  |  |  |  |
| larger than | MAX_BINDER_TRANSACTION_SIZE | when generat- | faces, corresponding to the generation and use of interfaces. |  |  |  |  |  |  |
| inter-transaction dependency, as inputs that do not satisfy the | Generation Dependency | If an interface can be retrieved |  |  |  |  |  |  |  |
| dependency usually fall back to error handling paths. | via another interface, we say that there is a generation depen- |  |  |  |  |  |  |  |  |
| 3.4.5 | Type Definition Extraction | top-level interfaces, directly from the service manager. As re- |  |  |  |  |  |  |  |
| • | Structure-like Definition. | This kind of types includes | Use Dependency | If an interface is used by another inter- |  |  |  |  |  |
| union and structure. We could easily extract the member | face, we say that there is a use dependency between these two |  |  |  |  |  |  |  |  |
| of these kinds of objects from the AST. | interfaces. We find that when an interface A is used by another |  |  |  |  |  |  |  |  |
| • | Enumeration Definition: | As for enumeration type, we | interface B, B will call | readStrongBinder | to deserialize A |  |  |  |  |
| should extract all given (constant) enumeration values. | from | data | parcel. Hence, we can utilize this pattern to infer |  |  |  |  |  |  |
| 3 | t y p e d e f | _ _ p i d _ t | p i d _ t ; | There are two types of variable dependencies, i.e., intra- |  |  |  |  |  |
| 4 | t y p e d e f | s t r u c t | e f f e c t _ d e s c r i p t o r _ s | { | transaction | and inter-transaction | dependency, based on |  |  |
| 6 | e f f e c t _ u u i d _ t | u u i d ; | whether the variable pair is in a same transaction. |  |  |  |  |  |  |
| 8 | u i n t 3 2 _ t | f l a g s ; | Intra-Transaction Dependency | One variable sometimes |  |  |  |  |  |
| 10 | u i n t 1 6 _ t | memoryUsage ; | depends on another in the same transaction. As demonstrated |  |  |  |  |  |  |
| 11 | c h a r | name [ EFFECT_STRING_LEN_MAX ] ; | in Section 3.4.4, there could be conditional dependency, loop |  |  |  |  |  |  |
| 13 | } | e f f e c t _ d e s c r i p t o r _ t ; | dependency, and array size dependency between variables in a |  |  |  |  |  |  |
| Listing 5: Typedef Statement Example | the value of one variable decides whether another exists or |  |  |  |  |  |  |  |  |
| USENIX Association | 29th USENIX Security Symposium | 313 |  |  |  |  |  |  |  |

---

## Page 9

| Algorithm 1 | Inference of Inter-Transaction Dependency | fuzzer manager | will sync the crash logs from smartphones |
| --- | --- | --- | --- |
| Input: | Interface Model (M) | regularly. Here we mainly demonstrate the test case generator, |  |
| Output: | Inter-Transaction Dependency Graph (G) | as other parts are straightforward in FANS. Interested readers |  |
| G | = | {} | could refer to the source code we open source for details. |
| I | = [ ] | // input variables | When fuzzing Android native system services, we are |

O = [ ] // output variables

for variable in M do

if variable is input then

add variable into I

end if

add variable into O

end if

end for

for iVar in I do

end if

end if

end for

end for

as the variables size and key in Listing 3. For the last one,

Inter-Transaction Dependency A variable sometimes de-

pends on another variable in a different transaction. In other

words, input in one transaction can be obtained through output

in another transaction. We propose Algorithm 1 to deal with

this kind of dependency. Specifically, we extract the inter-

transaction dependencies following the principles below: 1

one variable is input, and the other is output; 2 these two

variables are located in different transactions; 3 input vari-

able’s type is equal to the output variable’s type; 4 either

the input variable type is complex (not primitive type), or the

input variable name and the output variable name are similar.

The similarity measurement algorithm can be customized.

3.6 Fuzzer Engine

After inferring the dependencies, we can start fuzzing An-

droid native system services. Firstly, the fuzzer manager will

fuzzing the transaction specified by the transaction code.

Therefore we can randomly generate a transaction at first

and then invoke its corresponding interface.

a transaction one by one based on the interface model. During

the generation, we follow the principles in order as below.

• Constraint First. If a variable is constrained by another

do not follow this principle for a low probability.

• Type and Name Third. We may generate a variable

according to its type and name, no matter the aforemen-

tioned dependencies exist or not. For example, in Listing

1, we will generate a valid package name ( String16 )

dependency.

4 Implementation

We implemented a prototype of FANS from scratch, rather

than developing one based on an existing fuzzer, e.g.,

AFL [25], for the following reasons. First, it takes huge en-

gineering work to port AFL to Android. Second, AFL-based

fuzzers are effective at testing one standalone program or

service, thus we have to compile and test each target service

one by one, which is non-scalable. Third, AFL is not effective

at testing service-based applications, including the binder IPC

based services. Table 1 shows the statistics of this implemen-

tation.

| if | variable is output | then | Transaction Generator | We can generate input variables of |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| for | oVar in O | do | variable, we should check the constraints before gener- |  |  |  |
| if | iVar.txID != oVar.txID | then | ating the variable. For instance, as shown in Listing 2, |  |  |  |
| if | iVar.type==oVar.type | then | isFDValid | should be checked before generating | fd | . |
| if | iVar.type is complex | then | • | Dependency Second. | If a variable can be generated by |  |
| add edge (iVar, oVar) into G | other transactions, we should use them to generate it |  |  |  |  |  |
| else if | iVar.name and oVar.name are similar | then | with a high probability. In such circumstances, we should |  |  |  |
| add edge (iVar, oVar) into G | generate the dependent transaction first, and then get the |  |  |  |  |  |
| end if | output from the corresponding | reply | parcel. Also, we |  |  |  |
| not. For example, | fd | in Listing 2 conditionally depends on | for | opPackageName | . Besides, we will generate a valid |  |
| isFdValid | . Loop dependency refers to the case where one | process ID ( | int | ) for | pid | . For a complex type, we will |
| variable decides the number of times another is read or written, | generate its members recursively according to this rule. |  |  |  |  |  |
| the size of an array variable is specified by another variable. | Interface Acquisition | As for top-level interfaces, we can |  |  |  |  |
| When generating this array variable, we should generate the | get them through the service manager. Multi-level interfaces |  |  |  |  |  |
| specified number of items. | can then be recursively obtained via the recognized interface |  |  |  |  |  |
| sync the fuzzer binary, interface model, and dependencies to | Interface Collector | To be able to collect interfaces effi- |  |  |  |  |
| mobile phone and start the fuzzer on the smartphone. Then | ciently, we first compile the AOSP codebase, recording the |  |  |  |  |  |
| the fuzzer will generate a test case, i.e., a transaction and its | compilation commands in the meantime. Then we walk these |  |  |  |  |  |
| corresponding interface to fuzz the remote code. Besides, the | commands while scanning for the characteristics pointed out |  |  |  |  |  |
| 314 | 29th USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 10

| Interface Collector | Python | 145 |
| --- | --- | --- |
| Interface Model Collector | C++, Python | 5238 |
| Dependency Inferer | Python | 291 |
| Fuzzer Engine | C++, Python | 5070 |
| Total | C++, Python | 10744 |

in Section 3.3 and Section 3.4.4. This step can be easily im-

plemented with Python.

We do an approximate slice on the AST and only preserve

statements relevant to input and output variables, omitting

others. Finally, we do a post-process on the rough model so

tem services check the caller’s permission when receiving

RPC requests, the fuzzer is executed under root privilege.

To accelerate the execution, we always make asynchronous

need the outputs in reply , e.g., dependency inference, we

make synchronous calls. Finally, in order to analyze triggered

crashes, we use the builtin logcat tool of Android for log-

ging. Besides, we will also record native crash logs located in

Multi-level generated Top-level in AOSP

Multi-level in AOSP

Top-level in AOSP

23(33.8%)

Multi-level in AOSP

20(29.4%)

20(29.4%)

Top-level generated

Figure 3: Interface Statistics: 43 top-level Android native

smartphones with AOSP build number PQ3A.190801.002 ,

i.e., android-9.0.0_r46 , which is a recent version support-

5.1 Interface Statistics and Dependency

cies among these interfaces.

5.1.1 Interface Statistics

takes a few seconds to find the interfaces in the source code.

As shown in Figure 3, multi-level interfaces account for as

the necessity to examine more interfaces than registered at the

| Table 1: Implementation Details of FANS | Top-level generated |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Component | Language | LoC | 5(7.4%) | Multi-level generated |  |
| Interface Model Extractor | As we are extracting interface | system interfaces are discovered, of which 23 are from AOSP |  |  |  |
| models from AST, we first convert the compilation commands | and 20 are generated from AIDL files. 25 multi-level Android |  |  |  |  |
| to | cc1 | commands while linking with the Clang plugin which | native system interfaces are discovered, of which 20 are from |  |  |
| is used to walk the AST and extract a rough interface model. | AOSP and 5 are generated from AIDL files. |  |  |  |  |
| that | fuzzer engine | can easily use it. The interface model is | (3) How effective is FANS in discovering vulnerabilities of |  |  |
| stored in JSON format. | Android native system services? (Section 5.3) |  |  |  |  |
| Dependency Inferer | Given the interface model described | Experimental Setup | As shown in Figure 2, we implement |  |  |
| with JSON, dependency inferer traverses the model and makes | the first three components on Ubuntu 18.04 with i9-9900K |  |  |  |  |
| interface dependency inference as explained in Section 3.5.1. | CPU, 32 GB memory, 2.5 T SSD. As for test devices, we |  |  |  |  |
| Besides, dependency inferer will also get the inter-transaction | use the following Google’s Pixel series products: Pixel * 1, |  |  |  |  |
| dependency according to Algorithm 1. | Pixel 2XL * 4, and Pixel 3XL * 1. We flash systems of these |  |  |  |  |
| Fuzzer Engine | We implement a simple fuzzer manager | ing these devices when writing this paper. Although the An- |  |  |  |
| so as to run fuzzer on multiple phones together with sync- | droid release versions are the same, the source code can be |  |  |  |  |
| ing data between host and smartphones. We build the en- | slightly different for different Pixel models. For the following |  |  |  |  |
| tire AOSP with ASan enabled. The fuzzer is implemented | two sections (Section 5.1, Section 5.2), we report the experi- |  |  |  |  |
| in C++ as a native executable. As some Android native sys- | ment results carried out on Pixel 2XL. |  |  |  |  |
| RPCs through marking the | flag | argument of | transact | as | In this section, we systematically analyze the interfaces col- |
| 1 when the outputs in | reply | are not needed. When we do | lected by the interface collector and introduce the dependen- |  |  |
| /data/tombstones/ | . | It takes about an hour to compile AOSP. However, it only |  |  |  |
| 5 | Evaluation | many as 37% of all native service interfaces, which highlights |  |  |  |
| In this section, we evaluate FANS to answer the following | service manager. Besides, interfaces generated by AIDL tools |  |  |  |  |
| questions: | also take a large part, so we should extract interfaces directly |  |  |  |  |
| (1) How many interfaces have been found? What is the rela- | inside AOSP and interfaces generate from AIDL files. We are |  |  |  |  |
| tionship between them? (Section 5.1) | not able to compare the number of interfaces discovered by |  |  |  |  |
| (2) What does the extracted interface model look like? Is the | FANS with any other existing research, as none ever focused |  |  |  |  |
| model complete and precise? (Section 5.2) | on Android native system services. |  |  |  |  |
| USENIX Association | 29th USENIX Security Symposium | 315 |  |  |  |

---

## Page 11

Legend Top-level Code

IDataSource Generation Use Multi-level Code

| IMediaExtractorService | IEffectClient | IAudioFlingerClient |  |
| --- | --- | --- | --- |
| IMediaExtractor | IAudioFlinger |  |  |
| IMediaSource | IAudioRecord | IAudioTrack | IEffect |

IMemory

IMemoryHeap IMediaDrmService

Figure 4: Part of the Interface Dependency Graph

5.1.2 Interface Dependency

tionship. As the full interface dependency graph is too large

interface dependency with one of its representative parts, as

whose ancestor is IMediaExtractorService . It requires

five steps to get the IMemoryHeap interface. Without depen-

system functionality as needed and can be manually instan-

tiated by developers and passed to top-level or multi-level

interfaces. For example, IEffectClient interface is trans-

ferred to some transaction A of IAudioFlinger . Transaction

A will call the method provided by the IEffectClient in-

terface later. To the best of our knowledge, we are the first

to systematically investigate the dependencies between the

interfaces in Android native system services.

5.2 Extracted Interface Model

281(34.6%)

548(39.9%)

827(60.1%)

530(65.4%)

Figure 5: Transaction Details in Interface: 530 top-level trans-

level transaction paths and 548 multi-level transaction paths

are found.

We start this section by discussing the extracted interface

model statistics, and then talk about the completeness and

transaction and variable.

Variable We only count in variables that are directly inside

onTransact . That is, we do not count variables recursively.

For instance, onTransact uses readFromParcel to read a

structure. It is only in readFromParcel that the structure’s

members are dealt with, so we exclude them from the statis-

tics. Otherwise, the statistics would be imprecise. As shown

in Figure 6, there are various types as described in Section

3.4.4, e.g., structure and file descriptor. We explain the fig-

ure from three aspects: variable patterns, type aliases, and

| ICrypto | IDrm | actions and 281 multi-level transactions are found. 827 top- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| It just takes seconds to infer the interface dependency rela- | precision of the interface model. |  |  |  |  |  |
| (see Figure 8 in Appendix), we demonstrate the complexity of | 5.2.1 | Extracted Interface Model Statistics |  |  |  |  |
| shown in Figure 4. The deepest interface is | IMemoryHeap | , | We discuss the extracted interface model from two aspects: |  |  |  |
| dency relationships, we could not obtain such a deep interface | Transaction | As shown in Figure 5, there are 811 trans- |  |  |  |  |
| easily and automatically. It also comes to our notice that | actions inside the Android native system services, in which |  |  |  |  |  |
| a multi-level interface can be obtained from several upper | multi-level transactions account for 281, a proportion of about |  |  |  |  |  |
| interfaces. For example, | IMemory | can be obtained from the | 35%. Besides, in either top-level interfaces or multi-level in- |  |  |  |
| IMediaSource | , | IEfect | , and | IAudioTrack | interfaces. There- | terfaces, the transaction path quantity is over 1.5 times that |
| fore, we can explore different paths to fuzz a same interface. | of the transaction, which means many transactions hold more |  |  |  |  |  |
| Besides, there are some other interfaces which are neither | than one return statement in the sliced AST. In other words, |  |  |  |  |  |
| top-level interfaces nor multi-level interfaces, but the archi- | if we do not distinguish between different transaction paths, |  |  |  |  |  |
| tecture remains the same. We call such interfaces customized | we cannot obtain an explicit dependency since some inter- |  |  |  |  |  |
| interfaces. Customized interfaces are designed to customize | transaction dependencies only exist on a particular path. |  |  |  |  |  |
| The process of extracting a rough interface model takes about | inter-transaction variable dependencies. |  |  |  |  |  |
| an hour. The post-process of the interface model extractor | • | Variable Pattern. | According to variable patterns, we |  |  |  |
| only takes seconds. We also give the time for inferring the | divide variables into three kinds as demonstrated in |  |  |  |  |  |
| variable dependency as follows. The time used to infer intra- | Section 3.4.4: sequential variable, conditional variable |  |  |  |  |  |
| transaction dependencies has already been counted into that | and loop variable. We notice that few variables are in |  |  |  |  |  |
| of extracting the interface model. As to the time for inter- | simple sequential statements, and most variables pro- |  |  |  |  |  |
| transaction dependency inference, it is also a matter of sec- | cessed in sequential statements have | String | type. The |  |  |  |
| onds. | reason behind this is that nearly all interfaces check |  |  |  |  |  |
| 316 | 29th USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 12

Conditional Pattern

Loop Pattern

10 2

10 2

10 1

10 0 10 1

String Binder String

Function

Primitive Type Enumeration FileDescriptor Structure-Like Enumeration

Array or Vector Primitive Type FileDescriptor

Figure 6: Classification Result of Variables by Variable Pattern, Type Alias, and Dependency

tions and the only one GET_METRICS transaction in the

use typedef statements for more semantic types, which

semantic knowledge of variables without these typedef

statements.

• Variable Dependency. Here we consider inter-

transaction dependencies. Since there is no dependency

on output variables, we focus on input variables.

Moreover, we generate array dependency according

to the array item type. As shown in Figure 6, there

are dependencies among almost all variable types, in

particular primitive types and the string type. Besides,

structure-like and binder-type variables can also be

generated based on dependency, which helps generate

more semantic and well-structured inputs, resulting in

deep fuzzing into Android native system services.

5.2.2 Completeness and Precision of Extracted Inter-

face Model

10 3

Alias Type Exist Dependency

10 2

10 1

| Binder | String | Binder |  |  |
| --- | --- | --- | --- | --- |
| Function | Function |  |  |  |
| Structure-Like | Enumeration |  |  |  |
| Array or Vector | Primitive Type | FileDescriptor | Structure-Like | Array or Vector |

3.5.2.

To evaluate how effective FANS is, we intermittently ran

FANS on our six smartphones for around 30 days. However,

we were not able to get the precise run-time of FANS during

the 30 days’ experiment due to the following reasons: (1) The

fuzzer might crash every several minutes. (2) As we ran the ex-

periment on real machines, once the Android system crashed,

we had no choice but to re-flash them manually. Moreover, the

device could enter recovery mode even when the fuzzer had

started less than ten minutes ago. These situations decreased

the fuzzing efficiency and also prevented collecting statistics

about run-time. Despite this, we have discovered 30 unique

bugs from thousands of crashes reported by FANS.

All of the 30 vulnerabilities are listed in Table 2. Apart

from the 22 vulnerabilities found in Android native sys-

tem services, there are five vulnerabilities in the libraries

libcutils.so , libutils.so and libgui.so , which are

| 10 | 3 | Sequential Pattern | 10 | 3 | Raw Type | None Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| the interface token at the beginning of each transaction | precise but good enough. What’s more, inter-transaction vari- |  |  |  |  |  |
| except several | SHELL_COMMAND_TRANSACTION | transac- | able dependencies are calculated with Algorithm 1 in Section |  |  |  |
| IMediaRecorder | interface. In other words, almost all | As far as we know, no previous work focuses on Android |  |  |  |  |
| variables are conditional variables. Therefore, we have | native system services, precluding any comparison. However, |  |  |  |  |  |
| to extract the constraints imposed on variables to gener- | we argue that most existing researches cannot handle Android |  |  |  |  |  |
| ate valid inputs. Constraint extraction is also necessary | native system services effectively. Chizpurfle [10] focuses |  |  |  |  |  |
| for solving intra-transaction dependencies. Additionally, | on vendor-implemented Java services and cannot deal with |  |  |  |  |  |
| it is possible for almost all variable types to occur in a | Android native system services. BinderCracker [6] tests all |  |  |  |  |  |
| loop. | services in Android but is unable to infer a more complete |  |  |  |  |  |
| • | Type Alias. | As for type alias, i.e., type defined in | and precise model than FANS when applied to Android native |  |  |  |
| typedef | statement, we notice that all aliases are for | system services. This is due to the fact that BinderCracker is |  |  |  |  |
| three types: primitive types, enumeration types, and | based on app traffic, which might miss rarely used RPCs and |  |  |  |  |  |
| structure-like types. This makes sense as we usually | lose various variable semantics like variable names and types. |  |  |  |  |  |
| can be seen from List 5. By all means, we would lose | 5.3 | Vulnerability Discovery |  |  |  |  |
| As there is no ground truth about the interface model, we ran- | used as public libraries in Android native system services. |  |  |  |  |  |
| domly select ten interfaces and manually check whether the | Furthermore, we found three vulnerabilities in Linux system |  |  |  |  |  |
| extracted model is complete and precise according to the prin- | components. For instance, we discovered a stack overflow in |  |  |  |  |  |
| ciple mentioned in Section 3.4.1. We find that we successfully | iptables-restore | . This program is a user-space program |  |  |  |  |
| recover all the transaction codes, fulfilling completeness. Al- | for firewall configuration provided by Linux kernel. These vul- |  |  |  |  |  |
| most all variable patterns, variable names and variable types | nerabilities prove that inputs generated by FANS can drive the |  |  |  |  |  |
| are recovered as well. In conclusion, the model is not entirely | control flow into deep paths under complicated constraints. |  |  |  |  |  |
| USENIX Association | 29th USENIX Security Symposium | 317 |  |  |  |  |

---

## Page 13

Table 2: Vulnerabilities found by FANS

| Component | Vulnerability File (binary or so) | AndroidID | Vulnerability Type | Status |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | libsensor.so | - | Heap user after free | Reported |  |  |  |  |
| 2 | libsensor.so | 128919198 | Out of Memory | Confirmed |  |  |  |  |
| 3 | libsensor.so | 128919198 | Out of Memory | Confirmed |  |  |  |  |
| 4 | libsensor.so | - | Assertion failure | Reported |  |  |  |  |
| 5 | libsensorservice.so | 143896234 | Illegal fd | Confirmed |  |  |  |  |
| 6 | libmediadrm.so | 143897317 | new_capacity overflow | Confirmed |  |  |  |  |
| 7 | libmediadrm.so | 143895981 | new_capacity overflow | Confirmed |  |  |  |  |
| 8 | libmediadrm.so | 143896237 | Null pointer dereference | Confirmed |  |  |  |  |
| 9 | libmediametrics.so | 143896917 | Null pointer dereference | Confirmed |  |  |  |  |
| 10 | libsurfaceflinger.so | 143899028 | invalid memory access | Confirmed |  |  |  |  |
| 11 | Android Native | libsurfaceflinger.so | 143897162 | invalid memory access | Confirmed |  |  |  |
| 12 | System Service | libaaudioservice.so | 143895840 | Null pointer dereference | Confirmed |  |  |  |
| 13 | libaudiopolicymanagerdefault.so | - | key not found | Reported |  |  |  |  |
| 14 | libmediaplayerservice.so | - | CHECK failure | Reported |  |  |  |  |
| 15 | installd | 143899228 | Stack buffer overflow | Confirmed |  |  |  |  |
| 16 | installd | 143898908 | incomplete check | Confirmed |  |  |  |  |
| 17 | installd | - | CHECK failure | Reported |  |  |  |  |
| 18 | installd | - | CHECK failure | Reported |  |  |  |  |
| 19 | statsd | 143897309 | Null pointer dereference | Confirmed |  |  |  |  |
| 20 | statsd | 143895055 | Out-of-bound access | Confirmed |  |  |  |  |
| 21 | incidentd | 143897849 | Null pointer dereference | Confirmed |  |  |  |  |
| 22 | gatekeeperd | 143894186 | Null pointer dereference | Duplicated |  |  |  |  |
| 23 | libcutils.so | 143898908 | integer overflow | Confirmed |  |  |  |  |
| 24 | libcutils.so | 143898343 | Null pointer dereference | Confirmed |  |  |  |  |
| 25 | Basic Library | libutils.so | - | integer overflow | Reported |  |  |  |
| 26 | libgui.so | - | mul-overflow | Reported |  |  |  |  |
| 27 | libgui.so | - | Null pointer dereference | Reported |  |  |  |  |
| 28 | iptables-restore | 143894992 | Stack buffer overflow | Duplicated |  |  |  |  |
| 29 | Linux Component | ip6tables-restore | 143895407 | Stack buffer overflow | Duplicated |  |  |  |
| 30 | fsck.f2fs | - | heap-buffer-overflow | Reported |  |  |  |  |
| Moreover, although | we | aim | to | discover vulnerabil- | services. However, Android began to support clang only after |  |  |  |
| ities | in | Android | native | system | services | implemented | Android 7.0. As we utilize an LLVM plugin to extract the |  |
| in | C++, | we | triggered | 138 | Java | exceptions, | such | interface model, it is not easy to port our approach to lower |
| as | FileNotFoundException | , | DateTimeException | , | Android versions. Besides, BinderCracker is closed-source, so |  |  |  |
| NoSuchElementException | , and | NullPointerException | . | we cannot test it on modern Android, e.g., android-9.0.0_r46. |  |  |  |  |
| This can be attributed to the fact that Java applications | Moreover, BinderCracker did not show detailed vulnerabil- |  |  |  |  |  |  |  |
| sometimes depend on Android native system services. Some | ity types. We are thus forced to a simple comparison of the |  |  |  |  |  |  |  |
| native services also invoke Java methods. Since robustness | number of vulnerabilities discovered by the two tools. Binder- |  |  |  |  |  |  |  |
| and stability are important for Android native system services, | Cracker found 89 vulnerabilities on Android 5.1 and Android |  |  |  |  |  |  |  |
| these Java exceptions should not have occurred. Stricter | 6.0, both native vulnerabilities and java exceptions included. |  |  |  |  |  |  |  |
| checks should be enforced to solve this problem. | Although we only focus on Android native system services, |  |  |  |  |  |  |  |
| We have reported all native vulnerabilities to Google. 20 of | we found 30 native vulnerabilities and 138 Java exceptions, |  |  |  |  |  |  |  |
| them were confirmed and 18 Android IDs were given, three | way more than 89. We believe this comparison is convincing |  |  |  |  |  |  |  |
| of which are duplicate with undisclosed vulnerability report. | that FANS is superior over BinderCracker as Android security |  |  |  |  |  |  |  |
| Up to now, Google has assigned moderate severity to Android | has been improving over the years. |  |  |  |  |  |  |  |

ID 143895055 and 143899228. Google has also assigned

CVE-2019-2088 to Android ID 143895055 and will put us in

5.4 Case Studies

their acknowledgment page in the future. Submission of Java

exceptions is in progress.

We present three vulnerabilities discovered by FANS. Firstly,

we look into the root causes of these vulnerabilities and

| Comparison with Existing Research | It is not trivial work | demonstrate how to trigger vulnerabilities. Also, we explain |
| --- | --- | --- |
| to compare our solution with related work. To the best of | how design choices (e.g., categorizing variables as sequential, |  |
| our knowledge, BinderCracker [6] is the most relevant one. | conditional, and loop ones) help generate inputs that trigger |  |
| BinderCracker works on Android system services before An- | vulnerabilities. Secondly, we show our insights into these |  |
| droid 6.0, including Java system services and native system | vulnerabilities and devise mitigation for them. |  |
| 318 | 29th USENIX Security Symposium | USENIX Association |

---

## Page 14

5.4.1 Case Study I: new_capacity overflow Inside read- Attacker netd ip(6)tables-restore

Vector of IDrm

Attack There are multiple new_capacity overflow vul-

nerabilities in IDrm , a second-level interface obtained via

IMediaDrmService . The bugs are all triggered by the

same function, BnDrm::readVector . The function invokes

insertAt to allocate a buffer whose size is decided by the

variable size in data . Inside insertAt , there is a sanity

check on the insertion index, which will return BAD_INDEX

in case of a lousy index. However, no check is made on the

size argument. According to the interface dependency graph,

FANS could generate IDrm interface automatically. When

it comes to the variable name size , FANS generates some

a very vulnerable one. Vulnerabilities can easily occur dur-

tunately, there are safely implemented deserialization func-

These standard functions are preferable to the error-prone

customized functions. In this case, replacing readVector

with Parcel::readByteVector would fix the vulnerability

neatly.

5.4.2 Case Study II: Out-of-bound Access Inside infor-

mAllUidData of statsd

to generate the malformed transaction, FANS first identifies

addInterface

main

wakeupAddInterface execIptables

add_param_to_argv

execute

Figure 7: Call Trace of ip(6)tables-restore stack overflow

might not be able to generate such effective inputs as it

restore

Attack An unexpected stack overflow bug is found to re-

side in the ip(6)tables-restore binary. As we focus on An-

droid native system services, we do not find the vulner-

ability directly. It is found when we fuzz the netd dae-

mon, whose interface file is generated automatically. We

craft in_ifName with a sufficiently long string quoted in

mentioned above.

| dangerous values, e.g., -1, which can easily trigger the vulner- | the variable types of these three inputs from AST. Then it |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ability. We could further achieve DoS attack through this kind | generates these vectors one by one through (1) generating the |  |  |  |  |  |  |  |  |
| of vulnerability, preventing other apps from using necessary | vector size; (2) generating the corresponding number and type |  |  |  |  |  |  |  |  |
| services. | of elements. However, existing work like BinderCraker [6] |  |  |  |  |  |  |  |  |
| Insight | Buffer allocation is a core step in IPC, and also | ignores the semantics of these variables. |  |  |  |  |  |  |  |
| ing this process if the server puts any trust in the client and | Insight | In this case, the same index is used for different |  |  |  |  |  |  |  |
| skips necessary sanity checks. Unfortunately, this problem | vectors, resulting in an OOB vulnerability. This bug, just as |  |  |  |  |  |  |  |  |
| is prevalent among Android native system services and is | the last case, arises from failure in input validation. Never- |  |  |  |  |  |  |  |  |
| persistent. In | BnDrm | alone, the problematic | readVector | is | theless, it is a more interesting bug. Hopefully it can yield |  |  |  |  |
| called for more than 30 times, making an easy target for at- | an exploitation other than DoS if appropriately used. This |  |  |  |  |  |  |  |  |
| tackers. Performing proper sanity checks would effectively | case demonstrates FANS’s ability to discover meaningful |  |  |  |  |  |  |  |  |
| mitigate this problem. Nevertheless, it is not an easy task | bugs. Google has already fixed this vulnerability and assigned |  |  |  |  |  |  |  |  |
| considering the mass body of Android source codes. For- | CVE-2019-2088 to us. So we do not give the mitigation here. |  |  |  |  |  |  |  |  |
| tions provided by | Parcel | , which perform input validations. | 5.4.3 | Case Study III: Stack Overflow Inside ip(6)tables- |  |  |  |  |  |
| Attack | The native system service | statsd | is a daemon in | the transaction | Call::WAKEUPADDINTERFACE | , then it calls |  |  |  |
| Android 9. In the transaction | Call::INFORMALLUIDDATA | , | wakeupAddInterface | . Finally it triggers the stack overflow |  |  |  |  |  |
| statsd | deserializes | three | vectors | from | data | par- | vulnerabilities in the | add_param_to_argv | function. |
| cel | containing | items | of | int32_t | , | int64_t | and | Figure 7 gives the detailed execution path. However, we |  |
| ::android::String16 | respectively. | These | vectors | still need to craft | in_ifName | carefully as the string is de- |  |  |  |
| are passed into | informAllUidData | and then forwarded to | serialized from | data | parcel through | readUtf8FromUtf16 |  |  |  |
| the | updateMap | method of | UidMap | . Function | updateMap | which executes many checks. To take the last step towards |  |  |  |
| iterates on the three vectors in a loop. The size of vector | uid | successful attack, FANS tags | in_ifName | with | utf8=true |  |  |  |  |
| out of the three is used as the loop count. Since items in any | when extracting the interface model. Later FANS uses the |  |  |  |  |  |  |  |  |
| one vector are supposed to have a one-to-one correspondence | corresponding serialization method | writeUtf8AsUtf16 | to |  |  |  |  |  |  |
| to those in the other two vectors, the three vectors are | serialize | in_ifName | into | data | , which can pass the sanity |  |  |  |  |
| expected to have the same length, so that the iteration | checks. In contrast, BinderCracker [6] may well miss such |  |  |  |  |  |  |  |  |
| can work normally. Nevertheless, this requirement is left | transactions because popular apps rarely use them. Even if it |  |  |  |  |  |  |  |  |
| unchecked. Out-of-bound access can then be achieved by | could get such a transaction input format, it would randomly |  |  |  |  |  |  |  |  |
| passing in a longer vector of | uid | than the rest two. In order | mutate the traffic which is likely to fail quickly in the checks |  |  |  |  |  |  |
| USENIX Association | 29th USENIX Security Symposium | 319 |  |  |  |  |  |  |  |

---

## Page 15

| Insight | This vulnerability crosses three processes: attacker | experiment, we found that a smartphone can enter into re- |  |  |  |
| --- | --- | --- | --- | --- | --- |
| process, | netd | and | ip(6)tables-restore | . In other words, | covery mode even just after starting the fuzzer ten minutes. |
| this bug is buried deep. Furthermore, although we mainly | As a result, we needed to flash the phone manually, which |  |  |  |  |
| focus on fuzzing Android native system services, we find a | significantly affects the efficiency of FANS. We think this can |  |  |  |  |
| vulnerability in a Linux component. It suggests that there is a | be solved, either limiting the privilege of fuzzer or finding a |  |  |  |  |
| close relationship between Android system services and basic | way to flash the device automatically. |  |  |  |  |

Linux components. In the light of this, we can assert that there

is another way to fuzz Linux components. Besides, these two

bugs are also present in iptable package and can be found

on a regular Linux distribution. They have been fixed by the

netfilter team in April 2019 and assigned CVE-2019-11360.

So here we do not give the mitigation. However, at the time

of writing this paper, they have not been fixed in Android.

a linked list, the loop size is undetermined, not as we guess. In

such circumstances, we believe that it is not easy to improve

it. Besides, even if a developer defines a semantic type some-

where, he might accidentally use the original type instead of

the type alias. Thus we can not get a more semantic variable

type, which would also affect the variable dependency gener-

ation. Other than those mentioned above, the dependency we

got might be incomplete because there might exist specific

order between the transaction calls as service can be seen as

a state machine. However, as we are fuzzing, if we always

follow the specified order, we may miss some vulnerabili-

ties. Meanwhile, we have already found some vulnerabilities

caused by incomplete state machine processing in service.

Interface-based Fuzzing in Android In Android 9, there

mainly exists three kinds of services located in different do-

mains: normal domain, vendor domain and hardware domain.

In Pixel series products, applications can access only normal

domain services registered in the service manager. In this pa-

per, we mainly pay attention to the native system services in

normal domain. However, these three kinds of services share

terface implementation. Consequently, we could easily trans-

terfaces, which do not belong to the parts mentioned above.

7 Related Work

IPC and Service Security in Android While the security

of the Android operating system has always been the focus

of academic and industrial research, similar researches for

IPC and system services are deficient. In early times, vul-

nerable Intents were widely exploited in attacking userland

applications. Therefore, the main target of the previous re-

searches [2, 11, 16] on IPC in Android was the Intent.

Gong [7] is the first one who paid attention to the Binder

IPC interface. He pointed out Binder is the actual security

boundary of Android system services, and proved it inse-

cure by discovering critical vulnerabilities manually. Wang

to understand the input model and transaction dependencies

| 6 | Discussion | the same architecture in the aspect of communication and in- |
| --- | --- | --- |
| We have demonstrated FANS’s effectiveness in excavating | fer the method demonstrated in this paper to other domain |  |
| vulnerabilities in the Android native system service. Now we | services, even service implemented in Java language. Besides, |  |
| discuss its limitations and what we will do in the future. | there also exist some similar interfaces, i.e., customized in- |  |
| Interface Model Accuracy | Although we have tried our | These interfaces are designed to be implemented and instan- |
| best to extract the interface models, the interface model is | tiated by applications and passed to the server-side by the |  |
| not perfect. For example, we assume that the loop size is the | clients. We can also fuzz these implementations with the |  |
| previous variable before the loop when we can not get the | methods proposed in this paper. The major drawback is that |  |
| loop size directly. However, for loop statements that traverse | we need to instantiate these interfaces manually. |  |
| Coverage Guided Fuzzing | Nowadays, coverage guided | et al. [12] further proposed a solution to fuzz Java interfaces |
| fuzzing is popular. For FANS, even though we do not use | generated from AIDL files, while Chizpurfle [10] targeted |  |
| coverage knowledge of Android native system services, we | vendor implemented Java services. Further, there are some |  |
| find many vulnerabilities in system services audited by many | researches [3,26] that focus on input validation vulnerabilities |  |
| experts. However, to our belief, guided with coverage, FANS | related to Android services. Several other researches [1, 8, 17] |  |
| can find more vulnerabilities. Moreover, as system service is | concentrate on the inconsistency of access control in the An- |  |
| state-sensitive, its coverage might be affected by inputs gen- | droid framework related to Android services. |  |
| erated previously or by other applications’ calls. This could | BinderCracker [6] extends the testing to native services. It |  |
| be a challenge when integrating coverage to FANS. | monitors the IPC traffic of several popular user apps, and tries |  |
| Fuzzing Efficiency | As some Android system services run | through the recorded traffic, then generates new test cases |
| as a daemon or might check the caller’s permission, for conve- | accordingly. However, this solution highly depends on the |  |
| nience, we run fuzzer as root. Nevertheless, the root privilege | diversity of the recorded traffic and is not effective. First, it |  |
| is very high, which can change lots of things. During the | cannot systematically recognize all interfaces including multi- |  |
| 320 | 29th USENIX Security Symposium | USENIX Association |

---

## Page 16

| level interfaces to test, and cannot recognize the complete | BNRist Network and Software Security Research Program |
| --- | --- |
| dependencies between interfaces, either. Second, the interface | under Grant BNR2019TD01004 and BNR2019RC01009. |

model and the transaction dependencies inferred from the

traffic are neither (1) complete, since the traffic may overlook

rarely-used transactions; nor (2) precise, since the inference is

made from data which has lost many information (e.g., types).

erally, they fall into two categories. Generation-based fuzzers

tation. Mutation-based fuzzers mutate existing test cases to

recent fuzzing tools [18, 24, 27], referred to as hybrid fuzzers,

In this work, FANS is designed to meet the challenges in

that FANS is also capable of inferring the complex depen-

pattern, type alias and variable dependency. We intermittently

We would like to thank all anonymous reviewers and our

Grant 61772308, 61972224, U1736209 and U1936121, and

References

[1] Yousra Aafer, Jianjun Huang, Yi Sun, Xiangyu Zhang,

Ninghui Li, and Chen Tian. Acedroid: Normalizing

and Privacy (SP) , pages 711–725. IEEE, 2018.

Fuzzer , 34, 2011.

[9] HyungSeok Han, DongHyeon Oh, and Sang Kil Cha.

find vulnerabilities in javascript engines. In NDSS , 2019.

2017.

| Fuzzing for Structured Input | Numerous approaches have | diverse android access control checks for inconsistency |  |  |
| --- | --- | --- | --- | --- |
| been proposed to generate structured input for fuzzing. Gen- | detection. In | NDSS | , 2018. |  |
| generates test cases from templates or predefined grammar. | [2] Paulo Barros, René Just, Suzanne Millstein, Paul Vines, |  |  |  |
| Peach [5] is one of the most popular fuzzer based on tem- | Werner Dietl, Michael D Ernst, et al. Static analysis of |  |  |  |
| plates. DomFuzz [15] utilized grammar to generate dom | implicit control flow: Resolving java reflection and an- |  |  |  |
| structures for the target program. These methods suffer man- | droid intents (t). In | 2015 30th IEEE/ACM International |  |  |
| ual participation and poor scalability. Thus more advanced | Conference on Automated Software Engineering (ASE) | , |  |  |
| researches [9, 20, 22, 23] are proposed to handle this limi- | pages 669–679. IEEE, 2015. |  |  |  |
| generate new ones without any input grammar or input model. | [3] Chen Cao, Neng Gao, Peng Liu, and Ji Xiang. Towards |  |  |  |
| VUzzer [14] runs dynamic taint analysis (DTA) to capture | analyzing the input validation vulnerabilities associated |  |  |  |
| common characteristics of valid inputs. TaintScope [21] uses | with android system services. | In | Proceedings of the |  |
| DTA to identify the checksum field. T-Fuzz [13] also bypasses | 31st Annual Computer Security Applications Confer- |  |  |  |
| sanity checks and fuzzes the guarded codes directly. Some | ence | , pages 361–370. ACM, 2015. |  |  |
| combine fuzzing with concolic execution. This may be a | [4] Peng Chen and Hao Chen. Angora: Efficient fuzzing by |  |  |  |
| promising way of fuzzing programs with structured inputs. | principled search. In | 2018 IEEE Symposium on Security |  |  |
| 8 | Conclusion | [5] Michael Eddington. | Peach fuzzing platform. | Peach |
| fuzzing Android native system services. Experiments have | [6] Huan Feng and Kang G Shin. Understanding and de- |  |  |  |
| validated its ability to automatically generate transactions and | fending the binder attack surface in android. | In | Pro- |  |
| invoke the corresponding interface, which greatly helps to | ceedings of the 32nd Annual Conference on Computer |  |  |  |
| fuzz Android native system services. Our evaluation shows | Security Applications | , pages 398–409. ACM, 2016. |  |  |
| dencies between these interfaces. Moreover, we discover that | [7] Guang Gong. Fuzzing android system services by binder |  |  |  |
| the interface model is very complex in three aspects: variable | call to escalate privilege. | BlackHat USA | , 2015, 2015. |  |
| ran FANS on our six smartphones for around 30 days and | [8] Sigmund Albert Gorski, Benjamin Andow, Adwait Nad- |  |  |  |
| reported 30 native vulnerabilities to Google, of which 20 have | karni, Sunil Manandhar, William Enck, Eric Bodden, |  |  |  |
| been confirmed. These vulnerabilities imply that without a | and Alexandre Bartel. Acminer: Extraction and analysis |  |  |  |
| precise interface model, we could not fuzz Android native sys- | of authorization checks in android’s middleware. | In |  |  |
| tem services deeply. Surprisingly, 138 Java exceptions were | Proceedings of the Ninth ACM Conference on Data and |  |  |  |
| also exposed, which may deserve further study. | Application Security and Privacy | , pages 25–36, 2019. |  |  |
| Acknowledgement | Codealchemist: Semantics-aware code generation to |  |  |  |
| shepherd, Dr. Manuel Egele, for their valuable feedback that | [10] Antonio Ken Iannillo, Roberto Natella, Domenico Cotro- |  |  |  |
| greatly helped us improve this paper. Besides, we would like | neo, and Cristina Nita-Rotaru. Chizpurfle: A gray-box |  |  |  |
| to thank Xingman Chen, Kaixiang Chen, Zheming Li for | android fuzzer for vendor service customizations. | In |  |  |
| revising the draft of this paper. This work was supported in | 2017 IEEE 28th International Symposium on Software |  |  |  |
| part by National Natural Science Foundation of China under | Reliability Engineering (ISSRE) | , pages 1–11. IEEE, |  |  |
| USENIX Association | 29th USENIX Security Symposium | 321 |  |  |

---

## Page 17

[11] Fauzia Idrees and Muttukrishnan Rajarajan. Investi- IEEE Symposium on Security and Privacy (SP) , pages

gating the android intents and permissions for malware 579–594. IEEE, 2017.

detection. In 2014 IEEE 10th International Conference

fuzzing test for dynamic vulnerability detection on an-

[13] Hui Peng, Yan Shoshitaishvili, and Mathias Payer. T-

fuzz: fuzzing by program transformation. In 2018 IEEE

[14] Sanjay Rawat, Vivek Jain, Ashish Kumar, Lucian Co-

jocar, Cristiano Giuffrida, and Herbert Bos. Vuzzer:

Application-aware evolutionary fuzzing. In NDSS , vol-

ume 17, pages 1–14, 2017.

[15] Jesse Ruderman. Releasing jsfunfuzz and domfuzz,

2015.

crafting intents of death. In Proceedings of the 2014

Joint International Workshop on Dynamic Analysis

ACM, 2014.

[18] Nick Stephens, John Grosen, Christopher Salls, Andrew

execution. In NDSS , volume 16, pages 1–16, 2016.

[19] Dmitry Vyukov. Syzkaller, 2015.

fire: Data-driven seed generation for fuzzing. In 2017

for automatic software vulnerability detection. In 2010

512. IEEE, 2010.

vulnerability discovery. In 2019 IEEE Symposium on

Security and Privacy (SP) , pages 769–786. IEEE, 2019.

Semantics-based automatic generation of proof-of-

concept exploits. In Proceedings of the 2017 ACM

SIGSAC Conference on Computer and Communications

Security , pages 2139–2154. ACM, 2017.

[24] Insu Yun, Sangho Lee, Meng Xu, Yeongjin Jang, and

Taesoo Kim. { QSYM } : A practical concolic execution

engine tailored for hybrid fuzzing. In 27th { USENIX }

745–761, 2018.

[26] Lei Zhang, Zhemin Yang, Yuyu He, Zhenyu Zhang,

pages 1165–1178. ACM, 2018.

A Appendix

| on Wireless and Mobile Computing, Networking and | [21] Tielei | Wang, Tao | Wei, Guofei | Gu, and Wei | Zou. |  |
| --- | --- | --- | --- | --- | --- | --- |
| Communications (WiMob) | , pages 354–358. IEEE, 2014. | Taintscope: A checksum-aware directed fuzzing tool |  |  |  |  |
| [12] Wang Kai, Zhang Yuqing, Liu Qixu, and Fan Dan. A | IEEE Symposium on Security and Privacy | , pages 497– |  |  |  |  |
| droid binder mechanism. In | 2015 IEEE Conference on | [22] Wei You, Xueqiang Wang, Shiqing Ma, Jianjun Huang, |  |  |  |  |
| Communications and Network Security (CNS) | , pages | Xiangyu Zhang, XiaoFeng Wang, and Bin Liang. Pro- |  |  |  |  |
| 709–710. IEEE, 2015. | fuzzer: On-the-fly input type probing for better zero-day |  |  |  |  |  |
| Symposium on Security and Privacy (SP) | , pages 697– | [23] Wei You, Peiyuan Zong, Kai Chen, XiaoFeng Wang, |  |  |  |  |
| 710. IEEE, 2018. | Xiaojing Liao, Pan Bian, and Bin Liang. | Semfuzz: |  |  |  |  |
| [16] Raimondas Sasnauskas and John Regehr. Intent fuzzer: | Security Symposium ( | { | USENIX | } | Security 18) | , pages |
| (WODA) and Software and System Performance Test- | [25] Michal Zalewski. | American | fuzzy lop. | URL: |  |  |
| ing, Debugging, and Analytics (PERTEA) | , pages 1–5. | http://lcamtuf. coredump. cx/afl | , 2017. |  |  |  |
| [17] Yuru Shao, Qi Alfred Chen, Zhuoqing Morley Mao, | Zhiyun Qian, Geng Hong, Yuan Zhang, and Min Yang. |  |  |  |  |  |
| Jason Ott, and Zhiyun Qian. | Kratos: Discovering in- | Invetter: Locating insecure input validations in android |  |  |  |  |
| consistent security policy enforcement in the android | services. | In | Proceedings of the 2018 ACM SIGSAC |  |  |  |
| framework. In | NDSS | , 2016. | Conference on Computer and Communications Security | , |  |  |
| Dutcher, Ruoyu Wang, Jacopo Corbetta, Yan Shoshi- | [27] Lei Zhao, Yue Duan, Heng Yin, and Jifeng Xuan. Send |  |  |  |  |  |
| taishvili, Christopher Kruegel, and Giovanni Vigna. | hardest problems my way: Probabilistic path prioritiza- |  |  |  |  |  |
| Driller: Augmenting fuzzing through selective symbolic | tion for hybrid fuzzing. In | NDSS | , 2019. |  |  |  |
| [20] Junjie Wang, Bihuan Chen, Lei Wei, and Yang Liu. Sky- | A.1 | Full Interface Dependency Graph |  |  |  |  |
| 322 | 29th USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 18

I IA

IUpdateEngineCallback IUpdateEngine

IDrmServiceListener IDrmManagerService

IResourceManagerClient IResourceManagerService

IClientInterface

IWificond

IInterfaceEventCallback IPnoScanEvent IWifiScannerImpl

IScanEvent

IApInterface IIncidentReportStatusListener IIncidentManager

IApInterfaceEventCallback

IShellCallback IStatsManager

IAppOpsCallback IAppOpsService

IPerfProfd

IVoldListener

IResultReceiver IGpuService

IVold

IVoldTaskListener ISensorServer

ISensorEventConnection

IBinder

IStatsCompanionService

IProducerListener

IKeystoreService

IRemoteDisplay

IRemoteDisplayClient IAudioPolicyService

IMediaPlayerService IMediaCodecList IAudioPolicyServiceClient

IMediaPlayerClient

ISurfaceComposer IDisplayEventConnection

IMediaHTTPService

IStreamSource

IMediaMetadataRetriever IMediaPlayer

ISurfaceComposerClient

ICameraRecordingProxy IGraphicBufferProducer

IMediaRecorder

ISoundTrigger

IMediaRecorderClient ISoundTriggerClient ISoundTriggerHwService

IDrmClient

IDrm

IDataSource

IMediaExtractorService IMediaExtractor IMediaSource IMediaDrmService

IMemory ICrypto

IAudioTrack

IMemoryHeap

IEffectClient

IAudioFlinger IAudioRecord ICamera

IAudioFlingerClient IEffect

ICameraService ICameraDeviceUser

ICameraClient

ICameraServiceListener

ICameraDeviceCallbacks

Use

Legend

Generation

IThermalService

IThermalEventListener

IAAudioClient IAAudioService

IUpdateEngine

IUpdateEngineCallback

IDrmServiceListener IDrmManagerService

IClientInterface

IPnoScanEvent IWifiScannerImpl

IScanEvent

Figure 8: Full Interface Dependency Graph

IApInterface IIncidentReportStatusListener IIncidentManager

IShellCallback IStatsManager

IAppOpsCallback IAppOpsService

IPerfProfd

IResultReceiver IGpuService

ISensorServer

ISensorEventConnection

IBinder

IStatsCompanionService

IProducerListener

IKeystoreService

IRemoteDisplay

IRemoteDisplayClient IAudioPolicyService

iaPlayerService diaCodecList udioPolicyServiceClient

USENIX Association 29th USENIX Security Symposium 323

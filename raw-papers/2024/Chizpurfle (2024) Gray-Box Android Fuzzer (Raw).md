---
title: "22_Iannillo_et_al.,_Chizpurfle_Gray-Box_Android_Fuzzer"
creator: "TeX"
pages: 12
---

# 22_Iannillo_et_al.,_Chizpurfle_Gray-Box_Android_Fuzzer

> **總頁數**：12 頁

---

## Page 1

Chizpurfle: A Gray-Box Android Fuzzer

for Vendor Service Customizations

Antonio Ken Iannillo ∗ , Roberto Natella ∗ , Domenico Cotroneo ∗ , Cristina Nita-Rotaru †

∗ Universit` a degli Studi di Napoli Federico II, Naples, Italy † Northeastern University, Boston, USA

∗ { antonioken.iannillo, roberto.natella, cotroneo } @unina.it † c.nitarotaru@neu.edu

Abstract —Android has become the most popular mobile OS, Fuzzing is a well-established and effective software testing

as it enables device manufacturers to introduce customizations technique to identify weaknesses in fragile software inter-

to compete with value-added services. However, customizations faces by injecting invalid and unexpected inputs. Fuzzing was

make the OS less dependable and secure, since they can introduce

source code and the services cannot be run on a device emulator.

Chizpurfle has been designed to run on an unmodified Android

services.

Index Terms —Android OS; robustness testing; fuzzing; vendor

Android comes in different flavors, depending on which

vendor is implementing it. Nowadays, more than 20 original

equipment manufacturers (OEMs), including but not limited

to Samsung, HTC, Huawei, Motorola, and LG, base their

devices on the Android Open Source Project (AOSP). Hard-

ware capabilities are not the only factor that support the

customers’ choice. Software customizations play a key role in

this aspect, making user experience unique and more enjoy-

able. For example, vendor customizations include services for

providing mobile personal assistants [1]–[3], advanced photo

enhancement [4], [5], mobile payments [6], etc .

than the core AOSP codebase, and their vulnerabilities take

For example, recent devices based on Qualcomm chipsets suffer from a

code or by running the target code in a virtual machine

tools are not applicable to proprietary Android services, since

virtual machine environments ( e.g. , device emulators) do not

In this paper, we introduce a novel “gray-box” tool, named

Chizpurfle , to address the gap in the spectrum of mobile

fuzzers, and to improve the effectiveness of fuzzing on vendor

customizations. Similarly to recent white-box fuzz approaches,

Chizpurfle leverages test coverage information, while avoiding

the need for recompiling the target code, or executing it in a

special environment. The tool has been designed to be de-

ployed and run on unmodified Android devices, including any

vendor customization of the Android OS. The tool leverages

a combination of dynamic binary instrumentation techniques

(such as software breakpoints and just-in-time code rewriting)

to obtain information about the block coverage. Moreover,

feedback.

software flaws. Such flaws can be found by using fuzzing, a initially conceived as a “black-box” testing technique, using

popular testing technique among security researchers. random or grammar-driven inputs [12]. More recently, “white-

This paper presents Chizpurfle , a novel “gray-box” fuzzing box” techniques have been leveraging information about the

tool for vendor-specific Android services. Testing these services program internals (such as the test coverage) to steer the

is challenging for existing tools, since vendors do not provide generation of fuzz inputs, either by instrumenting the source

OS on an actual device. The tool automatically discovers, fuzzes, [13], [14]. The visibility of the test coverage has dramatically

and profiles proprietary services. This work evaluates the appli- improved the effectiveness of fuzzing tools, as showed by

cability and performance of Chizpurfle on the Samsung Galaxy the high number of subtle vulnerabilities found in many

S6 Edge, and discusses software bugs found in privileged vendor large software systems [13], [15], [16]. Unfortunately, these

customizations. vendors are not willing to share their source code, and since

I. I NTRODUCTION support the execution of these proprietary extensions.

Unfortunately, these customizations often introduce new Chizpurfle is able to guide fuzz testing only on the vendor

software defects, which are vendor-specific. Because they are customizations, by automatically extracting the list of vendor

proprietary, vendor customizations are not integrated in the service interfaces on an Android device. The tool also provides

open-source Android and do not benefit from the feedback a platform for experimenting with fuzz testing techniques

loop of the whole ecosystem. Thus, they are less scrutinized (such as evolutionary algorithms) based on coverage-based

significantly more time to be patched: for example, the Google We validated the applicability and performance of the

Android security team publishes a monthly security bulletin Chizpurfle tool by conducting a fuzz testing campaign on

[7] with new and patched security vulnerabilities, but it has to the vendor customizations of the Samsung Galaxy S6 Edge,

refer the users to vendor-specific security bulletins such as the running Android version 7. We found that Chizpurfle improves

ones by LG [8], Motorola [9], and Samsung [10]. It is worth the depth of testing compared to the black-box approach, by

noting that vendors customizations consist of code running increasing the test coverage by 2.3 times on average and 7.9

with special privileges, thus exacerbating the security issues 1 . times in the best case, with a performance overhead that is

1 comparable to existing dynamic binary instrumentation frame-

vulnerability in the Qualcomm service API that allows privilege escalation works. Moreover, we discuss two bugs found in privileged

and information disclosure [11]. services during these evaluation experiments.

---

## Page 2

| The rest of this paper is structured as follows. Background | TABLE I |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and motivations for this work are discussed in Section II. | V | ENDORS | ’ S | MARTPHONE | C | USTOMIZATIONS ON | S | YSTEM | S | ERVICES |
| Previous related work and tools are discussed in Section III. | Huawei | HTC | Samsung |  |  |  |  |  |  |  |
| The design of Chizpurfle is described in Section IV, while its | P8 | One | Galaxy S6 |  |  |  |  |  |  |  |

evaluation is presented in Section V. Finally, conclusions and

II. B ACKGROUND AND M OTIVATION

open source software stack from the Android Open Source

Project (AOSP). Unlike AOSP, customizations are usually

• System services : they enhance the Android OS with ad-

ditional APIs for both stock and third-party applications.

We focus on the third type of customizations, i.e. , system

| Lite | M9 | Edge |  |
| --- | --- | --- | --- |
| # new services | 30 | 7 | 82 |
| # new C services | 13 | 2 | 20 |
| # extended Java services | 15 | 25 | 52 |

fuzzing tools.

III. R ELATED W ORK

| future work conclude the paper in Section VI. | Android version | 5.0 | 6.0 | 7.0 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| When a vendor delivers a new smartphone on the market, | # new Java services | 17 | 5 | 62 |  |  |
| it includes several customizations of the | vanilla | Android, the | # new Java methods | 325 | 166 | 2,272 |

closed source and undocumented, and vary among vendors. testing needs to guide the generation of inputs according to test

Vendors’ software customizations are focused on three areas: coverage, as demonstrated by empirical experience in several

• Device drivers : they support proprietary hardware com- security-critical contexts [13], [15], [16]. However, the lack of

ponents of the smartphone; source code for proprietary services, and the inability to run

• Stock applications : they are pre-installed on the smart- these proprietary extensions on a device emulator, defy the

| phone along with the default AOSP stock applications; | strategies for profiling coverage that are adopted by existing |
| --- | --- |
| services, because they usually run as privileged processes | This section gives an overview of previous work in the gen- |

(thus, they have a major potential impact on robustness and eral area of fuzzing, and discusses how Chizpurfle improves

security); they are directly exposed to (potentially buggy and over existing tools for mobile device fuzzing.

malicious) user applications; they provide wrappers to lower- OS and systems software fuzzing. Since its initial years,

level interfaces, such as device drivers; and they represent a fuzz testing has been extensively adopted for testing systems

large part of vendor customizations. software, such as network servers, shell applications, libraries,

In order to understand the extent of deployment of vendor and OS kernels. The early study by Miller et al. on fuzzing

customizations, we conducted a preliminary analysis of system UNIX system utilities [12], by injecting random inputs through

services from vendor customizations in three commercial their command line interface and standard input stream, found

smartphones, namely the HTC One M9, the Huawei P8 Lite, a surprisingly high number of targets that experienced crashes,

and the Samsung Galaxy S6 Edge. We extracted the services leaks and deadlocks, even when exposed to apparently trivial

interfaces on the three devices and on their corresponding (but invalid) inputs. Other approaches for OS robustness

Android AOSP versions, using the same techniques of the testing, such as BALLISTA [17], MAFALDA [18], and the

Chizpurfle tool (that are further discussed in § IV-B), and DBench project [19] injected invalid inputs by bit-flipping

compared the two lists. them or replacing them with “difficult” inputs, or forced the

TABLE I reports the results of this analysis. The first row is failure of kernel APIs and device drivers [20], [21].

the version of the Android Platform running on each device. Among the most modern and mature fuzzing tools, Ameri-

The second row is the number of services found only on the can Fuzzy Lop (AFL) is well-known for having found notable

device, but not in the corresponding AOSP; in the third and vulnerabilities in dozens of popular libraries and applications

forth rows, this number is split between Java and C services. [13]. AFL is an “instrumentation-guided genetic fuzzer”,

The next two rows refer only to the Java-implemented services, which modifies the target program at compile-time in order

of which we could retrieve the methods signatures through to efficiently profile the branch coverage during the execution

Java Reflection. The fifth row considers the common Java of the tests, and to communicate with the main AFL process.

services, present in both AOSP and vendor devices, that have Based on coverage measurements, AFL iteratively improves

new methods in the vendor version. Finally, the last row shows the quality of fuzz inputs, by mutating the previous inputs that

how many new methods are present in the vendor services discovered new paths. AFL has also been extended to avoid

that do not exist in the AOSP. Our analysis shows that there compile-time instrumentation, by using the QEMU virtual

is a significant number of customized services and vendor- machine to trace the instructions executed by the target (at

specific methods. Moreover, most of these services execute the cost of higher run-time overhead and of the additional

in the context of privileged processes (such as system server , dependency on a virtual machine emulator). Another example

media server , etc. ), where any failure can have a severe impact of coverage-guided fuzzer is syzkaller [22], which also uses

the whole OS. QEMU and compile-time instrumentation to fuzz the whole

The large vulnerability surface and high privilege of pro- Linux kernel through its system call interface.

prietary services motivate the need for specialized tools to Another significant advance has been represented by white-

evaluate their robustness. To achieve its full potential, fuzz box fuzzing techniques that leverage symbolic execution. The

---

## Page 3

ANDROID DEVICE

| METHOD | FUZZ INPUT |  |
| --- | --- | --- |
| SEED MANAGER | TEST EXECUTOR | OUTPUT ANALYZER |
| EXTRACTOR | GENERATOR |  |

INSTRUMENTATION

MODULE STORAGE

SYSTEM SERVICE

ORCHESTRATOR

Fig. 1. Overview of the Architecture of Chizpurfle.

most well-known is KLEE [14], a virtual machine envi- To the best of our knowledge, the few notable studies on

ronment, based on the LLVM compiler infrastructure, with fuzzing Android system services are the ones by Cao et al.

a symbolic state for every memory location ( i.e., boolean [33] and Feng et al. [34]. Cao et al. [33] focus on the input

conditions that must hold at a given point of the execution) validation of Android system services. Their tool, Buzzer ,

that is updated as code is executed by an interpreter. When sends crafted parcels (i.e., the basic messages on the Binder)

KLEE encounters a branch condition, it forks in two execution to invoke AOSP system services with fuzzed arguments. Since

flows, each with a different constraint on the variables involved Buzzer was an early tool of its kind, it relied on manual

in the branch condition. When a failure path is found, a efforts for several tasks, such as to identify the arguments of

constraint solver is used to find an input that fulfills all the service methods, to avoid fuzzing on methods that could not be

conditions on that path. SAGE [23] is another well-known invoked by third-party apps anyways (due to limited permis-

fuzzing tool by Microsoft: starting from some (tentative) sions), etc. . Feng et al. [34] developed BinderCracker , a more

concrete input, the tool traces the program execution using a sophisticated parameter-aware fuzzer that can automatically

record&replay framework [24] to identify the path constraints understand the format of Binder messages and that supports

for the input; then, it negates one of these constraints, and more complex communication patterns over the Binder (such

uses a constraint solver to generate inputs to cover the new as callback objects returned by system services). However,

conditions. It is important to note that white-box fuzzing is both these tools are purely black-box approaches and do not

extremely powerful, but very resource-consuming due to the gather any information about the internal coverage of the tested

overhead of constraint solving and to the exponential explosion services, thus missing the opportunity to improve the efficiency

of program paths. Thus, these techniques are best applied in of fuzzing. This problem has only been partially addressed

combination with black-box fuzzing: Bounimova et al. [15] by Luo et al. [35], which recently developed a successor of

report a split of 66%-33% of bugs found respectively by black- Buzzer that exploits symbolic execution. However, this tool is

and white-box fuzzing during the development of Microsoft’s not applicable to vendor customizations, since it is designed

Windows 7. Moreover, white-box fuzzing can only be applied to run outside the Android system and requires the availability

when the target is executed in an environment (such as a virtual of the target source code.

machine) able to trace and to fork symbolic states.

IV. T OOL D ESIGN

Android fuzzers. In Android-related research, fuzzing has

been extensively used to attack network and inter-process The Chizpurfle tool architecture is presented in Fig. 1. It

interfaces. For example, Mulliner and Miller [25] found severe includes six software modules running on the target Android

vulnerabilities in the SMS protocol. Droidfuzzer [26] targets device, that are implemented in Java and C. These modules

Android activities that accept MIME data through Intents (a cooperate to profile the target system service and to generate

higher-level IPC mechanism based on Binder); Sasnauskas fuzz inputs according to test coverage. We designed Chizpurfle

and Regehr [27] developed a more generic Intent fuzzer that to be as less intrusive as possible, and to only require root

can mutate arbitrary fields of Intent objects. Mahmood et al. permissions for few debug operations discussed in this section.

[28] adopted the white-box fuzzing approach by decompiling The Methods Extractor produces a list of system services

Android apps to identify interesting inputs and running them and their methods, marking the custom vendor services as

on Android emulator instances on the cloud. However, these described in Section II. It also provides a map between services

and similar tools [29]–[32] focus on the robustness of Android and their hosting processes. The Seed Manager iterates over

apps, and can not be directly applied to fuzz Android system the custom vendor services and methods, and it provides initial

services. inputs ( seeds ) for testing them. The Fuzz Input Generator

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

---

## Page 4

takes a seed (either the initial seed, or any previous worthwhile

of the test coverage. The outcomes of the test are collected,

feedback to the Seed Manager with seeds for the next test

iteration. Finally, the Orchestrator provides a simple user

A. Orchestrator

The Orchestrator is the only part of Chizpurfle that runs

outside the target Android device ( i.e., on the user’s work-

station), that loads and controls the other modules using

the Android Debug Bridge (ADB) [36] through an USB

connection. Chizpurfle minimizes the amount of interactions

through ADB, since this connection is notoriously unstable,

processes, and which provides a pristine copy of the Android

utility (the same utility that starts Zygote at boot). This enables

Chizpurfle to keep working and gather data even if key system

processes fail due to vulnerabilities in vendor customizations.

The Method Extractor gets the list of services from the

Service Manager in a vendor-customized Android device, and

SERVICE

SYSTEM CE

SERVICE JAVA (AOSP or JAVA CLIENT

kernel

1

3

BINDER DRIVER

Fig. 2. Android Services and Service Manager.

for testing.

invocations of the function:

static int

svc_can_register(const uint16_t *name,

pid_t spid,

uid_t uid)

| input) and generates new actual inputs for the target method, | MANAGER | SERVI | SERVI |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| by applying fuzzing operators to the values of method param- | SERVI | CE | SERVI |  |  |  |  |  |
| eters. Then, the | Test Executor | applies the fuzzed inputs to the | JAVA | SERVICE | CE | JAVA | SERVICE | CE |
| target service, while the | Instrumentation Module | keeps track | LIST | VENDOR) |  |  |  |  |
| analyzed, and saved by the | Output Analyzer | . It also provides | userspace |  |  |  |  |  |
| interface for | Chizpurfle | . | 2 | 4 |  |  |  |  |
| and we could not rely on it due to potential side effects of | The | Method Extractor | queries the Service Manager on the |  |  |  |  |  |

fuzzing. Thus, Chizpurfle is detached from the ADB shell target device to get the list of all registered services, including

process right after it is started, in order to avoid any issue customizations. By iterating on these names, it retrieves the list

related to the ADB connection. Test data are recorded on a of service descriptors. In case of Java-implemented services

local file on the device and later pulled from the target device (supported by the current version of the tool), a service

by the Orchestrator ; the Orchestrator periodically checks the descriptor is the string name of the Java Interface that is im-

progress of fuzz tests by briefly connecting with ADB and plemented by that system service ( e.g., the Package Manager

inspecting the logs of Chizpurfle . service implements the android.content.pm.IPackageManager

We also need to prevent the early termination of Chizpurfle Java Interface). Then, Java Reflection API is used to inspect

in the case of crashes of system processes. If Chizpurfle ran as the definition of the interfaces, and to get the signatures of

a standard Android app, it would be bound to Zygote , which the methods in the service. The methods that are not in the

is a daemon process that serves as parent for all Android AOSP are marked as “vendor customizations” and considered

Runtime environment for its children through copy-on-write Another task of the Method Extractor is to map every

mechanism. When the Zygote dies, all children processes die service to the system process that hosts that service. This

as well. Thus, we run Chizpurfle modules in a distinct Android mapping is obtained by hooking calls to the Service Manager,

Runtime from the Zygote , that is launched by the app process before the services are registered. In particular, we focus on

B. Method Extractor size_t name_len,

it compares them with a blueprint of the AOSP with the same where spid is the PID of the process that wants to register

Android version. the service named name . The functions of Service Manager

The Android OS provides a service-oriented architecture are hooked by copying a breakpoint handler in the memory

to manage its several services, as shown in Fig. 2. At boot address space of the process and by modifying the symbol

time , 1 the Service Manager registers itself as the “context table to hijack function invocations (the technique to modify

manager”, by sending a special message to the Binder driver, the memory of the target process is further discussed in the

which is the main inter-process communication mechanism next subsection about the Instrumentation Module ). We force

provided by the Linux kernel of Android. Then, 2 a service the system services to be published again (thus invoking the

provider publishes its services by sending a message through Service Manager) by restarting the Zygote process, which in

the Binder driver to the Service Manager. When a client turn forces the restart of system processes and their services.

application wants to contact a service, 3 it first queries the If the method returns 1 , then the service has been correctly

Service Manager with the service name, and then 4 it invokes registered, and the Methods Extractor retrieves the name of

the service directly through Binder. the process and saves the mapping.

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

*[Image: Page 4 Image]*

---

## Page 5

C. Instrumentation Module CHIZPURFLE TARGET PROCESS

The Instrumentation Module interacts with the process that

by taking into account the following requirements: (1) it must

service, in order to identify any new code block covered by the

test; (2) it has to attach to system processes that are already

vendors’ ones) cannot be directly controlled by external tools

such as Chizpurfle , and since most of these service are already

running since the boot of the target device; and (3) it should

be able to instrument proprietary services on the actual device

(which is the goal of this study), thus excluding any approach

that recompiles the source code or that runs in an emulated

environment.

to measure coverage. Hardware solutions typically take advan-

tage of special CPU features for debugging purposes, such as

performance counters. The ARM processors (the CPU family

also adopted in Android devices) provide the CoreSight on-

chip trace and debug utility to trace the execution of program

[37]. However, this specific feature is not mandatory for ARM

CPUs, and it is not available on the CPUs typically used in

Android devices. Thus, we could not use the hardware support

from the CPU, since this solution could not be applied on

commercial devices.

We then focused on software-based solutions, which typ-

ically have a higher run-time overhead, but they can also

provide more flexibility and have less requirements about the

underlying hardware. In particular, we based our design on the

ptrace system call of the Linux kernel: it allows a debugger

process (in our context, the Instrumentation Module ) to inspect

and to write on the memory address space and CPU registers

of the debuggee (in our context, the process that runs the

target system service). Typically, debugging tools use ptrace

to install software breakpoints , by replacing an instruction of

the debugged program with another instruction that stops the

program and triggers a breakpoint handler function.

the exit branch is reached, the control flow is returned to

the interpreter, which retrieves the next basic block, applies

some transformations (such as just-in-time compilation and

INSTRUM.

SERVER

FOLLOW

for each test

for each block

BLOCK

ADDRESS

STOP

ADDRESSES

the target process a small C library by using ptrace; then,

before restoring the execution of the traced process, it starts a

new thread in the process to run the library code, which starts

the “stalker” server. This server opens a local socket to talk

back with the Instrumentation Module . At the beginning of a

test campaign, Chizpurfle sends a message over this socket to

enable the tracing of any thread in the target process. Then,

the stalker server rewrites the current code block; from this

point on, the code blocks will return the control flow to the

injected library, which will rewrite the next code block that

will be executed by the target. For every rewritten block, the

tool adds instructions to log the memory address of the code

block, in order to record that the block has been covered. The

list of the addresses of covered code blocks is collected by the

stalker server in a global data structure. At the end of testing,

Chizpurfle sends a message to disable logging, and to let the

stalker send back to Chizpurfle the list of code blocks that

have been covered.

In the current version of Chizpurfle , we implemented this

approach using the Frida framework [38]. Frida is a generic

dynamic instrumentation toolkit that provides basic facilities

of code blocks.

D. Seed Manager

| runs the target service, in order to collect information about | MODULE | PROCESS |  |  |
| --- | --- | --- | --- | --- |
| the test coverage. We designed the | Instrumentation Module | INJECT | STALKER | THREAD |
| be able to intercept the execution of branches by the target | INJECT |  |  |  |
| running, since the life cycle of Android services (including | START | REWRITE |  |  |
| We initially explored both hardware and software solutions | Fig. 3. | Chizpurfle Instrumentation and Tracing Mechanism. |  |  |

We leverage the ptrace mechanism to profile the target for dynamic binary rewriting, in order to let developers

code through dynamic binary rewriting , which is a general to insert probes in a program for debugging and reverse-

technique used by virtual machine interpreters. The program engineering purposes. We have ported Frida to 64-bit ARM

is divided in basic blocks , which are small groups of se- processors in order to let it run on actual Android devices, and

quential machine instructions that end with a branch. When we extended the code rewriting process to trace the coverage

instrumenting the final branch instruction) and moves the The Seed Manager is in charge of providing seeds ( i.e., ini-

control flow to the block; or the exit branch directly jumps tial inputs for the target service) to the Fuzz Input Generator .

to the next basic block if it has already been processed and The Seed Manager manages a priority queue of seeds to be

cached. In our context, we apply the same principle to keep fuzzed, which are ordered with respect to their score π . This

track of which code blocks are executed, in order to compute score is assigned by the Output Analyzer (as discussed later

the test coverage. in § IV-G), after that the seed has been submitted to the target,

Fig. 3 shows the instrumentation and tracing mechanism and that the coverage for the input has been measured. The

used by Chizpurfle . The Instrumentation Module injects into score π represents the number of new blocks executed by the

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

---

## Page 6

traced process. If π is greater than zero, the seed is fed back We implemented in Chizpurfle a rich library of fuzz operators,

to the Seed Manager to be further fuzzed in subsequent tests. including operators that are often adopted in existing fuzzing

This workflow represents the cornerstone for applying evo- tools (including the ones in Section III). For each parameter

lutionary algorithms to drive fuzz testing towards deeper type, the fuzz operators are:

| testing of the target service. To select the next seed from | • | Primitive types | (boolean, byte, char, double, float, integer, |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the priority queue, we adopt an exploitation-based constant | long, | short): | substitute | with | a | random | value, | substi- |
| schedule, where a seed is not used more than once [39]. | tute with the additive identity (0), substitute with the |  |  |  |  |  |  |  |
| The termination criterion of | Chizpurfle | is to stop when all | multiplicative identity (1), substitute with the maximum |  |  |  |  |  |
| seeds have been consumed from the queue, and no more | value, substitute with the minimum value, add a random |  |  |  |  |  |  |  |
| seeds are available for further fuzzing. Moreover, | Chizpurfle | delta, subtract a random delta, substitute with a special |  |  |  |  |  |  |
| represents a basis for applying several algorithms for fuzz | character (only for char); |  |  |  |  |  |  |  |
| testing, e.g., by changing or tuning the queue scheduling policy | • | Strings | : substitute with a random string, substitute with |  |  |  |  |  |
| and the termination criterion. This is a valuable opportunity | a very long random string, truncate string, add random |  |  |  |  |  |  |  |
| for research on fuzzing in mobile devices, as the heuristics | substring, remove random substring, substitute random |  |  |  |  |  |  |  |
| and algorithms adopted by existing tools (such as AFL) have | character from string with special character, substitute |  |  |  |  |  |  |  |
| evolved over the years on the basis of empirical experience | with empty string, substitute with null; |  |  |  |  |  |  |  |
| and experimentation with alternative approaches, which is | • | Arrays | and | Lists | : substitute with array of random length |  |  |  |
| facilitated by tools such as | Chizpurfle | . | and items, remove random items, add random items, |  |  |  |  |  |
| At the beginning of a fuzz testing campaign for a target | apply fuzz operator on a item value according to its type, |  |  |  |  |  |  |  |
| method, the | Seed Manager | creates a new initial seed with | substitute with empty array, substitute with null; |  |  |  |  |  |
| empty (for primitive types) or null (for object types) values. | • | Objects | : substitute with null, invoke constructor with |  |  |  |  |  |
| This initial seed is not mutated, but immediately submitted as | random parameters, apply fuzz operator on a field value |  |  |  |  |  |  |  |
| test input. This input will trigger the target method to cover | according to its type. |  |  |  |  |  |  |  |
| an initial set of | π | code blocks; then, the input is immediately | For | Object | types, the | Fuzz Input Generator | provides ad- |  |

fed back to the Seed Manager to be used as first actual seed ditional ad-hoc fuzzers for important specific classes defined

with score π . The steps to fuzz a vendor service method are by the Android OS. For example, the android.content.Intent

summarized in Algorithm 1. class has a specific fuzzer that injects into the fields of an

Intent (such as actions, categories and extras) special values

Algorithm 1 fuzzing a vendor service method

that have a meaning for the Intent ( e.g., ACTION MAIN and

| Input: | Service s, Method m, Process pid | ACTION CALL for the Intent actions) [40]; and the fuzzer for |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1: | parameters = createInitialSeed(s, m) | the | android.content.ComponentName | class takes into account |  |  |  |
| 2: | outputs = executeTest(s, m, parameters, pid) | which components are installed on the target device, in order |  |  |  |  |  |
| 3: | analyzedOutputs = analyzeAndSave(outputs) | to use and to mutate valid component names during fuzz |  |  |  |  |  |
| 4: | priorityQueue = | {} | testing. For all the other classes, a generic object fuzzer |  |  |  |  |
| 5: | priorityQueue.push(parameters, analyzedOutputs. | π | ) | uses the Java Reflection API to create new objects using the |  |  |  |
| 6: | repeat | class constructor with random parameters, and to invoke | setter |  |  |  |  |
| 7: | parameters, | π | = priorityQueue.pop() | methods of the class to place random values in the fields of |  |  |  |
| 8: | for | i = 1 | to | π | do | the object. |  |
| 9: | parameters’ = mutate(parameters) | The | Fuzz Input Generator | keeps a list of all the inputs |  |  |  |
| 10: | outputs = executeTest(s, m, parameters’, pid) | generated so far, in order not to submit again the same input to |  |  |  |  |  |
| 11: | analyzedOutputs = analyzeAndSave(outputs) | the test executor. Seeds are mutated by using a random number |  |  |  |  |  |
| 12: | if | analyzedOutputs. | π > | 0 | then | generator to select fuzz operators and to guide them ( | e.g., |
| 13: | priorityQueue.push(parameters’, | new values replacing the previous ones are selected randomly). |  |  |  |  |  |
| analyzedOutputs. | π | ) | These probabilities are tunable using a configuration file. |  |  |  |  |
| 14: | end if |  |  |  |  |  |  |
| 15: | end for | F. Test Executor |  |  |  |  |  |
| 16: | until | priorityQueue == | {} | The | Test Executor | performs tests on the Android device, |  |

by invoking the service method with the input provided by

the Fuzz Input Generator . It generates a proxy for that service

E. Fuzz Input Generator using the IBinderObject associated to the target service. Before

The Fuzz Input Generator receives a seed to be mutated, invoking the target method, it flushes the logs collected by

and generates inputs for the Test Executor . Several inputs are the Android OS (the logcat , which is a global collector for

obtained from the same seed, by applying different fuzz op- log messages produced both by user applications and system

erators. The number of new inputs to generate is proportional processes [41]). Then, Chizpurfle sends the start message to

to the score π of the seed, and the fuzz operators are selected the stalker server in the target process ( § IV-C) and calls the

according to the types of the parameters of the target method. target method. Any potential exception thrown by the service

---

## Page 7

is caught, so that the Test Execution is not aborted in the case are detected, the test input is assigned a score π , and the new

of service failures. After the method call, it sends another blocks are added to the list of covered blocks.

message to the stalker to stop the tracing, and retrieves logs The outcomes of this analysis, along with general informa-

from the logcat. The steps of the Test Executor are summarized tion about the test inputs and the tested service, are saved on

in Algorithm 2. a file. If the input receives a non-zero π score, the input is

Input: Service s, Method m, Parameters p, Process pid

Output: Outputs o

3: try: call(s, m, p)

4: catch e: o.setException(e)

6: o.logs = stopLogcat()

The Output Analyzer parses the outputs produced by the

Test Executor , and stores the information and results of the

tests on a file on the target device.

This component analyzes the logs to identify any failure that

has been triggered by the fuzzing test. A failure is detected

using the following criteria:

• A/F messages : the system generates log messages with

a high-severity level (either assert (A) or fatal (F)) [41],

[42]; such messages are never generated in failure-free

conditions, and should be considered as failure symp-

a “FATAL EXCEPTION”, which denotes an uncaught

sent to the Seed Manager for the next iteration of the fuzzing

Algorithm 3.

Output: AnalyzedOuput ao

1: ao = o

“A” in ao.logs.level) then

3: ao.hasFailures = true

4: end if

6: ao.serviceDead = true

7: end if

8: newBranches = ao.branches \ getExecutedBranches()

9: if size (newBranches) > 0 then

10: addExecutedBranches (newBranches)

11: ao. π = size (newBranches)

12: end if

13: saveToFile(ao)

H. Further Optmizations

of the fuzz tests.

| Algorithm 2 | execute test | loop. The steps of the | Output Analyser | are summarized in |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1: | flushLogcat() | Algorithm 3 | analyze and save results |  |  |  |  |  |  |  |  |
| 2: | startBranchTracing(pid) | Input: | Outputs o, DeathRecipient r |  |  |  |  |  |  |  |  |
| 5: | o.branches = stopBranchTracing() | 2: | if | (“FATAL” | or | “ANR” | in | ao.logs.message) | or | (“F” | or |
| G. Output Analyzer | 5: | if | ao.deathRecipient.deathNotified | then |  |  |  |  |  |  |  |
| toms; | When we initially applied the | Chizpurfle | tool to the Sam- |  |  |  |  |  |  |  |  |

• ANR messages : the system generates a log message sung Galaxy S6 Edge, we needed to address an important

that reports an ANR condition (i.e., Application Not technical problem: the system services (including the ones

Responding) [43]; this condition denotes that the fuzzed from vendors’ customizations) execute in the context of a few

input from the Test Executor propagated and triggered a system processes, along with dozens of other threads, such as

long-running operation or an indefinite wait on the main the system server process, which contains about 160 threads.

thread of some process; Unfortunately, instrumenting all these threads at the same time

• FATAL messages : the system logs a message reporting causes a high overhead, that would slow down the execution

exception on the service side. We enabled Chizpurfle to avoid instrumenting threads that

It must be noted that we focus on errors logged by system are unrelated to the target service being tested. We base this

processes rather than the Test Executor ; since the Test Executor approach on a simple, yet effective heuristic to detect unrelated

stimulates the system service with invalid input, it is correct for threads: for all the services running in the context of the same

the service to raise exceptions and not to provide any service to process of the target service, we tokenize the name of the

the Test Executor . Thus, we do not consider these exceptions service, and retain the tokens that belong only to that specific

as failure symptoms as they indicate the correct handling of service (for example, in the case of CocktailBarService , we

wrong inputs. retain the tokens “Cocktail” and “Bar”); then, we get the

Another check for failure detection is made when the Test names of the threads of the process, using the comm entry

Executor retrieves the Binder proxy for the tested service in the proc file system; finally, we identify the threads whose

( § IV-F). Chizpurfle registers a callback, using the linkToDeath name include the tokens of services different that the one under

of the IBinder API for the service [44], to receive a notification testing (for example, we exclude the “ CocktailBarVisi ” thread

if the Binder object of the service is not available. This when testing services different than the CocktailBarService ).

happens when the process that hosts the target service dies. The associations between threads and services can be easily

The Output Analyzer component also analyzes the list of reviewed by Chizpurfle ’s users before starting the testing

block addresses reported by the Instrumentation Module . It campaign. This heuristic reduces the run-time overhead of

keeps trace of all blocks covered by tests so far, and compares the instrumentation and only avoids threads that are likely

them with the block addresses of the current test. If new blocks unrelated to the service under testing.

---

## Page 8

We did another minor optimization to avoid few false pos- The bug can have two different effects on the Android OS,

itives that happened during the tests. During our preliminary depending on which process will consume the injected events

tests, some false positives occurred when the Android device from the Input Manager. If the events are consumed by the

reached a low battery level, that caused the Android OS process com.android.systemui , the uncaught exception triggers

to switch to battery-saver mode. This change, together with the restart of the process, and a black screen of the user

the workload of fuzz tests, slowed down the smartphone, interface for a few seconds. If the events are consumed by

and caused spurious ANRs in processes not related to the android.ui , which is a thread of the system server process, the

service under testing. We prevented these false positives by fuzzed inputs has a higher impact: it crashes the system server

periodically checking the battery level and pausing the tests if and causes a restart of the whole Android device. Several

the level is too low. We carefully checked and reproduced all method calls with exactly the same parameters values can be

the other failures described in next sections, to assure that our arbitrarily managed in both ways.

results are free from false positives. The second bug was triggered up when fuzzing the method

callInVoIP of the Samsung’s voip service. The method likely

V. E VALUATION C AMPAIGN

is used to place a call with Samsung WE VoIP app [47],

We applied Chizpurfle to a well-known commercial smart- a stock application that provides voice-over-IP for corporate

phone, the Samsung Galaxy S6 Edge. Before testing, we users. The method takes as input parameter a string that repre-

updated this device with the most recent Android OS officially sents a SIP address URI (such as “sip:1-999-123-4567@voip-

released by Samsung based on Android 7 “Nougat”. First, we provider.example.net”). Chizpurfle found that input strings

perform a fuzz testing campaign on all the service methods that include specific SQL control expressions (similarly to

introduced by Samsung. Then, we perform additional tests single quotes in SQL injection) trigger an uncaught SQLLite-

to evaluate the performance overhead and the test coverage, Exception by the com.samsung.android.incallui process. This

compared to a pure black-box approach. process is a customized version of the com.android.incallui

process of the AOSP, which handles the UI that appears during

A. Bugs in Samsung Customizations

a call, providing several on-screen functions. The uncaught

Chizpurfle detected 2,272 service methods from Samsung exception crashes the com.samsung.android.incallui process,

customizations. In this first experimental campaign, Chizpurfle cutting off any ongoing call.

performed 34,645 tests on these methods. The tool reported

that 9 tests caused failures, which are summarized in TA- B. Comparison with Black-Box Fuzzing

BLE II. We executed again the tests, and we found that the We compared Chizpurfle with the black-box approach, to

failures were reproducible. Then, we analyzed the failure mes- provide a baseline for evaluating our gray-box approach. We

sages reported on the logs, which include uncaught exceptions first analyze the performance overhead of Chizpurfle , that is,

and the stack trace at the time of the failures. Despite the the relative slow-down of fuzz testing when applying the gray-

source code not being available, we notice that the failures box approach. The overhead includes the time for generating

affected high-privilege system processes, and were caused by inputs and profiling the coverage of the tests. During the whole

2 distinct bugs (respectively, the first 4 failures, and the other test campaign on the Samsung Galaxy S6 Edge, Chizpurfle

5 failures). measured the overall time spent for executing the test. An

The first bug was found in the service spengestureservice , individual test takes on average 6 . 65 seconds, while testing a

hosted by the system server process. The bug was triggered whole method takes on average 527 . 60 seconds.

by the method injectInputEvent . To understand the role of this To get the test duration that would be obtained with black-

method, we analyzed the AOSP, and found a similar method box fuzzing, we performed a second round of tests by dis-

(with the same name and minor differences in the method abling both the Chizpurfle ’s Seed Manager and Instrumenta-

signature) provided by the InputManager class of AOSP, tion Module (the two distinctive elements of gray-box test-

which handles input devices such as keyboards. This method ing). This usage mode Chizpurfle (denoted as Chizpurfle BB )

“injects an input event into the event system on behalf of an is equivalent to perform black-box fuzzing, without neither

application” [45]. It is likely that the method with the same collecting coverage nor using coverage for selecting the test

name in the spengestureservice performs the same operation inputs. In Chizpurfle BB , the inputs are instead generated

for input events from the “S Pen” in Samsung devices [46]. randomly. For each target method, we used Chizpurfle BB by

One of the input parameters for this method is an array applying the same number of inputs that were also generated

of android.view.InputEvent objects, which is an abstract class by the gray-box Chizpurfle for that method.

for representing input events from hardware components. By comparing the time to run Chizpurfle BB with the time

During the fuzz testing campaign, Chizpurfle detected a FATAL to run the gray-box Chizpurfle , we obtain a performance slow-

EXCEPTION when this array is non-null and non-empty, and down per service of 11.97x on average. To put this number into

at least one of its elements is null (instead, the service does context, we must consider that the performance slow-down

not fail if the array is simply null or empty). This input causes is inline with other tools for dynamic binary instrumentation.

the service to throw a NullPointerException that is not caught, For example the Valgrind framework (which also uses dynamic

causing a crash. We found that this bug is fully reproducible. binary rewriting for complex analyses, such as finding memory

---

## Page 9

TABLE II

D ETECTED F AILURES IN

TESTID INPUT

7

22

162

spengestureservice injectInputEvent

186

{ ??9??\u001a??b\u0004A\"1??HanI???\u

0017??!\u0014?\u001a\u0006?Fu??UN?\u

54 0015Q??_?\/??\u0007#\u001aX?\u0012?L

‘??6}-f??fc??$\u0001?8$s5p?OTg?}??Wu

??1=?]?W\u0019 ?z?\u0011?Q?? }

55

{ ??y\u0014?˜?\u0011??E\u0007\u000b?‘

?%?\u0016yD\u0018??9t?i\u000f?NO?6˜z

??Q?(\u0018??\u0002??)\u0003?n?˜

voip -?\u0017??ˆb?\u0015\u00034\u0015PX\u

callInVoIP 0001?!?G\u0002?\u00 00}?_??z??v{?

A\"Z5?‘v?)??f??\u0006n6?j9 }

{ ??o??\bF?%?\u0003?#,??t\u001a??9?ˆ??

86 Z$??J\u0016?\u0011\u0018?\u0016p\u0

011x\u001c?\u001dTa0 U‘?h?3?????\

{ 7??L6?I?{<81>?P!:?\u0005?\/?Gˆ\u000

3?#\u0000??+c\u0016?\u001eA2??|\f???

| voip | 1f@??i-:?˜??1\u000f\u001dWSjm??? |
| --- | --- |
| callInVoIP | ;???\u000f?\u0019\u000f??N[?\u001fWV |

rewarded by a higher bug-finding power, and it is in many

E VALUATION C AMPAIGN

FAILURE

FATAL EXCEPTION: mainProcess: com.android.systemui, PID:

12884 java.lang.NullPointerException: Attempt to invoke virtual

SmartClipRemoteRequestDispatcher.dispatchInputEventInjection

FATAL EXCEPTION: mainProcess: com.android.systemui, PID:

4025 java.lang.NullPointerException: Attempt to invoke virtual

SmartClipRemoteRequestDispatcher.dispatchInputEventInjection

!@*** FATAL EXCEPTION IN SYSTEM PROCESS: android.ui

java.lang.NullPointerException: Attempt to invoke virtual

SmartClipRemoteRequestDispatcher.dispatchInputEventInjection

(SmartClipRemoteRequestDispatcher.java:201)[...]

!@*** FATAL EXCEPTION IN SYSTEM PROCESS: android.ui

java.lang.NullPointerException: Attempt to invoke virtual

SmartClipRemoteRequestDispatcher.dispatchInputEventInjection

FATAL EXCEPTION: mainProcess: com.samsung.android.incallui,

PID: 23452 android.database.sqlite.SQLiteException: near \",\" :

FATAL EXCEPTION: mainProcess: com.samsung.android.incallui,

PID: 25500 android.database.sqlite.SQLiteException: unrecognized to-

(code 1): , while compiling: SELECT reject number FROM re-

ject num WHERE reject number= ’??9??\u0 [...]

FATAL EXCEPTION: mainProcess: com.samsung.android.incallui,

PID: 32445 android.database.sqlite.SQLiteException: near \"???\" :

}

FATAL EXCEPTION: mainProcess: com.samsung.android.incallui,

PID: 5745 android.database.sqlite.SQLiteException: near

SELECT reject number FROM reject num WHERE

}

reject number= ’?0Q?@b}W\u000e [...]

coverage of black-box fuzzing on the vendor customization,

| { | 0, -2147483648, | array of | android.view.InputEvent | method | ’long | android.view.InputEvent.getEventTime()’ | on | a |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| objects with a null item | , false, NULL | } | null | object | reference | at | com.samsung.android.content.smartclip. |  |  |
| spengestureservice | injectInputEvent | (SmartClipRemoteRequestDispatcher.java:201)[...] |  |  |  |  |  |  |  |
| { | -715676118, -1, | array of | android.view.InputEvent | method | ’long | android.view.InputEvent.getEventTime()’ | on | a |  |
| objects with a null item | , false, NULL | } | null | object | reference | at | com.samsung.android.content.smartclip. |  |  |
| spengestureservice | injectInputEvent | (SmartClipRemoteRequestDispatcher.java:201)[...] |  |  |  |  |  |  |  |
| { | 0, 91, | array of | android.view.InputEvent | objects with | method | ’long | android.view.InputEvent.getEventTime()’ | on | a |
| a null item | , false, NULL | } | null | object | reference | at | com.samsung.android.content.smartclip. |  |  |
| { | -188, 91, | array of | android.view.InputEvent | objects | method | ’long | android.view.InputEvent.getEventTime()’ | on | a |
| with a null item | , true, NULL | } | null | object | reference | at | com.samsung.android.content.smartclip. |  |  |
| spengestureservice | injectInputEvent | (SmartClipRemoteRequestDispatcher.java:201)[...] |  |  |  |  |  |  |  |
| voip | syntax error (code 1): , while compiling: SELECT reject number |  |  |  |  |  |  |  |  |
| callInVoIP | FROM reject num WHERE reject number= | ’\u000e?? | [...] |  |  |  |  |  |  |
| { | ??_??\u0010 | >\u0001\bK)?}?t’??R?G}T | FATAL | EXCEPTION: | mainProcess: | com.samsung.android.incallui, |  |  |  |

<T\u0001?\u001b?????N?d?V??Z\u0002?e? PID: 24643 android.database.sqlite.SQLiteException: near \"???\" :

| voip | ???O??#?\u001dS??\r?????g\u0016\u0002 | syntax error (code 1): , while compiling: SELECT reject number |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| callInVoIP | ?\u0002?ed\ | u0010? | } | FROM reject num WHERE reject number= | ’001?\u0 | [...] |  |  |  |
| 72 | ken: | \"’??9??\u001a?????\b?VN6g?,ˆ6\u0011???Lx?\" |  |  |  |  |  |  |  |
| voip | syntax error (code 1): , while compiling: SELECT reject number |  |  |  |  |  |  |  |  |
| callInVoIP | FROM reject num WHERE reject number= | ’?\u0011 | [...] |  |  |  |  |  |  |
| 105 | \"@?d???\" | : | syntax | error | (code | 1): | , | while | compiling: |

leaks and race conditions), when applied on the SPEC CPU side effect, thus preserving the intended behavior of the test

2006 benchmark [48], causes an average slow-down of 4.3x cases. Fig. 4 shows the performance overhead for the two

when the program is simply executed on the Valgrind virtual services previously discussed ( voip and spengestureservice ),

machine; and an average slow-down of 22.1x when performing and for other 10 randomly-chosen custom vendor services,

memory leak analysis. Such overhead when running tests is which cover the 10% of all the custom methods.

cases accepted by developers as shown by the widespread We then evaluate the gain, in terms of test coverage (the

adoption of Valgrind in automated regression test suites in higher, the better), obtained by applying gray-box fuzzing

open-source projects [49]. In our context, the slow-down still instead of black-box fuzzing, given the same time budget T

allows the Android system to execute without any noticeable available for both forms of fuzz testing. To measure the test

---

## Page 10

20x

18x

16x

14x

12x

10x

8x

6x

performance overhead 4x

2x

0x

| voip | AAS |
| --- | --- |
| sb_service | edm_proxy |
| semclipboard | gamemanager |
| mobile_payment | enterprise_policy |

SecurityManagerService

SecExternalDisplayService

vendor services

Fig. 4. Performance Overhead of Chizpurfle.

the only possible approach is to apply the Instrumentation

Module of Chizpurfle (but without using the Seed Manager ,

in order to fuzz inputs in a random way). We denote this mode

as Chizpurfle BB+COV

.

However, we need to take into account that code instru-

mentation slows down the execution of the black-box tests,

and thus simply applying Chizpurfle BB+COV for the same

amount of wall-clock time of the gray-box Chizpurfle would

unfairly penalize the black-box approach. Therefore, to obtain

a fair estimate of the test coverage for black-box fuzzing,

we compensate for the slow-down due to instrumentation by

granting it a higher time budget than gray-box fuzzing. The

experiments discussed above, here we applied to each method

its slow-down factor).

box approach. The gain in terms of test coverage is shown

in Fig. 5 (which focuses on the same services analyzed in

(see Fig. 6), we noticed that Chizpurfle was more effective

on those methods that take complex data in inputs, such as

VI. C ONCLUSIONS

7x

6x

5x

4x

3x

2x

code coverage gain

1x

0x

AAS voip

sb_service edm_proxy

gamemanager semclipboard

enterprise_policy mobile_payment

SecurityManagerService

SecExternalDisplayService

vendor services

Fig. 5. Code Coverage Gain of Chizpurfle.

9x

8x

7x

6x

5x

4x

3x

code coverage gain

2x

1x

0x

semclipboard: updateFilter

getActiveAdmins

gamemanager: enterprise_policy: getClipedStrings gamemanager:

createCallSession requestWithJson

enterprise_policy: edm_proxy:

getAdminUidForAuthorizedUid SecExternalDisplayService:

getApplicationStateEnabledAsUser

vendor services methods

on fuzzing in mobile devices, by allowing to experiment with

different heuristics for evolutionary fuzzing (e.g., for deter-

mining when to stop fuzzing, for prioritizing seeds, and for

| spengestureservice | AODManagerService | AODManagerService | spengestureservice |
| --- | --- | --- | --- |
| time budget is obtained by multiplying the time budget of | edm_proxy: | AuditLogger | voip: |
| gray-box fuzzing for the slow-down due to instrumentation | semclipboard: |  |  |
| (while 11.97x is the average slow-down according to the | identifyGamePackage | AODManagerService: | updateAODTspRect |
| On average, | Chizpurfle | covers 2.3x more code than the black | SecExternalDisplayCreateSurface |
| Fig. 4). By looking at the code coverage gain per method | Fig. 6. | Code Coverage Gain of Chizpurfle per Method. |  |

semclipboard ’s method updateFilter takes as input an object relevant bugs, that it has a reasonable overhead, and that it can

of type android.sec.clipboard.IClipboardDataPasteEvent for increase the test coverage compared to the black-box approach.

managing clipboard data. Instead, in the case of simpler The gray-box fuzzing represents a promising approach

methods, such as getters and setters, the gray-box approach for testing proprietary Android services in more depth. The

has a minor impact on test coverage. Chizpurfle tool represents a valuable opportunity for research

This paper presented Chizpurfle , a novel gray-box fuzzer selecting fuzz operators), as happened for similar fuzzing tools

designed to test custom system services from Android vendors. that were applied in different context than mobile devices.

This tool exploits dynamic binary instrumentation to measure Another possible extension of Chizpurfle is to include support

test coverage and to drive the selection of fuzz inputs. The for system services implemented in C; since there is not

experimental results on a commercial Android device from reflection API, other reverse engineering techniques should be

Samsung showed that the gray-box approach can discover used in order to extract the method signatures.

---

## Page 11

A CKNOWLEDGMENT [26] H. Ye, S. Cheng, L. Zhang, and F. Jiang, “Droidfuzzer: Fuzzing the

di San Paolo in the frame of Programme STAR (project

FIDASTE).

R EFERENCES

//www.samsung.com/us/samsung-pay/

[8] LG, “LG Security Bulletins,” March 2017. [Online]. Available:

software-upgrade-security/g id/5593

[10] Samsung, “Samsung Android Security Updates,” March 2017. [Online].

Available: http://security.samsungmobile.com/smrupdate.html

[Online]. Available: https://cve.mitre.org/cgi-bin/cvename.cgi?name=

CVE-2016-2060

[12] B. P. Miller, L. Fredriksen, and B. So, “An Empirical Study of the

Reliability of UNIX Utilities,” Communications of the ACM , vol. 33,

no. 12, pp. 32–44, 1990.

[13] Michal Zalewski, “American Fuzzy Lop (AFL),” December 2016.

[Online]. Available: http://lcamtuf.coredump.cx/afl/

Programs.” in OSDI , vol. 8, 2008, pp. 209–224.

constraints: Whitebox fuzz testing in production,” in Proceedings of the

vol. 26, no. 9, 2000.

Applications 7, 1999 , 1999.

analysis of program executions,” in Proceedings of the 2nd international

Hat USA, June , 2009.

android apps with intent-filter tag,” in Proceedings of International

2013.

[27] R. Sasnauskas and J. Regehr, “Intent fuzzer: crafting intents of death,”

in Proceedings of the 2014 Joint International Workshop on Dynamic

Analysis (WODA) and Software and System Performance Testing, De-

bugging, and Analytics (PERTEA) . ACM, 2014, pp. 1–5.

[28] R. Mahmood, N. Esfahani, T. Kacem, N. Mirzaei, S. Malek, and

security , 2014.

of Software Test . ACM, 2016.

ference . ACM, 2015.

[34] H. Feng and K. G. Shin, “Understanding and defending the binder attack

surface in android,” in Proceedings of the 32nd Annual Conference on

[35] L. Luo, Q. Zeng, C. Cao, K. Chen, J. Liu, L. Liu, N. Gao, M. Yang,

X. Xing, and P. Liu, “Context-aware System Service Call-oriented

Symbolic Execution of Android Framework with Application to Exploit

Generation,” arXiv preprint arXiv:1611.00837 , 2016.

[36] Android Studio, “Android Debug Bridge,” April 2017. [Online].

Available: https://developer.android.com/studio/command-line/adb.html

set.coresight/index.html

https://www.frida.re

java/android/content/Intent.java

logcat.html

IPX-LSMP/STD

ACM, 2007.

| This work has been supported by UniNA and Compagnia | Conference on Advances in Mobile Computing & Multimedia | . | ACM, |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [1] | Samsung, “Bixby,” May 2017. [Online]. Available: http://www.samsung. | A. Stavrou, “A whitebox approach for automated security testing of |  |  |  |  |  |  |  |  |  |  |
| com/global/galaxy/apps/bixby/ | android applications on the cloud,” in | Automation of Software Test (AST), |  |  |  |  |  |  |  |  |  |  |
| [2] | HTC, | “HTC | U | Ultra- | HTC | Sense | Companion,” | May | 2017. | 2012 7th International Workshop on | . | IEEE. |

[Online]. Available: http://www.htc.com/us/smartphones/htc-u-ultra/ [29] A. K. Maji, F. A. Arshad, S. Bagchi, and J. S. Rellermeyer, “An empirical

| #SenseCompanion | study of the robustness of inter-component communication in android,” |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [3] | Motorola, | “Moto | Enhancements,” | May | 2017. | [Online]. | Available: | in | IEEE/IFIP International Conference on Dependable Systems and |
| https://www.motorola.co.uk/products/moto-z#moto-enhancements | Networks (DSN 2012) | . | IEEE, 2012, pp. 1–12. |  |  |  |  |  |  |

[4] Huawei, “Huawei P9 co-engineered with leica reinvent smartphone [30] K. W. Y. Au, Y. F. Zhou, Z. Huang, and D. Lie, “Pscout: Analyzing the

| photography,” May 2017. [Online]. Available: http://consumer.huawei. | Android Permission Specification,” in | Proceedings of the 2012 ACM |
| --- | --- | --- |
| com/en/mobile-phones/p9/index.htm | conference on Computer and communications security | . |

[5] LG, “LG X Cam,” May 2017. [Online]. Available: http://www.lg.com/ [31] K. Yang, J. Zhuge, Y. Wang, L. Zhou, and H. Duan, “IntentFuzzer:

uk/mobile-phones/lg-K580 detecting capability leaks of android applications,” in Proceedings of

[6] Samsung, “Samsung Pay,” May 2017. [Online]. Available: http: the 9th ACM symposium on Information, computer and communications

[7] Android, “Android Security Bulletin,” May 2017. [Online]. Available: [32] Y. Hu and I. Neamtiu, “Fuzzy and cross-app replay for smartphone

| https://source.android.com/security/bulletin/ | apps,” in | Proceedings of the 11th International Workshop on Automation |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| https://lgsecurity.lge.com/security updates.html | [33] | C. Cao, N. Gao, P. Liu, and J. Xiang, “Towards analyzing the input |  |  |  |  |  |  |
| [9] | Motorola, | “Moto | Security | Updates,” | March | 2017. | [On- | validation vulnerabilities associated with android system services,” in |
| line]. | Available: | https://motorola-global-portal.custhelp.com/app/ | Proceedings of the 31st Annual Computer Security Applications Con- |  |  |  |  |  |
| [11] | Common Vulnerability and Eposures, “CVE-2016-2060,” May 2017. | Computer Security Applications | . | ACM, 2016. |  |  |  |  |

[14] C. Cadar, D. Dunbar, D. R. Engler et al. , “KLEE: Unassisted and [37] ARM, “CoreSight on-chip trace and debug,” May 2017. [Online].

Automatic Generation of High-Coverage Tests for Complex Systems Available: http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.

[15] E. Bounimova, P. Godefroid, and D. Molnar, “Billions and billions of [38] Ole Andr´ e V. Ravn˚ as, “F R IDA,” February 2017. [Online]. Available:

| 2013 International Conference on Software Engineering | . | [39] | M. B¨ | ohme, V.-T. Pham, and A. Roychoudhury, “Coverage-based grey- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [16] | Google | Inc., | “OSS-Fuzz | - | Continuous | Fuzzing | for | Open | Source | box fuzzing as markov chain,” in | Proceedings of the 2016 ACM SIGSAC |
| Software,” 2017. [Online]. Available: https://github.com/google/oss-fuzz | Conference on Computer and Communications Security | . |  |  |  |  |  |  |  |  |  |

[17] P. Koopman and J. DeVale, “The exception handling effectiveness of [40] AndroidXRef, “Cross Reference: Intent.java,” May 2017. [Online].

POSIX operating systems,” IEEE Transactions on Software Engineering , Available: http://androidxref.com/7.0.0 r1/xref/frameworks/base/core/

[18] J.-C. Fabre, F. Salles, M. R. Moreno, and J. Arlat, “Assessment of COTS [41] Android Developers, “Logcat Command-line Tool,” May 2017.

microkernels by fault injection,” in Dependable Computing for Critical [Online]. Available: https://developer.android.com/studio/command-line/

[19] K. Kanoun, Y. Crouzet, A. Kalakech, A.-E. Rugina, and P. Rumeau, [42] ——, “Write and View Logs with Logcat,” May 2017. [Online].

“Benchmarking the dependability of Windows and Linux using Post- Available: https://developer.android.com/studio/debug/am-logcat.html

Mark workloads,” in Software Reliability Engineering, 2005. ISSRE [43] ——, “Keeping Your App Responsive,” May 2017. [Online]. Available:

2005. 16th IEEE International Symposium on . https://developer.android.com/training/articles/perf-anr.html

[20] S. Winter, C. Sˆ arbu, N. Suri, and B. Murphy, “The impact of fault [44] AndroidXRef, “Cross Reference: IBinder.java - linkToDeath,”

| models on software robustness evaluations,” in | Proceedings of the 33rd | May | 2017. | [Online]. | Available: | http://androidxref.com/7.0.0 r1/xref/ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| International Conference on Software Engineering | . | ACM, 2011. | frameworks/base/core/java/android/os/IBinder.java#257 |  |  |  |  |  |  |  |  |
| [21] | D. Cotroneo, D. Di Leo, F. Fucci, and R. Natella, “Sabrine: State- | [45] | AndroidXRef, | “Cross | Reference: | InputManager.java | - |  |  |  |  |
| based robustness testing of operating systems,” in | Automated Software | injectInputEvent,” | May | 2017. | [Online]. | Avail- |  |  |  |  |  |
| Engineering (ASE), 2013 IEEE/ACM 28th International Conference on | . | able: | http://androidxref.com/7.0.0 r1/xref/frameworks/base/core/java/ |  |  |  |  |  |  |  |  |
| [22] | Google, | “syzkaller | - | linux | syscall | fuzzer,” | May | 2017. | [Online]. | android/hardware/input/InputManager.java#833 |  |
| Available: https://github.com/google/syzkaller | [46] | Samsung, “What are the advantages of S Pen,” May 2017. [Online]. |  |  |  |  |  |  |  |  |  |
| [23] | P. Godefroid, M. Y. Levin, D. A. Molnar | et al. | , “Automated whitebox | Available: http://www.samsung.com/global/galaxy/what-is/s-pen/ |  |  |  |  |  |  |  |
| fuzz testing.” in | NDSS | , vol. 8, 2008. | [47] | ——, | “WE | VoIP | Application | for | Business,” | May | 2017. |
| [24] | S. Bhansali, W.-K. Chen, S. De Jong, A. Edwards, R. Murray, M. Drini´ | c, | [Online]. | Available: | http://www.samsung.com/us/business/ |  |  |  |  |  |  |
| D. Mihoˇ | cka, and J. Chau, “Framework for instruction-level tracing and | business-communication-systems/unified-communication-solutions/ |  |  |  |  |  |  |  |  |  |
| conference on Virtual Execution Environments | . | ACM, 2006. | [48] | N. Nethercote and J. Seward, “Valgrind: A framework for heavyweight |  |  |  |  |  |  |  |
| [25] | C. Mulliner and C. Miller, “Fuzzing the Phone in your Phone,” | Black | dynamic binary instrumentation,” in | ACM Sigplan notices | , vol. 42, no. 6. |  |  |  |  |  |  |

---

## Page 12

[49] D. Cotroneo, M. Grottke, R. Natella, R. Pietrantuono, and K. S. Trivedi,

“Fault triggers in open-source software: An experience report,” in

Software Reliability Engineering (ISSRE), 2013 IEEE 24th International

Symposium on .

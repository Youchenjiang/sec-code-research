---year: 2011

secverify_category: "Legacy"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "DroidScope: Seamlessly Reconstructing the OS and Dalvik Semantic Views for Dynamic Android Malware Analysis"
creator: "LaTeX with hyperref package"
pages: 16
source: "DroidScope (2011) Seamlessly Reconstructing OS and Dalvik Semantic Views.pdf"
---

# DroidScope: Seamlessly Reconstructing the OS and Dalvik Semantic Views for Dynamic Android Malware Analysis (2011)

> **文獻存檔**：[PDF 原文](<../../raw-papers/2010-2019/DroidScope (2011) Seamlessly Reconstructing OS and Dalvik Semantic Views.pdf>) | [Markdown 原文](<../../raw-papers/2010-2019/DroidScope (2011) Seamlessly Reconstructing OS and Dalvik Semantic Views (Raw).md>)

> **總頁數**：16 頁

---

## Page 1

DroidScope: Seamlessly Reconstructing the OS and Dalvik Semantic Views

for Dynamic Android Malware Analysis

| †‡ | † |
| --- | --- |
| Lok Kwong Yan | Heng Yin |
| † | ‡ |
| Syracuse University | Air Force Research Laboratory |
| Syracuse, New York, USA | Rome, New York, USA |

{ loyan, heyin } @syr.edu

Abstract Malware analysis and exploit diagnosis on desktop

The prevalence of mobile platforms, the large market

share of Android, plus the openness of the Android Mar-

ket makes it a hot target for malware attacks. Once a mal-

ware sample has been identified, it is critical to quickly

reveal its malicious intent and inner workings. In this

paper we present DroidScope, an Android analysis plat-

form that continues the tradition of virtualization-based

malware analysis. Unlike current desktop malware anal-

ysis platforms, DroidScope reconstructs both the OS-

Android is a popular mobile operating system that is in-

stalled in millions of devices and accounted for more

than 50% of all smartphone sales in the third quarter of

2011 [22]. The popularity of Android and the open na-

ture of its application marketplace makes it a prime tar-

get for attackers. Malware authors can freely upload ma-

waiting for

unsuspecting users to download and install them. Ad-

ditionally, numerous third-party alternative marketplaces

make delivering malicious applications even easier. In-

deed recent research has shown that malicious applica-

tions exist in both the official and unofficial marketplaces

with a rate of 0.02% and 0.2% respectively [41].

systems is well researched. It is widely accepted that

dynamic analysis is indispensable, because malware is

often heavily obfuscated to thwart static analysis. Fur-

thermore, runtime information is often needed for exploit

diagnosis. In particular, much work has leveraged virtu-

alization techniques, either whole-system software emu-

lation or hardware virtualization, to introspect and ana-

lyze illicit activities within the virtual machine [11, 15,

18, 31, 33, 39, 37].

nel data structures [16, 21, 24]. Based on this idea, sev-

and TEMU [35]) have been implemented.

Despite the fact that Android is based on Linux, it

is not straightforward to take the same desktop analy-

sis approach for Android malware. There are two lev-

els of semantic information that must be rebuilt. In the

lower level, Android is a Linux operating system where

lated into a process. Within each App, a virtual machine

(known as the Dalvik Virtual Machine) provides a run-

time environment for the App’s Java components.

In essence, to enable the virtualization-based analysis

approach for Android malware analysis, we need to re-

construct semantic knowledge at two levels: 1) OS-level

semantics that understand the activities of the malware

1

| level and Java-level semantics simultaneously and seam- | The advantages of virtualization-based analysis ap- |  |  |
| --- | --- | --- | --- |
| lessly. | To facilitate custom analysis, DroidScope ex- | proaches are two-fold: | 1) as the analysis runs under- |
| ports three tiered APIs that mirror the three levels of an | neath the entire virtual machine, it is able to analyze even |  |  |
| Android device: hardware, OS and Dalvik Virtual Ma- | the most privileged attacks in the kernel; and 2) as the |  |  |
| chine. On top of DroidScope, we further developed sev- | analysis is performed externally, it becomes very diffi- |  |  |
| eral analysis tools to collect detailed native and Dalvik | cult for an attack within the virtual machine to disrupt |  |  |
| instruction traces, profile API-level activity, and track in- | the analysis. The downside, however, is the loss of se- |  |  |
| formation leakage through both the Java and native com- | mantic contextual information when the analysis com- |  |  |
| ponents using taint analysis. These tools have proven to | ponent is moved out of the box. To reconstruct the se- |  |  |
| be effective in analyzing real world malware samples and | mantic knowledge, virtual machine introspection (VMI) |  |  |
| incur reasonably low performance overheads. | is needed to intercept certain kernel events and parse ker- |  |  |
| 1 | Introduction | eral analysis platforms (such as Anubis [1], Ether [15], |  |
| licious applications to the Android Market | 1 | each Android application (or App in short) is encapsu- |  |
| 1 | The Android Market has been superceded by the Android Apps | process and its native components; and 2) Java-level se- |  |
| Store in Google Play. | mantics that comprehend the behaviors in the Java com- |  |  |

---

## Page 2

ponents. Ideally, to capture the interactions between Java

level and Java-level semantic views completely from the

Scope further provides a set of APIs to help analysts

capability of DroidScope, we have implemented several

tracer to log an App’s interactions with the Android sys-

We evaluated the performance impacts of these tools

on 12 different benchmarks and found that the instru-

mentation overhead is reasonably low and taint analysis

performance (from 11 to 34 times slowdown) is compa-

uated the capability of these tools using two real world

In summary, this paper makes the following contribu-

tions:

through Java Objects with the help of the Dalvik view

2

Zygote Services

Component System Libraries Libraries

In this section, we give an overview of the Android sys-

tem and existing Android malware analysis techniques to

motivate our new analysis platform.

is the parent process for all Android Apps. Each App

is assigned its own unique user ID ( uid ) at installation

time and group IDs ( gids ) corresponding to requested

apk file for distribution.

| and native components, we need a unified analysis plat- | Java | Java |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| form that can simultaneously rebuild these two semantic | Component | Component |  |  |  |  |
| views and seamlessly bind these two views with the exe- | Java Libraries |  |  |  |  |  |
| cution context. | System | Java Libraries | Java Libraries |  |  |  |
| With this goal in mind, we designed and implemented | Dalvik VM |  |  |  |  |  |
| a new analysis platform, | DroidScope | , for Android mal- | JNI |  |  |  |
| ware analysis. DroidScope is built on top of QEMU (a | Native | System | System |  |  |  |
| CPU emulator [3]) and is able to reconstruct the OS- | Libraries |  |  |  |  |  |
| outside. Enriched with the semantic knowledge, Droid- | Linux Kernel |  |  |  |  |  |
| implement custom analysis plugins. To demonstrate the | Figure 1: Overview of Android System |  |  |  |  |  |
| tools, including native instruction tracer and Dalvik in- | and analyze two real-world malware samples: Droid- |  |  |  |  |  |
| struction tracer to obtain detailed instruction traces, API | KungFu and DroidDream. |  |  |  |  |  |
| tem, and taint tracker to analyze information leakage. | 2 | Background and Motivation |  |  |  |  |
| rable with other taint analysis systems. We further eval- | 2.1 | Android System Overview |  |  |  |  |
| Android malware samples: | DroidKungFu and Droid- | Figure 1 illustrates the architecture of the Android sys- |  |  |  |  |
| Dream. They both have Java and native components as | tem from the perspective of a system programmer. | At |  |  |  |  |
| well as payloads that try to exploit known vulnerabili- | the lowest level, the Android system uses a customized |  |  |  |  |  |
| ties. We were able to analyze their behavior without any | Linux kernel to manage various system resources and |  |  |  |  |  |
| changes to the virtual Android device, and obtain valu- | hardware devices. System services, native applications |  |  |  |  |  |
| able insights. | and Apps run as Linux processes. In particular, Zygote |  |  |  |  |  |
| • | We describe two-level virtual machine introspection to | permissions. These | uids | and | gids | are used to control |
| rebuild the Linux and Dalvik contexts of virtual An- | access to system resources (i.e, network and file system) |  |  |  |  |  |
| droid devices. | Dalvik introspection also includes a | like on a normal Linux system. |  |  |  |  |
| technique to dynamically disable Dalvik Just-In-Time | All Apps can contain both Java and native compo- |  |  |  |  |  |
| compilation. | nents. | Native components are simply shared libraries |  |  |  |  |
| • | We present DroidScope, a new emulation based An- | that are dynamically loaded at runtime. The Dalvik vir- |  |  |  |  |
| droid malware analysis engine that can be used to an- | tual machine (DVM), a shared library named | libdvm.so | , |  |  |  |
| alyze the Java and native components of Android Ap- | is then used to provide a Java-level abstraction for the |  |  |  |  |  |
| plications. DroidScope exposes an event-based anal- | App’s Java components. At the same time, the Java Na- |  |  |  |  |  |
| ysis interface with three sets of APIs that correspond | tive Interface (JNI) is used to facilitate communications |  |  |  |  |  |
| to the three different abstraction levels of an Android | between the native and Java sides. |  |  |  |  |  |
| Device, hardware, Linux and Dalvik. | To create a Java component, an App developer first |  |  |  |  |  |
| • | We developed four analysis tools on DroidScope. The | implements it in Java, compiles it into Java bytecode, and |  |  |  |  |
| native instruction tracer | and | Dalvik instruction tracer | then converts it into Dalvik bytecode. | The result is a |  |  |
| provide detailed accounts of the analysis sample’s exe- | Dalvik executable called a | dex | file. | The developer can |  |  |
| cution, while the | API tracer | provides a high level view | also compile native code into shared libraries, | .so | files, |  |
| of how the sample interacts with the rest of the system. | with JNI support. The dex file, the shared libraries and |  |  |  |  |  |
| The | taint tracker | implements dynamic taint analysis | any other resources, including the | AndroidManifest.xml |  |  |
| on native instructions but is capable of tracking taint | file that describes the App, are packaged together into an |  |  |  |  |  |
| reconstruction. | These tools were used to instrument | For instance, | DroidKungFu is a malicious puzzle |  |  |  |

---

## Page 3

game found in alternative marketplaces [25]. Its Java

component exfiltrates sensitive information and awaits

commands from the bot master. Its native component is

used as a shell to execute those commands and it also in-

geting known vulnerabilities, adb setuid exhaustion and

For security analysts, once a new Android malware

workings. This often involves both static and dynamic

analysis.

2.2 Android Malware Analysis

Like malware analysis on the desktop environment, An-

droid malware analysis techniques can fall into two cat-

egories: static and dynamic. For static analysis, the sam-

ple’s dex file can be analyzed by itself or it can be disas-

sembled and further decompiled into Java using tools like

dex2jar and ded [13]. Standard static program analysis

techniques (such as control-flow analysis and data-flow

analysis) can then be performed. As static analysis can

give a complete picture, researchers have demonstrated

this approach to be very effective in many cases [20].

However, static analysis is known to be vulnerable

to code obfuscation techniques, which are common-

place for desktop malware and are expected for An-

droid malware. In fact, the Android SDK includes a

tool named Proguard [34] for obfuscating Apps. An-

droid malware may also generate or decrypt native com-

ponents or Dalvik bytecode at runtime. Indeed, Droid-

KungFu dynamically decrypts the exploit payloads and

executes them to root the device. Moreover, researchers

have demonstrated that bytecode randomization tech-

niques can be used to completely hide the internal logic

of a Dalvik bytecode program [14]. Static analysis also

falls short for exploit diagnosis, because a vulnerable

runtime execution environment is needed to observe and

3

analyze an exploit attack and pinpoint the vulnerability.

3

API

| Java | Java | Java | Java |  |  |
| --- | --- | --- | --- | --- | --- |
| Component | Component | Component | Component | Instrumentation Interface | Tracer |
| System | Java Libraries | Java Libraries |  |  |  |
| Java Libraries | Java-level |  |  |  |  |
| Zygote | Services | View | Native |  |  |

JNI

| Native | System | System |
| --- | --- | --- |
| Libraries | Insn. Tracer |  |
| Linux Kernel | View | Taint |

DroidScope

Figure 2: DroidScope Overview

Virtualization based analysis has proven effective

against evasion, because all of the analysis components

are out of the box and are more privileged than the run-

time environment being analyzed, including the mal-

ware. Based on dynamic binary translation and hard-

ware virtualization techniques, several analysis plat-

forms [1, 15, 38] have been built for analyzing desktop

malware. These platforms are able to bridge the seman-

tic gap between the hardware-level view from the virtual

machine monitor and the OS-level view within the vir-

tual machine using virtual machine introspection tech-

niques [16, 21, 24].

However, these tools cannot be immediately used for

Android malware analysis. Android has two levels of

semantic views, OS and Java, that need to be recon-

structed versus the one for desktop malware. To enable

virtualization-based analysis for Android malware, we

need a unified analysis platform that reconstructs these

two levels of views simultaneously and seamlessly binds

these two views such that interactions between Java com-

ponents and native components can be monitored and an-

alyzed.

Architecture

| cludes three resource files that are encrypted exploits tar- | Dalvik VM | Insn. Tracer |  |  |  |
| --- | --- | --- | --- | --- | --- |
| udev [12], in certain versions of Android. | Component | System | Libraries | Libraries | Dalvik |
| instance has been identified, it is critical to quickly re- | OS-level |  |  |  |  |
| veal its malicious functionality and understand its inner- | Tracker |  |  |  |  |
| Complementary to static analysis, dynamic analysis is | DroidScope’s architecture is depicted in Figure 2. The |  |  |  |  |
| immune to code obfuscation and is able to see the mali- | entire Android system (including the malware) runs on |  |  |  |  |
| cious behavior on an actual execution path. Its downside | top of an emulator, and the analysis is completely per- |  |  |  |  |
| is lack of code coverage, although it can be ameliorated | formed from the outside. By integrating the changes into |  |  |  |  |
| by exploiting multiple execution paths [6, 9, 31]. | The | the emulator, the Android system remains unchanged |  |  |  |
| Android SDK includes a set of tools, such as | adb | and | and different virtual devices can be loaded. To ensure the |  |  |
| logcat | , to help developers debug their Apps. | With | best compatibility with virtual Android devices, we ex- |  |  |
| JDWP (Java Debug Wire Protocol) support, the debug- | tended the QEMU [3] based Android emulator that ships |  |  |  |  |
| ger can even exist outside of the device. However, just | with the Android SDK. This is done in three aspects: 1) |  |  |  |  |
| like how desktop malware detects and disables debug- | we introspect the guest Android system and reconstruct |  |  |  |  |
| gers, malicious Android Apps can also detect the pres- | OS-level and Java-level views simultaneously; 2) as a |  |  |  |  |
| ence of these tools, and then either evade or disable the | key binary analysis technique, we implement dynamic |  |  |  |  |
| analysis. The fundamental reason is that the debugging | taint analysis; and 3) we provide an analysis interface to |  |  |  |  |
| components and malware reside in the same execution | help analysts build custom analysis tools. Furthermore, |  |  |  |  |
| environment with the same privileges. | we made similar changes to a different version of QEMU |  |  |  |  |

---

## Page 4

to enable x86 support. enable basic instrumentation support.

To demonstrate the capabilities of DroidScope, we

have developed several analysis tools on it. The API

tracer monitors the malware’s activities at the API level

to reason about how the malware interacts with the An-

droid runtime environment. This tool monitors how the

malware’s Java components communicate with the An-

droid Java framework, how the native components inter-

act with the Linux system, and how Java components and

native components communicate through the JNI inter-

face.

The native instruction tracer and Dalvik instruction

tracer look into how a malicious App behaves internally

by recording detailed instruction traces. The Dalvik in-

struction tracer records Dalvik bytecode instructions for

the malware’s Java components and the native instruc-

tion tracer records machine-level instructions for the na-

tive components (if they exist).

The taint tracker observes how the malware obtains

and leaks sensitive information (e.g., GPS location, IMEI

and IMSI) by leveraging the taint analysis component

in DroidScope. Dynamic taint analysis has been pro-

posed as a key technique for analyzing desktop malware

particularly with respect to information leakage behav-

ior [18, 39]. It is worth noting that DroidScope performs

dynamic taint analysis at the machine code level. With

We discuss our methodology for rebuilding the two lev-

els of semantic views in this section. We first discuss how

information about processes, threads, memory mappings

and system calls are rebuilt at runtime. This constitutes

the OS-level view. Then from the memory mapping, we

locate the Dalvik Virtual Machine and further rebuild the

Java or Dalvik-level view.

4.1 Reconstructing the OS-level View

4

Basic Instrumentation QEMU is an efficient CPU em-

ulator that uses dynamic binary translation. The normal

execution flow in QEMU is as follows: 1) a basic block

of guest instructions is disassembled and translated into

an intermediate representation called TCG (Tiny Code

Generator); 2) the TCG code block is then compiled

down to a block of host instructions and stored in a

code cache; and 3) control jumps into the translated code

block and guest execution begins. Subsequent execution

of the same guest basic blocks will skip the translation

phase and directly jump into the translated code block in

the cache.

To perform analysis, we need to instrument the trans-

lated code blocks. More specifically, we insert extra

TCG instructions during the code translation phase, such

that this extra analysis code is executed in the execu-

tion phase. For example. in order to monitor context

switches, we insert several TCG instructions to call a

helper function whenever the translation table registers

(system control co-processor c2 base0 and c2 base1 in

QEMU) are written to.

With basic instrumentation support, we extract the fol-

lowing OS-level semantic knowledge: system calls, run-

ning processes, including threads, and the memory map.

To obtain the system call information, we instrument

instructions, to call a callback function that retrieves ad-

ditional information from memory. For important sys-

tem calls (e.g. open, close, read, write, connect, etc.), the

system call parameters and return values are retrieved as

well. As a result, we are able to understand how a user-

level process accesses the file system and the network,

communicates with another process, and so on.

Processes and Threads From the operating system per-

spective, Android Apps are user-level processes. There-

| semantic knowledge at both OS and Java levels, Droid- | System Calls | A user-level process has to make system |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Scope is able to detect information leakage in Java com- | calls to access various system resources and thus obtain- |  |  |  |  |
| ponents, native components, or even collusive Java and | ing its system call behavior is essential for understanding |  |  |  |  |
| native components. | malicious Apps. On the ARM architecture, the service |  |  |  |  |
| We have implemented DroidScope to support both | zero instruction | svc #0 | (also known as | swi #0 | ) is used to |
| ARM and x86 Android systems. Due to the fact that the | make system calls with the system call number in register |  |  |  |  |
| ARM architecture is most widely used for today’s mo- | R7 | . This is similar to x86 where the | int 0x80 | instruction |  |
| bile platforms, we focus our discussion on ARM support, | is used to transition into privileged mode and the system |  |  |  |  |
| which is also more extensively tested. | call number is passed through the | eax | register. |  |  |
| 4 | Semantic View Reconstruction | these special instructions, i.e. insert the additional TCG |  |  |  |
| The OS-level view is essential for analyzing native com- | fore, it is important to know what processes are active |  |  |  |  |
| ponents. It also serves a basis for obtaining the Java-level | and which one is currently running. In Linux kernel 2.6, |  |  |  |  |
| view for analyzing Java components. | The basic tech- | the version used in Gingerbread (Android 2.3), the basic |  |  |  |
| niques for reconstructing the OS-level view have been | executable unit is the task which is represented by the |  |  |  |  |
| well studied for the x86 architecture and are generally | task struct | structure. A list of active tasks is main- |  |  |  |
| known as virtual machine introspection [16, 21, 24]. We | tained in a | task struct | list which is pointed to by |  |  |
| employ similar techniques in DroidScope. We begin by | init task | . To make this information readily available |  |  |  |
| first describing our changes to the Android emulator to | to analysis tools, DroidScope maintains a shadow task |  |  |  |  |

---

## Page 5

list with select information about each task.

parent pid .

Special attention is paid to a task’s name since the

comm field in task struct can only store up to 15

characters. This is often insufficient to store the App’s

To address this issue, we also obtain the complete appli-

cation name from the command line cmdline , which

is pointed to by the mm struct structure pointed to by

task struct . Note that the command line is located

in user-space memory, which is not shared like kernel-

space memory where all the other structures and fields

Memory Map The Dalvik Virtual Machine, libraries

and dex files are all memory mapped and we rely on the

knowledge of their memory addresses for introspection.

Therefore, it is important to understand the memory map

of an App. This is especially true for the latest version of

Android, Ice Cream Sandwich, since address space lay-

out randomization is enabled by default.

5

Opcode * 0x40 ldrh r7, [r4, #2]!

and ip, r7, #255

0x0 sub sp, sp, #4

nop

move/from16 nop

lsr r9, r7, #8

| 0x800 | cmp r0, #0 |
| --- | --- |
| array-length | . |

beq<dvmAsmSisterStart+0xe4>

Figure 3: Dalvik Opcode Emulation Layout in mterp

With the OS-level view and knowledge of how the DVM

operates internally, we are able to reconstruct the Java or

Dalvik view, including Dalvik instructions, the current

machine state, and Java objects. Some of the details are

presented in this section.

responding emulation block.

This design also simplifies the reverse conversion from

native to Dalvik instructions as well: when the pro-

gram counter ( R15 ) points to any of these code re-

gions, we are sure that the DVM is interpreting a byte-

code instruction. Furthermore, it is trivial to determine

the opcode of the currently executing Dalvik instruc-

tion. In DroidScope we first identify the virtual ad-

dress of rIBase, the beginning of the emulation code re-

| To distinguish between a thread and a process, we | add pc, r8, ip, lsl #6 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gather a task’s process identifier | pid | as well as its thread | rIBase:dvmAsmInstructionStart | push{r4,r5,r6,r7,r8,r9,sl,fp,lr} |  |  |  |  |  |  |  |
| group identifier | tgid | . | The | pgd | (the page global di- | 0x40 | nop | . |  |  |  |
| rectory that specifies the memory space of a process), | 0x80 | move | . |  |  |  |  |  |  |  |  |
| uid | (the unique user ID associated with each App), and | nop |  |  |  |  |  |  |  |  |  |
| the process’ name are also maintained as part of the | lsr | r3, r7, #12 |  |  |  |  |  |  |  |  |  |
| shadow task list. Additionally, our experience has shown | ldr | r0, [r5, r3, lsl #2] |  |  |  |  |  |  |  |  |  |
| that malware often escalates its privileges or spawns | and r9, r9, #15 |  |  |  |  |  |  |  |  |  |  |
| child process(es) to perform additional duties. | Thus, | 0x840 | instance-of | . |  |  |  |  |  |  |  |
| our shadow task list also contains the task’s credentials, | cmp r0, r1 |  |  |  |  |  |  |  |  |  |  |
| i.e. | uid, gid, | euid, | egid | as well as the process’ | b<dvmAsmSisterStart+0xd0> |  |  |  |  |  |  |
| full name, making it difficult to pinpoint a specific App. | 4.2 | Reconstructing the Dalvik View |  |  |  |  |  |  |  |  |  |
| reside. To retrieve it, we must walk the task’s page table | Dalvik Instructions | The DVM’s main task is to exe- |  |  |  |  |  |  |  |  |  |
| to translate the virtual address into a physical one and | cute Dalvik bytecode instructions by translating them |  |  |  |  |  |  |  |  |  |  |
| then read it based on the physical address. | into corresponding executable machine code. In Ginger- |  |  |  |  |  |  |  |  |  |  |
| According to the design of the Linux kernel, | the | bread and thereafter, it does so in two ways: interpreta- |  |  |  |  |  |  |  |  |  |
| task struct | for the current process can be easily | tion and Just-In-Time compilation (JIT) [8]. |  |  |  |  |  |  |  |  |  |
| located. | The current | thread info | structure is al- | The | interpreter, | named | mterp | , | uses | an | offset- |
| ways located at the ( | stack pointer & | 0x1FFF | ), and | addressing method to map Dalvik opcodes to machine |  |  |  |  |  |  |  |
| thread info | has a pointer pointing to the current | code blocks as shown in Figure 3. Each opcode has 64 |  |  |  |  |  |  |  |  |  |
| task struct | . | We iterate through all active tasks by | bytes of memory to store the corresponding emulation |  |  |  |  |  |  |  |  |
| following the doubly linked | task struct | list. | We | code, and any emulation code that does not fit within the |  |  |  |  |  |  |  |
| also update our shadow list whenever the base informa- | 64 bytes use an overflow area, | dvmAsmSisterStart | , |  |  |  |  |  |  |  |  |
| tion changes. We do this by monitoring four system calls | (see | instance-of | in Figure 3). This design simpli- |  |  |  |  |  |  |  |  |
| sys fork | , | sys execve | , | sys clone | and | sys prctl | , and updat- | fies the emulation of Dalvik instructions. mterp simply |  |  |  |
| ing the shadow task list when they return. | calculates the offset, | opcode | ∗ | 64, and jumps to the cor- |  |  |  |  |  |  |  |
| To obtain the memory map of a process, we iterate | gion, and then calculate the opcode using the formula |  |  |  |  |  |  |  |  |  |  |
| through the process’ list of virtual memory areas by fol- | ( | R | 15 | − | rIBase | ) | / | 64. | rIBase is dynamically calculated |  |  |
| lowing the | mmap | pointer in the | mm struct | pointed to | as the virtual address of | libdvm.so | (obtained from the |  |  |  |  |
| by the | task struct | . | To ensure the freshness of the | shadow memory map in the OS-level view) plus the off- |  |  |  |  |  |  |  |
| memory map information, we intercept the | sys mmap2 | set of | dvmAsmInstructionStart | (a debug sym- |  |  |  |  |  |  |  |
| system call and update the shadow memory map when it | bol). If the debug symbol is not available, we can identify |  |  |  |  |  |  |  |  |  |  |
| returns. | it using the signature for Dalvik opcode number | 0 | ( | nop | ). |  |  |  |  |  |  |

---

## Page 6

| Update | R0: | V4 (In 2) | Integer |
| --- | --- | --- | --- |
| Program Counter(PC) | R1: | V3 (In 1) | String |

| Is Code in JIT | Yes | Execute JIT |
| --- | --- | --- |
| Decrement block | Yes | Request JIT |

Code block and

reset Counter

No

Emulate Code

Using mterp

Figure 4: High Level Flowchart of mterp and JIT

The Just-In-Time compiler was introduced to improve

Figure 4 shows the general flow of the DVM. When

a basic block of Dalvik bytecode needs to be emulated,

the Dalvik program counter is updated to reflect the new

block’s address. That address is then checked against

the translation cache to determine if a translated trace for

the block already exists. If it does, the trace is executed.

6

| R2: | V2 (In 0) | “this” |
| --- | --- | --- |
| R3: | Stack grows | V1 |
| R4: rPC | V0 |  |

R5: rFP

R6: rGLUE

R7: rINST

| R8: rIBASE | { |
| --- | --- |
| R9: | … |

R10:

...

R12: Thread* self;

R13:

libdvm.so …

R14: mterp

R15: PC+4

framework.jar@

classes.dex

low address

android.app.ContextImpl.SharedPreferencesImpl.getInt:(Ljava/lang/String;I)I:

Figure 5: Dalvik Virtual Machine State

code.

ing the JIT cache as full during the next garbage collec-

tion event, which leads to a cache flush. While this is not

a perfect solution, we have found it to be sufficient.

In all cases, the only side effect is wasted CPU cy-

cles due to compilation; the execution logic is unaffected.

Therefore, the side effects are deemed inconsequential.

| code cache? | code block | InterpState |  |  |  |
| --- | --- | --- | --- | --- | --- |
| No | R11: | InterpState | Jvalue retval; |  |  |
| Counter | Is Counter 0? | Compilation for | } |  |  |
| performance by compiling heavily used, or hot, Dalvik | The | dvmGetCodeAddr | function is used to deter- |  |  |
| instruction traces (consisting of multiple code blocks) di- | mine whether a translated trace exists. It returns | NULL |  |  |  |
| rectly into native machine code. While each translation | if a trace does not exist and the address of the corre- |  |  |  |  |
| trace has a single entry point, there can be multiple ex- | sponding trace if it does. | Thus, to selectively disable |  |  |  |
| its known as | chaining cells | . These chaining cells either | JIT, we instrument the DVM and set the return value of |  |  |
| chain to other translation traces or to default entry points | dvmGetCodeAddr | to | NULL | for any translated trace we |  |
| of the mterp interpreter. Overall, JIT provides an excel- | wish to disable. To show that our change to the virtual |  |  |  |  |
| lent performance boost for programs that contain many | machine state does not have any ill side-effects, we make |  |  |  |  |
| hot code regions, although it makes fine-grained instru- | the following arguments. | First, if the original return |  |  |  |
| mentation more difficult. This is because JIT performs | value was | NULL | then our change will not have any side |  |  |
| optimization on one or more Dalvik code blocks and thus | effects. Second, if the return value was a valid address, |  |  |  |  |
| blurs the Dalvik instruction boundaries. | then by setting it to | NULL | , the profile counter is decre- |  |  |
| An easy solution would be to completely disable JIT | mented and if 0, i.e. the code region deemed hot again, |  |  |  |  |
| at build time, but it could incur a heavy performance | another compilation request is issued for the block. | In |  |  |  |
| penalty and more importantly it require changes to the | this case, the code will be recompiled taking up space in |  |  |  |  |
| virtual device, which we want to avoid. | Considering | the code-cache. This can be prevented by not instrument- |  |  |  |
| that we are often only interested in a particular section | ing the | dvmGetCodeAddr | call from the compiler. |  |  |
| of Dalvik bytecode (such as the main program but not | In addition to preventing the translated trace from be- |  |  |  |  |
| the rest of system libraries), we choose to | selectively | dis- | ing executed, setting the value to | NULL | also prevents it |
| able JIT at runtime. | Analysis plugins can specify the | from being chained to other traces. This is the desired |  |  |  |
| code regions for which to disable JIT and as a result only | behavior. For the special case where a translation trace |  |  |  |  |
| the Dalvik blocks being analyzed incur the performance | has already been chained and thus | dvmGetCodeAddr |  |  |  |
| penalty. | All other regions and Apps still benefit from | is not called, we flush the JIT cache whenever the dis- |  |  |  |
| JIT. | abled JIT’ed code regions change. This is done by mark- |  |  |  |  |
| If it does not then the profiler will decrement a counter | DVM State | Figure 5 illustrates how the DVM main- |  |  |  |
| for that block. | When this counter reaches 0, the block | tains the virtual machine state. When mterp is emulating |  |  |  |
| is considered hot and a JIT compilation requested. | To | Dalvik instructions, the ARM registers | R4 | through | R8 |
| prevent thrashing, the counter is reset to a higher value | store the current DVM execution context. More specifi- |  |  |  |  |
| and emulation using mterp commences. As can be seen | cally, | R4 | is the Dalvik program counter, pointing to the |  |  |
| in the flow chart, as long as the requested code is not in | current Dalvik instruction. | R5 | is the Dalvik stack frame |  |  |
| the code cache, then mterp will be used to emulate the | pointer, pointing to the beginning of the current stack |  |  |  |  |

---

## Page 7

struct Object { struct StringObject { struct ArrayObject {

u4 lock; u4 instanceData[1]; u4 length;

};

| ClassObject | * | ClassObject | * |
| --- | --- | --- | --- |
| lock | lock |  |  |
| hashcode | 0x0048 'H', 0x0045 'e' |  |  |
| instanceData | count | (5) | 0x006f 'o', 0x0000 |

contents

0x0000, 0x0000

frame. R6 points to the InterpState data structure,

called glue . R7 contains the first two bytes of the cur-

rent Dalvik instruction, including the opcode. Finally R8

stores the base address of the mterp emulation code for

the current DVM instruction. In x86, edx , esi , edi

and ebx are used to store the program counter, frame

pointer, mterp base address and the first two bytes of the

instruction respectively. The glue object can be found

on the stack at a predefined offset.

Dalvik virtual registers are 32 bits and are stored in

reverse order on the stack. They are referenced relative

to the frame pointer R5 . Hence, the virtual register V0

is located at the top of the stack (pointed to by the ARM

register R5 ,) and the virtual register V1 sits on top of V0

in memory, and so forth. All other Dalvik state infor-

mation (such as return value and thread information) is

obtained through glue pointed to by R6 .

After understanding how DVM state is maintained, we

are able to reconstruct the state from the native machine

and relative data structures, we can get the current DVM

program counter, frame pointer, all virtual registers, and

so on.

sentations, Dalvik creates a ClassObject for each defined

time object instance, i.e. member fields. Each Object

7

fields. Dalvik defines three types of Objects, DataOb-

Object* fully depends on the ClassObject that it points

to.

data structures involved as well as the struct defini-

tions on top. To access the String, we first follow the

reference in the virtual register V3 . Since Java ref-

ject. To determine the type of the object, we follow

the first 4 bytes to the ClassObject structure. This Clas-

sObject instance describes the java.lang.String

class. Internally, Dalvik does not store the String data

inside the StringObject and instead use a char[] .

Consequently, instanceData[0] is used to store

the reference to the corresponding char[] object and

instanceData[3] is used to store the number of

characters in the String, 5 in this case.

We then obtain the String’s data by following

instanceData[0] to the character array. Once again

we must follow the Object* within the new object to

correctly interpret it as an ArrayObject. Note that since

ARM EABI requires all arrays to be aligned to its ele-

ment size and u8 is 8 bytes in length, we inserted an im-

plicit 4 byte align pad into the ArrayObject to ensure

that the contents array is properly aligned. Given the

length of the String from the StringObject and the cor-

roborating length in the ArrayObject, the ”Hello” String

is found in the contents array encoded in UTF-16.

Symbols (such as function name, class name, field name,

etc.) provide valuable information for human analysts to

understand program execution. Thus, DroidScope seeks

the database.

bytecode.

| ClassObject* | clazz; | Object | obj; | Object | obj; | has a pointer to the ClassObject that it is an instance |
| --- | --- | --- | --- | --- | --- | --- |
| }; | }; | u8 | contents[1]; | of plus a | tail accumulator array | for storing all member |
| java.lang.String ClassObject | ject | , | StringObject | and | ArrayObject | that are all pointed to |
| V3 (In 1) | char[] ClassObject | by generic | Object* | s. The correct interpretation of any |  |  |
| ArrayObject | * | align | _ | pad | We use a simple String (”Hello”) to illustrate the |  |
| offset | (0) | 0x006c 'l', 0x006c 'l' | interpretation process. | Figure 6 depicts the different |  |  |
| Figure 6: String Object Example | erences are simply | Object* | s, | V3 | points to an Ob- |  |
| code execution. That is, by examining the ARM registers | 4.3 | Symbol Information |  |  |  |  |
| Java Objects | Java Objects are described using two data | to make the symbols readily available by maintaining a |  |  |  |  |
| structures. Firstly, | ClassObject | describes a class type and | symbol database. For portability and ASLR support, we |  |  |  |
| contains important information about that class: the class | use one database of offsets to symbols per module. At |  |  |  |  |  |
| name, where it is defined in a dex file, the size of the ob- | runtime, finding a symbol by a virtual address requires |  |  |  |  |  |
| ject, the methods, and the location of the member fields | first identifying the containing module using the shadow |  |  |  |  |  |
| within the object instances. To standardize class repre- | memory map, and then calculating the offset to search |  |  |  |  |  |
| class type and implicit class type, e.g. arrays. For exam- | Native library symbols are retrieved statically through |  |  |  |  |  |
| ple there is a ClassObject that describes a | char[] | which | objdump | and are usually limited to Android libraries |  |  |
| is used by | java.lang.String | . Moreover, if the App | since malware libraries are often stripped of all symbol |  |  |  |
| has a two dimensional array, e.g. | String[][] | , then | information. On the other hand, Dalvik or Java symbols |  |  |  |
| Dalvik creates a ClassObject to describe the | String[] | are retrieved dynamically and static symbol information |  |  |  |  |
| and another to describe the array of the previously de- | through | dexdump | is used as a fallback. This has the ad- |  |  |  |
| scribed | String[] | class. | vantage of ensuring the best symbol coverage for opti- |  |  |  |
| Secondly, as an abstract type, | Object | describes a run- | mized dex files and even dynamically generated Dalvik |  |  |  |

---

## Page 8

NativeAPI LinuxAPI DalvikAPI name), and end, and memory map update. One can also

| instruction begin/end context switch | Dalvik instruction begin |  |
| --- | --- | --- |
| register read/write | system call | method begin |
| memory r/w with pgd | get current context | interpret Java object |

disable JIT

Table 1: Summary of DroidScope APIs

pointed to by R6 has a field method that points to the

Method structure for the currently executing method.

There are times when this procedure fails though, e.g.

if the corresponding page of the dex file has not been

loaded into memory yet. In these cases, we first try to

look up the information in a local copy of the correspond-

ing dex file, and if that fails as well, use the static symbol

information from dexdump . DroidScope uses this same

basic method of relying on the DVM’s data structures to

retrive class and field names as well.

5 Interface & Plugins

taint analysis is implemented at the machine code level,

one can also set and check taint in memory and regis-

ters. Currently, the taint propagation engine only sup-

8

can also set and check taint in Java Objects as well.

5.2 Instrumentation Optimization

A general guideline for performance optimization in dy-

namic binary translation is to shift computation from the

cution time.

We follow this guideline in DroidScope. Conse-

quently, our instrumentation logic becomes more com-

plex. When registering for an event callback, one can

specify a specific location (such as a function entry) or a

memory range (to trace instructions or functions within a

particular module). Therefore, our instrumentation logic

supports single value comparisons and range checks for

controlling when and where event callbacks are inserted

during the translation phase.

The instrumentation logic is also dynamic, because we

often want to register and unregister a callback at execu-

reconstruct the Dalvik view and to perform analysis as

gins.

5.3 Sample Plugin

| Events | query symbols, obtain the task list, and get the current |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| memory read/write | task begin/end | execution context (e.g., current process and thread). At |  |  |  |  |
| block begin/end | task updated | the Dalvik level, one can instrument at the granularity |  |  |  |  |
| memory map updated | of Dalvik instructions and methods. One can query the |  |  |  |  |  |
| Query & Set | memory read/write | query symbol database query symbol database | Dalvik symbols, parse and interpret Java objects, read |  |  |  |
| register read/write | get task list | get/set DVM state | and modify DVM state, and selectively disable JIT for |  |  |  |
| taint set/check | taint set/check objects | certain memory regions. Through the Dalvik-view, one |  |  |  |  |
| We rely on the data structures of DVM to retrieve sym- | execution phase to the translation phase. For instance, if |  |  |  |  |  |
| bols at runtime. For example, the | Method | structure con- | we need to instrument a function call at address | x | using |  |
| tains two pointers of interest. | insns | points to the start | basic blocks, then we should insert the instrumentation |  |  |  |
| of the method’s bytecode, the symbol address, and | name | code for the block at | x | when it is being translated instead |  |  |
| points to the name. | Conveniently, the | glue | structure | of instrumenting every basic block and look for | x | at exe- |
| DroidScope exports an event based interface for instru- | tion time. | For example, when the virtual device starts, |  |  |  |  |
| mentation. We describe the general layout of the APIs, | only the OS-view instrumentation is enabled so the An- |  |  |  |  |  |
| present an example of how tools are implemented, and | droid system can start quickly as usual. When we start |  |  |  |  |  |
| finally describe available tools in this section. | analyzing an App, instrumentation code is inserted to |  |  |  |  |  |
| 5.1 | APIs | requested by the plugin. | When instrumenting a func- |  |  |  |
| DroidScope defines a set of APIs to facilitate custom | tion return, the return address will be captured from the |  |  |  |  |  |
| analysis tool development. The APIs provide instrumen- | link register | R14 | at the function entry during execution, |  |  |  |
| tation on different levels: native, OS and Dalvik, to mir- | and a callback is registered at the return address. | Af- |  |  |  |  |
| ror the context levels of a real Android device. At each | ter the function has returned, this callback is removed. |  |  |  |  |  |
| level, the analysis tool can register callbacks for different | Then when the analysis has finished, other instrumenta- |  |  |  |  |  |
| events, and also query or set various kinds of information | tion code is removed as well. To maintain consistency, |  |  |  |  |  |
| and controls. Table 1 summarizes these APIs. | DroidScope invalidates the corresponding basic blocks |  |  |  |  |  |
| At the native level, one can register callbacks for in- | in the translated code cache whenever necessary so that |  |  |  |  |  |
| struction start and end, basic block start and end, mem- | the new instrumentation logic can be enforced. Hence, |  |  |  |  |  |
| ory read and write, and register read and write. One can | the instrumentation logic in DroidScope is complex and |  |  |  |  |  |
| also read and write memory and register content. | As | dynamic. These details are hidden from the analysis plu- |  |  |  |  |
| ports copy and arithmetic operations, control flow depen- | Figure 7 presents sample code for implementing a simple |  |  |  |  |  |
| dencies are not tracked. | Dalvik instruction tracer. The | init | function at L19 will |  |  |  |
| At the OS level, one can register callbacks for context | be invoked once this plugin is loaded in DroidScope. In |  |  |  |  |  |
| switch, system call, task start, update (such as process | init | , it specifies which program to analyze by calling the |  |  |  |  |

---

## Page 9

1. void opcode_callback(uint32_t opcode) {

2. printf("[%x] %s\n", GET_RPC, opcodeToStr(opcode)); of the other bytecodes to improve performance. To log

3. } library calls from the App’s native components, we reg-

4.

5. void module_callback(int pid) { ister for the block end event for blocks that are located in

6. if (bInitialized || (getIBase(pid) == 0))

7. return; the App’s native components. When the callback for the

8.

9. gva_t startAddr = 0, endAddr = 0xFFFFFFFF; block end event is invoked, we check if the next block is

10. within the Apps native components or not. If not, we log

11. addDisableJITRange(pid, startAddr, endAddr);

12. disableJITInit(getGetCodeAddrAddress(pid)); this event.

13. addMterpOpcodesRange(pid, startAddr, endAddr);

14. dalvikMterpInit(getIBase(pid)); Native instruction tracer registers ARM or x86 in-

15. registerDalvikInsnBeginCb(&opcode_callback);

16. bInitialized = 1; struction callbacks to gather information about each in-

17. }

| 18. | struction including the raw instruction, its operands (reg- |
| --- | --- |
| 19. void _init() { | ister and memory) and their values. |

20. setTargetByName("com.andhuhu.fengyinchuanshuo");

21. registerTargetModulesUpdatedCb(&module_callback); Dalvik instruction tracer follows the basic logic of

22. }

the above example and logs the decoded instruction to

Figure 7: Sample code for Dalvik Instruction Tracer a file in the dexdump format. The operands, their values

and all available symbol information, e.g. class, field and

| setTargetByName | function. | It also registers a callback | method names, are logged as well. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| module callback | to be invoked when module informa- | Taint tracker | utilizes the dynamic taint analysis APIs |  |  |  |  |
| tion is updated. | module callback | will check if the DVM | to analyze information leakage in an Android App. | It |  |  |  |
| is loaded and if so, disable JIT for the entire memory | specifies sensitive information sources (such as IMEI, |  |  |  |  |  |  |
| space (L9 and L11.) | It also registers a callback, | op- | IMSI, and contact information) as tainted and keeps track |  |  |  |  |
| code callback | , for Dalvik instructions. | When invoked, | of taint propagation at the machine code level until they |  |  |  |  |
| opcode callback | prints the opcode information. | reach sinks, e.g. | sys write | and | sys send | . | With the OS |
| This sample code will print all Dalvik instructions for | and Dalvik views, it further creates a graphical represen- |  |  |  |  |  |  |
| the specified App, including the main program and all | tation to visualize how sensitive information has leaked |  |  |  |  |  |  |
| the libraries. | If we are only interested in the execu- | out. To construct the graph, we first identify function and |  |  |  |  |  |
| tion of the main program, we can add a function call | method boundaries. | Whenever taint is propagated, we |  |  |  |  |  |
| like | getModAddr(”example@classes.dex”, &startAddr, | add a node to represent the currently executing function |  |  |  |  |  |
| &endAddr) | at L10. This function locates the dex file in | or method and nodes for the tainted memory locations. |  |  |  |  |  |
| the shadow memory map and stores its start and end ad- | Since methods operate on Java Objects, we further try to |  |  |  |  |  |  |
| dresses in the appropriate variables. The rest of the code | identify the containing Object and create a node for it in- |  |  |  |  |  |  |
| can be left untouched. | stead of the simple memory location. Currently, we only |  |  |  |  |  |  |

do this check against the method’s input parameters and

| 5.4 | Analysis Plugins | the current Object, e.g. ”this”. Further improvements are |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| To demonstrate the capability of DroidScope for analyz- | left as future work. |  |  |  |  |  |  |
| ing Android malware, we have implemented four analy- | To identify method boundaries, we look for match- |  |  |  |  |  |  |
| sis plugins: API tracer, native instruction tracer, Dalvik | ing | invoke* | or | execute* | and | move-result* | Dalvik instruc- |
| instruction tracer, and taint tracker. | tions. We do not rely on the | return* | instructions since |  |  |  |  |
| API tracer | monitors how an App (including Java and | they are executed in the invokee context, which might not |  |  |  |  |  |
| native components) interacts with the rest of the sys- | be instrumented, e.g. inside an API. Since there are mul- |  |  |  |  |  |  |
| tem through system and library calls. | We first log all | tiple ways for native code to call and return from func- |  |  |  |  |  |
| of the App’s system calls by registering for system call | tions plus malicious code is known to jump into the mid- |  |  |  |  |  |  |
| events. We then build a whitelist of the virtual device’s | dle of functions, we do not rely on native instructions |  |  |  |  |  |  |
| built-in native and Java libraries. As modules are loaded | to determine function boundaries. Instead, we treat the |  |  |  |  |  |  |
| into memory, any library not in the whitelist is marked | nearest symbol that is less than or equal to the jump tar- |  |  |  |  |  |  |
| for analysis. | We instrument the | invoke* | and | execute* | get in the symbol database as the function. |  |  |

Dalvik bytecodes to identify and log method invoca-

6 Evaluation

tions, including those of the sample. The log contains

| the currently executing Java thread, the calling address, | We evaluated DroidScope with respect to efficiency and |  |  |  |
| --- | --- | --- | --- | --- |
| the method being invoked as well as a dump of its in- | capability. To evaluate efficiency, we used 7 benchmark |  |  |  |
| put parameters. Since Java Strings are heavily used, we | Apps from the official Android Market: AnTuTu Bench- |  |  |  |
| try to convert all Strings into native strings before log- | mark (ABenchMark) by AnTuTu, CaffeineMark by Ravi |  |  |  |
| ging them. | We then instrument the | move-result* | byte- | Reddy, CF-Bench by Chainfire, Mobile processor bench- |
| code instructions to detect when system methods return | mark (Multicore) by Andrei Karpushonak, Benchmark |  |  |  |
| and gather the return values. We do not instrument any | by Softweg, and Linpack by GreeneComputing. We then |  |  |  |

9

---

## Page 10

Percent of Baseline on the default Android emulator without any instrumen-

0% 20% 40% 60% 80% 100% 120% tation. Since DroidScope selectively disables JIT on the

Linpack/Multithread

Linpack/Singlethread

CPUBench (ms)

CFBench/Overall

0% 20% 40% 60% 80% 100% 120%

Dalvik Taint Tracker

Instruction

ran the benchmarks while using the different automatic

analysis tools described above on the benchmarks them-

selves. The results are presented in Section 6.1. To

evaluate capability, we analyzed two real world Android

tail, which will be presented in Sections 6.2 and 6.3.

These samples were obtained from the Android Malware

Genome project [40].

6.1 Performance

Apps, we also obtained a NOJIT baseline with JIT com-

pletely disabled at build time. The performance results

are summarized in the bar chart in Figure 8. Each tool

is associated with a set of bars that shows its benchmark

The ARM Instruction Tracer results are excluded as they

Please note that the benchmarks are not perfect repre-

results. For example, in CPUBenchmark the standard de-

is only 1%. This means that the results are consistent for

each plugin, but might not be across plugins. Further-

more, we removed the Softweg filesystem benchmarking

results due to high variability, σ > 27%.

( Context Only ) of reconstructing the OS-level view

has the worst performance as expected, because it reg-

curs 11x to 34x slowdown, which is comparable to other

special case is seen in the Dalvik instruction tracer re-

from guest memory for logging.

in some Java based benchmarks such as Linpack, CF-

the API tracer’s performance is greater than that of the

NOJIT Baseline, despite the fact that instrumentation is

taking place. This difference is due to Java libraries, such

as String methods, still benefiting from JIT in the API

tracer.

The DroidKungFu malware contains three components.

First, the core logic is implemented in Java and is con-

tained within the com.google.ssearch package.

unavailable at the time of our test and thus we did not

analyze this feature.

10

| Softweg/Memory | results (y-axis) relative to the baseline as a percentage. |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Softweg/Graphics | are similar to the taint tracker results. |  |  |  |  |  |  |  |  |
| Softweg/CPU | sentations of performance as evidenced by the | > | 100% |  |  |  |  |  |  |
| Multicore (ms) | viation, | σ | , for Baseline, Dalvik tracer and Context Only |  |  |  |  |  |  |
| CFBench/Java | We | can | see | from | Figure | 8 | that | the | overhead |
| CFBench/Native | is very small, up to 7% degradation. | The taint tracker |  |  |  |  |  |  |  |
| CaffieneMark | isters for instruction level events. | The taint tracker in- |  |  |  |  |  |  |  |
| ABenchMark | taint analysis tools [10, 39] on the x86 architecture. A |  |  |  |  |  |  |  |  |
| Percent of Baseline | sult for CaffeineMark. This result is attributed to the fact |  |  |  |  |  |  |  |  |
| NOJIT Baseline | Context Only | API Tracer | that the tracer dynamically retrieves symbol information |  |  |  |  |  |  |
| Tracer | The benefits of dynamically disabling JIT is evident |  |  |  |  |  |  |  |  |
| Figure 8: Benchmark Results | Bench/Java and CaffeineMark. | For those benchmarks, |  |  |  |  |  |  |  |
| malware samples: DroidKungFu and DroidDream in de- | 6.2 | Analysis of DroidKongFu |  |  |  |  |  |  |  |
| Experimental Setup | All experiments were conducted | This is the main target of our investigation. Second are |  |  |  |  |  |  |  |
| on an Acer 4830TG with a Core i5 @ 2.40GHz and 3GB | the exploit binaries which are encrypted in the apk, de- |  |  |  |  |  |  |  |  |
| of RAM running Xubuntu 11.10. The Android guest is | crypted by the Java component and then subsequently |  |  |  |  |  |  |  |  |
| a Gingerbread build configured as ”user-eng” for ARM | executed. Third is a native library that is used as a shell. |  |  |  |  |  |  |  |  |
| with the Linux 2.6.29 kernel and uses the QEMU default | It contains JNI exported functions that can run shell com- |  |  |  |  |  |  |  |  |
| memory size of 96 MB. No changes were made to the | mands and is the main interface for command and con- |  |  |  |  |  |  |  |  |
| Android source. | trol. Unfortunately the command and control server was |  |  |  |  |  |  |  |  |
| To measure the performance impact of instrumentation, | Discovering the Internal Logic | We began our investi- |  |  |  |  |  |  |  |
| we took the analysis tools and targeted the benchmark | gation by running the API tracer on the sample and an- |  |  |  |  |  |  |  |  |
| Apps while the Apps performed their tests. This was re- | alyzing the log. We first looked for system calls of in- |  |  |  |  |  |  |  |  |
| peated 5 times. As the baseline, we ran these benchmarks | terest and found a | sys open | for a file named “gjsvro”. |  |  |  |  |  |  |

---

## Page 11

getPermission { getDeviceId()

if checkPermission() then doSearchReport(); return

if exists("bin/su" or "xbin/su") then

getPermission2(); return

if !isVersion221() then getPermission3(); return

}

There was also a subsequent sys write to the file from

ally part of a Java ArrayObject which was populated

KungFu. Since decrypt takes a byte array as the param-

eter, we were able to search backwards and identify that

this particular array was read from an asset inside the

“chmod 4755” and the name of the file, making the file

executable and setting the setuid bit. After that, it called

Runtime.exec again for “su” which led to a sys fork . Fur-

thermore, the file path for “gjsvro” was then written to

a ProcessImpl OutputStream , followed immedi-

ately by “exit”. Since this stream is piped to the child’s

stdin , we know that the intention of “su” was to open a

shell which is then used to execute “gjsvro” followed by

“exit” to close the shell. This did not work though since

“su” did not execute successfully.

Next we used the Dalvik instruction tracer to obtain

a Dalvik instruction trace. The trace showed that the

decrypt and Runtime.exec methods were invoked from

a method called getPermission2 , which was called from

getPermission following a comparison using the result

of isVersion221 and some file existence checks. To get a

more complete picture of the getPermission method, we

ran dexdump and built the overview pseudocode shown

in Figure 9 . It is evident that to explore the getPermis-

sion1 and getPermission3 , we must instrument the sam-

ple and change the return values of the different method

invocations.

With the Dalvik view support, we manipulated the re-

turn values of isVersion221 and exist methods and were

able to explore all three methods getPermission1 , get-

Permission2 , and getPermission3 . They are essentially

different ways to obtain the root privilege on different

Android configurations. getPermission1 and getPermis-

sion2 only uses the “gjsvro” exploit. The main difference

is that getPermission1 uses Runtime.exec to execute the

exploit while the other uses the “su” shell. On the other

11

UrlEncodedFormEntity.<init>

String @ 0x4056a448

AbstractHttpClient.execute()

“POST /search/sayhi.php HTTP/1.1...”

Figure 10: Taint Graph for DroidKungFu

(ratc) exploits.

Analyzing Root Exploits Since Gingerbread has al-

ready been patched against these exploits, they never ex-

ecuted correctly. To further analyze these root exploits,

we first needed to remove the corresponding patches

from the virtual device build. Here we focus on “ratc,”

since “udev” is analyzed in the same manner. Due to

space constraints we present the exploit diagnosis of

“ratc” in Appendix A.

We first ran the API tracer on the ratc exploit, but did

not observe any malicious behavior in the API log. We

did see suspicious behavior in the process log provided as

part of the OS-view reconstruction. Particularly, we ob-

served that numerous ratc processes (descendants of the

original ratc process) were spawned, the adbd process

with uid 2000 ended, followed by more ratc processes

and then by an adbd process with uid 0 or root. This

signifies that the attack was successful. It is worth not-

ing that the traditional adb based dynamic analysis would

fail to observe the entire exploiting process because adbd

is killed at the beginning.

Further analysis of the logs and descendent processes

showed that there are in fact three types of ratc processes.

The first is the original ratc process that simply iterates

through the /proc directory looking for the pid of the

adbd process. Its child then forked itself until sys fork re-

turned -11 or EAGAIN. At this point it wrote some data

to a pipe and resumed forking. In the grandchild process

we see a call to sys kill to kill the adbd process followed

by attempts to locate the adbd process after it re-spawns.

| if !isVersion221() then | String @ 0x40524e80 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| if getPermission1() then return | “123456789012345” |  |  |  |  |
| Figure 9: getPermission Pseudocode | “imei=123456789012345&ostype=...” |  |  |  |  |
| a byte array. | We later found that this array is actu- | byte[ ] @ 405967c0 | / | void* @ 405967d0 |  |
| by the | Utils.decrypt | method, which is part of Droid- | sys_write(34, 0x405967d0, 397) |  |  |
| App’s package file called ”gjsvro”. | It means that dur- | Java and native components, our logs show that the li- |  |  |  |
| ing execution, DroidKungFu decrypts an asset from its | brary then calls | sys vfork | and | sys execve | to execute the |
| package and generates the ”gjsvro” file. We then found | commands. This indicates that | getPermission3 | was try- |  |  |
| that DroidKungFu called | Runtime.exec | with parameters | ing to run both “udev” exploit and “rage against the cage” |  |  |
| hand, | getPermission3 | decrypts “ratc”, “killall” (a wrap- | Triggering Data leakage | Reverting back to the default |  |
| per for “ratc”) and “gjsvro” and executes them using its | Gingerbread build, we sought to observe the informa- |  |  |  |  |
| own native library. | As the API tracer monitors both | tion leakage behavior in | doSearchReport | . | As depicted |

---

## Page 12

in Figure 9, this involves instrumenting checkPermission getSubscriberId()

during execution of getPermission . The Dalvik instruc-

Info , which obtains sensitive information about the de-

amongst other things. We also observed outgoing HTTP

then redirected these HTTP requests to our own HTTP

ther analyze this information leakage, we used the taint

which is shown in Figure 10. Objects, both Java and

native, are represented by rectangular nodes while meth-

codedFormEntity (the constructor) propagated the orig-

to a second String that looks like an HTTP request. The

AbstractHttpClient.execute . We finally see the taint ar-

riving at the sink at sys write . Note that sys write used

a void* at 0x405967d0, which is the contents array of

the byte array Object (see the StringObject example in

“com.droiddream.lovePositions:remote,” the other

process, is the malicious one. The logs show that Droid-

In order to observe this networking behavior, we instru-

ment the return values of sys connect and sys write to

make DroidDream believe these network operations are

12

“310260000000000”

String @ 0x40523288

crypt()

Figure 11: Taint Graph for DroidDream

SubscriberId is used to obtain the IMSI from the system

the encryption is being conducted on the byte[] in-place.

A snippet of the trace log is depicted in Figure 12.

Dream.

7 Discussion

| tion trace shows that | doSearchReport | invokes | update- | String @ 0x40522a10 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vice including the device model, build version and IMEI | Formatter.format() |  |  |  |  |  |  |  |
| requests, which failed because the server was down. We | “<?xml version="1.0" ...” |  |  |  |  |  |  |  |
| server by adding a new entry into | /etc/hosts | . | To fur- | getBytes() |  |  |  |  |
| tracker and built a simplified taint propagation graph, | byte[] @ 0x405232a8 |  |  |  |  |  |  |  |
| ods are represented by oval nodes. We see that | UrlEn- | ByteArrayInputStream |  |  |  |  |  |  |
| inal tainted IMEI number in the String @ 0x40524e80 | API Native Memory |  |  |  |  |  |  |  |
| taint then propagated to a byte array at 0x405967c0 by | sys_write(33, 405261a8, 257) |  |  |  |  |  |  |  |
| Section 4.2). This is expected since JNI provides direct | clude | crypt | which is the DroidDream method used to |  |  |  |  |  |
| access to arrays to save on the cost of | memcpy | . | xor-encrypt the byte array. | The graph shows that | get- |  |  |  |
| 6.3 | Analysis of DroidDream | as a String @ 0x40522a10. The IMSI String, along with |  |  |  |  |  |  |
| Like analyzing DroidKungFu, we first used the API | other information, is then encoded into an XML format |  |  |  |  |  |  |  |
| tracer to get a basic understanding of DroidDream, and | using | format | . The resulting String is then converted into |  |  |  |  |  |
| then obtained instruction traces and analyzed informa- | a byte[] @ 0x405232a8 for encryption by | crypt | . | The |  |  |  |  |
| tion leakage. | encrypted version is used to create a | ByteArrayInput- |  |  |  |  |  |  |
| From the log generated by the API tracer and the | Stream | . For brevity, we use a generic “API Native Mem- |  |  |  |  |  |  |
| shadow task list, we found that there are two Droid- | ory” node to illustrate that the taint further propagates |  |  |  |  |  |  |  |
| Dream processes. | “com.droiddream.lovePositions,” the | through memory until the eventual sink at | sys write | . |  |  |  |  |
| main process, does not exhibit any malicious behavior | We further investigated the | crypt | method by augment- |  |  |  |  |  |
| except using | Runtime.exec | to execute “logcat -c” which | ing the Dalvik instruction tracer to track taint propaga- |  |  |  |  |  |
| clears Android’s internal log. Again, this behavior indi- | tion and generate a taint-annotated Dalvik instruction |  |  |  |  |  |  |  |
| cates that traditional Android debugging tools fall short | trace. | Not only do we see the byte array being xor-ed |  |  |  |  |  |  |
| for malware analysis. | with a static field name “KEYVALUE,” we also see that |  |  |  |  |  |  |  |
| Dream retrieves the IMSI number along with other sen- | DroidDream | also | includes | the | udev | and | ratc | ex- |
| sitive information like IMEI, and encodes them into an | ploits (unencrypted), plus the native library terminal like |  |  |  |  |  |  |  |
| XML String. Then we observed a failed attempt to open | DroidKungFu. Since we have already analyzed them in |  |  |  |  |  |  |  |
| a network connection to | 184.105.245.17:8080 | . | DroidKungFu, we skipped the analysis on them in Droid- |  |  |  |  |  |
| successful. | Limited Code Coverage | Dynamic analysis is known to |  |  |  |  |  |  |
| Using the taint tracker, we marked these information | have limited code coverage, as it only explores a single |  |  |  |  |  |  |  |
| sources as tainted and obtained taint propagation graphs, | execution path at a time. To increase code coverage, we |  |  |  |  |  |  |  |
| which confirm that DroidDream did leak sensitive infor- | may explore multiple execution paths as demonstrated in |  |  |  |  |  |  |  |
| mation from these sources to a remote HTTP server. The | previous work [6, 9, 31]. In the experiments, we demon- |  |  |  |  |  |  |  |
| graph for leaking IMSI information is illustrated in Fig- | strated that we can discover different execution paths by |  |  |  |  |  |  |  |
| ure 11. We simplified the graph and annotated it to in- | manipulating the return values of system calls, native |  |  |  |  |  |  |  |

---

## Page 13

[43328f40] aget-byte v2(0x01), v4(0x405232a8), v0(186) ysis takes too long, certain timeout events are triggered

Getting Tainted Memory: 40523372(2401372)

[43328f4c] xor-int/2addr v2(62), v3(41)

Getting Tainted Memory: 410accec(42c5cec)

Adding M@410accec(42c5cec) len = 4

[43328f4e] int-to-byte v2(0x17), v2(23)

Adding M@410accec(42c5cec) len = 4

have not yet implemented symbolic execution and leave

it as future work. In particular, we seek to use tainting in

conjunction with the Dalvik view to implement a sym-

bolic execution engine at the Dalvik instruction level.

13

8 Related Work

structures (such as the task list) and extracting impor-

tant information from these data structures. For closed-

Android kernel, DroidScope is able to intercept certain

seamlessly.

Dynamic Binary Instrumentation PIN [27], Dy-

namoRIO [5], and Valgrind [32] are powerful dynamic

instrumentation tools that analyze user-level programs.

| Adding M@410accec(42c5cec) len = 4 | leading to different execution paths. | The analyst must |  |
| --- | --- | --- | --- |
| [43328f44] sget-object v3(0x0000005e), KEYVALUE// field@0003 | be aware of these new challenges. In summary, further |  |  |
| [43328f48] aget-byte v3(0x88), v3(0x4051e288), v1(58) | investigation in this area is needed. |  |  |
| Getting Tainted Memory: 410accec(42c5cec) | Virtual Machine Introspection | Virtual Machine Intro- |  |
| [43328f50] aput-byte v2(0x17), v4(0x405232a8), v0(186) | spection is a family of techniques that rebuild a guest’s |  |  |
| Getting Tainted Memory: 410accec(42c5cec) | context from the virtual machine monitor [21, 24]. This |  |  |
| Adding M@40523372(2401372) len = 1 | is achieved by understanding the important kernel data |  |  |
| Figure 12: | Excerpt of Dalvik Instruction Trace for | source operating systems, it is difficult to have complete |  |
| DroidDream. | A Dalvik instruction entry shows the location | understanding of the kernel data structures. To solve this |  |
| of the current instruction in square brackets, the decoded in- | problem, Dolan-Gavitt et al. developed a technique that |  |  |
| struction plus the values of the virtual registers in parenthesis. | automatically generates introspection tools by first mon- |  |  |
| A taint log entry is indented and shows tainted memory being | itoring the execution of a similar tool within the guest |  |  |
| read or written to. The memory’s physical address is shown in | system and then mimicking the same execution outside |  |  |
| parenthesis and the total bytes tainted is represented by ”len.” | of the guest system [16]. With deep understanding of the |  |  |
| APIs and even internal Dalvik methods of the App. This | kernel functions and traverse proper kernel data struc- |  |  |
| simple approach works fairly well in practice although a | tures to reconstruct the OS level view. | In comparison, |  |
| more systematic approach is desirable. One method is to | DroidScope takes it one step further to reconstruct the |  |  |
| perform symbolic execution to compute path constraints | Dalvik/Java view, such that both Java and native compo- |  |  |
| and then automatically explore other feasible paths. We | nents from an App can be analyzed simultaneously and |  |  |
| Detecting and Evading DroidScope | In the desktop en- | They are less ideal for malware analysis, because they |  |
| vironment, malware becomes increasingly keen to the | share the same memory space with user-level mal- |  |  |
| execution environment. Emulation-resistant malware de- | ware and thus can be subverted. | Bernat et al. | used |
| tect if they are running within an emulated environment | a formal model to identify observable differences due |  |  |
| and evade analysis by staying dormant or simply crash- | to instrumentation of | sensitive | instructions and created |
| ing themselves. Researchers have studied this problem | a | sensitivity-resistant | instrumentation tool called SR- |
| for desktop malware [2, 26, 36]. The same problem has | Dyninst [4]. | Like the other tools though, it cannot be |  |
| not arisen for Android malware analysis. | However, as | used to analyze kernel-level malware. |  |
| DroidScope or similar analysis platforms become widely | Anubis [1], PinOS [7], TEMU [35], and Ether [15] are |  |  |
| adopted to analyze Android malware, we anticipate sim- | based on CPU emulators and hypervisors. They have the |  |  |
| ilar evasion techniques will eventually appear. As mal- | full system view of the guest system and thus are better |  |  |
| ware may detect the emulated environment using emula- | suited for malware analysis. | These systems only sup- |  |
| tion bugs in the emulator, some efforts have been made to | port the x86 architecture and Ether, in principle, cannot |  |  |
| detect bugs in the CPU emulators and thus can improve | support ARM, because it relies on the hardware virtual- |  |  |
| emulation accuracy [28, 29]. | ization technology on x86. A new port must be devel- |  |  |
| More troubling are the intrinsic differences between | oped for ARM virtualization [30]. | While Atom based |  |
| the emulated environment and mobile systems. Mobile | mobile platforms are available, ARM still dominates the |  |  |
| devices contain numerous sensors, e.g. GPS, motion and | Android market and thus ARM based analysis is impor- |  |  |
| audio, with performance profiles which might be difficult | tant. | To the best of our knowledge, DroidScope is the |  |
| to emulate. | While exploring multiple execution paths | first fine-grained dynamic binary instrumentation frame- |  |
| may be used to bypass these types of tests, they might | work that supports the ARM architecture and provides a |  |  |
| still not be sufficient. | For example we have observed | comprehensive interface for Android malware analysis. |  |
| that Android, as an interactive platform, can be sensitive | We do not however support control flow tainting or dif- |  |  |
| to the performance overhead due to analysis. If the anal- | ferent tainting profiles like Dytan [10]. Since Dytan is |  |  |

---

## Page 14

| based on PIN, it is theoretically feasible to port the tool | References |  |  |
| --- | --- | --- | --- |
| to PIN for ARM [23], although it will still be limited to | [1] Anubis: | Analyzing Unknown Binaries. | http://anubis. |
| analyzing user-level malware. | iseclab.org/ | . |  |

violations [20]. While powerful, the authors note that

covery failures. DroidRanger is a static analysis tool that

operates on Dalvik bytecode directly and was success-

and across API calls. DroidBox is a project that uses

TaintDroid to build an android application sandbox for

cies that come with a real device are there. This can’t be

9 Conclusion

els of semantic information: operating system and Java.

This information is provided to the user in a unified in-

malware sample’s Java and native components as well

as evidenced by the successful analysis of DroidKungFu

and DroidDream using DroidScope. These capabilities

opinions, findings, and conclusions made in this material

14

[2] B ALZAROTTI , D., C OVA , M., K ARLBERGER , C., K RUEGEL ,

February 2010).

In USENIX Annual Technical Conference, FREENIX Track (April

2005).

[4] B ERNAT , A. R., R OUNDY , K., AND M ILLER , B. P. Efficient,

Symposium on Code Generation and Optimization (CGO’03)

(March 2003).

[6] B RUMLEY , D., H ARTWIG , C., K ANG , M. G., L IANG , Z., N EW -

2007.

framework for whole-system dynamic instrumentation. In Pro-

google.com/events/io/2010/sessions/

jit-compiler-androids-dalvik-vm.html , 2010.

Google I/O.

Proceedings of the 16th International Conference on Architectural

Support for Programming Languages and Operating Systems (AS-

PLOS) (Mar. 2011).

(2007), pp. 196–206.

attack prevention orthogonal to memory model. In Proceedings

of the 37th International Symposium on Microarchitecture (MI-

CRO’04) (December 2004).

http://archive.hack.lu/2010/Desnos_Dynamic_

[15] D INABURG , A., R OYAL , P., S HARIF , M., AND L EE , W. Ether:

L EE , W. Virtuoso: Narrowing the semantic gap in virtual ma-

chine introspection. In Proceedings of the 2011 IEEE Symposium

| Dalvik Analysis Tools | Enck et al. used | ded | to convert | C., K | IRDA | , E., | AND | V | IGNA | , G. | Efficient Detection of Split |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dalvik bytecode into Java bytecode and | soot | to further | Personalities in Malware. | In | Proceedings of the Network and |  |  |  |  |  |  |  |  |
| convert it into Java source code to identify data flow | Distributed System Security Symposium (NDSS) | (San Diego, CA, |  |  |  |  |  |  |  |  |  |  |  |
| some violations could not be identified due to code re- | [3] B | ELLARD | , F. | QEMU, a fast and portable dynamic translator. |  |  |  |  |  |  |  |  |  |
| ful in identifying previously unknown malicious Apps in | sensitivity resistant binary instrumentation. In | Proceedings of the |  |  |  |  |  |  |  |  |  |  |  |
| Android marketplaces [41]. | TaintDroid and DroidBox | 2011 International Symposium on Software Testing and Analysis |  |  |  |  |  |  |  |  |  |  |  |
| are two examples of dynamic analysis tools for Android | (New York, NY, USA, 2011), ISSTA ’11, ACM, pp. 89–99. |  |  |  |  |  |  |  |  |  |  |  |  |
| applications [17, 19]. | TaintDroid is a specially crafted | [5] B | RUENING | , D., G | ARNETT | , T., | AND | A | MARASINGHE | , S. An in- |  |  |  |
| DVM that supports taint analysis of Dalvik instructions | frastructure for adaptive dynamic optimization. In | International |  |  |  |  |  |  |  |  |  |  |  |
| analysis purposes. The biggest advantage of using Taint- | SOME | , J., P | OOSANKAM | , P., | AND | S | ONG | , D. | BitScope: Auto- |  |  |  |  |
| Droid is that it runs on actual devices. All of the hard- | matically dissecting malicious binaries. | Tech. Rep. CS-07-133, |  |  |  |  |  |  |  |  |  |  |  |
| ware, sensors, vendor software and unpredictable intrica- | School of Computer Science, Carnegie Mellon University, Mar. |  |  |  |  |  |  |  |  |  |  |  |  |
| achieved in an emulated environment. The major nega- | [7] B | UNGALE | , P. P., | AND | L | UK | , C.-K. | PinOS: a programmable |  |  |  |  |  |
| tive of all these tools is that they are limited to analyzing | ceedings of the 3rd international conference on Virtual execution |  |  |  |  |  |  |  |  |  |  |  |  |
| the Java portion of Apps. Thus, if there is a native com- | environments | (2007), VEE ’07, pp. 137–147. |  |  |  |  |  |  |  |  |  |  |  |
| ponent, like DroidKungFu has, they will not be able to | [8] C | HENG | , | B., | AND | B | UZBEE | , | B. | A | JIT | com- |  |
| fully analyze it. | piler | for | android’s | dalvik | VM. | http://www. |  |  |  |  |  |  |  |
| We presented DroidScope, a fine grained dynamic binary | [9] C | HIPOUNOV | , V., K | UZNETSOV | , V., | AND | C | ANDEA | , G. | S2E: A |  |  |  |
| instrumentation tool for Android that rebuilds two lev- | platform for in-vivo multi-path analysis of software systems. In |  |  |  |  |  |  |  |  |  |  |  |  |
| terface to enable dynamic instrumentation of both the | [10] C | LAUSE | , J., L | I | , W., | AND | O | RSO | , A. Dytan: a generic dynamic |  |  |  |  |
| Dalvik bytecode as well as native instructions. | In this | taint analysis framework. | In | Proceedings of the 2007 Interna- |  |  |  |  |  |  |  |  |  |
| manner, the analyst is able to reveal the behavior of a | tional Symposium on Software Testing and Analysis (ISSTA’07) |  |  |  |  |  |  |  |  |  |  |  |  |
| as interactions between them and the rest of the system | [11] C | RANDALL | , J. R., | AND | C | HONG | , F. T. | Minos: | Control data |  |  |  |  |
| are provided to the analyst without changing the guest | [12] Cve-2009-1185. | http://cve.mitre.org/cgi-bin/ |  |  |  |  |  |  |  |  |  |  |  |
| Android system and particularly with JIT intact. Our per- | cvename.cgi?name=CVE-2009-1185 | . |  |  |  |  |  |  |  |  |  |  |  |
| formance evaluation showed the benefits of dynamically | [13] ded: Decompiling Android Applications. | http://siis.cse. |  |  |  |  |  |  |  |  |  |  |  |
| disabling JIT for targeted analysis such as API tracing. | psu.edu/ded/index.html | . |  |  |  |  |  |  |  |  |  |  |  |
| The overall performance seems reasonable as well. | [14] Dynamic, | metamorphic | (and | opensource) | virtual | machines. |  |  |  |  |  |  |  |
| Acknowledgements | Metamorphic_Virtual_Machines-slides.pdf | . |  |  |  |  |  |  |  |  |  |  |  |
| We thank the anonymous reviewers for their insightful | malware analysis via hardware virtualization extensions. In | Pro- |  |  |  |  |  |  |  |  |  |  |  |
| comments towards improving this paper. | This work is | ceedings of the 15th ACM Conference on Computer and Commu- |  |  |  |  |  |  |  |  |  |  |  |
| supported in part by the US National Science Founda- | nications Security | (2008), pp. 51–62. |  |  |  |  |  |  |  |  |  |  |  |
| tion NSF under Grants #1018217 and #1054605. | Any | [16] D | OLAN | -G | AVITT | , B., L | EEK | , T., Z | HIVICH | , M., G | IFFIN | , J., | AND |
| are those of the authors and do not necessarily reflect the | on Security and Privacy | (Washington, DC, USA, 2011), SP ’11, |  |  |  |  |  |  |  |  |  |  |  |
| views of the NSF or the Air Force Research Laboratory. | IEEE Computer Society, pp. 297–312. |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 15

| [17] Droidbox: | Android application sandbox. | http://code. | [34] Proguard. | http://proguard.sourceforge.net | . |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google.com/p/droidbox/ | . | [35] TEMU: The BitBlaze dynamic analysis component. | http:// |  |  |  |  |  |  |  |  |  |  |  |
| [18] E | GELE | , M., K | RUEGEL | , C., K | IRDA | , E., Y | IN | , H., | AND | S | ONG | , D. | bitblaze.cs.berkeley.edu/temu.html | . |

Dynamic Spyware Analysis. In Proceedings of the 2007 Usenix

Annual Conference (Usenix’07) (June 2007).

phones. In Proceedings of the 9th USENIX conference on Op-

erating systems design and implementation (Berkeley, CA, USA,

2010), OSDI’10, USENIX Association, pp. 1–6.

S. A study of android application security. In Proceedings of the

20th USENIX Security Symposium (2011).

trospection based architecture for intrusion detection. In Pro-

ceedings of Network and Distributed Systems Security Symposium

(NDSS’03) (February 2003).

//gartner.com/it/page.jsp?id=1848514 , 2011.

and synthesis for embedded systems (New York, NY, USA, 2006),

CASES ’06, ACM, pp. 261–270.

and Communications Security (CCS’07) (October 2007).

[25] Security alert: New sophisticated android malware droidkungfu

ncsu.edu/faculty/jiang/DroidKungFu.html .

Sec’09) (November 2009).

[27] L UK , C.-K., C OHN , R., M UTH , R., P ATIL , H., K LAUSER , A.,

L OWNEY , G., W ALLACE , S., R EDDI , V. J., AND H AZELWOOD ,

D., AND M ANIATIS , P. Path-exploration lifting: Hi-fi tests for

lo-fi emulators. In Proceedings of the 17th International Confer-

International Symposium on Software Testing and Analysis (IS-

STA’09) (2009), pp. 261–272.

[30] M IJAR , R., AND N IGHTINGALE , A. Virtualization is coming to

[31] M OSER , A., K RUEGEL , C., AND K IRDA , E. Exploring mul-

heavyweight dynamic binary instrumentation. In PLDI (2007),

pp. 89–100.

[33] P ORTOKALIDIS , G., S LOWINSKA , A., AND B OS , H. Argos:

15

[36] Y AN , L.-K., J AYACHANDRA , M., Z HANG , M., AND Y IN , H.

V2E: Combining hardware virtualization and software emulation

[37] Y IN , H., L IANG , Z., AND S ONG , D. HookFinder: Identifying

and understanding malware hooking behaviors. In Proceedings of

the 15th Annual Network and Distributed System Security Sympo-

[38] Y IN , H., AND S ONG , D. Temu: Binary code analysis via whole-

system layered annotative execution. Tech. Rep. UCB/EECS-

Jan 2010.

[39] Y IN , H., S ONG , D., M ANUEL , E., K RUEGEL , C., AND K IRDA ,

E. Panorama: Capturing system-wide information flow for mal-

(October 2007).

CA, USA, May 2012), IEEE.

[41] Z HOU , Y., W ANG , Z., Z HOU , W., AND J IANG , X. Hey, you, get

ary 2012).

information on “ratc” and the setuid exhaustion vulnera-

bility.

we used DroidScope to gather an ARM instruction trace

operands. We have also indented the instructions to il-

lustrate the relative stack depth.

nel space and returns back to adb main at address

which is (-11 in 2’s complement or -EAGAIN).

Tracing backwards in the log reveals that this error

| [19] E | NCK | , W., G | ILBERT | , P., C | HUN | , B.-G., C | OX | , L. P., J | UNG | , J., | for transparent and extensible malware analysis. In | Proceedings of |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M | C | D | ANIEL | , P., | AND | S | HETH | , A. N. Taintdroid: an information- | the Eighth Annual International Conference on Virtual Execution |  |  |  |  |  |  |
| flow tracking system for realtime privacy monitoring on smart- | Environments (VEE’12) | (March 2012). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [20] E | NCK | , W., O | CTEAU | , D., M | C | D | ANIEL | , P., | AND | C | HAUDHURI | , | sium (NDSS’08) | (February 2008). |  |
| [21] G | ARFINKEL | , T., | AND | R | OSENBLUM | , M. | A virtual machine in- | 2010-3, EECS Department, University of California, Berkeley, |  |  |  |  |  |  |  |
| [22] Gartner says sales of mobile devices grew 5.6 percent in third | ware detection and analysis. | In | Proceedings of the 14th ACM |  |  |  |  |  |  |  |  |  |  |  |  |
| quarter of 2011; smartphone sales increased 42 percent. | http: | Conferences on Computer and Communication Security (CCS’07) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [23] H | AZELWOOD | , K., | AND | K | LAUSER | , A. | A dynamic binary in- | [40] Z | HOU | , Y., | AND | J | IANG | , X. | Dissecting android malware: Char- |
| strumentation engine for the arm architecture. | In | Proceedings | acterization and evolution. In | Proceedings of the 33rd IEEE Sym- |  |  |  |  |  |  |  |  |  |  |  |
| of the 2006 international conference on Compilers, architecture | posium on Security and Privacy (Oakland 2012) | (San Francisco, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [24] J | IANG | , X., W | ANG | , X., | AND | X | U | , D. Stealthy malware detection | off of my market: Detecting malicious apps in official and alter- |  |  |  |  |  |  |
| through vmm-based ”out-of-the-box” semantic view reconstruc- | native android markets. In | Proceedings of the 19th Network and |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tion. | In | Proceedings of the 14th ACM conference on Computer | Distributed System Security Symposium | (San Diego, CA, Febru- |  |  |  |  |  |  |  |  |  |  |  |
| found in alternative chinese app markets. | http://www.csc. | A | Trace-Based Exploit Diagnosis of “ratc” |  |  |  |  |  |  |  |  |  |  |  |  |
| [26] K | ANG | , M. G., Y | IN | , H., H | ANNA | , S., M | C | C | AMANT | , S., | AND | In this section, we provide an example of exploit diagno- |  |  |  |
| S | ONG | , D. | Emulating emulation-resistant malware. | In | Pro- | sis using DroidScope and the ARM instruction tracer on |  |  |  |  |  |  |  |  |  |
| ceedings of the 2nd Workshop on Virtual Machine Security (VM- | “ratc”. These results corroborate with publicly available |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| K. Pin: Building customized program analysis tools with dynamic | We know that | adbd | is supposed to downgrade its priv- |  |  |  |  |  |  |  |  |  |  |  |  |
| instrumentation. In | Proc. of 2005 Programming Language Design | ileges by setting its uid to AID SHELL (2000), and yet |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and Implementation (PLDI) conference | (june 2005). | adbd retained its root privileges after the attack. Thus, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [28] M | ARTIGNONI | , L., M | C | C | AMANT | , S., P | OOSANKAM | , P., S | ONG | , | in an effort to identify the root cause of the vulnerability, |  |  |  |  |
| ence on Architectural Support for Programming Languages and | that includes both user and kernel code. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Operating Systems (ASPLOS) | (London, UK, Mar. 2012). | A simplified and annotated log is shown in Figure 13. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [29] M | ARTIGNONI | , L., P | ALEARI | , R., R | OGLIA | , G. F., | AND | B | R | - | In the log, the instruction’s address comes first fol- |  |  |  |  |
| USCHI | , D. | Testing cpu emulators. | In | Proceedings of the 18th | lowed by a colon, the decoded instruction and then the |  |  |  |  |  |  |  |  |  |  |
| a platform near you. Tech. rep., ARM Limited, 2011. | The log begins when | setgid | returns from the ker- |  |  |  |  |  |  |  |  |  |  |  |  |
| tiple execution paths for malware analysis. | In | Proceedings of | 0x0000c3a4. Almost immediately, the log shows | setuid |  |  |  |  |  |  |  |  |  |  |  |
| the 2007 IEEE Symposium on Security and Privacy(Oakland’07) | being called. | After transitioning into kernel mode, we |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (May 2007). | see | sys setuid | being called followed by a call to | set user | . |  |  |  |  |  |  |  |  |  |  |
| [32] N | ETHERCOTE | , N., | AND | S | EWARD | , J. Valgrind: a framework for | Later we see | set user | returning an error code 0xfffffff5 |  |  |  |  |  |  |
| an emulator for fingerprinting zero-day attacks. In | EuroSys 2006 | code was the result of the | RLIMIT NPROC | check in |  |  |  |  |  |  |  |  |  |  |  |
| (April 2006). | set user | . | This reveals why | setuid | failed to downgrade |  |  |  |  |  |  |  |  |  |  |

---

## Page 16

;;;setgid returns from kernel back to adbd

0000813c: pop {r4, r7}

00008140: movs r0, r0

00008144: bxpl lr : Read Oper[0]. R14, Val = 0xc3a5

;; Return back to 0xc3a4 (caller) in Thumb mode

;;;adbd_main sets up for setuid

0000c3a4: movs r0, #250

0000c3a6: lsls r0, r0, #3 : Write Oper[0]. R0, Val = 0x7d0

;; 250 * 8 = 0x7d0 = 2000 = AID_SHELL

...

;;;Start of setuid section

;;; 213 is syscall number for sys_setuid

00008be0: push {r4, r7} : Write Oper[0]. M@be910bb8, Val = 0x7d0

;; push AID_SHELL onto the stack

00008be4: mov r7, #213

00008be8: svc 0x00000000

;; Make sys call

;;; === TRANSITION TO KERNEL SPACE ===

;;;sys_setuid then calls set_user in kernel mode

;;;inside sys_setuid

;; Has rlimit been reached?

c0048944: cmp r2, r3 : Read Oper[0]. R3, Val = 300 Read Oper[1]. R2, Val = 300

;;; RLIMIT(300) is reached and !init_user so return -11

c0048960: mvn r0, #10 : Write Oper[0]. R0, Val = 0xfffffff5

;; the return value is now -11 or -EAGAIN

c0048964: ldmib sp, {r4, r5, r6, fp, sp, pc}

;;;Return back to sys_setuid which returns back to userspace

;;; === RETURN TO USERSPACE ===

;;;setuid continues

00008bec: pop {r4, r7}

00008bf0: movs r0, r0 : Read Oper[0]. R0, Val = 0xfffffff5

;; -11 is still here

;;;Return back to adb_main at 0xc3ac (the return address) above

;;; Immediately starts other work, does not check return code

0000c3ac: ldr r7, [pc, #356] : Read Oper[0]. M@0000c514, Val = 0x19980330

Write Oper[0]. R7, Val = 0x19980330

;; 0x19980330 is _LINUX_CAPABILITY_VERSION

Figure 13: Annotated adbd trace

adbd’s privileges. Further analysis of the log shows that

the return value from setuid was not used by adbd nor

was a call to getuid seen. The same applies to setgid .

This indicates that adbd failed to ensure that it is no

longer running as root. Thus, our analysis shows that

the vulnerability is due to two factors, RLIMIT NPROC

and failure to check the return code by adbd.

16

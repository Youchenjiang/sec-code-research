---
title: "To Unpack or Not to Unpack: Living with Packers to Enable Dynamic Analysis of Android Apps"
author: "Mohammad Hossein Asghari; Lianying Zhao"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 19
---

# To Unpack or Not to Unpack: Living with Packers to Enable Dynamic Analysis of Android Apps

> **作者**：Mohammad Hossein Asghari; Lianying Zhao
> **總頁數**：19 頁

---

## Page 1

To Unpack or Not to Unpack:

Living with Packers to Enable Dynamic Analysis of Android Apps

| Mohammad Hossein Asghari | Lianying Zhao |
| --- | --- |
| Carleton University | Carleton University |
| hosseinasghari@cmail.carleton.ca | Lianying.Zhao@carleton.ca |
| Abstract | app from being tampered with, referred to as anti-analysis |

tampering with various anti-analysis techniques embedded in the

app. Meanwhile, packers also conceal certain behavior poten-

tially against the interest of the users, aside from being abused

by malware for stealth. Security practitioners typically try to

then propose Purifire , an evasion engine to bypass packers’ anti-

analysis techniques and enable dynamic analysis on packed apps

without unpacking them . Purifire is based on eBPF, a low-level

kernel feature, which provides observability and invisibility to

user space apps to enforce defined evasion rules while staying

low-profile. Our evaluation shows that Purifire is able to bypass

packers’ anti-analysis checks and more importantly, for previous

research works suffering from packers, we observe a significant

improvement (e.g., a much higher number of detected items such

as device fingerprints).

1 Introduction

Mobile applications (apps) are now a key part of daily

techniques hereafter. Over the decades, software commu-

hinder reverse engineering and analysis [71]. These meth-

ods inspired the more formal notion of “packing”, where

programs are transformed to conceal their content or ob-

Packers decrypt and load app code at runtime, add de-

pendencies, and use multiple protection techniques such

as anti-debugging, anti-instrumentation, and environment

checks. In addition to IP protection, packed apps ac-

tively respond to anomalies that trigger their runtime anti-

analysis mechanisms. These mechanisms may scan the file

system for specific artifacts or inspect process memory for

suspicious values. When such conditions are detected, the

app may terminate gracefully or intentionally crash to pre-

vent further analysis [46, 44, 50]. Additionally, packers

Frida [38] and Xposed [54], which are often used for run-

time inspection, finding vulnerabilities, and checking for

privacy risks [63].

1

Android apps have become a valuable target for app modifiers nities, both in open-source and commercial domains, have

and imitators due to its popularity and being trusted with highly relied on methods like code obfuscation and encryption

sensitive data. Packers, on the other hand, protect apps from in desktop environment such as Linux and Windows to

capture undesired behavior at runtime with hooking (e.g., Frida) fuscated to hinder analysis, often used both for legitimate

or debugging techniques, which are heavily affected by packers. hardening and malware evasion [25, 20]. Android packers

Unpackers have been the community’s continuous effort to ad- adopt concepts from desktop packers and, by leveraging

dress this, but due to the emerging commercial packers, our study the unique structure and execution model of Android apps,

shows that none of the unpackers remain effective, and they are provide similarly sophisticated packing features. These

unfit for this purpose as unpacked apps can no longer run. packers use encryption, code obfuscation, and other anti-

We first perform a large-scale prevalence analysis of Android analysis techniques to protect app code. While they help

packers with a real-world dataset of 12,341 apps, the first of its developers protect their work, these protections also make

kind, to find out what percentage of Android apps are actually security analysis harder, and they can be misused by mal-

packed and to what extent dynamic analysis is hindered. We ware authors to hide harmful behavior [34, 75].

arXiv:2509.16340v1 [cs.CR] 19 Sep 2025 can detect and block popular dynamic analysis tools like

life, supporting communication, shopping, entertainment, Previous approaches to analyzing packed apps, such as

and many other activities. Android has the largest market unpacking, proved effective at the time [66, 84, 28, 80],

share worldwide (71%) [70], which also makes it a target but their efficacy has diminished over time as packers have

for attackers who try to reverse-engineer or modify apps to evolved. Even if unpacking works, the recovered Dex

steal intellectual property, remove restrictions, or commit code is often incomplete [34, 76], obfuscated, dependent

fraud. To protect against these threats, Mobile Application on packer code due to on-demand dynamic code loading

Security Verification Standard (MASVS) [59] dictates se- and multi-layer packing [71], or at least missing metadata.

curity guidelines for Android developers to build their app As a result, obtaining only dumped Dex code still leaves

based on standard self-protection techniques to protect the it very challenging, if not impossible, to repackage and

---

## Page 2

| analyze the app dynamically at runtime. | Furthermore, | pass anti-analysis defenses without unpacking the |
| --- | --- | --- |
| numerous modern apps now execute mostly in native code | app. | Purifire enables dynamic analysis tools to op- |
| for performance reasons [75] limiting the usefulness of | erate transparently even on protected apps, offering a |  |
| dumped Dex code. | practical and customizable solution for security ana- |  |
| Nowadays, commercial packers provide developers with | lysts. |  |

accessible, zero-code solutions for app hardening with dif-

ferent subscription levels (see Section 3.2.1). Well-known

commercial packers include Chinese services such as Iji-

ami [47], Qihoo [8], Tencent [69], Bangcle [18], and Baidu

by enabling dynamic analysis without unpacking the app.

• We examine the technical aspects of Android packers

and unpacking techniques with a taxonomy, high-

lighting their impact on dynamic program analysis.

This serves as a foundation for future work in under-

standing and mitigating packing-related challenges.

• We propose and implement Purifire, the first kernel-

2

2 Motivation

and react.

the aforementioned tools like Frida, which support app-

specific instrumentation scripts to trace class and method

invocations, such as monitoring the transformation of net-

work packets. These tools enable hybrid analysis ap-

proaches that combine runtime visibility with targeted in-

spection, making them indispensable for modern Android

app analysis.

[17], and non-Chinese solutions such as Appdome [1], LI- Our findings indicate that a significant share of apps are af-

APP [53], and Dovern [2]. These services accept APK fected by packers (see Section 5), showing the importance

files as input and return a packed version of the app. The of being able to analyze packed apps as they are becoming

advent of commercial packers almost rendered the goal of common. Many existing tools and academic studies are

defeating packers unrealistic. built on ready-to-use well-maintained tools such as Frida

We propose a different approach. Instead of trying to and Xposed scripts (see Section 3.1). However, their ef-

fully defeat packers, we aim to live alongside with them fectiveness is often reduced by packers, which detect them

Our framework, called Purifire, uses the Extended Berke- Unpacking once promised a path to visibility, but it no

ley Packet Filter (eBPF) [35], a kernel feature to run priv- longer delivers what dynamic analysis actually needs. To

ileged code in a safe and event-driven manner, to intercept confirm this, we applied available unpacking approaches

and bypass anti-analysis checks while the app is running to our dataset to evaluate their effectiveness (see Sec-

without being detected. This allows tools like Frida to tion 4.2.1) and found that they failed to recover the majority

work on packed apps based on what is available at runtime of the apps, primarily due to their fixed configurations and

without being detected. Purifire employs a configurable outdated design. This is further worsened by the growth

evasion system that enables analysts to bypass anti-analysis of commercial Android packers with sophisticated tech-

techniques and examine both benign and malicious apps. niques never fully exposing clear code at runtime (but

In addition, we conduct a large-scale study of commercial on-demand), invalidating the design of most unpackers.

packer usage in Android apps to measure their prevalence Meanwhile, commercial packers actively evolve and

and perform dynamic analysis to identify implemented constantly add new unpacker “fingerprints”, which re-

anti-analysis techniques. This is to find out the actual flects the nature of an arms race. Our manual analysis

impact of Android packers and to what extent security shows packers like Ijiami [47] check for unpacker config-

analysis can be affected. We evaluate Purifire by con- uration files, path, and package names like: /data/fart

trasting how several academic security projects previously (FART [43]), /data/local/tmp/unpacker.config

blocked/affected by packers with the improvements after (Youpk [81]), /data/dexname (DexHunter [84]), and

Purifire is used (see Section 7). top.niunaijun.blackdex (BlackDex [28]).

Contributions. On the other hand, unpackers often rely on Android

• We conduct a large-scale prevalence analysis of An- Runtime (ART) instrumentation and emulation-based ap-

droid packers over 12,341 real-world apps – 7,913 proaches, both of which require advanced technical ex-

from Chinese app stores and 4,428 global, to mea- pertise, and are quickly outdated and based on modified

sure the actual impact of commercial packers. Our Android Open Source Project (AOSP), which is incom-

findings reveal that nearly 50% of Chinese apps use patible with Play Integrity [5] and Google Services. In

packing services (while non-Chinese apps see a much practice, analysts often use a real phone with a factory

lower percentage), and that existing analysis tools are image to remain low-profile, minimize the risk of trigger-

largely ineffective against these protections. To the ing anti-analysis techniques, and observe the app’s com-

best of our knowledge, this is the first systematic plete functionality, including interactions with Google Ser-

| prevalence study on this scale. | vices (e.g., Firebase [3]). Their common practice involves |
| --- | --- |
| level eBPF-based evasion framework designed to by- | The infeasibility of unpacking and the need for pre- |

---

## Page 3

serving well-established dynamic analysis tools call for and Xposed [54] allow analysts to hook Application Pro-

a paradigm shift toward analyzing packed apps without gramming Interface (API) calls, modify parameters or re-

unpacking them, as with malware analysts relying on de- turn values, replace method implementations, intercept

buggers to examine behavior in-place. To support this network traffic, audit cryptographic functions, and trace

goal, we propose an evasion engine that enables controlled, control flow. However, despite their popularity in aca-

single-stepping analysis via predefined evasion rules. This demic research, these DBI tools are highly detectable by

approach helps security analysts study packed apps at run- modern packers, which implement checks for tracing, run-

time, while still respecting the protections applied by de- time modifications, and instrumentation artifacts. As a re-

velopers to avoid outright code theft in its entirety. sult, they are often ineffective against packed apps, and the

In the Android app ecosystem, multiple stakeholders in-

teract with different levels of knowledge and control. App

developers create features and may rely on packing ser-

vices to protect their code/data, while app users only care

about the final functionality. Security analysts aim to eval-

uate app security without access to source code or packer

internals, and in our discussion context, evasion rule au-

thors develop rules to bypass anti-analysis methods (e.g.,

via reverse-engineering). Packing services, mostly driven

by economic incentives, intend to achieve the protection

apps often receive more trust than PC software due to

namic Binary Instrumentation (DBI) tools, and the unique-

ness of commercial Android packers.

3

rapid evolution of Android and packer techniques creates

a heavy maintenance burden. In the following, we provide

ty/privacy, and the foreseeable benefit of re-enabling them

in the face of packers.

Frida can be used for file and memory operations. Dong

et al. [32] hooked file-related APIs such as java.io.File

and open from libc to conduct a large-scale study of

tracking SDKs using external storage as a covert channel,

and Pourali et al. [60] retrieved stack traces to capture

insecure TLS certificate validation. Anglano et al. [12]

hooked popular encryption libraries (SQLCipher, Realm

and Jetpack Security) for forensic analysis.

four CVEs.

tive Interface (JNI) interactions, Blutter [74] for analyz-

ing apps that have been developed by Flutter [40], and

highlight the widespread adoption of DBI tools, within

3.2 Commercial Android Packers

without requiring expertise [79] in code obfuscation or

| 2.1 | Threat Model | a few examples of the use of DBI tools for better securi- |
| --- | --- | --- |
| goals by constantly improving packers. | Against the in- | Frida has also been used for API monitoring. Heid et |

terest of app users (and potentially other entities), while al. [45] modified device properties to study their effect on

malicious actors can abuse packers outright to conceal generated device fingerprints. Ibrahim et al. [46] exam-

harmful code, certain behavior introduced by app devel- ined the SafetyNet attestation API through Frida hooks.

opers in the first place, intentionally or inadvertently, may Cui et al. [29] identified privacy leakage from third-party

also remain unnoticed due to packers. libraries, while Aldoseri et al. [10] intercepted URI han-

These dynamics create a complex landscape. Mobile dling in the top 15 popular mobile browsers and discovered

Android’s sandboxing and permission control, allowing Additionally, Diamantaris et al. [30] utilized Xposed

sensitive operations that would be risky elsewhere. How- for real-time analysis of permission checks and stack

ever, the same isolation that shields users can also hide trace monitoring in Android apps. Moreover, community-

undesired behavior, with no single actor with complete developed frameworks with embedded Frida-based scripts

control or visibility. Our proposed evasion engine aims to are widely used in app analysis [83, 49], including tools

achieve a balance between stakeholders by avoiding fully such as Medusa [23] and Objection [6].

| unpacking apps (hence defeating packers) and allowing | Several tools have been developed to support dynamic |  |  |
| --- | --- | --- | --- |
| security analysts to observe app behavior at runtime. | analysis, including JNITrace [24] for intercepting Java na- |  |  |
| 3 | Background | Google’s Frida-based SSL logger [39]. | These examples |

To facilitate subsequent discussions, we first briefly dis- the Android security community and the potential conse-

cuss how Android app security analysis benefits from Dy- quence of commercial packers rendering them ineffective.

3.1 Android Dynamic Binary Instrumenta- Commercial packers can be considered to be packers-as-

tion a-service, aiming to enable developers to secure their code

Dynamic analysis is widely used to study Android apps, anti-analysis techniques, unlike most open-source ones.

as it helps bypass runtime decryption and obfuscation that These online packing platforms offer Android app harden-

hinder static analysis [19]. Frameworks such as Frida [38] ing, by just taking uploaded APK files as input.

---

## Page 4

3.2.1 Packing features filtering, now supports system introspection, performance

Packing services usually provide multiple tiers of protec-

tion, including free and professional (paid) plans. As a re-

sult, the same app version can exist in multiple packed vari-

ants, depending on the chosen protection level and distri-

bution platform (e.g., various app stores other than Google

Play) [73]. Chinese providers such as Tencent [69] and

Manxi [55] commonly market their products under terms

like “reinforcement” or “shielding” while non-Chinese ser-

vices like LIAPP [53] use more direct terminology. Un-

make our evasion design more informed and targeted.

Basic/free plans. Basic plans generally include well-

known anti-analysis measures. Tencent and Manxi offer

protections such as Dex code encryption, tamper checks,

anti-dumping, and anti-debugging, while LIAPP provides

more detailed options even at the basic tier. Notably, LI-

APP’s plan includes game engine protection for Unity [72],

game apps.

Advanced plans. Advanced plans introduce more sophis-

ticated defenses, often tied to paid subscriptions. Chi-

nese packers implement techniques like DexVirtualiza-

tion, DexToCPP conversion, and AndroidManifest.xml

tamper-proofing. Tencent extends protection to native li-

braries with obfuscation and encryption, while Manxi of-

fers custom native loader (see Appendix 14). Beyond

code hardening, advanced features also include root and

emulator detection, VM checks, APK/resource tamper-

proofing, SSL pinning, hook detection, VPN/overlay de-

tection, JDWP checks, and anti-bot measures. These ad-

vanced protections highlight the increasing complexity of

Android-specific anti-analysis strategies.

3.2.2 Registration requirements

ating a tightly controlled ecosystem. Developers are often

3.3 Extended Berkeley Packet Filter (eBPF)

4

monitoring, and security enforcement. With features like

maps, BTF type metadata, and probes (kprobes and up-

robes) [62], it enables efficient data sharing, cross-version

compatibility, and dynamic instrumentation in both kernel

and user space. The CO-RE (Compile Once, Run Ev-

erywhere) capability further allows portability without re-

compilation, and using Aya-Rust [16], our work is shipped

as a statically linked eBPF program for arm64 Android.

niques

In this section, we systematically analyze and survey cur-

rently known anti-analysis techniques and state-of-the-art

unpacking approaches.

Most anti-analysis techniques originated from PC packers

but have been adapted to the Android ecosystem by lever-

aging Android’s unique architecture. In the following, we

discuss several to facilitate subsequent discussions.

Debugger detection. Android packers employ diverse

anti-debugging techniques across both Java and native

layers. Common methods include checking debugger sta-

tus via APIs (e.g., Debug.isDebuggerConnected() ,

| getApplicationInfo() | ), | system | properties |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ( | ro.debuggable | ), | or | runtime | structures | like |
| gDvm.debuggerConnected | . | More | advanced | defenses |  |  |

hook components such as JdwpTransport to block de-

bugger connections altogether [26]. Packers also monitor

external signs of debugging, such as scanning running pro-

cesses, checking /proc/PID/status (e.g., TracerPid ),

inspecting debugger files in /data/local/tmp/ , or

analysis.

ing checks to detect execution delays, and monitor system-

level clues such as thread names (e.g., “ pool-frida ”), file

descriptors, memory permissions ( rwx which is abnor-

derstanding how packing features vary with tiers/plans can 4 Packing and Unpacking Tech-

Unreal [36], and Cocos [27], reflecting broader support for 4.1 Anti-analysis Techniques

Chinese packing services are region-specific, requiring using the ptrace syscall to detect tracing [82]. Timing

mainland phone numbers, real-name authentication [52], checks and signal handling further expose debugger

and sometimes government ID verification, CAPTCHAs, interference [21]. Together, these layered checks create

or VPN access (if accessed outside mainland China), cre- strong resistance against reverse engineering and dynamic

asked to specify the category of their app, which suggests DBI detection. Packers defend against DBI tools like

that different protection techniques may be applied based Frida and Xposed by detecting tampering through mem-

on the app type (e.g., finance, sports) [32]. In contrast, ory scans (e.g., injected artifacts or suspicious strings like

non-Chinese services are more accessible, typically re- “ frida-agent-32.so ” in /proc/self/maps file) [67],

quiring only an email for registration. These differences process and library checks (e.g., frida-server , files in

between Chinese and non-Chinese packing services high- /data/local/tmp ), or comparing reloaded libraries

light the varying levels of restriction and protection (e.g., against in-memory versions to spot hooks. They may

as a black-box in a closed ecosystem). also restore trampolined functions (unhooking), use tim-

Extended Berkeley Packet Filter (eBPF) [35] is a power- mal), or open communication ports (e.g., 27049). To-

ful Linux kernel feature that, beyond its origins in packet gether, these techniques provide layered defenses that

---

## Page 5

expose hidden DBI activity and hinder dynamic analy- BaseDexClassLoader . Tools like Youpk [81] and Dex-

sis [44]. Hunter [84] fall in this category. We tested Youpk on the

Systematization of anti-analysis principles. We present first app group, since the authors claimed Ijiami unpacking

a novel perspective on anti-analysis techniques by organiz- support, and found that in 86% of them, Youpk were not

ing them in a way that emphasizes their underlying princi- able to dump Dex code even after extending the wait time

ples. This approach is particularly beneficial for security beyond its recommended duration. Further differential

researchers seeking to design effective evasion strategies. analysis revealed that even in cases where Dex files were

In contrast to previous systematization [86, 63, 31], which dumped, they were incomplete or dependent on native in-

primarily focused on grouping detection methods into cat- teractions [78, 34]. Similarly, DexHunter [84], which is an

egories such as emulator detection, root detection, and academic unpacker designed for older Android versions,

other specific mechanisms, our taxonomy provides a more failed entirely when tested against our selected apps (sec-

technically actionable foundation. It is tailored to guide ond group), largely due to modern packers’ use of dynamic

the development of evasion rules that can bypass these loading patterns and DexLoader hooking, which disrupts

techniques in a systematic manner (see Table 1). For ex- static analysis techniques.

ample, debugger detection can be implemented using ei-

ther file-based techniques or Java-based APIs. The syntax

of the evasion rules can thus correspond to the principles

(column “Anti-analysis principle”) to capture the detection

source.

tiveness of traditional unpacking approaches and motivates

a paradigm shift: rather than attempting to fully unpack

apps, observing what remains available alongside packers

is a more practical and robust strategy.

4.2.1 Testing state-of-the-art unpackers

Most modern Android unpackers focus on dumping the de-

at runtime. These tools generally target the Java layer of

loading Dex code, such as DexClassLoader and

5

Memory-based unpackers. Memory-based unpackers

are also falling short in practice. BlackDex [28], which

operates without requiring root or Frida, proved outdated

and unable to handle modern Dex release methods, often

crashing during execution on the second group of apps.

Tools like frida-dexdump [4], while conceptually pow-

premature termination of the app before dumping can com-

In summary, our results show that existing unpack-

ing tools, whether ART instrumentation-based or mem-

ory scanning-based, struggle with the new techniques em-

ployed by modern Android packers.

based protections.

4.2 Android Unpackers erful, are easily detected by anti-Frida checks, leading to

In this section, we examine the limitations of existing An- plete. Similarly, KissKiss [65], which relies on ptrace

droid unpackers when confronted with modern packing to trace the app’s execution, fails due to being detected by

techniques. Our analysis highlights the growing ineffec- anti-debugging techniques early on.

coded Dex code from memory once it becomes available 4.2.2 Systematization of Android unpackers

an app and rely on either instrumentation of ART methods We have summarized current Android unpackers in Ta-

or scanning memory regions for Dex content. However, ble 2, of which we have tested available ones. Although

as our experimental evaluation shows, such approaches unpackers adopt various strategies, ranging from memory

are increasingly ineffective against modern commercial scanning and class loading hooks to runtime monitoring,

packers, which use advanced techniques like partial code symbolic execution [77], or hardware assistance [78], their

loading [76], JNI interactions, anti-instrumentation (emu- common goal is to recover hidden Dex code from commer-

lation detection [64, 26]), and anti-hooking protection to cial packers. Their key drawback is that the recovered Dex

resist analysis. To prevent unpackers from accessing or files do not contain all hidden Dex data [78], as they are

dumping Dex files in memory, packed apps often hook not released fully at a given time, if at all (depending on

file-related and memory-related functions to block such the covered functionality by the duration of interactions).

operations [85]. Early unpackers fail due to anti-debugging [65] and self-

We randomly selected 120 apps packed by Ijiami [47] modifying code; ART-based approaches are blocked by

as the first group, and another 20 arbitrary packed apps as anti-instrumentation or anti-emulation checks [34]; and

the second group to evaluate against available unpackers. advanced frameworks struggle with native code, multi-

We do not aim to test our full dataset due to the time- stage releases, or require manual effort. Hardware-assisted

consuming nature of the process. and recent solutions [78, 51, 85] remain constrained by

ART-based unpackers. ART-based unpackers op- heavy instrumentation making them , packer-specific as-

erate by hooking into the functions responsible for sumptions, and limited coverage (only Dex code) or VM-

---

## Page 6

| Anti-analysis principle | Detection goal | Example / details |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| emulator detection | /dev/qemu | , | /proc/cpuinfo | , thermal/sysfs artifacts |  |  |  |  |
| debugger detection | /proc/self/status | (TracerPid), | /proc/self/wchan |  |  |  |  |  |
| tools detection | /proc/self/maps | , | /data/local/tmp/frida-server | , |  |  |  |  |
| file-based | /proc/self/task/TID/stat | , Xposed/JDWP files |  |  |  |  |  |  |
| root detection | /system/bin/su | , | busybox | , RW | /system |  |  |  |
| Magisk detection | /sbin/.magisk | , | /data/adb/magisk |  |  |  |  |  |
| repackaging checks | Dex/signature checksum mismatch |  |  |  |  |  |  |  |
| process inspection | ps -A | , | top | for | frida | , | magiskd | , debuggers |
| package inspection | Detect apps: Magisk, SuperSU, Xposed, FridaGadget |  |  |  |  |  |  |  |
| emulator detection | ro.build.tags | = | test-keys | , abnormal | ro.product.* |  |  |  |

activity-based

| dev-mode checks | USB debugging / ADB over TCP enabled |  |  |
| --- | --- | --- | --- |
| user-interaction gating | Require gestures or sensor events before running logic |  |  |
| attestation checks | Play Integrity / SafetyNet results |  |  |
| tool detection | Abnormal RWX maps, SO injection |  |  |
| code-integrity checks | Validate function prologues, detect inline hooks |  |  |
| memory-based | unpacking resistance | Dex/string/class decryption only in protected regions |  |
| gadget/library probes | Detect | frida-gadget.so | or hooking libs in memory |
| ART/loader checks | Hidden class lookups, tampered class loaders |  |  |
| timing checks | System.nanoTime() | , loop delta anomalies |  |
| timer-based | delayed triggers | Long sleeps, time-of-day based activation |  |
| virtualization timing | I/O/RTT skew typical of emulators [68] |  |  |
| TLS pinning | Strict hostname/CA checks, custom trust store |  |  |
| proxy/MITM detection | Proxy configs, abnormal cert chains |  |  |

network-based

| tool comms detection | Scan JDWP ports, debugger sockets, ADB over TCP |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| emulator net probes | Emulator host routes (e.g., 10.0.2.2) |  |  |  |  |
| debugger detection | Debug.isDebuggerConnected() | , StrictMode |  |  |  |
| emulator detection | TelephonyManager | IMEI=000000, missing GMS |  |  |  |
| Java/Framework | code loading guards | Monitor | DexClassLoader | / | PathClassLoader |
| runtime API hardening | Checks on clipboard, overlays, sensitive APIs (e.g., |  |  |  |  |

Class.forName("de.robv.android.xposed.

XposedBridge") )

| reflection checks | Detect suspicious reflective lookups |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| debugger detection (ptrace) | ptrace(PTRACE_TRACEME) | self/parent attach |  |  |  |  |
| signal tricks | Custom SIGTRAP/SEGV handlers, anti-breakpoint |  |  |  |  |  |
| misc / native-level | environment artifacts | Emulator hardware names (Goldfish/Ranchu), MACs |  |  |  |  |
| sensor probing | Few or missing sensors (NFC, accelerometer, camera) |  |  |  |  |  |
| early-stage guards | Checks in | attachBaseContext | / | JNI_OnLoad | / | init_proc |

Table 1: Systematization of Android anti-analysis techniques.

5 Prevalence Analysis apps from the 360 App Store [9] and 4,428 non-Chinese

apps from APKPure [14]. We separated our dataset into

We conducted, to the best of our knowledge, the first Chinese and non-Chinese apps due to their fundamentally

experimental and large-scale packer prevalence analysis. different distribution channels and protection practices. In

This is different from previous efforts to examine packed China, where Google Play is unavailable, developers de-

apps, which only involved theoretical analysis or manu- pend on regional markets that commonly use domestic

ally checking apps at a small scale. Our purpose is to packers and stricter anti-analysis defenses shaped by lo-

understand the impact of Android packers on the over- cal regulations, while non-Chinese apps typically rely on

all app population which the general public and security global services focused on intellectual property protec-

practitioners are exposed to. tion. This distinction also accounts for apps released with

We first try to identify packed apps within our dataset region-specific features or protections (see Section 3.2), al-

and determine the specific packers used. Then, we conduct lowing us to capture technical and regulatory differences,

runtime analysis to assess the effectiveness of anti-Frida highlight ecosystem-specific anti-analysis behaviors, and

and anti-JDB techniques, which are commonly employed provide a fairer assessment of packer prevalence world-

to counter DBI and Android debugging, respectively. wide.

Downloading process. The data collection process, car-

5.1 Dataset ried out between June and August 2024, was fully auto-

mated and involved two phases: URL extraction and APK

To conduct a thorough analysis of Android packers and downloading. Selenium [57] was used to scrape download

their runtime anti-analysis techniques, we assembled a di- URLs by navigating the interface of both the APKPure and

verse dataset of 12,341 apps, comprising 7,913 Chinese 360 websites, while File Centipede [37] was employed as

6

---

## Page 7

| Unpacker | Code coverage | Working platform | Instrumentation level | Available | Year |
| --- | --- | --- | --- | --- | --- |
| KissKiss [65] | Dex | Phone | NA | Yes | 2014 |
| DexHunter [84] | Dex | Phone (KitKat Android | DVM & ART | Yes | 2015 |

4.4.3)

AppSpear [80] Dex incomplete Phone (Android 4.3 and DVM No 2015

4.4.2 using AOSP)

PackerGrind [76] Dex Phone (Android 6.0) Instruction and system No* 2017

level

DroidUnpack [34] Dex Emulator (QEMU) Android framework No* 2018

DexX [66] Dex Phone (Nexus 5) Android kernel and No 2018

framework

ReDex [22] Dex Phone (Android 4.4 Android VM (DVM & No 2020

DVM, Android 9.0 ART, reflection-based)

ART)

| Parema [77] | Partially Dex codes and | Phone (Android 6.0) | Instruction level (based | No* | 2021 |
| --- | --- | --- | --- | --- | --- |
| VMprotected code | on PackerGrind) |  |  |  |  |
| Happer [78] | Dex | Juno r2 dev board (An- | NA | No | 2021 |

droid 6.0)

| Gupacker [85] | Dex | Phone (Nexus 6) | Android framework | No | 2025 |
| --- | --- | --- | --- | --- | --- |
| BPFDex [51] | Dex | Phone (Pixel 6)& Emula- | NA | No | 2025 |

tor

Table 2: Current Android unpackers sorted by year. "*": The repositories did not have complete code or were not

maintained.

a download manager. During our analysis, we found 70 While APKiD mainly maps names and strings to Western-

apps that were available in both sources. Interestingly, ized labels, NP-Manager, on the other hand, offers more

41 apps shared identical package names but showed dif- regionally accurate names and, due to frequent updates, is

ferent behaviors in our runtime anti-analysis experiments often more reliable when APKiD fails to detect a packer.

(see Section 5.3), caused by version differences or market- To resolve disagreements between the two tools, we

specific modifications. This highlights the importance of manually inspected the filenames of associated shared li-

testing both regional variants [42]. braries (.so) and established mappings between the re-

For app categorization, we relied on a basic mapping ap- ported packer names. In certain cases, translations were

proach by translating Chinese category names and match- necessary, or packer labels were associated with broader

ing them with 29 predefined categories used for non- entities. For example, Baidu [17] is not only a provider of

Chinese apps. Although more sophisticated methods, various Internet products, but also offers Android packing

such as those proposed by Alecci et al. [11], are recog- services. The following mappings exemplify such find-

nized as potential future work, our simplified mapping ings: SecNeo is equivalent to Bang Bang (Bangcle) [18];

provided sufficient granularity for the current scope of Jiagu (as labeled by APKiD) is associated with 360 [8];

analysis. Overall, the dataset and collection methodology 百 度 (Baidu) and 网 易易 盾 (Yidun) are transliterations of

enabled us to systematically investigate how different types their original Chinese names; 腾 讯 御 安 全 is recognized

of apps and market contexts affect the use of anti-analysis as Mobile Tencent Protect; Instances labeled as “ UPX

and packing techniques. modified ” by APKiD were often correctly identified by NP-

Manager as Ijiami [47]. Given the structural and contex-

tual differences between Chinese and non-Chinese apps,

5.2 Packer Identification our analysis initially treated these datasets separately.

Commercial packers usually do not try to hide their pres- Findings. Chinese apps are packed much more frequently

ence, and their names or other traces are often visible in than non-Chinese ones. As shown in Figure 1 and Fig-

packed binaries. Tools like APKiD [13] detect such apps ure 2, the packer identification by APKiD and NP-Manager

by matching known strings, file structures, or libraries. varies due to differences in their databases and updates.

However, APKiD is not maintained as a commercial tool, Additionally, categories such as “finance” in Chinese apps

and its database has outdated entries, which makes it mis- and "sport and health" in non-Chinese apps contain a

classify packers, for example, treating the word “Jiagu” as higher number of packed apps, indicating the prevalence

a specific packer name instead of a general term for pro- of packers in specific app categories.

tection. This shows the need for better detection tools that Our results indicate that 38% (4,735 of 12,431) of the

consider region-specific factors and are up-to-date, such as entire dataset were detected as packed apps. Among

NP-Manager [58], which specializes in Chinese packers. the 7,913 Chinese apps, 4,652 (58.8%) were identified

7

---

## Page 8

as packed by at least one detection tool (NP-Manager or Findings. In total, we found that 2,236 Chinese apps

APKiD), whereas only 83 (2%) of the 4,428 non-Chinese (28.25%) and 366 non-Chinese apps (8.26%) deployed

apps were flagged as packed, supporting the fact that re- anti-Frida mechanisms, targeting either spawn or attach

search based solely on non-Chinese apps did not often operations (see Table 3). This corresponds to 2,078 spawn

report failures due to packers. We provide a more detailed failures and 536 attach failures, which overlap in some

breakdown of packer tier distribution across our dataset in apps, resulting in 2,236 unique cases. Among these, 378

Appendix 13. Chinese apps (4.77%) and 159 non-Chinese apps (3.59%)

5.3 Runtime Anti-analysis Techniques

matching string patterns, or dynamic analysis, e.g., check-

droid debugger respectively at runtime. We have used

nections) to investigate how common anti-Frida techniques

are in practice and not just by heuristics.

Packers react differently when anti-analysis techniques

are triggered. Some delay their response, while others

react immediately. In some cases, the app crashes; in

To determine whether an app crashed or terminated due

to anti-Frida techniques, we applied multiple crash detec-

tion methods in an automated manner. First, we monitor

the logcat output of each app execution for crash details,

such as " FATAL EXCEPTION " and " ANR " (Application Not

8

disrupted Frida in both modes, actively causing crashes

or forced terminations. These results indicate that Chi-

nese apps not only use packing more frequently but also

group.

5.3.2 JDB detection

ically requires setting the android:debuggable flag in

the AndroidManifest.xml file of the APK. However,

nisms [56], thereby compromising the integrity of the anal-

ysis. To overcome this limitation, we adopted an approach

based on modifying the Android source code to enable de-

bugging for non-debuggable apps. This modification was

tested on a Pixel device using the Youpk project [81].

Previous studies have either relied on static analysis such as integrate stronger runtime defenses.

| ing runtime file accesses, which might be inaccurate. For | Packed | Non-packed | Total |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example, an app accessing | /proc/self/maps | that can be | Chinese apps (7,913 total; Packed | 𝑛 | = | 4 | , | 652 | , Non-Packed | 𝑛 | = | 3 | , | 261 | ) |
| for loading Dex code during runtime [41, 15] may be mis- | Frida spawn failures | 1,574 (33.8%) | 504 (15.45%) | 2,078 (26.26%) |  |  |  |  |  |  |  |  |  |  |  |
| takenly marked as anti-DBI tricks by previous dynamic | Frida attach failures | 361 (7.8%) | 175 (5.36%) | 536 (6.77%) |  |  |  |  |  |  |  |  |  |  |  |
| analysis approaches [63, 33, 31]. | Non-Chinese apps (4,428 total; Packed | 𝑛 | = | 83 | , Non-packed | 𝑛 | = | 4 | , | 345 | ) |  |  |  |  |
| Instead, we directly test our dataset apps to identify | Frida spawn failures | 28 (33.7%) | 234 (5.38%) | 262 (5.91%) |  |  |  |  |  |  |  |  |  |  |  |
| Frida and JDB detection as candidates for DBI and An- | Frida attach failures | 23 (27.7%) | 240 (5.52%) | 263 (5.93%) |  |  |  |  |  |  |  |  |  |  |  |

Frida in both “attach” and “spawn” modes (which can pro- Table 3: Frida spawn and attach failure statistics across

vide more details about initial app interactions and con- Chinese and non- Chinese apps. Percentages are per sub-

others, it terminates gracefully or just warns the user that To analyze anti-debugging techniques at runtime, the app

the execution environment is not trusted (e.g., the phone must be executed in a debuggable mode, allowing it to

| is rooted). | launch with the | Waiting for debugger | option. | This typ- |
| --- | --- | --- | --- | --- |
| 5.3.1 | Frida detection | modifying this flag may trigger anti-tampering mecha- |  |  |
| Responding), and also verify app liveness using | ps -A | The dynamic analysis workflow involves forwarding the |  |  |

to detect crashes or terminations. Second, we verify the JDWP port, starting the target app in debug mode using

functionality of the Frida agent by: 1) executing a sim- am start -D -n ACTIVITY_NAME , and attaching to it

ple hooking script to observe expected strings, such as via JDB. If the app requests runtime permissions, they

system properties to make sure the Frida agent is still re- are automatically granted to preserve the fidelity of the

sponsive; 2) examining the Frida client; if it enters the analysis. Any unexpected app crash or premature ter-

truncated mode due to losing communication with the mination of the JDB session is interpreted as an indi-

Frida server, we consider this to be an app crash. Third, cation that an anti-debugging mechanism has been trig-

in the case of app crash or termination, we check the fore- gered. This methodology enables a comprehensive exam-

ground app package name. We use the mCurrentFocus ination of runtime anti-debugging techniques, including

and mFocusedApp properties to identify the focused app those studied through static analysis.

and foreground window in Android. If an app was termi- Findings. Our results shows that 1,960 apps crashed while

nated, the foreground app would differ from the one under attaching to Java Debugger (JDB) in total. Interestingly,

analysis. Additionally, in some cases, the app request per- the number of non-Chinese non-packed apps that expe-

missions through a dialog box, which our automation tool rienced crashes was higher than that of the non-Chinese

takes into account. packed apps. Our findings are summarized in Table 4.

---

## Page 9

400 387 384

341

320 320

294

300 291 285 293 290

205 206

200

175 178

100

38 40

0

photography productivity

20

15

1 2 2 1 2 2

0 1 0 0 1 1 0 1

0

entertainment food and drink house and homes

maps and navigation news and magazines

non-Chinese apps (packed 𝑛 = 83 , non-packed 𝑛 = 4 , 345 ), 4,428 total

JDB failures 11 (13.25%) 486 (11.18%) 497 (11.22%)

Table 4: JDB failure statistics across Chinese and non-

Chinese apps. Percentages are per subgroup.

bypassing runtime checks that would otherwise cause the

app to crash or terminate itself and still allowing the anal-

ysis tool to access whatever remains available at runtime

9

NP-Manager APKiD 358

337

277 284 287

273 269 267

253

237 233 236 230

208 213

189

150

53

Categories

21

NP-Manager APKiD

11

5

2 2 2

0 1 0 1 1 1 2 2 1 0 1

personalization photography

sport and health

travel and location

Categories

codeshare.frida.re ). Thus, we choose to use one to

enable the other to achieve a balance between stealth and

practicality to support effective yet undetectable dynamic

analysis.

Unlike prior dynamic analysis approaches that rely on

AOSP/kernel modifications or emulation, leading to poor

portability, instability and maintenance overhead, Purifire

remains lightweight, scalable, and safe while enable ex-

without app modification, supports Google Play services,

6.1 Purifire Overview

| #Packed Apps | 112 | 114 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| education | finance | music | parenting | reading | shopping | social | system | tools | video |
| communication | life and services | personalization | sport and health | tourism and hotel | travel and location |  |  |  |  |

Figure 1: Comparison of Chinese packed apps across different categories using NP-Manager and APKiD.

| 10 | 8 | 7 | 7 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #Packed Apps | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 |  |  |
| business | dating | finance | lifestyle | medical | parenting | reading | shopping | social | tools | vehicle | weather |

Figure 2: Comparison of non-Chinese packed apps across different categories using NP-Manager and APKiD.

| Packed | Non-packed | Total | making detection harder. | However, eBPF lacks Frida’s |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chinese apps (packed | 𝑛 | = | 4 | , | 652 | , non-packed | 𝑛 | = | 3 | , | 261 | ), 7,913 total | high-level programmability (e.g., Javascript and Python) |
| JDB failures | 872 (18.74%) | 591 (18.12%) | 1,463 (18.48%) | and usability for Android app analysis (e.g., | https:// |  |  |  |  |  |  |  |  |
| 6 | Living with the Packers | isting DBIs like Frida. Purifire achieves practical analysis |  |  |  |  |  |  |  |  |  |  |  |

In this section, we implement our proposed idea of living and offers a balanced trade-off between stealth, portability,

with packers, given the ineffectiveness of unpacking, by and effectiveness (see Table 5).

(already released/extracted for execution). We propose Purifire, an eBPF-based evasion engine that is

Balancing stealth and usability. Frida provides a flexible able to bypass anti-analysis techniques at runtime without

and programmable interface widely adopted by security being detected. It accepts Defined Evasion Rule (DER)s

analysts, but its popularity has led to the development of as configuration files and applies evasion rules on the fly

numerous detection methods. In contrast, eBPF operates to enable dynamic analysis tools such as Frida. To the

at the kernel level, offering lower visibility to the app and best of our knowledge, Purifire is the first offensive eBPF

---

## Page 10

No App Modification Not Visible to App Portable Scalable Safe System-Level Monitoring Google Play Services

| AOSP Modification | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kernel Module | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |
| App Modification | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ |
| Library Injection | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ |
| Purifire | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Table 5: Comparison of instrumentation techniques for enabling Android app dynamic analysis.

application that manipulates app memory to evade detec- function. Combined with stack backtraces obtained us-

tion. Previous eBPF-based works have mostly focused on ing the bpf_get_stack() eBPF helper, this process help

monitoring and instrumentation [86]. DER authors identify suspicious syscalls more accurately

Figure 3 provides an overview of Purifire. Purifire con- and avoid manipulating unrelated regions during the eva-

sists of three components: a userland program, an eBPF sion phase (see Appendix 12).

kernel-side program, and a configuration file named DER. Runtime evasion. It filters syscall events and manipulates

Purifire applies runtime memory patches based on DERs memory when specific conditions defined in the DERs are

to the app’s process context in order to bypass anti-analysis met, such as a particular syscall argument or a specific

techniques. value in a memory region.

read/write/execute

DERs config file Packed

apps'

( D efined E vasion

R ule) Purifire Packed app memory

User space

Kernel space

bpf_probe_write_user()

bpf_probe_read_user()

Kprobes (eBPF side)

Kernel

following.

Assisted analysis. It provides syscall-level observation

for the DER authors to find suspicious candidate to ma-

Defined evasion rules. DERs are Purifire’s configuration

files that define evasion strategies. Each DER rule consists

of two parts: condition and evasion. The condition spec-

ifies filters to exclude irrelevant events, ensuring that Pu-

rifire only targets anti-analysis techniques and avoids ma-

with the anti-analysis protection of a packer library. For

example, it can filter based on the package name (comm)

part of the rule identifies the userspace pointer that Pu-

rifire intends to modify by writing directly into the app’s

memory.

Components. The user-space program (controller) is re-

On the kernel-space side, the core enforcement logic is im-

plemented as eBPF programs attached to kprobes and tra-

cepoints for critical system calls (e.g., ptrace , mprotect ,

arguments, thread identifiers, and calling context. When a

6.3 Workflow

10

| syscalls | nipulating the wrong locations. Listing 1 illustrates how |  |  |  |
| --- | --- | --- | --- | --- |
| [RingBuffers] | a DER can focus on a specific syscall (event) associated |  |  |  |
| Tracepoints | Purifire | and then select the syscall to manipulate. | The | evasion |

Figure 3: Purifire Overview. This diagram illustrates how sponsible for parsing DER configuration files and translat-

Purifire captures system calls and manipulates application ing them into filtering and patching policies. It loads these

memory using eBPF. rules into the kernel via eBPF interfaces e.g., RingBuffers .

6.2 Architecture openat , readlinkat and prctl ). They monitor syscall

Our approach combines a configuration-driven controller DER matches (via bpf_probe_read_user() ), the eBPF

in user-space with an eBPF-based enforcement engine in programs can alter the syscall outcome or patch user mem-

kernel space, providing stealthy, flexible, and adaptive eva- ory directly via bpf_probe_write_user() . The packed

sion at runtime. The kernel-space and user-space compo- app continues executing as normal, with its runtime envi-

nents of Purifire achieve two purposes explained in the ronment transparently modified.

nipulate. We have also developed a syscall-memory map As one-time effort per packer version, a DER author can,

generator that finds which memory regions have been allo- manually, with the help of Purifire’s assisted analysis, iden-

cated and what syscalls are originally generated from what tify candidate syscalls to manipulate and refine them by

memory regions. We trace mmap and mprotect syscalls to targeting specific arguments. The author must then map

generate memory maps, including those originating from these syscalls to the corresponding anti-analysis princi-

the packer library at runtime. Each syscall is then linked ples (see Table 1) that cause the app to crash and construct

to its corresponding memory region to determine its caller DERs to bypass them. Figure 4 illustrates how the DER

---

## Page 11

Listing 1: DER configuration examples.

1 /* Example 1 */

2 {

| 6 | "syscall": "openat", |
| --- | --- |
| 7 | "args": { "1": "/proc/self/task/" } |
| 8 | }, |
| 10 | "where": "args1", |
| 11 | "data": "/data/local/tmp/fake" |

15 /* Example 2 */

16 {

| 20 | "syscall": "mprotect", |
| --- | --- |
| 23 | }, |
| 24 | "evasion": { |

28 }

example in Listing 1 can be applied to evade an anti-Frida

technique from the file-based tool detection category in

Table 1. As demonstrated, a single anti-analysis method

may expose multiple manipulation points (e.g., openat() ,

read() , clone syscalls) that the DER author can exploit

to construct different DERs. In some cases, it is also pos-

sible to completely nullify the anti-analysis protection by

preventing the creation of its monitoring thread (patching

code that calls clone() ).

Candidate frida-related thread

/proc/self/task/TID/stat

Actual string: (gum-js-pool)

| analyzer | mapper | tracer | Packer | /App | openat() |
| --- | --- | --- | --- | --- | --- |
| (3) | fake runtime data |  |  |  |  |
| read() | Purifire(DERs) | /data/local/tmp/fake |  |  |  |
| clone() | Fake | string: (main) |  |  |  |

data flow

sion, if the code and data can be patched statically, meaning

the anti-analysis logic already exists in the APK and does

not require runtime decryption, it is possible to patch the

ing is a more promising approach to bypass anti-analysis

techniques.

menting with different data manipulation strategies to find

syscall argument to redirect the app to a dummy file, or

versus without it, stack trace analysis, and syscall-region

Anti-analysis techniques are not limited to syscalls and

may also rely on memory checks, such as strstr()

or inline memory comparisons, which cannot be traced

via syscalls. In such cases, a DER author can leverage

stealthy eBPF-based memory dumpers [7] to locate sus-

picious strings in the app’s memory and calculate offsets

for use in the DER. For example, after decryption, the Iji-

ami packer actively opens /proc/self/wchan based on

syscall origin maps (see Appendix 12), while other checks

can be inferred from previously dumped data, such as lo-

cating the ptrace_stop string offset (part of debugging

final DER can then be defined by filtering mprotect or

Listing 1 Example 2, 0xde5ce is the size) and expected

memory location (in Listing 1 Example 2, args0 as base

address and 0x6aae4 as code offset resulted from stack

trace and memory-syscall mapping from previous runs).

Another example is identifying suicidal code (instructions

the kill syscall responsible for termination. Even if the

11

| 3 | "condition": { | APK directly but when it comes to modern packers that |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 4 | "comm": "com.example.test", | decrypt code and data at runtime, any beforehand patching |  |  |  |
| 5 | "tname": "*", | becomes challenging. As a result, runtime memory patch- |  |  |  |
| 9 | "evasion": { | DER considerations. | Designing DERs requires experi- |  |  |
| 12 | } | a working bypass, which is often challenging and require |  |  |  |
| 13 | } | manual analysis in this cat-and-mouse setting. Manipula- |  |  |  |
| 14 | tion points can vary; for example, altering an | openat() |  |  |  |
| 17 | "condition": { | modifying the subsequent | read() | syscall for finer-grained |  |
| 18 | "comm": "com.example.test", | control. In general, the fewer modifications made to the |  |  |  |
| 19 | "tname": "*", | app, the better stealthiness can be ensured. |  |  |  |
| 21 | "args": { "0": "arg0", "1": "0xde5c0", "2": "0x5" | The DER author can observe which syscall causes the |  |  |  |
| ... }, | app to crash or terminate and perform differential analysis |  |  |  |  |
| 22 | "data": "\\x28\\x10\\x80\\xd2\\x01\\x00\\x00\\xd4" | by comparing the app’s behavior when run with Frida |  |  |  |
| 25 | "where": "args0 + 0x6aae4", | mapping (assisted analysis using Purifire Figure 4). This |  |  |  |
| 26 | "data": "\\x00\\x00\\x80\\xd2\\x1f\\x20\\x03\\xd5" | process can highlight candidate syscalls for investigation, |  |  |  |
| 27 | } | narrowing the search space for effective evasion rules. |  |  |  |
| (1) | Analysis | (2) | Designing | DERs | fingerprints) and patching it once loaded into memory. A |
| identification | mmap | syscalls and validating arguments such as size (in |  |  |  |
| Differential | Syscall-region | Stack/syscall | (4) | data flow | data. If these conditions are met, Purifire overwrites the |

Figure 4: Purifire example scenario. This diagram il- that cause the app to crash or terminate) and patching it.

lustrates how Purifire uses DERs to bypass runtime anti- With the stack trace provided by Purifire’s assisted analy-

analysis techniques triggered by syscall events. sis, the DER author can locate caller functions and patch

Considering the workflow of packers, multi-stage tech- packer marks this code as read-and-execute only, the DER

niques [34], dynamic code loading (see Figure 5 in Ap- author can still calculate the syscall offset and apply the

pendix 15), and data encryption, the event-driven evasion patch on mprotect event (see Listing 1).

| engine is more effective than fixed patches, which are case- | In summary, Purifire’s assisted analysis tracks memory |
| --- | --- |
| specific and easily broken by minor packer changes. | region permission changes and provides stack trace–based |

Runtime memory patching. From the perspective of eva- offsets to help DER authors design precise filters and

---

## Page 12

patches. Despite the (semi-)manual effort, the resulting

DER configuration files can then be shared and maintained

havior. Note that certain works did not report how packed

apps affected their results or a dataset without Chinese

apps was used.

on a Pixel 7 Pro running Android 15 with kernel ver-

/data/local/tmp/purifire/ directory.

niques that lead to crash/termination while being spawned

under Frida instrumentation. We repeated the detection

pass known tricks, including anti-root and anti-Frida (cov-

Table 6 presents the apps on which Purifire success-

centrated in tools, finance, and system, whereas non-

12

Table 6: Purifire-enabled apps (packed vs. non-packed).

| Packed apps (N=448) | Non-packed apps (N=214) |  |  |  |
| --- | --- | --- | --- | --- |
| education | 38 | 8.48% | 8 | 3.74% |
| life_services | 26 | 5.80% | 12 | 5.61% |
| music | 19 | 4.24% | 6 | 2.80% |
| parenting | 18 | 4.02% | 3 | 1.40% |
| personalization | 15 | 3.35% | 5 | 2.34% |
| productivity | 25 | 5.58% | 10 | 4.67% |
| reading | 30 | 6.70% | 18 | 8.41% |
| social | 28 | 6.25% | 18 | 8.41% |
| tools | 55 | 12.28% | 7 | 3.27% |
| video | 14 | 3.12% | 12 | 5.61% |

(N=448).

| Jiagu | 161 | 35.94% |
| --- | --- | --- |
| Ijiami | 22 | 4.91% |
| Tencent Protect | 20 | 4.46% |
| SecNeo | 14 | 3.13% |
| Baidu | 6 | 1.34% |
| CrazyDog Wrapper | 3 | 0.67% |
| Approov | 1 | 0.22% |

their tool on our entire dataset.

| by the community, enabling other analysts to reuse them | Category | #bypassed | percentage (%) | #bypassed | percentage (%) |  |
| --- | --- | --- | --- | --- | --- | --- |
| for dynamic analysis and contributing to a growing public | communication | 3 | 0.67% | 9 | 4.21% |  |
| knowledge base. | finance | 48 | 10.71% | 17 | 7.94% |  |
| 7 | Evaluation | photography | 29 | 6.47% | 16 | 7.48% |
| In this section, we demonstrate experimentally and com- | shopping | 18 | 4.02% | 9 | 4.21% |  |
| paratively how Purifire can improve the outcome of state- | sport & health | 21 | 4.69% | 12 | 5.61% |  |
| of-the-art Android app security analysis, e.g., academic | system | 30 | 6.70% | 5 | 2.34% |  |
| papers involving hooking that could have been affected by | tourism_hotel | 8 | 1.79% | 1 | 0.47% |  |
| packers (see Section 3.1). | This shows how Purifire can | travel_location | 23 | 5.13% | 8 | 3.74% |
| benefit security research, e.g., against undesired app be- | Total | 448 | 100% | 214 | 100% |  |

Environment setup. We conducted our experiments Table 7: Purifire-enabled packed apps by packer names

| sion 5.10. | The device was rooted using Magisk [48] | Packer | #Bypassed apps | Percentage (%) |  |
| --- | --- | --- | --- | --- | --- |
| (version 28.1) with Zygisk enabled. | To facilitate dy- | SecNeo.A | 99 | 22.10% |  |
| namic analysis, we installed the Frida server and de- | yidun | 40 | 8.93% |  |  |
| ployed our tool, | Purifire, | alongside the DERs to the | SecNeo.B | 36 | 8.04% |
| 7.1 | Frida with Purifire | UPX / sharelib | 6 | 1.34% |  |
| Our prevalence analysis (see Section 5) confirmed that | Bangcle | 2 | 0.45% |  |  |
| 2,340 apps in our dataset employed anti-analysis tech- | Total | 448 | 100% |  |  |

phase with Purifire enabled and configured DERs to by- 7.2 Device Fingerprinting with Purifire

ering artifacts described in Section 4.1). We successfully Heid et al. [45] used Frida to hook specific APIs in order

ran Frida on additional 662 apps (enabled Frida on 28.2% to identify apps that perform device fingerprinting. We

of those with anti-analysis tricks or 5.30% on our entire evaluated their tool on our dataset and measured the num-

dataset) that would otherwise crash or terminate without ber of Total Device Fingerprints (TFD) it produced. We

Purifire. Note that the 662 apps were what our DERs en- then repeated the experiment, this time running Purifire

abled us to cover, not all the possibilities, e.g., if DERs for alongside their tool, and collected the resulting data. The

more packers were provided, the corresponding number of number of identified Unique Device Fingerprints (UDF)

| more apps would be saved. | increased significantly when Purifire was used. | We ran |
| --- | --- | --- |
| fully enabled Frida, highlighting clear differences between | • | Number of UDF without Purifire: 79,260 |
| packed and non-packed categories: packed apps are con- | • | Number of UDF with Purifire: 131,173 |

packed apps are more prevalent in social, reading, and The number of UDFs still observed without Purifire is

photography. Table 7 further illustrates the packer distri- due to anti-analysis checks triggered with a delay, dur-

bution in our evaluation, showing that Jiagu, SecNeo, and ing which the app or packer continued collecting UDFs.

yidun together account for nearly three quarters of packed Table 8 shows that Purifire increased UDF capture by

apps, underscoring both Purifire’s effectiveness and the 65.5% across 1,214 apps. The largest gains appeared in

dominance of a few commercial solutions in Android app music (+555.4%), beauty (+273.6%), event (+184.4%),

protection. personalization (+168.3%), and news_and_magazines

---

## Page 13

(+173.8%), while categories like video (+1.7%) and art side each other since they target different layers of the

(+2.5%) saw minimal change. These results highlight system. This enables security practitioners to leverage

Purifire’s effectiveness in enhancing fingerprint visibility, Purifire in conjunction with Frida scripts to effectively

particularly in user-facing domains where tracking and bypass anti-analysis checks while maintaining dynamic

personalization are common. instrumentation capabilities.

Table 8: Numbers of UDF/TDF captured before/after ap-

plying Purifire by category. UDF is from deduplicating

TDF.

| art | 12 | 1688 | 1730 | 26490 | 27609 | 2.49% |
| --- | --- | --- | --- | --- | --- | --- |
| business | 4 | 549 | 566 | 7369 | 8616 | 3.10% |
| communication | 32 | 1612 | 3884 | 29385 | 67273 | 140.94% |
| dating | 45 | 4984 | 6101 | 65284 | 88356 | 22.41% |
| education | 45 | 2191 | 4327 | 33776 | 87380 | 97.49% |
| event | 21 | 920 | 2616 | 16274 | 43666 | 184.35% |
| food_and_drink | 65 | 4610 | 8291 | 67783 | 135895 | 79.85% |
| life_services | 11 | 806 | 976 | 13930 | 16323 | 21.09% |
| location | 1 | 171 | 178 | 1492 | 1971 | 4.09% |
| medical | 23 | 2039 | 2474 | 35117 | 44783 | 21.33% |
| music | 192 | 1889 | 12381 | 23090 | 267838 | 555.43% |
| news_and_magazines | 97 | 4319 | 11824 | 45764 | 209824 | 173.77% |
| parenting | 13 | 1488 | 1561 | 27159 | 28118 | 4.91% |
| photography | 31 | 3412 | 3934 | 56701 | 66690 | 15.30% |
| reading | 34 | 3238 | 3682 | 55369 | 64524 | 13.71% |
| social | 78 | 3690 | 7086 | 56713 | 118919 | 92.03% |
| system | 30 | 1552 | 2204 | 23969 | 49773 | 42.01% |
| tourism_hotel | 3 | 80 | 169 | 2388 | 3490 | 111.25% |
| travel_location | 50 | 3711 | 5184 | 65612 | 101753 | 39.69% |
| video | 12 | 1383 | 1407 | 22575 | 23675 | 1.74% |

7.3 Covert Identifier Detection with Purifire

Dong et al. [32] used Frida in their dynamic analysis

pipeline to collect third-party SDK file operations on exter-

nal storage that allow them to track users across multiple

13

Low deployment requirement. To use Purifire, merely a

rooted phone is needed. Obviously, this can trigger root

detection mechanisms, which are then bypassed with well-

defined DERs. In comparison, most unpackers are more

even hardware support [78].

time.

ory analysis (e.g., heap dumping), and instrumentation

tasks such as function hooking [68].

9 Limitations

silently without clear logcat evidence, and our tests only

covered app launch and initial permissions. This limita-

may be triggered only through specific user interactions

| Category | #Apps | Í | UDF | 𝑏𝑒 𝑓 𝑜𝑟𝑒 | Í | UDF | 𝑎 𝑓 𝑡𝑒𝑟 | Í | TDF | 𝑏𝑒 𝑓 𝑜𝑟𝑒 | Í | TDF | 𝑎 𝑓 𝑡𝑒𝑟 | UDF | Δ | (%) | invasive, requiring, e.g., custom AOSP builds [80, 66], |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| beauty | 21 | 769 | 2873 | 10085 | 40091 | 273.60% | ART modifications [84, 85], loading kernel modules or |  |  |  |  |  |  |  |  |  |  |
| entertainment | 9 | 663 | 884 | 9438 | 18237 | 33.33% | Code and data integrity checks by packers. | Cur- |  |  |  |  |  |  |  |  |  |
| finance | 43 | 3694 | 5517 | 54726 | 83184 | 49.35% | rently, Purifire targets | syscall_enter | events, and it is |  |  |  |  |  |  |  |  |
| house_and_homes | 32 | 3562 | 4208 | 51070 | 64040 | 18.14% | possible to roll back changes and memory patches at |  |  |  |  |  |  |  |  |  |  |
| lifestyle | 28 | 2902 | 3311 | 46206 | 56885 | 14.09% | syscall_exit | by reverting the DER configurations. This |  |  |  |  |  |  |  |  |  |
| maps_and_navigation | 45 | 4011 | 5635 | 66324 | 98694 | 40.49% | helps avoid integrity checks performed by packers at run- |  |  |  |  |  |  |  |  |  |  |
| personalization | 32 | 1188 | 3187 | 22750 | 64583 | 168.27% | How | Purifire | helps | security | researchers. | By | en- |  |  |  |  |
| productivity | 10 | 481 | 678 | 12185 | 15825 | 40.96% | abling tools like Frida on packed apps, Purifire revives |  |  |  |  |  |  |  |  |  |  |
| shopping | 58 | 4644 | 7182 | 64207 | 109206 | 54.65% | research areas such as privacy leakage, SDK misuse, |  |  |  |  |  |  |  |  |  |  |
| sporthealth | 65 | 6315 | 8388 | 81439 | 125831 | 32.83% | and fingerprinting studies that were previously hindered. |  |  |  |  |  |  |  |  |  |  |
| tools | 29 | 2875 | 3667 | 41799 | 59668 | 27.55% | Through bypassing runtime anti-analysis techniques, it al- |  |  |  |  |  |  |  |  |  |  |
| vehicle | 9 | 803 | 1002 | 10431 | 15408 | 24.78% | lows Frida-based inspection for network traffic analysis |  |  |  |  |  |  |  |  |  |  |
| weather | 34 | 3021 | 4066 | 52758 | 74493 | 34.59% | (e.g., detecting Personally Identifiable Information (PII) |  |  |  |  |  |  |  |  |  |  |
| Total | 1,214 | 79,260 | 131,173 | 1,199,658 | 2,282,621 | 65.50% | exposures, certificate pinning, and TLS/SSL issues), mem- |  |  |  |  |  |  |  |  |  |  |

apps, as a covert channel. They acknowledged failures DER creation. Purifire is an evasion engine that relies

with a subset of apps due to packing services. In con- on DERs (the rules) to function. While this involves man-

sideration of this, unlike our previous two experiments, ual effort and domain knowledge (although with the help

we opted to be more targeted to packed apps (more accu- of Purifire’s assisted analysis), the effort is one-time per

rately apps with anti-analysis techniques that hindered the packer version and can be circulated in the community.

authors’ analysis). Kernel version. Since Purifire relies on specific eBPF

To measure Purifire’s benefit, we randomly selected 70 functionality, devices with kernel version 5.10 or higher,

apps from the 662 apps which we have the DERs for from such as Google Pixel 6 and newer, are required. Although

Section 7.1. This small subset is due to the nature of eBPF can also run on emulators, kernel version remains

Dong et al.’s analysis requiring manual interaction with critical for both devices and emulators, as different ver-

each app’s UI, hence limiting the scale of the test. We sions support varying features that impact effectiveness.

observed that on 35 such apps, Purifire boosted the total Ensuring compatibility between the kernel and the re-

number of observed shared-location file accesses from 267 quired eBPF features is therefore essential to avoid lim-

to 7,565 and unique accesses from 133 to 3,355, indicating itations or inconsistent behavior.

| an improvement of 27 | × | more total and 24 | × | more unique | Conditional | anti-analysis | checks. | Identifying | anti- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| file operations for tracking users. | analysis tricks was challenging, as some crashes occurred |  |  |  |  |  |  |  |  |
| 8 | Discussion | tion is common in dynamic analysis, where protections |  |  |  |  |  |  |  |

Frida and Purifire cooperation. Purifire operates inde- or delayed routines. Since our runtime analysis was re-

pendently of Frida, allowing both tools to function along- stricted to 15 seconds, certain defenses may have gone

---

## Page 14

undetected, making the results in Section 5 a conservative anti-analysis techniques of the packers. We evaluated Puri-

lower bound. fire by measuring the number of additional apps (for which

Java-based anti-analysis checks. Purifire is limited in we have the known DERs) and more importantly, the ex-

fully Java-based APIs manipulation due to parsing ART tent to which past dynamic analysis works can benefit from

functions and stack unwinding as eBPF programmability Purifire, e.g., we were able to see significantly more de-

is very limited and has to pass verifier. We consider this vice fingerprints for a fingerprinting detection paper and

to be future work. access operations for an SDK covert channel detection

Non-writable memory regions. In general, writing to paper, compared to when running without Purifire. Our

memory regions that are not flagged as writable is a lim- work sheds light on future research to achieve a balance

itation of Purifire. Nonetheless, by combining runtime between privacy, security, and intellectual property.

offset calculation with the use of mprotect events, it be-

comes possible to write to memory locations that were

initially loaded with rw- permissions and later changed to

read-only regions.

10 Related Work

There has been a vast collection of published studies on

packing/unpacking efforts as well as related analyses and

surveys. In this section, we briefly discuss several. Refer

sis artifacts, but suffers from maintainability issues and

fective against native-code anti-analysis techniques. Rug-

gia et al. [63] propose DroidDungeon, a sandbox with

stack unwinding, but its reliance on fixed anti-evasion lists

limits adaptability. PackDiff [31] applies multi-layer in-

strumentation for differential analysis but is constrained

by Android versioning and its only focus on free pack-

ing services. Finally, NCScope [86] combines hardware

tracing (ETM 1 ) with eBPF for semantic analysis, though

its dependency on specialized hardware restricts usability.

For identifying anti-analysis tricks, Sue et al. [67] manu-

11 Conclusion

By confirming the high impact of Android packers with a

prevalence analysis (particularly on Chinese apps), and the

allow tools like Frida to analyze what remains available

at runtime. We designed and implemented Purifire using

eBPF that takes evasion rules (DERs) as input to bypass

14

References

[1] Appdome – ai-native protection for the mobile busi-

ness. https://www.appdome.com/ . Accessed:

2025-08-12.

[2] Doverunner – complete mobile application and con-

tent security. https://doverunner.com/ . Ac-

cessed: 2025-08-12.

15.

[5] Play integrity api – google play security and in-

tegrity services. https://developer.android.

com/google/play/integrity . Accessed: 2025-

08-13.

[6] sensepost/objection: Runtime mobile exploration

toolkit powered by frida. https://github.com/

sensepost/objection . Accessed: 2025-08-15.

//github.com/eurecom-s3/lemon , 2025. Ac-

cessed: 2025-08-19.

[8] 360 Developer. 360 developer platform, 2025. Ac-

cessed: 2025-02-09.

[10] Abdulla Aldoseri and David Oswald. insecure:: Vul-

nerability analysis of uri scheme handling in android

mobile browsers. In Workshop on Measurements,

| to Section 4.2 for a survey of unpackers. | [3] Firebase — google’s mobile and web app devel- |  |  |
| --- | --- | --- | --- |
| To achieve packer evasion, Davinci [33] uses a kernel | opment platform. | https://firebase.google. |  |
| module to hook specific system calls and conceal analy- | com/ | . Accessed: 2025-08-13. |  |
| limited flexibility as they only manipulate syscall return | [4] hluwa/frida-dexdump: A frida tool to dump dex in |  |  |
| values. Rasthofer et al. [61] addressed emulator detection | memory for malware analysis. | https://github. |  |
| with Dex code slicing, but their approach remains inef- | com/hluwa/frida-dexdump | . Accessed: 2025-08- |  |
| ally created fingerprints and applied them to detect similar | [7] eurecom-s3/lemon: Lemon – an ebpf memory dump |  |  |
| techniques in other apps. | tool for x64 and arm64 linux and android. | https: |  |
| ineffectiveness of current unpackers with an experimental | [9] 360 Security Technology Inc. So app - mobile secu- |  |  |
| survey, this paper proposed a paradigm shift to create an | rity and utility application. | https://app.so.com/ | , |
| evasion framework that exists alongside packers, to still | 2025. Accessed: 2024-05-23. |  |  |
| 1 | Embedded Trace Macrocell, an optional hardware component in | Attacks, and Defenses for the Web (MADWeb) 2022 | . |
| ARM processors that provides real-time instruction and data tracing. | The Internet Society, 2022. |  |  |

---

## Page 15

[11] Marco Alecci, Jordan Samhi, Tegawende F. Bis- [23] Ch0pin. medusa: A binary instrumentation frame-

| syande, and Jacques Klein. Revisiting android app | work based on frida. | GitHub repository, | https: |  |
| --- | --- | --- | --- | --- |
| categorization. | In | Proceedings of the IEEE/ACM | //github.com/Ch0pin/medusa | , 2025. Accessed: |
| 46th International Conference on Software Engineer- | 2025-08-15. |  |  |  |

ing , ICSE ’24, New York, NY, USA, 2024. Associa-

pollina, Davide Freggiaro, Alderico Gallo, and

Marco Guazzone. Enabling the forensic study of

[13] APKiD. https://github.com/rednaga/APKiD ,

2025.

[14] APKPure. Apkpure - free and safe android apk down-

loads. https://apkpure.com/ , 2025. Accessed:

2024-04-20.

[15] Daniel Arp, Michael Spreitzenbarth, Malte Hubner,

Hugo Gascon, Konrad Rieck, and CERT Siemens.

Drebin: Effective and explainable detection of an-

droid malware in your pocket. In Ndss , volume 14,

dev/ , 2025. Accessed: 2025-01-08.

tents (t). In 2015 30th IEEE/ACM International Con-

ference on Automated Software Engineering (ASE) ,

pages 669–679. IEEE, 2015.

[22] Jiajin Cai, Tongxin Li, Can Huang, and Xinhui Han.

Redex: Unpacking android packed apps by executing

and Communications (TrustCom) , pages 337–344.

IEEE, 2020.

15

usage of the jni api in android apps. https:

cessed: 2025-05-24.

Security Symposium (USENIX Security 21) , pages

3451–3468, 2021.

[26] Haehyun Cho, Jongsu Lim, Hyunki Kim, and

Jeong Hyun Yi. Anti-debugging scheme for pro-

tecting mobile apps on android platform. J. Super-

comput. , 72(1):232–246, January 2016.

[27] Cocos. Cocos - cross-platform game development

engine. https://www.cocos.com/en , 2025. Ac-

cessed: 2025-01-08.

01-08.

Wang, Dali Zhu, Ting Su, Xiaodong Zhang, and

[30] Michalis Diamantaris, Elias P Papadopoulos, Evan-

gelos P Markatos, Sotiris Ioannidis, and Jason Po-

lakis. Reaper: real-time app analysis for augmenting

gineering Conference and Symposium on the Foun-

dations of Software Engineering , ESEC/FSE 2022,

tion for Computing Machinery. [24] chame1eon. jnitrace: A frida-based tool that traces

[12] Cosimo Anglano, Massimo Canonico, Andrea Ce- //github.com/chame1eon/jnitrace , 2025. Ac-

application-level encrypted data in android via a [25] Binlin Cheng, Jiang Ming, Erika A Leal, Haotian

| frida-based decryption framework. | In | Proceedings | Zhang, Jianming Fu, Guojun Peng, and Jean-Yves |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| of the 18th International Conference on Availability, | Marion. | { | Obfuscation-Resilient | } | executable payload |  |
| Reliability and Security | , pages 1–10, 2023. | extraction from packed malware. | In | 30th USENIX |  |  |
| pages 23–26, 2014. | [28] CodingGay. | Blackdex - runtime decryption of |  |  |  |  |
| [16] Aya Rust. Aya - a rust library for ebpf and bpf type | android | applications. | https://github.com/ |  |  |  |
| format (btf) in the linux kernel. | https://aya-rs. | CodingGay/BlackDex/ | , 2025. | Accessed: | 2025- |  |
| [17] Baidu. Baidu app, 2025. Accessed: 2025-02-09. | [29] Huajun Cui, Guozhu Meng, Yan Zhang, Weiping |  |  |  |  |  |
| [18] Bangcle. | Bangcle security solutions, 2025. | Ac- | Yuejun Li. | Tracedroid: | A robust network traffic |  |
| cessed: 2025-02-09. | analysis framework for privacy leakage in android |  |  |  |  |  |
| [19] Paulo Barros, René Just, Suzanne Millstein, Paul | apps. | In | Science of Cyber Security: | 4th Interna- |  |  |
| Vines, | Werner | Dietl, | Marcelo | d’Amorim, | and | tional Conference, SciSec 2022, Matsue, Japan, Au- |
| Michael D Ernst. | Static analysis of implicit con- | gust 10–12, 2022, Revised Selected Papers | , page |  |  |  |
| trol flow: Resolving java reflection and android in- | 541–556, Berlin, Heidelberg, 2022. Springer-Verlag. |  |  |  |  |  |
| [20] Ulrich Bayer, Imam Habibi, Davide Balzarotti, Engin | the android permission system. | In | Proceedings of |  |  |  |
| Kirda, and Christopher Kruegel. A view on current | the Ninth ACM Conference on Data and Application |  |  |  |  |  |
| malware behaviors. In | LEET | , 2009. | Security and Privacy | , pages 37–48, 2019. |  |  |

[21] Stefano Berlato and Mariano Ceccato. A large-scale [31] Zikan Dong, Hongxuan Liu, Liu Wang, Xiapu Luo,

| study on the adoption of anti-debugging and anti- | Yao Guo, Guoai Xu, Xusheng Xiao, and Haoyu |  |  |
| --- | --- | --- | --- |
| tampering protections in android apps. | Journal of | Wang. What did you pack in my app? a systematic |  |
| Information Security and Applications | , 52:102463, | analysis of commercial android packers. In | Proceed- |
| 2020. | ings of the 30th ACM Joint European Software En- |  |  |
| every method. In | 2020 IEEE 19th International Con- | page 1430–1440, New York, NY, USA, 2022. Asso- |  |
| ference on Trust, Security and Privacy in Computing | ciation for Computing Machinery. |  |  |

---

## Page 16

| [32] Zikan Dong, Tianming Liu, Jiapeng Deng, Li Li, | [43] hanbinglengyue. | Fart | - | a | framework | for |
| --- | --- | --- | --- | --- | --- | --- |
| Minghui Yang, Meng Wang, Guosheng Xu, and | android | reverse | engineering | and | taint | analy- |
| Guoai Xu. | Exploring covert third-party identifiers | sis. | https://github.com/hanbinglengyue/ |  |  |  |
| through external storage in the android new era. In | FART/tree/master | , 2025. Accessed: 2025-01-08. |  |  |  |  |

33rd USENIX Security Symposium (USENIX Secu-

Workshops, AIBlock, AIHWS, AIoTS, Cloud S&P,

[34] Yue Duan, Mu Zhang, Abhishek Vasisht Bhaskar,

Heng Yin, Xiaorui Pan, Tongxin Li, Xueqiang Wang,

[35] eBPF.io. ebpf - extended berkeley packet filter.

[36] Epic Games. Unreal engine mobile games -

08.

[37] filecxx. File centipede: All-in-one internet file up-

load/download manager. https://filecxx.com/

en_US/index.html , 2025. Accessed: 2025-05-08.

velopers, reverse engineers, and security researchers.

https://frida.re/ , 2025. Accessed: 2025-01-

08.

ssl_logger , 2015. Archived by Google on Decem-

2025-01-08.

[41] Pierre Graux, Jean-François Lalande, and Valérie

Viet Triem Tong. Obfuscated android application de-

velopment. In Proceedings of the Third Central Eu-

ropean Cybersecurity Conference , pages 1–6, 2019.

Cai. Code speaks louder: Exploring security and

privacy relevant regional variations in mobile appli-

cations. In IEEE Symposium on Security and Privacy

(S&P) , pages 3952–3970, 2025.

16

der, Julian Kirsch, and Tilo Müller. Honey, i shrunk

ciplinary Cybersecurity Conference , pages 11–18,

2024.

Applications, and Services , pages 150–162, 2021.

2025-02-09.

[49] Simon Koch, Benjamin Altpeter, and Martin Johns.

The { OK } is not enough: A large scale study of

consent dialogs in smartphone applications. In 32nd

USENIX Security Symposium (USENIX Security 23) ,

[50] Brian Kondracki, Babak Amin Azad, Najmeh Mi-

ramirkhani, and Nick Nikiforakis. The droid is in the

details: Environment-aware evasion of android sand-

Mingxue Zhang, and Xiaosong Zhang. Bpfdex: En-

and Security , 2025.

[52] Yijing Liu, Yiming Zhang, Baojun Liu, Haixin Duan,

Qiang Li, Mingxuan Liu, Ruixuan Li, and Jia Yao.

Tickets or privacy? understand the ecosystem of

chinese ticket grabbing apps. In 33rd USENIX Secu-

5124, 2024.

| rity 24) | , pages 4535–4552, 2024. | [44] Vincent Haupert, Dominik Maier, Nicolas Schnei- |  |  |
| --- | --- | --- | --- | --- |
| [33] Alexander Druffel and Kris Heid. | Davinci: | An- | your app security: | The state of android app hard- |
| droid app analysis beyond frida via dynamic system | ening. In | International Conference on Detection of |  |  |
| call instrumentation. In | Applied Cryptography and | Intrusions and Malware, and Vulnerability Assess- |  |  |
| Network Security Workshops: ACNS 2020 Satellite | ment | , pages 69–91. Springer, 2018. |  |  |

SCI, SecMT, and SiMLA, Rome, Italy, October 19– [45] Kris Heid and Jens Heider. Haven’t we met before?-

| 22, 2020, Proceedings 18 | , pages 473–489. Springer, | detecting device fingerprinting activity on android |
| --- | --- | --- |
| 2020. | apps. In | Proceedings of the 2024 European Interdis- |

and XiaoFeng Wang. Things you may not know about [46] Muhammad Ibrahim, Abdullah Imran, and Antonio

| android (un)packers: | A systematic study based on | Bianchi. | Safetynot: | on the usage of the safetynet |
| --- | --- | --- | --- | --- |
| whole-system emulation. In | Network and Distributed | attestation api in android. In | Proceedings of the 19th |  |
| System Security Symposium | , 2018. | Annual International Conference on Mobile Systems, |  |  |
| https://ebpf.io | , 2025. Accessed: 2025-01-08. | [47] iJiami. | ijiami security solutions, 2025. | Accessed: |

develop, optimize, and scale mobile games. [48] John Wu. Magisk - a modern rooting solution

| https://www.unrealengine.com/en-US/ | for android. | https://github.com/topjohnwu/ |  |  |
| --- | --- | --- | --- | --- |
| uses/mobile-games | , 2025. | Accessed: 2025-01- | Magisk | , 2025. Accessed: 2025-01-08. |
| [38] Frida. Frida - dynamic instrumentation toolkit for de- | pages 5467–5484, 2023. |  |  |  |
| [39] Jason Geffner. ssl_logger: Decrypts and logs a pro- | boxes. In | Proceedings of the 29th Network and Dis- |  |  |
| cess’s ssl traffic. | https://github.com/google/ | tributed System Security Symposium (NDSS) | , 2022. |  |
| ber 29, 2022. Accessed: 2025-05-24. | [51] Mingyang Li, Weina Niu, Jiacheng Gong, Song Li, |  |  |  |
| [40] Google Developers. | Flutter - build apps for any | abling robust android apps unpacking via android |  |  |
| screen. | https://flutter.dev/ | , 2025. Accessed: | kernel. | IEEE Transactions on Information Forensics |
| [42] Jiawei Guo, Yu Nong, Zhiqiang Lin, and Haipeng | rity Symposium (USENIX Security 24) | , pages 5107– |  |  |

---

## Page 17

[53] Lockin Company. Liapp - mobile application secu- [66] Caijun Sun, Hua Zhang, Su-Juan Qin, Nengqiang

| rity and anti-tampering solution. | https://liapp. | He, Jiawei Qin, and Hongwei Pan. | Dexx: A dou- |
| --- | --- | --- | --- |
| lockincomp.com/ | , 2025. Accessed: 2025-01-08. | ble layer unpacking framework for android. | IEEE |

[54] LSPosed Team. Lsposed - a riru/enhanced xposed

[55] Manxi Inc. Manxi inc., 2025. Accessed: 2025-02-

09.

[56] Alessio Merlo, Antonio Ruggia, Luigi Sciolla, and

Luca Verderame. You shall not repackage! demys-

tifying anti-repackaging on android. Computers &

Security , 103:102181, 2021.

[57] Baiju Muthukadan. Selenium with python. https:

//selenium-python.readthedocs.io/ , 2025.

[59] OWASP Foundation. Mobile application secu-

cate validation: a hijacker’s guide to the android tls

[61] Siegfried Rasthofer, Steven Arzt, Marc Miltenberger,

Merlo, Davide Balzarotti, and Simone Aonzo. Un-

masking the veiled: A comprehensive analysis of

android evasive malware. In Proceedings of the 19th

ACM Asia Conference on Computer and Communi-

cations Security , pages 383–398, 2024.

[64] Onur Sahin, Ayse K. Coskun, and Manuel

Egele. Proteus: Detecting android emulators

from instruction-level profiles. In Michael Bai-

ley, Thorsten Holz, Manolis Stamatogiannakis, and

[65] T. Strazzere. Android hacker protection level 0, 2014.

DEF CON 22 Presentation.

17

Access , PP:1–1, 10 2018.

runtime analysis code in android apps. IEEE Trans-

actions on Software Engineering , 2025.

[68] Thomas Sutter, Timo Kehrer, Marc Rennhard, Bern-

hard Tellenbach, and Jacques Klein. Dynamic se-

curity analysis on android: A systematic literature

review. IEEE Access , 12:57261–57287, 2024.

[69] Tencent Cloud. Tencent cloud, 2025. Accessed:

2025-02-09.

gust 3,2025.

spection: A longitudinal study of the complexity of

2025-01-08.

A large-scale comparative study of chinese android

puting Machinery.

[74] Worawit Wang. Blutter - a linux kernel exploit frame-

work. https://github.com/worawit/blutter ,

2025. Accessed: 2025-01-08.

[75] Michelle Y Wong and David Lie. Tackling runtime-

based obfuscation in android with { TIRO } . In 27th

USENIX security symposium (USENIX security 18) ,

pages 1247–1262, 2018.

Software Engineering (ICSE) , pages 358–369, 2017.

| module | for | android. | https://github.com/ | [67] Dewen Suo, Lei Xue, Le Yu, Runze Tan, Weihao |
| --- | --- | --- | --- | --- |
| LSPosed/LSPosed | , 2025. Accessed: 2025-01-08. | Huang, and Guozi Sun. | Arap: | Demystifying anti |
| Selenium Python Bindings Documentation. | [70] Turner, Ash. Android vs. apple market share: Lead- |  |  |  |
| [58] normalplayer. | Np | manager. | http: | ing mobile operating systems (os), January 2025. |
| //normalplayer.top/ | , 2024. | BankMyCell; updated January4,2025; accessed Au- |  |  |

rity verification standard (masvs). https://mas. [71] Xabier Ugarte-Pedrero, Davide Balzarotti, Igor San-

| owasp.org/MASVS/ | , 2025. Accessed: 2025-08-03. | tos, and Pablo G Bringas. | Sok: | Deep packer in- |
| --- | --- | --- | --- | --- |
| [60] Sajjad Pourali, Xiufen Yu, Lianying Zhao, Moham- | run-time packers. In | 2015 IEEE Symposium on Se- |  |  |
| mad Mannan, and Amr Youssef. Racing for tls certifi- | curity and Privacy | , pages 659–673. IEEE, 2015. |  |  |

galaxy. In Proceedings of the 33rd USENIX Confer- [72] Unity Technologies. Unity mobile solutions - build,

ence on Security Symposium , SEC ’24, USA, 2024. operate, and grow mobile games and apps. https://

USENIX Association. unity.com/solutions/mobile , 2025. Accessed:

and Eric Bodden. Harvesting runtime values in [73] Haoyu Wang, Zhe Liu, Jingyue Liang, Narseo

| android applications that feature anti-analysis tech- | Vallina-Rodriguez, Yao Guo, Li Li, Juan Tapiador, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| niques. In | NDSS | , 2016. | Jingcun Cao, and Guoai Xu. | Beyond google play: |  |
| [62] Liz Rice. | Learning eBPF | . " O’Reilly Media, Inc.", | app markets. | In | Proceedings of the Internet Mea- |
| 2023. | surement Conference 2018 | , IMC ’18, page 293–307, |  |  |  |
| [63] Antonio Ruggia, Dario Nisi, Savino Dambra, Alessio | New York, NY, USA, 2018. Association for Com- |  |  |  |  |

Sotiris Ioannidis, editors, Research in Attacks, In- [76] Lei Xue, Xiapu Luo, Le Yu, Shuai Wang, and Ding-

trusions, and Defenses , pages 3–24, Cham, 2018. hao Wu. Adaptive unpacking of android apps. In

Springer International Publishing. 2017 IEEE/ACM 39th International Conference on

---

## Page 18

[77] Lei Xue, Yuxiao Yan, Luyi Yan, Muhui Jiang, Xi- [82] Rowland Yu. Android packers: facing the challenges,

| apu Luo, Dinghao Wu, and Yajin Zhou. Parema: an | building solutions. In | Proceedings of the 24th Virus |
| --- | --- | --- |
| unpacking framework for demystifying vm-based an- | Bulletin International Conference | , 2014. |

droid packers. In Proceedings of the 30th ACM SIG-

SOFT International Symposium on Software Testing [83] Simone Zerbini, Samuele Doria, Primal Wijesek-

| and Analysis | , pages 152–164, 2021. | era, Serge Egelman, and Eleonora Losiouk. | R+ |  |  |
| --- | --- | --- | --- | --- | --- |
| r: | Matrioska: | A | user-centric | defense | against |
| [78] Lei Xue, Hao Zhou, Xiapu Luo, Yajin Zhou, Yang | virtualization-based repackaging malware on an- |  |  |  |  |
| Shi, Guofei Gu, Fengwei Zhang, and Man Ho Au. | droid. | In | 2024 Annual Computer Security Appli- |  |  |
| Happer: | Unpacking android apps via a hardware- | cations Conference (ACSAC) | , pages 843–856. IEEE, |  |  |
| assisted approach. In | 2021 IEEE Symposium on Se- | 2024. |  |  |  |

curity and Privacy (SP) , pages 1641–1658, 2021.

[84] Y. Zhang, X. Luo, and H. Yin. Dexhunter: Toward

| [79] Shishuai Yang, Guangdong Bai, Ruoyan Lin, Jialong | extracting hidden code from packed android applica- |  |  |
| --- | --- | --- | --- |
| Guo, and Wenrui Diao. Beyond the horizon: Explor- | tions. In | Computer Security – ESORICS 2015: 20th |  |
| ing cross-market security discrepancies in parallel | European Symposium on Research in Computer Se- |  |  |
| android apps. In | 2024 IEEE 35th International Sym- | curity, Vienna, Austria, September 21-25, 2015, Pro- |  |
| posium on Software Reliability Engineering (ISSRE) | , | ceedings, Part II | , pages 293–311. Springer, 2015. |

pages 558–569, 2024.

[85] Tao Zheng, Qiyu Hou, Xingshu Chen, Hao Ren,

| [80] Wenbo Yang, Yuanyuan Zhang, Juanru Li, Junliang | Meng Li, Hongwei Li, and Changxiang Shen. Gu- |  |  |
| --- | --- | --- | --- |
| Shu, Bodong Li, Wenjun Hu, and Dawu Gu. Apps- | packer: | Generalized unpacking framework for an- |  |
| pear: Bytecode decrypting and dex reassembling for | droid malware. | IEEE Transactions on Information |  |
| packed android malware. In | Proceedings of the 18th | Forensics and Security | , 2025. |

International Symposium on Research in Attacks, In-

trusions, and Defenses - Volume 9404 , RAID 2015, [86] Hao Zhou, Shuohan Wu, Xiapu Luo, Ting Wang,

| page 359–381, Berlin, Heidelberg, 2015. Springer- | Yajin Zhou, Chao Zhang, and Haipeng Cai. Ncscope: |
| --- | --- |
| Verlag. | hardware-assisted analyzer for native code in android |

apps. In Proceedings of the 31st ACM SIGSOFT

[81] Youlor. Unpacker - a tool for extracting and analyz- International Symposium on Software Testing and

ing packed android applications. https://github. Analysis , pages 629–641, 2022.

com/youlor/unpacker , 2025. Accessed: 2025-

01-08.

18

---

## Page 19

12 Syscall-region Mapping 14 Packers Loading Native Library

Assisted analysis – showing candidate anti-analysis Packers load their libraries at app’s launch us-

syscalls that are originated from the same code region ing Java function calls to System.load() or

| (e.g. | /proc/self/wchan | ). | System.loadLibrary() | , | typically | within | the |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [region 94] 0x7a41c45000 - 0x7a41d235c0 (r-x) | onCreate() | method. | Runtime | library | load- |  |  |  |  |
| openat(*pathname=0x7a41d2d030(/proc/self/status)) | ing | is | handled | by | the | Android | loader, | located | at |

openat(*pathname=0x7a41d2d090(/proc/self/wchan))

/lib64/libart.so))

openat(*pathname=0x7fdc6f1a10(/system/lib64/liblog.so))

openat(*pathname=0x7a3d505080(/apex/com.android.run-

openat(*pathname=0x7fdc6f17b0(/apex/com.android.art

/lib64/libart.so))

openat(*pathname=0x7fdc6f17b0(/apex/com.android.art

/lib64/libart.so))

openat(*pathname=0x7fdc6f1ba0(/apex/com.android.art

openat(*pathname=0x7a41d2d030(/proc/self/status))

[region 95] 0x7d79b34000 - 0x7d79b35000 (---)

| 360 | 加 | 固 | (Basic) | 2638 (33.33%) |  |
| --- | --- | --- | --- | --- | --- |
| 360 | 付 | 费 | 版 | (Paid) | 18 (0.22%) |
| 梆梆 | 加 | 固 | (Basic) | 95 (1.2%) |  |

梆梆 加 固 (Bangcle)

| 爱 | 加 | 密 | (Basic) | 82 (1.03%) |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 爱 | 加 | 密 | 企 | 业 | 版 | (Enterprise) | 312 (3.94%) |  |  |  |  |  |  |  |
| 腾 | 讯 | 御 | 安 | 全 | (Basic) | 218 (2.75%) |  |  |  |  |  |  |  |  |
| 腾 | 讯 | 御 | 安 | 全 | (Tencent) | 腾 | 讯 | 御 | 安 | 全 | ( | 旧 | ) (Legacy) | 246 (3.10%) |
| 腾 | 讯 | 御 | 安 | 全 | 企 | 业 | 版 | (Enterprise) | 11 (3.10%) |  |  |  |  |  |

Table 9: NP-Manager packer tier identification (Chinese

apps).

19

initializations.

| Packer's main code | Packer's main code | Packer's main code |  |
| --- | --- | --- | --- |
| (1) mmap(+w) | (3) mprotect(+x) |  |  |
| region 1 (rw?) | stage-1-code-decrypted (r?x) | stage-1-code-decrypted (r?x) |  |
| region 2 (rw?) | stage-2-code-decrypted (r?x) |  |  |
| region 3 (rw?) | (5) mmap(+w) | stage-3-code-decrypted (r?x) |  |
| stage-1-code-encrypted | stage-1-code-encrypted | stage-1-code-encrypted |  |
| stage-2-code-encrypted | stage-2-code-encrypted | (6) write | stage-2-code-encrypted |
| ... | ... | ... |  |

(?): Whether the permission is enabled or not (rwx), (#):

Dynamic code loading step numbers.

| openat(*pathname=0x7a41d2a588(/proc/self/maps)) | /apex/com.android.runtime/bin/linker64 | . |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openat(*pathname=0x7fdc6f19e0(/apex/com.android.art | Packers | can | define | custom | library | constructors, |  |  |  |  |  |  |  |  |  |
| openat(*pathname=0x7fdc6f1a10(/apex/com.android.art | which | are | invoked | by | symbols | like | do_dlopen() |  |  |  |  |  |  |  |  |
| /lib64/libart.so)) | or | call_constructor() | in | linker64 | . | Additionally, |  |  |  |  |  |  |  |  |  |
| openat(*pathname=0x7a3d701090(/apex/com.android.art | while JNI functions typically initialize in | JNI_OnLoad | , |  |  |  |  |  |  |  |  |  |  |  |  |
| /lib64/libart.so)) | another function, | init_proc | , executes beforehand. | To |  |  |  |  |  |  |  |  |  |  |  |
| time/bin/linker64)) | hook into these functions, security researchers must first |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| openat(*pathname=0x7a41d2d0e4(/proc/self/maps)) | intercept the Android loader and exclude other library |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| /lib64/libart.so)) | 15 | Packer Code Release Stages |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | Distribution of Packers Across | (4) mmap(+w) | (8,9) mprotect(+x) |  |  |  |  |  |  |  |  |  |  |  |  |
| Tiers | ... | (2) write | ... | ... |  |  |  |  |  |  |  |  |  |  |  |
| Packer | Variant | #apps (%) | stage-3-code-encrypted | stage-3-code-encrypted | (7) write | stage-3-code-encrypted |  |  |  |  |  |  |  |  |  |
| 360 | 付 | 费 | 版 | (360 Security) | 360 | 加 | 固 | 企 | 业 | 版 | (Enterprise) | 44 (0.55%) | stage-N-code-encrypted | stage-N-code-encrypted | stage-N-code-encrypted |
| 梆梆 | 加 | 固 | 企 | 业 | 版 | (Enterprise) | 352 (4.4%) | Figure 5: Packer multi-stage code release overview. Shows |  |  |  |  |  |  |  |
| 爱 | 加 | 密 | (Ijiami) | how packers decrypt their code for next stages at runtime. |  |  |  |  |  |  |  |  |  |  |  |

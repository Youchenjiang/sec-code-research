---year: 2024

secverify_category: "Category B"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "22_Iannillo_et_al.,_Chizpurfle_Gray-Box_Android_Fuzzer"
creator: "TeX"
pages: 12
source: "Chizpurfle (2024) Gray-Box Android Fuzzer.pdf"
---

# Chizpurfle (2024) Gray-Box Android Fuzzer

> **文獻存檔**：[PDF 原文](<../../raw-papers/2024/Chizpurfle (2024) Gray-Box Android Fuzzer.pdf>) | [Markdown 原文](<../../raw-papers/2024/Chizpurfle (2024) Gray-Box Android Fuzzer (Raw).md>)

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

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABHCAYAAABF/NaGAAAE6UlEQVR4nO3dX0tqWRyH8W/HbfRHkIL04InoIqwu8sZAiEqCoODsvCn6I1hj5Xn/L2HYw7NgZ9OUpaRrvsJzMRfHPcFnLX97KWzJL7/8+uc1J+kHFSQlzk24Qs7c3KRAZxcpSpqXtCBpSdKypJJzE2oZZwu4K+awfxl6QB1AZxcsS1qVtCapIumncxOqgrNV3JVy0APyT+/WSQ51doGqpHVJm5K2JNUl7dCuc2MqmKrjbBN3VRwG5Mmou3iAnX0ELLJishW0wcX2JDUltSQdSDqUdOTcmDvEVwtve/jbwGMZn8VRgAfY2ayzIqnG6mlwobakU0nnkn5LSiVdUMe5LxYspfg6x1sbfw081vC5lAP+LuyEFZH9w1+Stlk5x5LO+B+4lHQt6VbSnaSuc2PuDl/XeOvg7xiP2/hcwWvyX8DnGNIX2PJrvMG+pBNW0hUX7kl6kPSXpL6kR+fGXB9fD3jr4i/F4z4+a3hdwO+/jic/uAstMdNssUJOWDU3XCS76JOkAf1xbkIFY0+46+Gwg8smTiu4nX9r9w679ipDe4OPgJQ3vGdFGbT7jp7xd4/HFJ8NvK7mdu9XI0kR/VXuSlvMOFesGMN2390Ahz1cnuG0jtsSjl+MJmEkKXOeuMfdaYdZp2/Ybkp6xmMXn228ruP31WjyIzeSbDLLnHKX2mPm+e4/yrnQEy4vcdrEbRhNXuAucF64xoDe4nzxmrtV79pumhrg8hqnLdyu4fjF3J3wI5UK88sBB+i3HMcYt5umBri8xekBbis4ToZxl/ixyg5ffaYcpPen4I9xbrg+PlO87uC39B7uI74C7XJ3+t1/iHPDPeLzAq8fwr1r3G4GGsa9OwrujnG7Ke4xdxxo3C6qjNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20fYl3H6ygpvmPvVkBT8Tx81Cn3omjp9m5mahkZ5m5udQullppOdQ+gnCbpYa6QnCfva7m6VGevZ79h/zksqS1iXtSWrnjgP73r3dlPSMx3AM2MbrOn7nh3HPSSoyjFeZX7Kt/kzSFavk0cDdNzfAYQ+XZzit47aE4zkNvQq50WRDUkPSMXejN5LueePnKfgj3f+vZ/zd4zHFZwOvYSQpDMPOjyYl7jq3mGVO2P5vWDF9Zp6Bd3I34YKxJ9z1cNjBZROnFdy+Gknyo0nYvbPZpSZpW9I+b5TyUdDlIg8cx/RZUc6Nsz6+HvDWxV+Kx3181vAadu1XI0l+987OCBclrUj6xRs0+Qg4Y9Vccgxzy0F617kxd4eva7x18HeMx218ruA1eWvXHgZe5LxwhZWxxWzT4u70lPPF36ykC+o498WCpRRf53hr46+Bxxo+l/D6LuwwngTgi2z5FYb2OscuTS50wFefR86NuUN8tfC2h78NPJbxGWC/OY68BTxhlilxN1rlPHGT1VPnO/0dfpXl3DgKpuo428RdFYclXCajwh4eUQrchQbkZS6wxgr66dyEquBsFXcB9TwuPzSKfGQXL/AREKAv8SOVknMTahlnAXQxh/pTu/VHoAfsiXMTrpAzN3bQfvk1k6+/AfUiQnpoLJnBAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABICAYAAAC0qmRTAAAE/klEQVR4nO3d0UsiaxzG8afMrE1qlZCMgqA1CvJmgi6ilS4OEqt24ULkAWtNPf//n3Do8H1hmq0tS8ne8wx8b2cIPvP6e2eCkXz48PHfsSBpkXK05NyMCsaCuYVZgQ6QlyWtSPoiaU1S0bkZtYazFdwtpbC/G/oCJ8tzgYcLbkgqS9qUVJG05dyMquCsjLsiDvO4fBPwsFo/3CkFTlriYjuS9iR9k3Qg6ZCOnJtSwdQBzvZwV8FhEZdLk67iadirktY56a6kmqRjSYmkU0lnks7pu3NTKpg6w1mCuxoOK7hcnRR4GvZXSVVJ+5LqXKgh6S9Jl5J+SGpL6tCVc+8sWGrj6xJvDfzV8VjFZxr4i6t2GvY2Pw0Jd1STC3clXUu6kdSjv52bUsHUDc66uGviMMHldgb4s6t32DwWWPKrnOBE0oWklqSfXLQv6U7SL0kDSffOTbkBvu7w1sNfC48n+KzitfCnTeYiu9AiM80+d8gFPxHXXOThokNJI0ljSf84N6PGOBviro/DNi4TnFZwm39uPMnxmKXE0F7nJ6DFCW+5o0Zz8Ee7/18j/N3isYXPOl5L+M09N2uHVbvG8N7kp6DPib1Su49sjMM+Lps4raVW799m70XeAG3wPPGY3WmHWWfgFdvNSSM89vDZwOsOfpezo8kiS3qZB+YJj1+63CXDOfijnAsNcdnFaYLbMo4f4c7xDn+TN0KnPF+8ZrfqVdvNUyNcXuP0FLebOM5lca8xtxzwZugHzxl/edZ2c9YYlzc4PcNtBcePcIfN5Bbv9M953BLm7Y/+Y5zLFubuNl4P8Rs2lX/EHTaT93PwhziX7T61qXw17iOeH3Z4FWrcbh67x2cHr0eT4L4ybjfHBdxXxu1iy7hdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLtXbj92RA3z73psyH+4JP7DL3pg0/+VJ/7DL36U33+yKr7TE30kVV/Htt9pib6PPYiH4Qv84H4hA/Gd/mA/HAO/iDnQkNcdnGa4LaM48Us7mVJG5J2JB1LaqQ2lQOv3m5OGqXm7Q5Oj3G7geNHuBdSm8qHuaXGUt+U9JO75N6zt/vgxjjs47KJ0xpuw2ZyQZkjx5JekrQrqc7zwxazzS0n9gruPqIR/m7x2MJnHa8l/OaysMNokk+t3vvMMhc8brnmjhkw84y8krsZN8bZEHd9HLZxmeA0rNr57EiSHk0e1BckrUuq8njlhBO1+CnocZE7HscMuKOcm2YDfN3hrYe/Fh5P8FnFawG/v40k2dl7VdJXSducIOEnoMkQ3+UOuuGiPV6FOjeNgqkbnHVx18RhgsttnK4+N2s/NZ6kgVdZ+usM7w0ev1zyAL3NhTv8E4tz7ylYauPrEm8N/NXxWM3AfnIceWr1TgNfZ6bZZVd6zJ1zypuhc/ru3JQKps5wluCuhsMKLtOwX1y1nwJeYFgvcdIdHph/46fhkI6cm1LB1AHO9nBXwWERlxPDziLPsQtd4aQbvAna5GJbzs2oCs7KuCviMP/S5nHSVTzHnbLMBb7wTypF52bUGs5WcLeEwzev1q+BHrAH8M7NolwK80xA+/DxKY9/Afs2hjGrCaNjAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAAA/CAYAAACW9Jg2AAAMEElEQVR4nO2ciW4jOw5FK7vtOPG+O3Z5TdKdnuX/f25ggAQOLqgq53VjPH4jAkIcR6USqSuKknhTFFmyZMmSJUuWLFmyZMmSJUuWLFmyZMmSJUuWLP+ncvONcmvl3Pq/25c/3f9z2v2u7n+lj3V2PKdPVy1qiDspt2eUU717Kw9W7qX494+Jon9nO1X9iAZTdbhLDHKqfqq/1KvOPmqTlM51+kVt1rUXtan9SdU7t1wc/DeimBvhCeUxAKIO7qleoyiKZlEULStN+64hf2sXRfFi5fT5Gc+07PdnfN9EPx6CyaGgY//93f7snQzmQ6Cv9lf7Qr1S9lG7eDuqe0v6F01gtvuI9lJ2bMjYRX1pnfHu1Lgr6C8G4FsxCg38aj+fMWBPgRH8mVP9TlEUXSsdtPGCv/WLohha6VvpovTwfc+ee0kASD1PQ/rjpW3PqIdvCgheoHsH/aE+r2KfdmCfJkDvuvcC3TvyfCOYMGr3tj2nbXk/Xd92Yoxo61eMb1Pqpsbdf3dncBHw3tjLfRBfzAADM8jYykCM4gNCsJ3qjKz+xH6OBKAj+9u8KIqlldPnKZ45fZ6hTO37IUDeAaBbUtrWnyH6MrHfO9b3BkDeRd0RwDCS570PA9hnlLAPQeKAdd2o+8za6GISvGCC9/E36te152aBHccJp8CJM5a6PdiUzqUfjHsb/WkYgG8vBd4HALcPA78VRbG2srABHGGGDzC4U6uztOfeAoOOYeyyKIpdURRba3+FQVjZd6WVtbW3sPYmaK8v3vUVOnhbG2tnac904TW1rvdDdfH3T6Gv28ifUftwQnDCrqH7ytoaAmQD2Mr17QNAr1Z/Lm2tpZ8++Sfo8wz9SI0RxzIa9z760zLHdxHw3trL3QNNTCkH13tRFEcYZwlFZwK4EkAp7btFDXg3AO8b3r21v/vApIA8xlLZszK29k7PHYqi+DA9tgBw30AyBQBOeu6hwxbvXgt45/aOnb1jF9hnCvBMA/BuAPoBPN4ENtJJ5+AdCHg3sOES76JdOTHfpD4nrNtunxj3CezeNu97dwnw3tnLX8wgCzPE3gb9qyiKn/b5YMo4eFbwzBzsLUC5gGcZYVa70UvxbgTE0coBQN4BTO61BrKUz60Pp2d/FEXxD9Pjw/rl3mRmbbiuP6Dn3n4e8E4Fb2mT4jOwDwExBXhV9zkmk4cvHIO91ZsaWLhizAI7LjGx1xiLDQC+QP+WssKWsEeklz87M3u/XBK89xYydAxcPpgc+F/2+Qc8WAnDlAnwrmRwfDmcYzl3g3DWH+w9H/Cae4CK750hRvVl+k0m379Mjx+mVwkPyHq/bMB80nzAG5cAvYN3Y3V+JuxTwrPS+1L3qcSnE3vuCP339m6GSD2ry7bmVmbo3wGTYGf1uJ9wD73BavduOlXptbB+vxp4LxI23Fvc0oXhFLxf9vkLADhgRq4lRt0IeEeyWZgAqHOJxVZY6n+INzwmwDtC0cE/AfLf0OMToQHf84W/HzF5CN65gLeUftI+DpYlQqax6D4LYuS5PfcJ8BwNdEOAt2vtqR3Zvy0movcp1R8HLidznV5D87xPlwDvDeLdnim/BXg/EDL45y8sJx+myEqW/rXEiSPEo/S+C9l8Ta2tIwbvp30+wHAbtD+TwZhh0HwQ/glwfiGO/8QA+bveMVG4ZK6C2H0tQFf7HAAWrgyuu59S8DRiBcfxE15vhU1dByEG2+IkniHmd/Du4Ex4orIQ8B5ljFN6DSzmfbzEUZlv1tpmvDnAy6Xbf6c38J/7YIe+BsBW2JDw+I0brgi86nkVuFy+5ihLDIAvf7/QZw8NdHLQw7vu7xLvccPCDdsusI+D7i0AL3UniHypf0d/P+33EuGXg30kbRG8OpYeuzP0Uc+7lf1GNO7Ua2CO7+FS4H3CEdkcCuwAGPekXGarwKuhwzSIS32ZG8l56pt4f4YK3KitcfLAY5+VxMcfAMAnPMgnwKEbQ303TwXG2Oy9oU+0zyeW2ZTnncn3BNERffTQpYQT4Jk57UgbzxHH+pj6aQtjY57+6N6lTq++hZz3/23gErxt7F5LiV1XWJr8eIubiW0FeEsB7wAXGVMsmwPxPtE5rx7r+MkEi3/HHTYn4QFgUM+6Fb33MmmiEGcBz6f2eccyzQ3ZELGpTmg/weHk9z69wV7aln7vR4C0UYkjL56EVB2pVek1s9DlYicN0RnvUsoUxuUs3QK4C1m2VwDcQjYlXPKi258xjpZmUqZy7KTHPGp8gvxNjo54nMfB9DPQjUxAXZr1hkrtswHgqGcfXrIfADHS3b3rADbsJuzYxe0b21qIg3FHkLLvpEavkW0cL7JZI3h5uzaW0g+uDKcAKzcxExhqgaWxJzdgHXynuQS9ROnDu9B76zUzr5NHossUdfwnvSlBqTeFXJp5rtxL2Ed155Uxr2I7kvPAmJZ68/o5smMb5UXaG4hu8yB0Uc9dp1fXQoaLXg3fS3IKDfMaJHYwwaQns505EUw60WSaliR8MIOLyShMTtHB6QTvG8AL6ZXxq9zCRYk2BAQ3UvRummikfWXy0ask1jDhRvMxmAgT5Wq0g+/r7NiWSaM2o61epP45ej1dOinnFul7DQCsKWmIjxUpdTRylGmlqYyPifTGx+B9+t5ogJg1pmCJ0jFbMplSKZsENVMOm5JpFfVTM97qdKxKPU3lPqfs+CDpnZqSqemYmjWW6p/qdX8pr6sAvqvJ19R82bqcXs2f1RzaKIk7Sh6veqe+jwNZlYNaVaLc5KboFCWQp/papbs+k0psr7LLuXaMdNPJon2p0+uiebwEsLIKvkPRSRnuuzSf77zndxgf32GEpCZzlY3qmB51dc9hi/yO/SJb/Wn6UxaIGr8OOCkPdg4FRilA59Bk6mhFVf1N0Xq8f/8THi7LX5MbDLDGeVWUnijePIcC8yTxcVPqpTyy0pC06CTwuk+ykX2WvmUAX7HcYkPJXXQdpUd36M9nUmCUKkPGRlM2d3U0JJ4UPAn4qZPSjZS25KDPckXix3kNnF/6sVgVpcfPZHtylFdFgXmVw3/mAAwSR2tVNCReQnTRV4Lc60bv6+BI6uI7+yzfF00emuGmqI7SswwuUaooMCO5UeJtHS80RnKWnaIh8fZqbGDUM1/ebJJu5Bccnux9scuALH9dPP/i1QZ5LUkmEaVnL6mMS8lBSFFg9O+85o5yAupoSGuUufWTocyLTYCl5HFwYraz571ecZpSzwDgmWLvFZSeT6TubZGfsJTrZM2NYEKQJvxoquca+cQpGtJOJtoQMXYbXrdE8pCyFFqIefOG7crEmR59A9E78krPofRoZlgVBWaDz+ptl8g2IyjnQXbYm+TR7oUJ0Q7SUJWx4fywJkKGDN4rEqflP9tgroLM/ojS88toP5/I0SXZMUWB0bxXJvAsADLm/s4lCZw0JNZ15gHBO5DkeQfvDCFGDhmuVG6wWRsaeN+FcxZRer5A6eFyPJPNllJgdmBrzIMUzIgTphNilqi3AHh9gzkSL+0ef4KsrRwyXKmQ6eHgJbeujtKzl0TzeQUFZocE9B12/XNs5LYIBUhojGhI76BRHZDby1zcKbw06UY8mcjgvVK5xfnuEF7qeAalZ4+NFXfxEQWGsa6Dlxu1hcTGWi+iIR3BPDgEjBJy1pRuNMqbtesXgrcPSsq2htJTyhHZUo7FIgrMShgipbBBFnICUSZOJVbiyX3DtoLnV6+vm8p80vA3EHLs/FhpcQalJ/rfW/MKCgyX/FKOw1ZB/DuV8+CIhrRCH0mXIt2GlCrSjRy8zQze6xW/XWvB+yqdJaL0DOXioC+0oYi9O5TJwRs4Ehx7QotJ0ZD0H/Exho7+zhvBQQbv9cstMrSUplRF6SE9h2yLKgqM02T6Qv8Z4Ar6OUjwSdGQmEsxEv5bxC0bg24U5TRk8F6ZKE0p+o/lEaUnouY0aygwDckoI7WoFWSPRfUj7pe2R0oRJ41OvEbOJrt+qaMpVTEevkOBuZecX/3v30qNuZf2lIYU0ZRSpRlMvofsdf8e8icpRFUUmHMYEMWZbVbRiur4efreLFmyZMmSJUuWLFmyZMmSJUuWLFmyZMmSJUuWLFmyZMmSJUuWLFmyZMmSJUuWLNch/wHLmzOhjNbJnQAAAABJRU5ErkJggg==)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABHCAYAAABF/NaGAAAE6UlEQVR4nO3dX0tqWRyH8W/HbfRHkIL04InoIqwu8sZAiEqCoODsvCn6I1hj5Xn/L2HYw7NgZ9OUpaRrvsJzMRfHPcFnLX97KWzJL7/8+uc1J+kHFSQlzk24Qs7c3KRAZxcpSpqXtCBpSdKypJJzE2oZZwu4K+awfxl6QB1AZxcsS1qVtCapIumncxOqgrNV3JVy0APyT+/WSQ51doGqpHVJm5K2JNUl7dCuc2MqmKrjbBN3VRwG5Mmou3iAnX0ELLJishW0wcX2JDUltSQdSDqUdOTcmDvEVwtve/jbwGMZn8VRgAfY2ayzIqnG6mlwobakU0nnkn5LSiVdUMe5LxYspfg6x1sbfw081vC5lAP+LuyEFZH9w1+Stlk5x5LO+B+4lHQt6VbSnaSuc2PuDl/XeOvg7xiP2/hcwWvyX8DnGNIX2PJrvMG+pBNW0hUX7kl6kPSXpL6kR+fGXB9fD3jr4i/F4z4+a3hdwO+/jic/uAstMdNssUJOWDU3XCS76JOkAf1xbkIFY0+46+Gwg8smTiu4nX9r9w679ipDe4OPgJQ3vGdFGbT7jp7xd4/HFJ8NvK7mdu9XI0kR/VXuSlvMOFesGMN2390Ahz1cnuG0jtsSjl+MJmEkKXOeuMfdaYdZp2/Ybkp6xmMXn228ruP31WjyIzeSbDLLnHKX2mPm+e4/yrnQEy4vcdrEbRhNXuAucF64xoDe4nzxmrtV79pumhrg8hqnLdyu4fjF3J3wI5UK88sBB+i3HMcYt5umBri8xekBbis4ToZxl/ixyg5ffaYcpPen4I9xbrg+PlO87uC39B7uI74C7XJ3+t1/iHPDPeLzAq8fwr1r3G4GGsa9OwrujnG7Ke4xdxxo3C6qjNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20fYl3H6ygpvmPvVkBT8Tx81Cn3omjp9m5mahkZ5m5udQullppOdQ+gnCbpYa6QnCfva7m6VGevZ79h/zksqS1iXtSWrnjgP73r3dlPSMx3AM2MbrOn7nh3HPSSoyjFeZX7Kt/kzSFavk0cDdNzfAYQ+XZzit47aE4zkNvQq50WRDUkPSMXejN5LueePnKfgj3f+vZ/zd4zHFZwOvYSQpDMPOjyYl7jq3mGVO2P5vWDF9Zp6Bd3I34YKxJ9z1cNjBZROnFdy+Gknyo0nYvbPZpSZpW9I+b5TyUdDlIg8cx/RZUc6Nsz6+HvDWxV+Kx3181vAadu1XI0l+987OCBclrUj6xRs0+Qg4Y9Vccgxzy0F617kxd4eva7x18HeMx218ruA1eWvXHgZe5LxwhZWxxWzT4u70lPPF36ykC+o498WCpRRf53hr46+Bxxo+l/D6LuwwngTgi2z5FYb2OscuTS50wFefR86NuUN8tfC2h78NPJbxGWC/OY68BTxhlilxN1rlPHGT1VPnO/0dfpXl3DgKpuo428RdFYclXCajwh4eUQrchQbkZS6wxgr66dyEquBsFXcB9TwuPzSKfGQXL/AREKAv8SOVknMTahlnAXQxh/pTu/VHoAfsiXMTrpAzN3bQfvk1k6+/AfUiQnpoLJnBAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABHCAYAAABF/NaGAAAE6UlEQVR4nO3dX0tqWRyH8W/HbfRHkIL04InoIqwu8sZAiEqCoODsvCn6I1hj5Xn/L2HYw7NgZ9OUpaRrvsJzMRfHPcFnLX97KWzJL7/8+uc1J+kHFSQlzk24Qs7c3KRAZxcpSpqXtCBpSdKypJJzE2oZZwu4K+awfxl6QB1AZxcsS1qVtCapIumncxOqgrNV3JVy0APyT+/WSQ51doGqpHVJm5K2JNUl7dCuc2MqmKrjbBN3VRwG5Mmou3iAnX0ELLJishW0wcX2JDUltSQdSDqUdOTcmDvEVwtve/jbwGMZn8VRgAfY2ayzIqnG6mlwobakU0nnkn5LSiVdUMe5LxYspfg6x1sbfw081vC5lAP+LuyEFZH9w1+Stlk5x5LO+B+4lHQt6VbSnaSuc2PuDl/XeOvg7xiP2/hcwWvyX8DnGNIX2PJrvMG+pBNW0hUX7kl6kPSXpL6kR+fGXB9fD3jr4i/F4z4+a3hdwO+/jic/uAstMdNssUJOWDU3XCS76JOkAf1xbkIFY0+46+Gwg8smTiu4nX9r9w679ipDe4OPgJQ3vGdFGbT7jp7xd4/HFJ8NvK7mdu9XI0kR/VXuSlvMOFesGMN2390Ahz1cnuG0jtsSjl+MJmEkKXOeuMfdaYdZp2/Ybkp6xmMXn228ruP31WjyIzeSbDLLnHKX2mPm+e4/yrnQEy4vcdrEbRhNXuAucF64xoDe4nzxmrtV79pumhrg8hqnLdyu4fjF3J3wI5UK88sBB+i3HMcYt5umBri8xekBbis4ToZxl/ixyg5ffaYcpPen4I9xbrg+PlO87uC39B7uI74C7XJ3+t1/iHPDPeLzAq8fwr1r3G4GGsa9OwrujnG7Ke4xdxxo3C6qjNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20fYl3H6ygpvmPvVkBT8Tx81Cn3omjp9m5mahkZ5m5udQullppOdQ+gnCbpYa6QnCfva7m6VGevZ79h/zksqS1iXtSWrnjgP73r3dlPSMx3AM2MbrOn7nh3HPSSoyjFeZX7Kt/kzSFavk0cDdNzfAYQ+XZzit47aE4zkNvQq50WRDUkPSMXejN5LueePnKfgj3f+vZ/zd4zHFZwOvYSQpDMPOjyYl7jq3mGVO2P5vWDF9Zp6Bd3I34YKxJ9z1cNjBZROnFdy+Gknyo0nYvbPZpSZpW9I+b5TyUdDlIg8cx/RZUc6Nsz6+HvDWxV+Kx3181vAadu1XI0l+987OCBclrUj6xRs0+Qg4Y9Vccgxzy0F617kxd4eva7x18HeMx218ruA1eWvXHgZe5LxwhZWxxWzT4u70lPPF36ykC+o498WCpRRf53hr46+Bxxo+l/D6LuwwngTgi2z5FYb2OscuTS50wFefR86NuUN8tfC2h78NPJbxGWC/OY68BTxhlilxN1rlPHGT1VPnO/0dfpXl3DgKpuo428RdFYclXCajwh4eUQrchQbkZS6wxgr66dyEquBsFXcB9TwuPzSKfGQXL/AREKAv8SOVknMTahlnAXQxh/pTu/VHoAfsiXMTrpAzN3bQfvk1k6+/AfUiQnpoLJnBAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABHCAYAAABF/NaGAAAE6UlEQVR4nO3dX0tqWRyH8W/HbfRHkIL04InoIqwu8sZAiEqCoODsvCn6I1hj5Xn/L2HYw7NgZ9OUpaRrvsJzMRfHPcFnLX97KWzJL7/8+uc1J+kHFSQlzk24Qs7c3KRAZxcpSpqXtCBpSdKypJJzE2oZZwu4K+awfxl6QB1AZxcsS1qVtCapIumncxOqgrNV3JVy0APyT+/WSQ51doGqpHVJm5K2JNUl7dCuc2MqmKrjbBN3VRwG5Mmou3iAnX0ELLJishW0wcX2JDUltSQdSDqUdOTcmDvEVwtve/jbwGMZn8VRgAfY2ayzIqnG6mlwobakU0nnkn5LSiVdUMe5LxYspfg6x1sbfw081vC5lAP+LuyEFZH9w1+Stlk5x5LO+B+4lHQt6VbSnaSuc2PuDl/XeOvg7xiP2/hcwWvyX8DnGNIX2PJrvMG+pBNW0hUX7kl6kPSXpL6kR+fGXB9fD3jr4i/F4z4+a3hdwO+/jic/uAstMdNssUJOWDU3XCS76JOkAf1xbkIFY0+46+Gwg8smTiu4nX9r9w679ipDe4OPgJQ3vGdFGbT7jp7xd4/HFJ8NvK7mdu9XI0kR/VXuSlvMOFesGMN2390Ahz1cnuG0jtsSjl+MJmEkKXOeuMfdaYdZp2/Ybkp6xmMXn228ruP31WjyIzeSbDLLnHKX2mPm+e4/yrnQEy4vcdrEbRhNXuAucF64xoDe4nzxmrtV79pumhrg8hqnLdyu4fjF3J3wI5UK88sBB+i3HMcYt5umBri8xekBbis4ToZxl/ixyg5ffaYcpPen4I9xbrg+PlO87uC39B7uI74C7XJ3+t1/iHPDPeLzAq8fwr1r3G4GGsa9OwrujnG7Ke4xdxxo3C6qjNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20fYl3H6ygpvmPvVkBT8Tx81Cn3omjp9m5mahkZ5m5udQullppOdQ+gnCbpYa6QnCfva7m6VGevZ79h/zksqS1iXtSWrnjgP73r3dlPSMx3AM2MbrOn7nh3HPSSoyjFeZX7Kt/kzSFavk0cDdNzfAYQ+XZzit47aE4zkNvQq50WRDUkPSMXejN5LueePnKfgj3f+vZ/zd4zHFZwOvYSQpDMPOjyYl7jq3mGVO2P5vWDF9Zp6Bd3I34YKxJ9z1cNjBZROnFdy+Gknyo0nYvbPZpSZpW9I+b5TyUdDlIg8cx/RZUc6Nsz6+HvDWxV+Kx3181vAadu1XI0l+987OCBclrUj6xRs0+Qg4Y9Vccgxzy0F617kxd4eva7x18HeMx218ruA1eWvXHgZe5LxwhZWxxWzT4u70lPPF36ykC+o498WCpRRf53hr46+Bxxo+l/D6LuwwngTgi2z5FYb2OscuTS50wFefR86NuUN8tfC2h78NPJbxGWC/OY68BTxhlilxN1rlPHGT1VPnO/0dfpXl3DgKpuo428RdFYclXCajwh4eUQrchQbkZS6wxgr66dyEquBsFXcB9TwuPzSKfGQXL/AREKAv8SOVknMTahlnAXQxh/pTu/VHoAfsiXMTrpAzN3bQfvk1k6+/AfUiQnpoLJnBAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAABHCAYAAABF/NaGAAAE6UlEQVR4nO3dX0tqWRyH8W/HbfRHkIL04InoIqwu8sZAiEqCoODsvCn6I1hj5Xn/L2HYw7NgZ9OUpaRrvsJzMRfHPcFnLX97KWzJL7/8+uc1J+kHFSQlzk24Qs7c3KRAZxcpSpqXtCBpSdKypJJzE2oZZwu4K+awfxl6QB1AZxcsS1qVtCapIumncxOqgrNV3JVy0APyT+/WSQ51doGqpHVJm5K2JNUl7dCuc2MqmKrjbBN3VRwG5Mmou3iAnX0ELLJishW0wcX2JDUltSQdSDqUdOTcmDvEVwtve/jbwGMZn8VRgAfY2ayzIqnG6mlwobakU0nnkn5LSiVdUMe5LxYspfg6x1sbfw081vC5lAP+LuyEFZH9w1+Stlk5x5LO+B+4lHQt6VbSnaSuc2PuDl/XeOvg7xiP2/hcwWvyX8DnGNIX2PJrvMG+pBNW0hUX7kl6kPSXpL6kR+fGXB9fD3jr4i/F4z4+a3hdwO+/jic/uAstMdNssUJOWDU3XCS76JOkAf1xbkIFY0+46+Gwg8smTiu4nX9r9w679ipDe4OPgJQ3vGdFGbT7jp7xd4/HFJ8NvK7mdu9XI0kR/VXuSlvMOFesGMN2390Ahz1cnuG0jtsSjl+MJmEkKXOeuMfdaYdZp2/Ybkp6xmMXn228ruP31WjyIzeSbDLLnHKX2mPm+e4/yrnQEy4vcdrEbRhNXuAucF64xoDe4nzxmrtV79pumhrg8hqnLdyu4fjF3J3wI5UK88sBB+i3HMcYt5umBri8xekBbis4ToZxl/ixyg5ffaYcpPen4I9xbrg+PlO87uC39B7uI74C7XJ3+t1/iHPDPeLzAq8fwr1r3G4GGsa9OwrujnG7Ke4xdxxo3C6qjNtFm3G7aDNuF23G7aLNuF20GbeLNuN20WbcLtqM20WbcbtoM24Xbcbtos24XbQZt4s243bRZtwu2ozbRZtxu2gzbhdtxu2izbhdtBm3izbjdtFm3C7ajNtFm3G7aDNuF23G7aLNuF20GbeLNuN20fYl3H6ygpvmPvVkBT8Tx81Cn3omjp9m5mahkZ5m5udQullppOdQ+gnCbpYa6QnCfva7m6VGevZ79h/zksqS1iXtSWrnjgP73r3dlPSMx3AM2MbrOn7nh3HPSSoyjFeZX7Kt/kzSFavk0cDdNzfAYQ+XZzit47aE4zkNvQq50WRDUkPSMXejN5LueePnKfgj3f+vZ/zd4zHFZwOvYSQpDMPOjyYl7jq3mGVO2P5vWDF9Zp6Bd3I34YKxJ9z1cNjBZROnFdy+Gknyo0nYvbPZpSZpW9I+b5TyUdDlIg8cx/RZUc6Nsz6+HvDWxV+Kx3181vAadu1XI0l+987OCBclrUj6xRs0+Qg4Y9Vccgxzy0F617kxd4eva7x18HeMx218ruA1eWvXHgZe5LxwhZWxxWzT4u70lPPF36ykC+o498WCpRRf53hr46+Bxxo+l/D6LuwwngTgi2z5FYb2OscuTS50wFefR86NuUN8tfC2h78NPJbxGWC/OY68BTxhlilxN1rlPHGT1VPnO/0dfpXl3DgKpuo428RdFYclXCajwh4eUQrchQbkZS6wxgr66dyEquBsFXcB9TwuPzSKfGQXL/AREKAv8SOVknMTahlnAXQxh/pTu/VHoAfsiXMTrpAzN3bQfvk1k6+/AfUiQnpoLJnBAAAAAElFTkSuQmCC)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGIAAAArCAYAAACD8l2qAAAE00lEQVR4nO2Z124jMQxF6bjFvdvT3J26//9/CwMkcPZi4k0eYr+IABFHohovSXEos0SJEiVKlChRokSJEiV6HDW+yU/O35Vv/GCt3zjHT8/5EArFNs2sZWZt55ZwtHeEKduskWffE1jXa4tcA/tryNivDEHn/c7aPEvIP90TEG78uqGumfXMrO98/f0Mjr6hmY2chyLbFdngZ4DWrllvgHm63t+sUZyCT5no1/V17U7N2gORvSsYccCOb+qq1ImZTZ2vv8dQevTNzWzpPPe2sY8fiuwU/QNfh4CG3Mx54u09sdBQMEHrQiaA7cv6E6zdv7E2zxBrB8i/Sg2A0PdNLMxsbWYb/7uCsuf+/7WvMLPKOfc2yi0hm/lcSyh6DEDXLpNDdu4yfXhj7HEO8IfitQOfP/YaZ1hA0WPIxFnjvAvvGziorXsB0fKDjF1RoeCt/y2gnLUr69p+MLOzmZ3MbCeAZD6uvDHXSubb+Zx7l899PxN42dTH5T7XBoCFF4YM9xCyAcgC88T+ti67dmMZObDtewDx5N4w8MVzKOTgv8sfAFF4fwlv2Xr/Fm0lAI/1Tpjv4PIZLHnmyisdrJAJ75nBCzLx2DCADTyg8LWPMIAAIjztbh4RQAz9wAWUcsTmMoSaDMo4AzAqmBZWCSh78HWNi/OLmb363wCjREhbYX8x5ugyG/EwemMJIHL0b32dC85R+loREuOO+PXL+n9A7LwtrC7uD1qTglBKqOLhKx8T1n9Vwpvzu/MblFzh3oi9vUL2BcZCAGIvBUDIZB8HgH/x/ws/48jDdfteWROBmCM0HQWIFVx/6RZYoT8XhW0B4BrhoIIVvrjSP83sw/nTFXzB+iXAvbjcH5d9Q2jciicW2FsmIXPn414FiNzPeNewxIwp7ohQ1l7i5gqpJb2iRNxdSzaVI+NaIr4TiHco9Y/zhwARIS284RNjCNpB9lwIBwB7hDeGwp3vf3rvsBQZU9ctYObKrBC/D9hgZBtLlytrrH4tHrGRC7JCWAogPuENqtw9FHeCBwVg767MM8LpAYkBEwWG3BM8MoCIi3/yiPuh5SnayF1yg/jJ8JTBspdQuLYv3RPqwkMuc5/EKl/x+wzrDvmz938AhDcAcRQgdjWJwQnMsBT30epRF3VbviEyUdZBgGAOnknqOBMwqxvp6lbS5D1+s02VeRCFH5FhUa5ufh0XmRcztIdlTF8BsYMi4o5QhUfbBOWPMbxCP+ZyudTzmsuUWY2yylGWGVslZ4hz7MQIjmJsBYDoPeKOeJY7IkemkuNLcyzlgVlN/SbKC/yoKjBPeNUc6TABnkmJheWRBYxghvErCZkb+aArASLn5Bd1hY/HhwDRhFdEeWAhxbyJKJvVyh6Kbh0U3MZQqhYFRyhZDDF3zKlFxynKHH3hoRQkx/gKXwD4GeaZ4Jwr8PyLGtPdK69RMBuJwqhsLSF3UIZmibqHub4qk3cFxE5NaZqleFZhWY3touzOyuwIXGdIQ/HykHu+Z9U1SB9ROnKoDt4E9F1A2/Rdg3N1RZEErimsj0R1bw76PqEPV3Vr65x8M6GBtB/xKKSA3FLyd58U6+a69Zp26wm2bhzXuTWu7hz/A1LPnChRokSJEiVKlChRokSJEiVKlChRokSJEiX6l/4CMItlCBpiAe8AAAAASUVORK5CYII=)

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

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAABHCAYAAAAX8ymIAAADaUlEQVR4nO2dbWviQBSFT30prRVcC11qpRSs2qolpWrF+tb9/79qiXtmuZsqYpqwV3ICz5daM3iezJ1RyA2g4+SOMwAlUgZQEX8pm2zO8go+HqQK4BzABYAagCsAdbHNocZczplTOSshIfwQfDxgA8A1gBsAPwHcim0ON8ylwZyCkCAj9dVfMeE3OVgbwAOADoAugB6AfoHpMYcOc2kzp6aRUTl2VgQB8ZS6pNn4pPccbAAgAvAGYAJgCuC9wEyZwxtzGTCne+bWYI7VY0QEAXGN+wGgRctDDjQD8AFgCWAFYC22OSyZy4w5DZlbiznWjIiDAio0F7/xjlYjWo8H2gD4TLApMLuyWDKviPndMc9LU5r2lqEya1iDBuMTvAKY07gdKNhf8AooKgtTFayUNXN7ZY4t5nrBnHeWpRJX8zprWYcm5zz5LxP+nNMu1MNxgQnr4oy5rBJ5zZljh7nWmfPO2RBmQZOLypBTam1OuODfwiL0AmDE/y0qI+YQNivvzCmIWPNvQ+baNLPhSymqmlnQ5QmXpvwsaDziCZ8SW7SiErboT8wlYk4LU56WzLNrZkM1WZJCKWpwnzvg9AonWZmF5pkDP3KKiT88Mpdns5FZmYt4xlzbzPlLSSpxilzzC0fERefT1LWw7ZKAwyLCdn5uLuQP5vrAnC+SEsrcx97wZLYUrWgx4pSTgMMinpjXzMyGUJI6zLmWXBcq/BEqrAeTxJunXHz6Dj7kKdBnXtPExTwx68IVc/9HQp0/RvX45vC9YME3j/ja//6Ap0CPeU2YX/jeMOVrt8x7r4S+2ZpuWMvGrHNdBx/wFOgyrzHz25ital8SJKEwSIIDJMEBkuAASXCAJDhAEhwgCQ6QBAdIggMkwQGS4ABJcIAkOEASHCAJDpAEB0iCAyTBAZLgAElwgCQ4QBIcIAkOkAQHSIIDJMEBkuAASXCAJDhAEhwgCQ6QBAdIggMkwQHflqC7N79P6rs3dR9zdqS6j1l39GdH6jv61dsiOwGpe1uoy0t2AlJ3eVG/o/Rk1u8Iezp/zdT56yCZdf6CeuClJtMeeOoGmY5Mu0FCfVFTkWlfVCtCHYKPI9MOwVCv7KPJpVc21DX+KHLpGp8sTXp+wmFyeX7CrlmhJ4nsJ9cniewTomfqfCXXZ+royPn4DXLChQVUL+XkAAAAAElFTkSuQmCC)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAACVCAYAAADYFu1jAAAGMElEQVR4nO3YXUsbWxSH8cfEGtTiWxAPUr2oIhq8EAlFxN4ELYhaK4o1RY7x7Xz/j3AIPFOm0Vo9etp0dQX+t5lZv71m7T0D+evr34CpmCowGDTVUp1F3T8FuOINDAE1YBgYAUaB18Eyam3D1jpk7ZX/C7wAfuUFuxcfAyaBOjANzAB/BcuMtdWtdczaa1q8GHi5g2uu8IQXnwXmgbfAIrAELJuV3zxFHUvW9tZaZ619QovaS3R4uYu7j864F3kDLAANYA1oAhvAJrAFvA+SLWvasMY1a17QYFqT4ed094CbwJArN+Vqdi+y6oW7N9ICPgC7wB6wDxyYj79pivvft6Zda2xZc1ODBU2mNBrS7NHYRScXyN35NOejtO7FdryRI+AEOAXOgDbwJUja1nRqjUfWvKPBuiZzGhXYj+7sYlwUyPM+Mu9c1e4qH3sT58DfQAe4NFdBUtTTscZzaz7WoKVJQ6MCuxgjP+zmQefOlKvVcE5tA4fAZy/a8YZugFvgn6C5tcYraz7X4FCTDY3mNBvW8MGurriTjjt/ll217h9+8nG6+EOAHwK/0OKTNu+0mtWu9lBXD5RGxrTDft1H5NA/7q7o9R8GfB/4tRZtbVpaLWhXjJB7u7ro5gmPL6sO/T0flYtEvoN9oc2eVqvaTXyvq4vZPFLq5qY77LFz6SqR72BfaXOsVbPU1SP3zeoBjyZjzpmGK7TvTttxPv3q4votN9qcabWl3ayWQ73QxdiY9Kiy5tw5ym5+MOWuPtJsTcPJ+8ZHxWNJ3ff6pm9DJ54hs5u/nxuNTjRraljX9Bvoamk+L3o23PWtqJPd/GBuNTrVbEPDYk5Xy9CDHklm/GK16U565tvRry6m33Op1Z52S1qOavsN9Gu/wS6XNsJ2Qj8aul3aEJe1fP0j6Pd+wfrisP/VhfR7rrQ60O5R0CsJ/WzoladAf0zoJ0N/TOiEDpGETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYSeiEjpWETuhYeRb0QUI/GfrgKdDLCf1s6OXHQm8B+0AbuOyDQvo9l1rta/cg9CgwAywBm8AecJbQj4Y+02xTwxlNv4GuAiPANLAIbAC7wCnQAW77oJh+za1Gp5ptaDitabUMXQGGgTrwFmgCH4AT4G/gpg8K6tfcaHSiWVPDuqaVXugaMAnMA2tACzgCzh322dV3c6vNuVYt7ea1rPVCDwBDwBgwCzRKG+KZj0Z29d3caHNW2ggbGo5pOtALPVia0ws+AjvAcXb1vSl387FWTe2K+TzYC10eHxPAG2DVFerupJ+BC+A6sb8iX2vyWaMtzd5oeGdslLv6lUeSoqvXnTuHnhM7if0VuaPJoUbrpW4e1fJON/d29bhzpnvwfgdsA5/84wsfmZs/DPzWmq80aGuyrdGyZuMPdXPvrO4eS6aAOYf7hn946KNy7or+CeBl4I61f9ZiW5uGVlPa3Tub7+vqYoTUPao0XLWW8+jYnfbcM2THt6NLbyhCino61nhuzccatDRpaFQvjYwHu7nc1RWPJgX2nI/GukN/x+PMkQf1U2+i7ceVCGlb06k1HlnzjgbrmsyVkIe0+2E3l7GrJewp58+CO2vTi7V8G9p1lff9gnXgt9nfMcX971vTrjW2rLmpwYImUyXk6lOQezv7lXNn3B31jRdp+BbUdE5teiPvg2TLmjascc2aFzSY1mS4NC6ejNyLPehOOuoZcdrVnPe9ftEvVstm5TdPUceStb211llrn9Cips2zkL/X3TXfesZ8n6978Rm/wUbKjLXVrXXM2msv0cWPAR90JtV8dEZc4dfBMmptw9Y69NId/BjwAr3iJjAYNNVSnQM/Czh///H3LyiXCPQXNk80AAAAAElFTkSuQmCC)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

![Page 4 Image](data:image/png;base64,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)

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

![Page 5 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHYAAABACAYAAADPhIOhAAADMElEQVR4nO2dW0sbURRGVy5eaIKKkLQPCopVFAKCDwa8PSlUND5ICUYUjZr+/59QAl9gTElr7IyZbL+B9RbOkL3O2efMwOwNvj79VQCKogSUzYdQSsS9kLbMgchZYB74AlSAqsmUimI9r9gnRb9bckGDzGjg/o0WgWWgBtSBbyZT6or1smJflYsZuRlbblGzY06zZkk3WQHWgO/AFrAtdkyqDOK6pVivKfZ1uajITVmuxpLanxkLmjGrwCbQAPaAJnAAHAHHJhOOFOOmYt6Qg1U5WZCjN8ktDEn9Cqxr0H3gBDgFfgAXwCXQAq5MqrQU2wvF+lSx35eLdblJyh2Zlgd76lxC6gawCxwCZ7rhNdAGboAOcGsyoaMYtxXzlhwcyslGQu7c3/bcojblipb6ugbop4VzDd6/2T3wADwCXeDJZEJXMX5QzDtycC4nu3JUk7OZUSm5pGW9pDze0OzoD/QTuNONnoEXoAf8MpnSU6yfFfs7uTiXm4ZcLcldadTeWtXJa1P5/Eyz5E6zyEInK/hJLq7lZl+u6nL3x15b1APwoo7VDW3WLaWARw086T/42XmRi47cnMjVitzNDqfjopbysp6Z9nQSu1Z+f/ZKzQU9ubiXm1O5WpO7+WGxJb26qumBuKljdlubt1drfniRk7YcNeWsJoev9tmyTlZ1ve040DPUjZa+V2t+6MnJjRwdyFldDsvDYqt6P7mttx6XyuXdHPwZ85qu3FzK1bbcVf8l9lib861OYpP+I+Y1T3LTkqs3id3Rj68sNrcMxF7J1Y7FxsBig2KxQbHYoFhsUCw2KBYbFIsNisUGxWKDYrFBsdigWGxQLDYoFhsUiw2KxQbFYoNisUGx2KBYbFAsNigWGxSLDYrFBsVig2KxQbHYoFhsUN4l1p9R5p93fUbpD5/zz1gfPrtUwXQwVqkCFxeZHsYqLuJyQNPB2OWAXMBrOhi7gJdL7uWbd5fcw0Uyc8l/F8nEZW1zR2plbV2IOl+kVogal47PDamWjk+mZDd7mDypNnsYluv2LJMhk/YsybTshkqTJfWGSkm5boE2OTJpgTZKspsWfiyZNC30NaXXbye18XlbugWlAAAAAElFTkSuQmCC)

![Page 5 Image](data:image/png;base64,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)

![Page 5 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHYAAABBCAYAAAAE2FAEAAADS0lEQVR4nO2dwUojQRRFjyYmMnFEJDSCswgzEjSCCxEXoitdBEkEHYQ4Cppo5v8/YQjcghjUMbHb7pS34SxTTb9T9arTUO+Bry9/LQCLoiTKJlNCnEPcF9KWGSRWgGXgG1ADVkym1BTrZcW+PCZ6ZslB6pIGHt1kFVgH6kACbJhMSRTrdcW+JhdLs8oNq7SiwdZ0k02gAfwCmsC22DGpEuLaVKwbin0iFzW5Cav33VJHS74KfNeM+QFsAbvAPnAIHAHH4sSkSojrkWK9r9hvyUVdbqpy9V+5C5oFVS39RLNlNOiBbnoKtIFzoAN0xYVJhRDPjmLcVsxP5KAlJ4kcVeXs1bQc9tSKZsPohz+BPc2cM93sCrgGesCN+GNSJcS1p1hfKfZncrEnN4lcVd7ac8OLUk1LvaEBjjVrLnWjO+AeeAD6wMBkQl8xvlfMe3LQlpM9OarL2dJrKbmkN6415fFdzY7RQL+BW93oEXgChsBfkylDxfpRsb+Vi7bctORqTe5KL6Xhsswn2qQPtPQvNWDfQnMX3JeLS7k5kKtE7sqT6Tjsrat6rd7VZt1RCnjQwHk/4FfnSS56cnMiV5tyV5lMx4tayuvK2/t6E7tSfn/0Si0EQ7m4k5tTuWrI3fKk2JI+XdX1h/hQefxam7dXa3F4kpNrOTqUs7oclibFhv21qY35fCwNe7UWh+FYOj6Xq+bYPvtMbFkfnTf0KetYOfxGG3beD2Oe05ebjlxty92KXL4ptqsfDwrwIOY5A7npTiN2R29bXX0FsdjiMZCbrlztTCP2wmILSxB7YbFxYbGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGRYrGR8iGxPm1XXGY6befzscVnpvOxPtFefN59ot01KOaHqWpQuGrM/DBV1RjXeZoPpq7z5Mps88HUldlcS7HYzFxLkReqn7Zc/TR3Plz9FNcrLhyp1St2hfHikGqFcd7oCdByT4BPI/WeAOMp2V088iX1Lh7jct13Jz8y6bsznpbdKStfUu+UNSnXve3yIZPedq9JdjfKzyOzbpS+5vT6B1zcG1Ke89qOAAAAAElFTkSuQmCC)

![Page 5 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAABGCAYAAAAtpKGgAAAIfElEQVR4nO2cCU8jORCFi4GQgyQkISF30jkIDOzMrvb6/z9tNdIr6VOpAx7CiN7IT7IC3Y7brnIdXX5glpGRkZGRkZGRkZGRkZGRkZGRkXEEF2b2JbFdHml+/0KNY8cWn33s3mtjxJYy19Q1vjaXSsAXfGVm12ZWR7tWq6n5/YaZNUNroG8U0KXGv3pFeMeUf3FECfzdx47zjHNthHXFfo0j66icAn3xNU34xsw6ZtbVZ1vXWmo3uvbjfs/M+vq81bUbjVMLwryGUFxwV6FPHQK7CkplnzLBu3LiPH0tt0fWxPWwX1v365hLZZR3IaVda5JdKWJoZiN93pnZAMrp69qP+xMzm6rdq38PynOhNiWIW7WOnteAIpr6Hr97FTyBj9NG33aJgnqYp6/F5zfAZuuF9dyrjXStp7F9I375bIU5vmhCLS14KGXMzWyhNtM1X/hY15ZmtjGznZltzWyl6yON1YIFdCWIscYaqk877Pg+hNWE5XFjDbCZ+HMUPtexVJtjLeznfX6sYa1P73unTdHQXD7d6tzaGhLIUJP9MelCSlmHBY9lXUv1eTCzJzM7qP8CinOL8LFnGq9QvyGsuCcB+W53q72Gpfk4U43FNoH1z8LG2uiZaz13gg001TVf7xYbsZAsptpQPp9Pt7oL7aCWBDXR4jh5Xyx36gSLdcU9qO9Uu5+WNNB17/8gIU3himnJE4zhbvRG12YaZ4tWwDPM1ZbheTv0G0Nxc817h7ZX8/GXml9Hc6mE4mpBKJsw8bUWxxh2r74r9Tuo70L3bhH0u7KgFZT8pO8tsBnofqdSZhvJTFf9Cn3/Wc3HWsHS3GvsdP8Rm2UOF+nWttUavD3q0+WwVv+u5lIZxbXkCmaIWfsQt+6RoHis8kX74mgpzWBtWwnxRQI/BGHPEGNmQXFNPXcqBXw3sz/UvmOsKdyfb6qv8AgFYvD9kX5PQdm+KVxxlbE4usqxJukuYgOBeDzyVwCPNWsIhEG8CStZSbi/mdk3fT5h/CWUtoK79eyypd8XEvCfZva32h8SsrtAt96lBB8VN4HXmMITPKvvV1iyu1iPx+2qxDhPs5shgVghqK/hXqi4OwnBBT8OrwF0v1sJ5BsU91W72ROHAsnARB6ghfg21L0XKexfM/tHijvATY+OKI5eYQR3X0jxL5qXt2ckXDPM59Ozygu8CjSRrjPx2EJ5E7jKPixuBaH18FLblQDX2NGuOHeXjxLoDlZOxd1obh0Je63vusX9ZWa/a3xa3ASWFOPbKMTpAi78m1zvNyhurXHdTV5WQXF88e7hHY6K22HRQ7w7jZDez5HCtxHb5kgQXmBtL1DeU0gM+CyvcvQ1r0Lf+Y72LOUvESsXsKTHEN+GyGDnet5B8/h6JOkZaR6VcJMe3xqa1ACZ3QpJyg4Zo1cT7qA4xsBbVC9GEuYOmdpTaM8lSYGn3xNUOIawjgMUcoA1rVAw8DjN7JCKG2GtRXgNeAhZNeNb7bOtzZBRMr5NkEpvQpIyCxbnrtLjXx8WcivhLJC8rPGzC+sRzRW3U79ZiFncUByPyQ0rHzsoli54GLLKJYoMq5LGRKkyirsKVZMphE0BefIxQH1vgAzuDtbWLqlwTPHSOw7vTzu8Cz7CNS9Dej+DRU3CeBPcX8Li9hhvhcRkFN4dZ6EEdo/neuxuVUlxlwq4bSiC71MeN8ayqE4o5rr1sZLe0s99xJM+Ku5epB5B2LRwbhaWslxJo1Ag7iHmUsmrkmx1CsUMYX0svd1iju5hOqibfrriDFllA0nAEItjhfwmnFW1kIiUVfnbUDTvN3CfVflxUJIL9y5YejccMbFCEyv9tMh7bCIeQXVxUhGPhDooJlxX4VXAcXHkHO72yJlULZyt1UvOz67C+Vg8jPQDzzqU30GhuRcEG8/OmiWHutcQOk8a4pjdsNlaJYe/PONrlBwvVUJxduTkuxFOin/2NPvYPZ5kX75ymt565bT6tefVSoTeLFFSPSg/jhlP1Ct7Am5vUAPipFN4HynckjLKwlVoZRyRFJ7JqeO9tYaMjF+H15hfb5F53sOoStntb1naWTK6UvEW86sW3FBZvPpZRlWZayuLkSQPxVh5loyuVKQwv1ohofgIRlUzCLQeEohLbJJGeHfslIx7FoyuVKQwvwbhnaiHUth7GVV9pO1dCLQZrKaOecUxRyc8v7KMrlSkML+meLH9KEYVx3QFDEpeutsSMqslc9QXz4rRlYqfYX4tSirypzCqWO6aB2Gy0uFK47y2qOhvzonRlYpU5hd3LKv9pzCqduFUnAVud3s8UipCkdrP9s6K0ZWKVObXIuz2x8DVeA+jilQ6Wu8cdUySgbbqf9C53suJz68koysVqcwvjxMFTrmdS/JeRtVDcHebkkPS+NwHbJpTn19JRlcqUplftDgXRhTcexhVGyQMJC0VIcaSWvEAizv1+ZVjdKUilflF4bkwXj6AUeWJCbkj+0ArKEKytAcV4qwYXalIZX5tgzAfsYtPZVRNcR43hbCfkHxsAlVhi+TkrBhdqUhlfu2DMI/Fl/cwqsbhe5FyfkDC4n8jsDlXRlcqUplfD2HhL2Ann8qoGqHacS8roOL2YIF5il8gSzwrRlcqUplf+5CV0Ro+glHVg7Uvwp9yFeo3QuVkHRRwNoyuVKQyv/hetw+7/SMYVV3UR1kAoCX1QXBalmS9Z8HoSkUq86vsnYop+ymMqi7+INLd9QSMr7tAvB0g1T9LRlcqUphfLog73PtIRhXP1Nqo6vdCn2bYYGfJ6EpFCvOrA7bUr2BU1dDqgUBUD4enjfAfIM6S0ZWKFObXW/+q4lRGVRljrOy7PFQ9e0ZXKt5ifr0m4FMZVantVz0/IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyPjf47/ABbQ6NSnT61nAAAAAElFTkSuQmCC)

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

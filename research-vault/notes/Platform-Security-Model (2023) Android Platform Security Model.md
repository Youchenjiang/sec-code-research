---year: 2023

secverify_category: "Category A"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "The Android Platform Security Model (2023)"
creator: "LaTeX with acmart 2020/11/15 v1.75 Typesetting articles for the Association for Computing Machinery and hyperref 2023-04-22 v7.00x Hypertext links for LaTeX"
pages: 51
source: "Platform-Security-Model (2023) Android Platform Security Model.pdf"
---

# The Android Platform Security Model (2023)

> **文獻存檔**：[PDF 原文](<../../raw-papers/2023/Platform-Security-Model (2023) Android Platform Security Model.pdf>) | [Markdown 原文](<../../raw-papers/2023/Platform-Security-Model (2023) Android Platform Security Model (Raw).md>)

> **總頁數**：51 頁

---

## Page 1

∗

The Android Platform Security Model (2023)

RENÉ MAYRHOFER, Google and Johannes Kepler University Linz, Austria

JEFFREY VANDER STOEP, Google, Switzerland

CHAD BRUBAKER, Independent, USA

DIANNE HACKBORN, Google, USA

BRAM BONNÉ, Google, Switzerland

GÜLIZ SERAY TUNCAY, Google, USA

ROGER PIQUERAS JOVER, Google, USA

MICHAEL A. SPECTER, Google, USA

Android is the most widely deployed end-user focused operating system. With its growing set of use cases

encompassing communication, navigation, media consumption, entertainment, finance, health, and access to

sensors, actuators, cameras, or microphones, its underlying security model needs to address a host of practical

threats in a wide variety of scenarios while being useful to non-security experts. To support this flexibility,

Android’s security model must strike a difficult balance between security, privacy, and usability for end users;

provide assurances for app developers; and maintain system performance under tight hardware constraints.

This paper aims to both document the assumed threat model and discuss its implications, with a focus on

the ecosystem context in which Android exists. We analyze how different security measures in past and

current Android implementations work together to mitigate these threats, and, where there are special cases

in applying the security model in practice; we discuss these deliberate deviations and examine their impact.

1 INTRODUCTION

Android is the most widely deployed end-user operating system. With more than three billion

monthly active devices [13] and a general trend towards mobile use of Internet services, Android is

now the most common interface for global users to interact with digital services. Across different

form factors, including phones, tablets, wearables, TVs, Internet-of-Things, automobiles, and more,

Android supports a vast – and still growing – range of use cases including communication, media

consumption, entertainment, finance, health, and physical sensors/actuators.

Many of these applications are increasingly security and privacy critical, and Android’s success

continues to depend on the operating system’s ability to provide sufficient assurances to all

relevant stakeholders. Securing Android therefore requires balancing the different (and sometimes

conflicting) needs of users, application developers, content producers, service providers, and

arXiv:1904.05572v3 [cs.CR] 9 Jan 2024 employers.

To manage the complexity of the diverse interests of all stakeholders, Android’s security design

has fundamentally been based on a multi-party authorization model : an action should only

happen if all involved parties authorize it . 1 The rationale for this model is straightforward; If any

party does not agree to an action, the safe-by-default choice is for that operation to be blocked. This

∗ Last updated in December 2023 based on Android 14 as released. A previous version was published in ACM Transactions

on Privacy and Security from April 2021.

1 Throughout the paper, the term “authorization” is used to refer to various technical methods of declaring or enforcing

a party’s intent, rather than the legal requirement of “consent” found in many privacy legal regimes around the world.

In previous versions, the term “consent” was also used for the technical declaration of intent. This version clarifies the

distinction by using the more technical notion of “authorization”.

Authors’ addresses: René Mayrhofer, Google and Johannes Kepler University Linz, Austria, rmayrhofer@google.com; Jeffrey

Vander Stoep, Google, Switzerland, jeffv@google.com; Chad Brubaker, Independent, USA, chad.m.brubaker@gmail.com;

Dianne Hackborn, Google, USA, hackbod@google.com; Bram Bonné, Google, Switzerland, brambonne@google.com; Güliz

Seray Tuncay, Google, USA, gulizseray@google.com; Roger Piqueras Jover, Google, USA, rogerpiqueras@google.com;

Michael A. Specter, Google, USA, mikespecter@google.com.

---

## Page 2

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

2 Piqueras Jover, and Michael A. Specter

is a significant departure from the security models implemented by traditional operating systems,

which are focused on user access control and do not explicitly consider other stakeholders.

The goal of this paper is to document the Android security model, development, and implemen-

tation over time, with special consideration to the Android ecosystem’s constraints and unique

history. While the multi-party authorization model has implicitly informed the architecture and

design of the Android platform from the beginning, it has been refined and extended based on

experience gathered from subsequent releases. Our hope is that this work will serve as a canonical

resource on Android’s security posture, providing insight for both researchers and the general

public.

Specifically, we make the following contributions:

(1) We provide security-relevant background on Android’s history, design, and governance

structure.

(2) We motivate and define the Android security model based on security principles and the

wider context in which Android operates. Note that the core multi-party authorization

model described in this paper has been implicitly informing Android security mechanisms

since the earliest versions, and we therefore systematize knowledge that has, in part, been

discussed only informally as folklore.

(3) We present Android’s threat model, and discuss how the platform security model addresses

commonly seen threats, including necessary special case handling.

(4) We explain how the Android Open Source Project (AOSP), as the reference implementation

of the Android platform, enforces the security model based on multiple interacting security

measures at various layers of Android’s stack.

(5) We identify open gaps and potential for future improvement of this implementation, as well

as a number of open problems in Android security.

Structure. We begin by introducing the ecosystem context and threat analysis that are the basis

of the Android security model (Section 2). Next, we define the central security model (Section 3)

and its implementation in the form of architecture and enforcement mechanisms on various layers

of the operating system (Section 4). Finally, we discuss special cases (Section 5) and basic related

academic work on Android security (Section 6).

All historical presentations are based on an analysis of security relevant changes to the whole

AOSP code base between Android releases 4.x and 14 (inclusive), spanning about 13 years of code

evolution. Note that all implementation specific sections refer to Android 14 at the time of its

initial release unless mentioned otherwise (cf. [107, 126], [121, 174], [137, 184], [36, 70, 160], [51],

and [138] for some of the relevant changes in Android 14 to 9, respectively). We will refer to

earlier Android version numbers instead of their code names: 4.1–4.3 (Jelly Bean), 4.4 (KitKat), 5.x

(Lollipop), 6.x (Marshmallow), 7.x (Nougat), 8.x (Oreo), and 9.x (Pie).

2 ANDROID BACKGROUND AND SCOPE

At its core, Android is an end-user focused operating system , intended for everyday users of varying

levels of expertise on consumer devices. As a result, it must be both useful to users and attractive

to developers; user interfaces and workflows need to be safe by default and require explicit intent

for any actions that could compromise security or privacy. This also means that the OS must

not offload technically-challenging security or privacy decisions to non-expert users who are not

sufficiently skilled or experienced to make them [15]. For developers, the operating system must

provide adequate flexibility for a variety of use cases while providing sufficient guardrails to allow

for interoperability between devices and protect against unintentional misuse of OS mechanisms.

---

## Page 3

The Android Platform Security Model (2023) 3

Here we provide an overview of security-relevant parts of the Android platform, particularly

those that have direct implications to the security model. We focus on the actors involved, their

various levels of control over the ecosystem, and how they interoperate in the development of

Android devices in practice. We begin with a discussion of the Android ecosystem, how Android is

defined by compatibility requirements , and discuss the scope of this paper. Finally, we conclude the

section with a discussion of the threats Android is designed to prevent.

2.1 Android as an open ecosystem

Android is not a vertically-integrated product, developed and maintained by one company. Instead,

devices in the Android ecosystem are supported by hundreds of different Original Equipment

Manufacturers (OEMs), who have collectively launched tens of thousands of Android devices in

varying form factors [140] (including smartphones, tablets, watches, glasses, headsets, Internet

of things devices, handheld scanners/displays and other special-purpose devices, TVs, cars, and

exercise equipment). Some OEMs do not have detailed technical expertise, and instead rely on

Original Device Manufacturers (ODMs) for developing hardware and firmware and then re-package

or re-label devices with their own brand. OEMs and ODMs also often depend on external silicon

manufacturers to develop particular low-level hardware components for their devices, as well as

firmware or kernel-level driver software. For simplicity, we often refer to these groups collectively

as device manufacturers .

While some parts of the platform may be customized or proprietary for different device manufac-

turers, AOSP provides reference implementations for nearly all components. This includes the Linux

kernel, 2 an ARM trusted execution environment called Trusty, 3 and a bootloader called libavb

that provides a cryptographically verified boot process. In practice, device manufacturers often

alter these reference implementations to form the distribution of Android that ultimately reaches

the user’s device. As a result, device manufacturers are responsible for customizing, building,

distributing, and supporting Android for their devices.

Another goal of Android is to provide application developers with maximum flexibility. As a

result, Android:

(1) Explicitly supports installation of apps from arbitrary sources, including alternative app

stores and apps independently distributed without a store at all. 4

(2) Allows applications to be written in any programming language, with or without runtime

support, compiled or interpreted. 5

These design decisions have immediate implications for the security posture; Android cannot rely

on compile-time checks or any other assumptions on the build environment, nor can it depend

exclusively on a centralized store to enforce compatibility and security.

2.2 Android is defined by compatibility requirements

Managing the complex ecosystem of device manufacturers, application developers, and users is a

core challenge for Android. For example, without compatibility between devices, app developers

2 https://android.googlesource.com/kernel/common/

3 https://android.googlesource.com/trusty/vendor/google/aosp/

4 Consequently, there is a long tail of apps with a very specific purpose, being installed on only a few devices, and/or

targeting old Android API releases. The definition of and changes to APIs, therefore, need to consider the large number of

such legacy applications that are part of the Android ecosystem.

5 Android does not currently support non-Java language APIs for the basic process lifecycle control, because they would

have to be supported in parallel, making the framework more complex and therefore more error-prone. Note that this

restriction is not directly limiting, but apps need to have at least a small Java language wrapper to start their initial process

and interface with fundamental OS services.

---

## Page 4

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

4 Piqueras Jover, and Michael A. Specter

would be forced to handle device-specific idiosyncracies, significantly increasing development time

and effort. New device manufacturers would also have difficulty entering the market if applications

were by-default incompatible with their systems, requiring app developers to spend resources to

support their system, and users would have to contend with a complicated environment where

certain applications may or may not function depending on the device. Android succeeds in

managing this complexity (and preventing these headaches) through various levels of compatibility

requirements, standards, and compliance tests, allowing all participants to enjoy the network effects

of the ecosystem.

In fact, the Android platform is defined as the set of AOSP components that together form

an operating system that adheres to standards called the Compatibility Definition Document

(CDD) [19]. AOSP provides a series of tests, including the Compatibility Test Suite (CTS), which

allow a device manufacturer to test if their system complies with the CDD. It may be the case that a

system that passes CTS does not follow the CDD, for example the CDD is a “whole device standard,”

so a virtual machine or emulator running AOSP might pass CTS, but still not follow the CDD.

Devices that do not conform to the CDD (and/or do not pass CTS), by definition, are not Android.

Further, devices that advertise themselves as Android as a trademarked name need to, at minimum,

pass CTS and an additional set of tests called the Vendor Test Suite (VTS). Finally, Android devices

are subjected to additional requirements to be certified to run Google Mobile Services, which we

call GMS Android. Though devices based purely on AOSP are only required to ensure that they

meet publicly documented compatibility tests, those shipping with Google services are held to a

stricter standard, including additional compliance tests focusing on security and privacy.

CDD CTS VTS GMS & Security Tests Is Android?

| Untested fork of AOSP | ✗ | ✗ | ✗ | ✗ | ✗ |
| --- | --- | --- | --- | --- | --- |
| AOSP | ✓ | ✓ | ✗ | ✗ | ✓ |
| Trademarked Android | ✓ | ✓ | ✓ | ✗ | ✓ |
| GMS Android | ✓ | ✓ | ✓ | ✓ | ✓ |

Table 1. The various types of “Android” systems. A ✓ here indicates that the OS is guaranteed, in some way,

to be compliant with the requirement, whereas ✗ indicates that the OS is either not compliant or that the

compliance is not guaranteed. For example, something forked from AOSP and not tested may happen to

comply with the Android specification, but this cannot be guaranteed without passing the CDD and the CTS.

The term Android is commonly used to refer to a number of different items in the Android

ecosystem, including:

• The Android Open Source Project (AOSP), which is a reference implementation of the

Android operating system.

• Operating systems forked from AOSP, that happen to be capable of running Android

applications.

• Devices running trademarked Android operating system.

• Devices running trademarked Android, as well as Google services.

This paper focuses on security and privacy measures in the Android platform itself, i.e. code

running on user devices that is part of AOSP. We define the platform as the set of AOSP components

that together form a complete system that is compliant with CDD, much of which is enforced by a

suite of tests defined by Google called the Compatibility Test Suite or CTS (more fully discussed

below in Section 3).

---

## Page 5

The Android Platform Security Model (2023) 5

In contrast, there are a number of proprietary services that, while they do affect the security pos-

ture of Android in practice, are not relevant for understanding the security model we outline in this

paper. These include specific code running under Private Compute Core (see Section 4.3.6), Google

Mobile Services (GMS), Google Play Services, the Google Play Store, Google Search, Chrome, and

other standard apps that are colloquially considered part of Android, as they provide dependencies

for common services such as location estimation or cloud push messaging. Android devices certified

to support GMS are publicly listed. 6 While replacements for these components exist (including

an independent, minimal open source version called microG 7 ), they may be incomplete or behave

differently than what is described in this work. Again, we do not consider these services as part

of the platform, as they are also subject to the security policy defined and enforced by AOSP

components. 8

There are also a class of devices that, though they may run a fork of AOSP, do not adhere to

CTS/CDD or follow the threat model described here, and so we cannot consider or adequately

describe the security of these devices – these “forked” platforms are outside the scope of this work.

In a practical sense, it is difficult to reason about their threat model, and any customizations done

to these systems may not be compatible with the security and privacy goals of Android.

2.3 Threat model

Threat models for mobile devices are extended from those commonly used for desktop or server

operating systems for two major reasons: by definition, mobile devices are easily lost or stolen,

and they connect to untrusted networks as part of their expected usage. At the same time, by

being close to users at most times, they are also exposed to more privacy sensitive data than many

other categories of devices. Therefore, modern mobile device platforms, among other extensions,

primarily tend to assign less trust to locally installed applications than traditional desktop operating

systems, which may be argued to not have sufficiently adapted to the changed threat landscape. 9

Recent work [131] previously introduced a layered threat model for mobile devices which we

adopt for discussing the Android security model within the scope of this paper; however, where

meaningful, we order threats in each category with lower numbers representing more constrained

and higher numbers more capable adversarial settings:

Adversaries can get physical access to Android devices. For all mobile and wearable devices, we

have to assume that they will potentially fall under physical control of adversaries at some point.

The same is true for other Android form factors such as wearables, cars, TVs, etc. Therefore, we

assume Android devices to be either directly accessible to adversaries or to be in physical proximity

to adversaries as an explicit part of the threat model. This includes loss or theft, but also multiple

(benign but potentially curious) users sharing a device (such as a TV or tablet). We derive specific

threats due to physical or proximal (P) access:

6 https://storage.googleapis.com/play_public/supported_devices.html

7 https://github.com/microg/android_packages_apps_GmsCore/wiki

8 In terms of higher-level security measures, there are services complementary to those implemented in AOSP in the form of

Google Play Protect scanning applications submitted to Google Play and on-device (Verify Apps or Safe Browsing as opt-in

services) as well as Google Play policy and other legal frameworks. These are also out of scope of the current paper, but are

covered by related work [16, 59, 90, 161]. However, it is worth noting that restrictions in Google Play can work in tandem

with the platform to yield significant positive effects for security. For example, Play now requires that apps target a recent

Android API level, which will allow the Android platform to deprecate and remove APIs known to be abused or that have

had security issues in the past [75]. Similarly, Google Play Services have been used to “backport” security improvements

(such as permission revocation [177]) to devices running older versions of AOSP.

9 Newer (Linux) desktop operating systems have started adopting some of the concepts like read-only system images

and sandboxed applications as well, although the basic association of permissions to the logged-in user account is still

problematic under the threat of actively malicious local applications.

---

## Page 6

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

6 Piqueras Jover, and Michael A. Specter

T.P1 (Screen locked or unlocked) devices in physical proximity to, but not under direct control

of, an adversary with the assumed capability to control all available radio communication

channels, including cellular, WiFi, Bluetooth, UWB, GPS, NFC, and FM, e.g. direct attacks

through Bluetooth [2, 73]. Although NFC could be considered to be a separate category to

other proximal radio attacks because of the scale of distance, we still include it in the threat

class of proximity instead of physical control.

T.P2 Powered-off devices under complete physical control of an adversary (with potentially

high sophistication up to nation state level attackers), e.g. border control or customs checks.

T.P3 Screen locked devices under complete physical control of an adversary, e.g. thieves

trying to exfiltrate data for additional identity theft.

T.P4 Screen unlocked (shared) devices under control of an authorized but different user, e.g.

intimate partner abuse, voluntary submission to a border control or customs check.

Network communication is untrusted. The standard assumption of network communication under

complete control of an adversary certainly also holds for Android devices. This includes the first

hop of network communication (e.g. captive WiFi portals breaking TLS connections and malicious

fake access points) as well as other points of control (e.g. mobile network operators or national

firewalls), summarized in the usual Dolev-Yao model [79] with additional relay threats for short-

range radios (e.g. NFC or BLE wormhole attacks [145]). For practical purposes, we mainly consider

three network-level (N) threats:

T.N1 Passive eavesdropping and traffic analysis, including tracking devices within or across

networks, e.g. based on MAC address or other device network identifiers.

T.N2 Active manipulation of network traffic, e.g. machine-in-the-middle (MITM) or on-path

attacks (OPA) on TLS connections or relaying.

T.N3 Adversarial cellular network provider, e.g. rogue cellular operator [11] or rogue/false

cellular base station [139, 153]. The peculiarities of cellular protocols expose devices to

threats that are unique to these types of networks and not addressed by mitigations to

[T.N1] and [T.N2] [107].

These threats are different from [T.P1] (proximal radio attacks) in terms of scalability of attacks.

Controlling a single choke point in a major network can be used to attack a large number of devices,

while proximal (i.e., last hop) radio attacks require physical proximity to target devices.

Untrusted code is executed on the device. One fundamental difference to other mobile operating

systems is that Android intentionally allows, with explicit authorization by end users, installation

of application (A) code from arbitrary sources, and does not enforce vetting of apps by a central

instance. This implies attack vectors on multiple levels (cf. [131]):

T.A1 Abusing APIs supported by the OS with malicious intent, e.g. spyware.

T.A2 Abusing APIs provided by other apps installed on the device [6].

T.A3 Untrusted code from the web (i.e. JavaScript) is executed without explicit authoriza-

tion [72, 127, 168].

T.A4 Mimicking system or other app user interfaces to confuse users (based on the knowl-

edge that standard in-band security indicators are not effective [78, 143]), e.g. to input

PIN/password into a malicious app [89], permission phishing [169].

T.A5 Reading content from system or other app user interfaces, e.g. to screen-scrape confi-

dential data from another app [105, 114].

T.A6 Injecting input events into system or other app user interfaces [92].

T.A7 Exploiting bugs in the OS to escalate privileges or gain code execution, e.g. in the kernel,

drivers, or system services [3–5, 7], or in the firmware running on other processors within

---

## Page 7

The Android Platform Security Model (2023) 7

the SoC that perform various specialized tasks (e.g. cellular communications) [95], or in the

protected components of other apps [120, 167].

T.A8 Surreptitiously adding potentially harmful code to system images or other code or data

executed or interpreted on-device through insider capabilities such as access to private code

signing keys.

Untrusted content is processed by the device. In addition to directly executing untrusted code,

devices process a wide variety of untrusted data, including rich (in the sense of complex structure)

media. This directly leads to threats concerning the processing of data (D) and metadata:

T.D1 Abusing unique identifiers for targeted attacks (which can happen even on trusted

networks), e.g. using a phone number or email address for spamming or correlation with

other datasets, including locations. This includes using stable device identifiers to cross

profile boundaries or factory resets, without explicit involvement from the platform.

T.D2 Exploiting code that processes untrusted content in the OS, firmware, or apps, e.g. in

media libraries [1], or libraries parsing ASN.1-encoded cellular messages [12]. This can be

both a local as well as a remote attack surface, depending on where input data is taken from.

Many stakeholders in the ecosystem can act as supply chain attack vectors. In addition to the explicit

[T.A8] modeling injection of harmful code shipped with the device or apps, (technical) insider

attacks can occur at many more levels in the complex supply chain of hard- and software vendors,

including chipset manufacturers, ODMs, OEMs, contributors to the AOSP code base, third party

libraries, or even malicious insiders at the platform vendor (i.e., Google). Insiders with privileged

access may be able to leak or abuse access to code signing keys, directly modify code shipped to all

users of a particular subsystem or device model, create targeted modifications for only a subset of

users, or tamper with keys created for individual user devices (e.g., to inject weak cryptographic

keys or properties useful for fingerprinting in the field). Android is far more concerned about attacks

on integrity than on confidentiality of code running on user devices, particularly considering that

most of the code is open source in the first place.

Another class of supply chain attacks are organizational attacks on a legal or political level. These

may for example take the form of compelled technical insider attacks to access available data or

make changes to code controlled by an organization, or targeted or national/global censorship of

code or data available or accessed through a platform. We note that, due to the open nature of the

Android ecosystem without a single point of vetting of code or data, it is inherently more robust to

censorship or organizational attacks against single targets.

The possibility of insider and/or organizational attacks at many levels is an effect of the ecosystem

size, and such attacks need to be part of a realistic threat model.

3 THE ANDROID PLATFORM SECURITY MODEL

The basic security model described in this section has informed the design of Android, and has been

refined but not fundamentally changed. Given the ecosystem context and threat model explained

above, the Android security model balances security and privacy requirements of users with security

requirements of applications and the platform itself. The threat model described above includes

threats to all stakeholders, and the security model and its enforcement by the Android platform

aims to address all of them. The Android platform security model is informally defined by five

rules:

○ 1 Multi-party authorization. No action should be executed unless all main parties agree — in

the standard case, these are user , platform , and developer (implicitly representing stakeholders such

as content producers and service providers). Any one party can veto the action. This multi-party

---

## Page 8

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

8 Piqueras Jover, and Michael A. Specter

authorization spans the traditional two dimensions of subjects (i.e., users and application processes)

vs. objects (i.e., files, network sockets and IPC interfaces, memory regions, virtual data providers,

etc.) that underlie most security models (e.g. [158]). Any party (or more generally actor) that

creates a data item is implicitly granted control over this particular instance of data representation.

Focusing on (regular and pseudo) files as the main category of objects to protect, the default control

over these files depends on their location and which party created them:

• Data in shared storage is controlled by users.

• Data in private app directories and app virtual address space is controlled by apps.

• Data in special system locations is controlled by the platform (e.g. list of granted permis-

sions).

Data in run-time memory (RAM) is by default controlled by the respective platform or app process.

However, it is important to point out that, under multi-party authorization, even if one party

primarily controls a data item, it may only act on it if the other involved parties authorize the

respective access. Control over data also does not imply ownership — which is a legal concept rather

than a technical one and therefore outside the scope of an OS security model.

The same notion of authorization applies to data or resources that are technically controlled by

external parties outside the Android platform, such as cloud services. Any external dependencies of

apps or the platform itself are treated as parts of the respective party from an authorization point

of view: services provided by the OEM are considered to be part of the platform as long as they

obey the security model, and services used by apps are considered to be part of the app domain

(e.g., external web resources loaded by an embedded WebView). Data on such external services

may only be used in ways covered by mutual authorization — both for data retrieved from external

services and used on-device and data created on-device and then used externally.

While this principle has long been the default for filesystem access control (DAC, cf. Section 4.3.1

below), we consider it a global model rule and exceptions such as device backup (cf. Section 5) can

be argued about within the scope of the security model. There are other corner cases in which only

a subset of all parties may need to authorize — for actions in which the user only uses platform/OS

services without involvement of additional apps — or an additional party may be introduced (e.g.

on devices or profiles controlled by a mobile device management, this policy is also considered as a

party for authorizing an action).

Public information and resources are out of scope of this access control and available to all

parties; particularly all static code and data contained in the AOSP system image and apps (mostly

in the Android Package (APK) format) is considered to be public (cf. Kerckhoff’s principle) —

if an actor publishes the code, this is interpreted as implicit consent to access. However, it is

generally accepted that such public code and data is read-only to all parties and its integrity

needs to be protected, which is explicitly in scope of the security measures.

○ 2 Open ecosystem access. Both users and developers are part of an open ecosystem that is not

limited to a single application store. Central vetting of developers or registration of users is not

required. This aspect has an important implication for the security model: generic app-to-app

interaction is explicitly supported. Instead of creating specific platform APIs for every conceivable

workflow, app developers are free to define their own APIs they offer to other apps.

○ 3 Security is a compatibility requirement. The security model is part of the Android specifica-

tion, which is defined in the Compatibility Definition Document (CDD) [19] and enforced by the

Compatibility (CTS), Vendor (VTS), and other test suites. Devices that do not conform to CDD and

do not pass CTS are not Android. Within the scope of this paper, we define rooting as modifying the

system to allow starting processes that are not subject to sandboxing and isolation. Such rooting,

---

## Page 9

The Android Platform Security Model (2023) 9

both intentional and malicious, is a specific example of a non-compliant change which violates CDD.

As such, only CDD-compliant devices are considered. While many devices support unlocking their

bootloader and flashing modified firmware 10 , such modifications may be considered incompatible

under CDD if security assurances do not hold. Verified boot and hardware key attestation can be

used to validate if currently running firmware is in a known-good state, and in turn may influence

consent decisions by users and developers.

○ 4 Factory reset restores the device to a safe state. In the event of security model bypass leading to a

persistent compromise, a factory reset, which wipes/reformats the writable data partitions, returns

a device to a state that depends only on integrity protected partitions. In other words, system

software does not need to be re-installed, but wiping the data partition(s) will return a device to

its default state. Note that the general expectation is that the read-only device software may have

been updated since originally taking it out of the box, which is intentionally not downgraded by

factory reset. Therefore, more specifically, factory reset returns an Android device to a state that

only depends on system code that is covered by Verified Boot , but does not depend on writable data

partitions. An important aspect is supply chain security of these factory images in the sense of

integrity and authenticity of system code (cf. Section 4.7.2).

○ 5 Applications are security principals. The main difference to traditional operating systems that

run apps in the context of the logged-in user account is that Android apps are not considered to be

fully authorized agents for user actions. In the traditional model typically implemented by server

and desktop OSes, there is often no need to even exploit the security boundary because running

malicious code with the full permissions of the main user is sufficient for abuse. Examples are many,

including file encrypting ransomware [110, 148], which does not violate the OS security model if it

simply re-writes all the files the current user account has access to, and private data leakage (e.g.

browser login tokens [124], history or other tracking data, cryptocurrency wallet keys, etc.).

Summary. Even though, at first glance, the Android security model grants less power to users

compared to traditional operating systems that do not impose a multi-party consent model, there

is an immediate benefit to end users: if one app cannot act with full user privileges, the user cannot

be tricked into letting it access data controlled by other apps. In other words, requiring application

developer consent – enforced by the platform – helps avoid user confusion attacks and therefore

better protects private data.

The Android platform security model does not currently have a simple, consistent representation

in formal notation because these rules evolved from practical experience instead of a top-down

theoretical design; the meaning of the term “model” is consequently slightly different from how

conventional security models use it. Balancing the different requirements of a complex ecosystem is

a large scale engineering problem that requires layers of abstraction. Therefore, we have to combine

multiple different security controls, such as memory isolation, filesystem DAC/MAC, biometric

user authentication, or network traffic encryption, that operate under their own respective models

and are not necessarily consistent with each other (see e.g. [97] for interactions between only the

DAC and MAC policies). The five rules are, at the time of this writing, the simplest expression of

how these different security controls combine at the meta level.

10 Google Nexus and Pixel devices as well as many others support the standard fastboot oem unlock command to allow

flashing any firmware images to actively support developers and power users. However, executing this unlocking workflow

will forcibly factory reset the device, wiping all data, to make sure that security guarantees are not retroactively violated for

data on the device.

---

## Page 10

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

10 Piqueras Jover, and Michael A. Specter

Appendix A gives a first, albeit incomplete, formalization of the access control properties of these

rules. It is subject to future work to model all important aspects more formally and to reason about

the cross-abstraction interactions of these rules with lower level models of underlying security

controls.

4 IMPLEMENTATION

Android’s security measures implement the security model and are designed to address the threats

outlined above. A high-level summary of the historical design and development can be found in

the 2023 Android Enterprise Security White Paper [13], including the fundamental use of Linux

kernel user separation mechanisms as one of the underlying security building blocks in Android.

In this section we describe the combination of multiple interlocking security measures and indicate

which threats they mitigate, taking into account the architectural security principles of “defense in

depth” and “safe by design”:

Defense in depth. A robust security system is not sufficient if the acceptable behavior of the

operating system allows an attacker to accomplish their goals without bypassing the security model

(e.g. ransomware encrypting all files it has access to under the access control model). Specifically,

violating any of the above principles should require such bypassing of controls on-device, in contrast

to relying on off-device verification (e.g. at build time).

Therefore, the primary goal of any security system is to enforce its model. For Android operating

in a multitude of environments (see above for the threat model), this implies an approach that

does not immediately fail when a single assumption is violated or a single implementation bug is

found, even if the device is not up to date. Defense in depth is characterized by rendering individual

vulnerabilities more difficult or impossible to exploit, and increasing the number of vulnerabilities

required for an attacker to achieve their goals. We primarily adopt four common security strategies

to prevent adversaries from bypassing the security model: isolation and containment (Section 4.3),

exploit mitigation (Section 4.6), integrity (Section 4.7), and patching/updates (Section 4.8), as well as

the special case of cellular security defense mechanisms for mobile device networks (Section 4.9).

Safe by design/default. Components should be safe by design. That is, the default use of an

operating system component or service should always protect security and privacy assumptions,

potentially at the cost of blocking some use cases. This principle applies to modules, APIs, com-

munication channels, and generally to interfaces of all kinds. When variants of such interfaces

are offered for more flexibility (e.g. a second interface method with more parameters to override

default behavior), these should be hard to abuse, either unintentionally or intentionally. Note that

this architectural principle targets developers, which includes device manufacturers, but implicitly

includes users in how security is designed and presented in user interfaces. Android targets a wide

range of developers and intentionally keeps barriers to entry low for app development. Making it

hard to abuse APIs not only guards against malicious adversaries, but also mitigates genuine errors

resulting e.g. from incomplete knowledge of an interface definition or caused by developers lacking

experience in secure system design. As in the defense in depth approach, there is no single solution

to making a system safe by design. Instead, this is considered a guiding principle for defining

new interfaces and refining – or, when necessary, deprecating and removing – existing ones. For

guarding user data, the basic strategies for supporting safety by default are: enforced authorization

(Section 4.1), user authentication (Section 4.2), and by-default encryption at rest (Section 4.4) and in

transit (Section 4.5).

---

## Page 11

The Android Platform Security Model (2023) 11

4.1 Enforcing meaningful consent in authorization decisions

Methods allowing for meaningful consent vary greatly depending on the actor and situational

constraints.

We use three examples to better describe the authorization parties:

• An app getting access to the user’s location requires:

– app authorization by specifying in its manifest that it may request this permission

(for auditability), and at runtime in an appropriate context telling the platform it

would like to request this permission;

– platform authorization by verifying the app has correctly specified the permission

in its manifest, and prompting the user to allow this access; and

– user authorization by affirming in the runtime permission prompt that access is

allowed.

• Opening an external file for an app to access requires:

– app authorization by using ACTION_GET_CONTENT to request that it get access to a

file;

– platform authorization by presenting the available files and creating and enforcing

the accessibility of only the appropriate file; and

– user authorization by using the platform’s ACTION_GET_CONTENT UI to select the

file(s) they would like the app to access.

• Sharing data from app A to app B requires:

– user authorization by selecting data in app A that they would like to share;

– app A authorization by using ACTION_SEND to request that this data be shared

elsewhere;

– platform facilitates and enforces the share by presenting a list of possible share

targets (if there is ambiguity) and tracking the access to this data, which forms a

temporary trust relationship between the two apps;

– user authorization by reviewing and approving app B ’s UI of the data being shared

to it (such as a new message containing the data that will be sent); and

– app B authorization by accepting and processing the shared data.

Actors authorizing any action must be empowered to base their decision on information about

the action and its implications and must have meaningful ways to grant or deny this authorization.

This applies to both users and developers, although very different technical means of enforcing (lack

of) authorization apply. For users, the technical mechanism of authorization is a means of providing

consent for an action. Authorization is not only required from the actor that created a data item, but

from all involved actors. Authorization decisions should be enforced and not self-policed, which

can happen at run-time (often, but not always, through platform mediation) or build respectively

distribution time (e.g. developers including or not including code in particular app versions).

4.1.1 Developer(s). Unlike traditional desktop operating systems, Android ensures that the de-

veloper authorizes actions on their app or their app’s data. This prevents large classes of abusive

behavior where unrelated apps inject code into or access/leak data from other applications on a

user’s device.

Authorization for developers is given via the code they sign and the system executes, uploading

the app to an app store and agreeing to the associated terms of service, and obeying other relevant

policies (such as CDD for code by an OEM in the system image). For example, an app can authorize

the user sharing its data by providing a respective mechanism, e.g. based on OS sharing methods

such as built-in implicit Intent resolution chooser dialogs [33] and by utilizing custom (e.g.,

---

## Page 12

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

12 Piqueras Jover, and Michael A. Specter

signature) permissions to regulate access to the exported app components [28]. Another example

is debugging; as assigned virtual memory content is controlled by the app, debugging from an

external process is only allowed if an app authorizes it (specifically through the debuggable flag

in the app manifest). By uploading an app to the relevant app store, developers also provide the

authorization for this app to be installed on devices that fetch from that store under appropriate

preconditions (e.g. after successful payment).

For authorization to be clear from a developer point of view, the platform needs to ensure

that APIs and their behaviors are clear and the developer understands how their application is

interacting with or providing data to other components. We assume that developers of varying skill

levels may not have a complete understanding of security nuances, and as a result APIs must also be

safe by default and difficult to incorrectly use in order to avoid accidental security regressions. One

example of a lesson learned in these regards is the changed default for exporting app components

to false , away from the “smart” behavior of default true if the component has an intent-filter,

which caused unintentional over-exporting in the past.

Android 9 introduced a major change by only supporting access to APIs explicitly listed as

external 11 and putting restrictions on others [39]. Developer support was added e.g. in the form of

specific log messages to point out internal API usage for debuggable versions of apps. This has

two main benefits: a) the attack surface is reduced, both towards the platform and apps that may

rely on undefined and therefore changing internal behavior; and b) refactoring of internal platform

interfaces and components from one version to another is enabled with fewer app compatibility

constraints.

In order to ensure that it is the app developer and not another party that is authorizing, applica-

tions are signed by the developer. This prevents third parties from replacing or removing code or

resources in order to change the app’s intended behavior 12 . However, the app signing key is trusted

implicitly upon first installation, so replacing or modifying apps in transit when a user first installs

them (e.g. when initially side-loading apps) is currently out of scope of the platform security model.

Previous Android versions relied on a single developer certificate that was trusted on initial install

of an app and therefore made it impossible to change the underlying private key e.g. in the case

of the key having become insecure [56]. Starting with Android 9, independently developed key

rotation functionality was added with APK Signature Scheme v3 [47] to support delegating the

ability to sign to a new key by using a key that was previously granted this ability by the app using

so-called proof-of-rotation structs 13 .

These three examples (i.e., default component exporting, controlled access to internal Android

platform components and developer signing key rotation) highlight that handling multi-party

authorization in a complex ecosystem is challenging even from the point of a single party: some

developers may wish for maximum flexibility (i.e., access to all internal components and arbitrarily

complex key handling), but the majority tends to be overwhelmed by the complexity. As the

ecosystem develops, changes are therefore necessary to react to lessons learned. In these examples,

platform changes largely enabled backwards compatibility without changing (i.e., no impact when

key rotation is not used by a developer) or breaking (i.e., most apps do not rely on internal APIs)

existing apps. When changes for developers are necessary, these need to be deployed over a longer

period to allow adaptation, typically with warnings in one Android release and enforced restrictions

only in the next one.

11 See https://developer.android.com/reference/packages

12 One exception is app stores holding those signing keys and signing a final version of the APK as shipped to end-user

devices in the name of the developer.

13 The Google Play app store now explicitly supports key rotation through Play Signing, but does not yet support key

rotation with multiple developer-held keys. The Android platform itself supports arbitrarily complex key rotation strategies.

---

## Page 13

The Android Platform Security Model (2023) 13

4.1.2 The Platform. While the platform, like the developer, authorizes via code signing, the goals

are quite different: the platform acts to ensure that the system functions as intended. This includes

enforcing regulatory or contractual requirements (e.g. communication in cellular networks) as

well as taking an opinionated stance on what kinds of behaviors are acceptable (e.g. mitigating

apps from applying deceptive behavior towards users). Platform authorization is enforced via

Verified Boot (see below for details) protecting the system images from modification, internal

compartmentalization and isolation between components, as well as platform applications using

the platform signing key and associated permissions, much like applications.

Note on the platform as a party: Depending on how the involved stakeholders (i.e., parties

for authorization) and enforcing mechanisms are designated, either an inherent or an apparent

asymmetry of power to authorize may arise:

(a) If the Android “platform” is seen as a single entity, composed of hardware, firmware, OS

kernel, system services, libraries, and app runtime, then it may be considered omniscient in

the sense of having access to and effectively controlling all data and processes on the system.

Under this point of view, the conflict of interest between being one party of authorization and

simultaneously being the enforcing agent gives the platform overreaching power over all other

parties.

(b) If Android as a platform is considered in depth, it consists of many different components.

These can be seen as individual representatives of the platform for a particular interaction

involving multi-party authorization, while other components act as the enforcing mechanism

for that authorization. In other words, the Android platform is structured in such a way as to

minimize trust in itself and contain multiple mechanisms of isolating components from each

other to enforce each other’s limitations (cf. Section 4.3). One example is playing media files:

even when called by an app, a media codec cannot directly access the underlying resources if the

user has not granted this through the media server, because MAC policies in the Linux kernel

do no allow such bypass (cf. Section 4.3.5). Another example is storage of cryptographic keys,

which is isolated even from the Linux kernel itself and enforced through hardware separation

(cf. Section 4.3.8). While this idealized model of platform parties requiring authorization for

their actions is the abstract goal of the security model we describe, in practice there still are

individual components that sustain the asymmetry between the parties. Each new version of

Android continues to further strengthen the boundaries of platform components among each

other, as described in more detail below.

Within the scope of this paper, we take the second perspective when it comes to notions of

authorization involving the platform itself, i.e. considering the platform to be multiple parties

whose authorization is being enforced by independent mechanisms (i.e., mostly the Linux kernel

isolating platform components from each other, but also including out-of-kernel components in

a trusted execution environment). However, when talking about the whole system implementing

our Android security model, in favor of simpler expression we will generally refer to the platform

as the combination of all (AOSP) components that together act as an enforcing mechanism for

other parties, as defined in the introduction.

Lessons learned over the evolution of the Android platform are clearly visible through the

introduction of new security mitigations and tightening of existing controls, as summarized in

Tables 2 to 6 and too extensive to describe here. The platform not only manages authorization for

its own components, but mediates user and developer authorization responses, and therefore has

to adapt to changes in the ecosystem (e.g. to prevent apps deceiving users to provide authorization

against their wishes through use of deceptive strings, namespaces, and links).

---

## Page 14

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

14 Piqueras Jover, and Michael A. Specter

4.1.3 User(s). Achieving meaningful user authorization is by far the most difficult and nuanced

challenge in determining meaningful consent. For users that use their Android devices with their

own personal data and for their own, potentially highly sensitive purposes, technical authorization

of software actions directly means consent to having their data processed or actions taken in their

name. That is, especially for users — in contrast to developers and the platform or other parties —,

this consent implies concerns beyond the pure technical mechanism of providing authorization

decisions and reaches into the multi-faceted aspects of meaningful and informed consent that

includes legal, usability, social, and ethical concerns.

Some of the guiding principles concerning this user consent have always been core to Android,

while others were refined based on experiences over 10 years of development so far:

• Avoid over-prompting. Over-prompting the user leads to prompt fatigue and blindness

(cf. [17]). Prompting the user with a yes/no prompt for every action does not lead to

meaningful consent as users become blind to the prompts due to their regularity.

• Prompt in a way that is understandable. Users are assumed not to be experts or under-

stand nuanced security questions (cf. [88]). Prompts and disclosures must be phrased in a

way that a non-technical user can understand the effects of their decision.

• Prefer pickers and transactional consent over wide granularity. When possible,

we limit access to specific items instead of the entire set through ACTION_GET_CONTENT ,

typically presenting the available files and creating and enforcing the accessibility of only

the appropriate file. This also allows the user to select from a list of applications that can

provide content of the requested type, such as apps providing access to cloud file storage.

As a more specific example, the Photo Picker allows the user to select a specific picture to

share with the application instead of using the Storage permission. These both limit the

data exposed as well as present the choice to the user in a clear and intuitive way.

• The OS must not offload a difficult problem onto the user. Android regularly takes an

opinionated stance on which behaviors are too risky to be allowed and may avoid adding

functionality that may be useful to a power user but dangerous to an average user.

• Provide users a way to undo previously made decisions. Users can make mistakes.

Even the most security and privacy-savvy users may simply press the wrong button from

time to time, which is even more likely when they are being tired or distracted. To mitigate

against such mistakes or the user simply changing their mind, it should be easy for the user

to undo a previous decision whenever possible. This may vary from denying previously

granted permissions to removing an app from the device entirely. It has always been a

core design goal of the Android platform to allow an app to be cleanly removed without

depending on it to do so, so that apps cannot — through malicious behavior or simple coding

errors — prevent their own removal. This makes malware removal trivial, compared to often

requiring a complete platform re-install on traditional desktop/server operating systems.

Over time, users might forget about consent decisions made in the past, especially if an

app hasn’t been used for a long time. For this reason, since Android 11, the platform

automatically revokes permissions when an app hasn’t been used for some time [25].

Additionally, it is critical to ensure that the user who is authorizing is the legitimate user of the

device and not another person with physical access to the device ([T.P2]-[T.P4]), which directly

relies on the next component in the form of the Android lockscreen. Implementing model rule 1 ○

(multi-party authorization) is cross-cutting on all system layers.

For devices that do not have direct, regular user interaction (embedded IoT devices, shared

devices in the infrastructure such as TVs, etc.), user authorization may be given slightly differently

depending on the specific form factor. A smart phone may often act as a UI proxy to configure

---

## Page 15

The Android Platform Security Model (2023) 15

consent/policy for other embedded devices. For the remainder of this paper but without loss of

generality, we primarily assume smart phone/tablet type form factors with direct user interaction.

As with developer authorization, lessons learned for user consent over the development of the

ecosystem will require changes over time. The biggest changes for user autorization were the

introduction of runtime permissions with Android 6.0, moving the point of authorization from

install time to access time and therefore granting users better implicit context and granularity, and

non-binary, explicitly context dependent permissions with Android 10 (cf. Section 4.3.1). Other

examples are restrictions to accessibility service APIs (which require user authorization but were

abused), clipboard access and background activity launches starting in Android 10, app hibernation

in Android 11 [25], and mitigations against tapjacking attacks in Android 12 (cf. Table 2).

4.2 Authentication

Authentication is a gatekeeper function for ensuring that a system interacts with its owner or

legitimate user. On mobile devices the primary means of authentication is via the lockscreen. Note

that a lockscreen is an obvious trade-off between security and usability: On the one hand, users

unlock phones for short (10-250 seconds) interactions about 50 times per day on average and

even up to 200 times in exceptional cases [85, 100], and the lockscreen is obviously an immediate

hindrance to frictionless interaction with a device [98, 99]. On the other hand, devices without a

lockscreen are immediately open to being abused by unauthorized users ([T.P2]–[T.P4]), and the

OS cannot reliably enforce user consent without authentication.

In their current form, lockscreens on mobile devices largely enforce a binary model — either the

whole phone is accessible, or the majority of functions (especially all security or privacy sensitive

ones) are locked. Neither long, semi-random alphanumeric passwords (which would be highly

secure but not usable for mobile devices) nor swipe-only lockscreens (usable, but not offering any

security) are advisable. Therefore, it is critically important for the lockscreen to strike a reasonable

balance between security and usability, as it enables further authentication on higher levels.

4.2.1 Tiered lockscreen authentication. Towards this end, recent Android releases use a tiered

authentication model where a secure knowledge-factor based authentication mechanism can be

backed by convenience modalities that are functionally constrained based on the level of security

they provide. The added convenience afforded by such a model helps drive lockscreen adoption and

allows more users to benefit both from the immediate security benefits of a lockscreen and from

features such as file-based encryption that rely on the presence of an underlying user-supplied

credential. As of August 2020, starting with Android 7 we see that 77% of devices with fingerprint

sensors have a secure lockscreen enabled, while only 54% of devices without fingerprints have a

secure lockscreen 14 .

As of Android 10, the tiered authentication model splits modalities into three tiers.

• Primary Authentication modalities are restricted to knowledge-factors and by default include

password, PIN, and pattern 15 . Primary authentication provides access to all functions on

the phone. It is well-known that the security/usability-balance of these variants is different:

complex passwords have the highest entropy but worst usability, while PINs and patterns are

a middle balance but may suffer e.g. from smudge [54] ([T.P2]–[T.P3]) or shoulder surfing

attacks [81, 109] ([T.P1]). However, a knowledge-factor is still considered a trust anchor for

device security and therefore the only one able to unlock a device from a previously fully

locked state (e.g. from being powered off).

14 These numbers are from internal analysis that has not yet been formally published.

15 We explicitly refer to patterns connecting multiple dots in a matrix, not the whole-screen swipe-only lockscreen interaction

that does not offer any security.

---

## Page 16

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

16 Piqueras Jover, and Michael A. Specter

• Secondary Authentication modalities are biometrics — which offer easier, but potentially less

secure (than Primary Authentication), access into a user’s device 16 . Secondary modalities

are themselves split into sub-tiers based on how secure they are, as measured along two

axes:

– Spoofability as measured by the Spoof Acceptance Rate (SAR) of the modality [136].

Accounting for an explicit attacker in the threat model on the level of [T.P2]–[T.P3]

helps reduce the potential for insecure unlock methods [133].

– Security of the biometric pipeline , where a biometric pipeline is considered secure if

neither platform or kernel compromise confers the ability to read raw biometric data

or inject data into the biometric pipeline to influence an authentication decision.

These axes are used to categorize secondary authentication modalities into three sub-tiers,

where each sub-tier has constraints applied in proportion to their level of security [70]:

– Class 3 (formerly ‘strong’): SAR<7% and secure pipeline

– Class 2 (formerly ‘weak’): 7%<SAR<20% and secure pipeline

– Class 1 (formerly ‘convenience’): SAR>20% or insecure pipeline

All classes are required to have a (naïve/random) false acceptance rate (FAR) of at most

1/50000 and a false rejection rate (FRR) of less than 10%. Biometric modalities not meet-

ing these minimum requirements cannot be used as Android unlock methods. Secondary

modalities are prevented from performing some actions — for example, they cannot decrypt

file-based or full-disk encrypted user data partitions (such as on first boot) and are required

to fallback to primary authentication once every 72 (Class 3) or 24 (Class 1 and 2) hours.

Only Class 3 biometrics can unlock Keymint auth-bound keys and only Class 3 and 2 can

be used for in-app authentication.

The benefits of using a secondary modality in addition to a primary modality aren’t lim-

ited to convenience: they help mitigate against the aforementioned smudge and shoulder

surfing attacks by reducing the number of opportunities for an attacker to capture primary

authentication attempts.

Android 10 introduced support for implicit biometric modalities in BiometricPrompt for

modalities that do not require explicit interaction, for example face recognition. Android 11

further introduced new features such as allowing developers to specify the authentication

types accepted by their apps and thus the preferred level of security [50].

• Tertiary Authentication modalities are alternate modalities such as unlocking when paired

with a trusted Bluetooth device, or unlocking at trusted locations; they are also referred to

as environmental authentication. Tertiary modalities are subject to all the constraints of

secondary modalities. Additionally, like the weaker secondary modalities, tertiary modalities

are also restricted from granting access to Keymint auth-bound keys (such as those required

for payments) and also require a fallback to primary authentication after any 4-hour idle

period. Android 10 switched tertiary authentication from an active unlock mechanism into

16 While the entropy of short passwords or PINs may be comparable to or even lower than for good biometric modalities and

spoofability based on previous recordings is a potential issue for both, knowledge factors used as primary authentication

offer two specific advantages: a) knowledge factors can be changed either (semi-) regularly or after a compromise has

become known, but biometrics can typically not — hence biometric identification is not generally considered a secret;

b) knowledge factors support trivial, bit-for-bit comparison in simple code and hardware (cf. use of TRH as described in

Section 4.3.8) instead of complex machine learning methods for state-of-the-art biometric sensors with liveness detection

— this simplicity leaves less room for implementation errors and other attack surface. Additionally, this perfect recall of

knowledge factors allows cryptographic key material, e.g. for file encryption, to be directly entangled respectively derived

from them.

---

## Page 17

The Android Platform Security Model (2023) 17

an extending unlock mechanism that can only keep a device unlocked for a longer duration

(up to 4 hours) but no longer unlock it once it has been locked.

The Android lockscreen is currently implemented by Android system components above the

kernel, specifically Keyguard and the respective unlock methods (some of which may be OEM

specific). User knowledge factors of secure lockscreens are passed on to Gatekeeper/Weaver (ex-

plained below in Section 4.3.8) both for matching them with stored templates and for deriving keys

for storage encryption. One implication is that a kernel compromise could lead to bypassing the

lockscreen — but only after the user has logged in for the first time after reboot.

Android devices as a second factor. As of April 2019, lockscreen authentication on Android 7+ can

be used for FIDO2/WebAuthn [8, 178] authentication to web pages, additionally making Android

phones second authentication factors for desktop browsers through implementing the Client to

Authenticator Protocol (CTAP) [156]. While this support is currently implemented in Google Play

Services [91], the intention is to include support directly in AOSP in the future when standards

have sufficiently settled down to become stable for the release cycle of multiple Android releases.

Identity Credential. While the lockscreen is the primary means for user-to-device (U2D) authen-

tication and various methods support device-to-device (D2D) authentication (both between clients

and client/server authentication such as through WebAuthn), identifying the device owner to other

parties has not been in focus so far. Through the release of a JetPack library 17 , apps can make use of

a new “Identity Credential” subsystem to support privacy-first identification [102] (and, to a certain

degree, authentication). One example are third-party apps to support mobile driving licenses (mDL)

according to the ISO 18013-5 standard [9]. The first version of this subsystem targets in-person

presentation of credentials, and identification to automated verification systems is subject to future

work.

Android 11 started including the Identity Credential subsystem in the form of a new HAL, a new

system daemon, and API support in AOSP [29, 187]. If the hardware supports direct connections

between the NFC controller and tamper-resistant dedicated hardware, credentials will be able to

be marked for “Direct Access” 18 to be available even when the main application processor is no

longer powered (e.g. in a low-battery case).

In Android 13, an API for presenting multiple documents in a single session was added for

improved usability in more complex scenarios (e.g. entrance tickets presented together with a

nationally issued photo ID), and Android 14 adds ECDSA authentication in addition to the previously

standardized MAC authentication for the underlying mdoc structures.

4.3 Isolation and Containment

One of the most important parts of enforcing the security model is to enforce it at runtime against

potentially malicious code already running on the device. The Linux kernel provides much of

the foundation and structure upon which Android’s security model is based. Process isolation,

and specifically of processes with different UIDs, provides the fundamental security primitive for

sandboxing. With very few exceptions, the UID/process boundary is where security decisions are

made and enforced — Android intentionally does not rely on in-process compartmentalization

such as the Java security model. The security boundary of a process is comprised of the process

boundary and its entry points and implements rule 5 ○ (apps as security principals) and rule 2 ○

(open ecosystem): an app does not have to be vetted or pre-processed to run within the sandbox,

17 Available at https://developer.android.com/jetpack/androidx/releases/security

18 See the HAL definition at https://android-review.googlesource.com/c/platform/hardware/interfaces/+/1151485/30/identity/

1.0/IIdentityCredentialStore.hal.

---

## Page 18

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

18 Piqueras Jover, and Michael A. Specter

Fig. 1. Layers of sandboxing

because it is contained within its own UID and associated process isolation. Strengthening this

boundary can be achieved by a number of means such as:

• Access control: adding permission checks, increasing the granularity of permission checks,

or switching to safer defaults (e.g. default deny) to address the full range of threats [T.A1]–

[T.A7] and [T.D1]–[T.D2].

• Attack surface reduction: reducing the number of entry points, particularly [T.A1], [T.A2],

[T.A7], and [T.A8].

• Containment: isolating and de-privileging components, particularly ones that handle un-

trusted content as in [T.A3] and [T.D2].

• Architectural decomposition: breaking privileged processes into less privileged components

and applying attack surface reduction for [T.A2]–[T.A8] and [T.D2], i.e. the principle of

least privilege.

• Separation of concerns: avoiding duplication of functionality.

In this section we describe the various sandboxing and access control mechanisms used on

Android on different layers and how they improve the overall security posture. Figure 1 summarizes

the multiple layers of sandboxing above and below the Linux kernel.

4.3.1 Access control. Android uses three distinct permission mechanisms to perform access control:

• Discretionary Access Control (DAC): Apps run within their associated UNIX user ID

(UID). App processes may grant or deny access to resources that are owned by their UID, by

modifying permissions on the object (e.g., granting world read access) or by passing a handle

to the object over IPC. On Android this is implemented using UNIX-style permissions that

are enforced by the kernel. Processes running as the root user often have broad authority

to override UNIX permissions of any other UID (subject to MAC permissions).

• Mandatory Access Control (MAC): The system has a security policy that dictates what

actions are allowed. Only actions explicitly granted by policy are allowed. On Android

this is implemented using SELinux [154] and primarily enforced by the kernel. Android

makes extensive use of SELinux to protect system components and assert security model

requirements during compatibility testing. SELinux based MAC supports enforcing security

---

## Page 19

The Android Platform Security Model (2023) 19

boundaries even between processes running with the same UID, and therefore offers finer

granularity of isolation.

• Android permissions add higher-level semantic permissions (such as location or camera

access) that are granted to UIDs, as well as URI permission grants to provide the core

mechanism for fine-grained access control, allowing an app to grant selective access to

pieces of data it controls. Enforcement is primarily done in userspace by the data/service

provider (with notable exceptions such as INTERNET ). Permissions are defined statically

in an app’s AndroidManifest.xml [26]. As Android permissions are the most direct user-

visible component of the access control elements, we describe them in more detail in the

following Section 4.3.2.

Each of the three permission mechanisms roughly aligns with one of the three parties of the multi-

party authorization (rule 1 ○ ). The platform utilizes MAC, apps use DAC, and users authorize by

granting Android permissions. Note that permissions are not intended to be a complete mechanism

for obtaining consent in the legal sense, but a technical measure to enforce auditability and control.

It is up to the app developer processing personal user data to meet applicable legal requirements.

4.3.2 Android permissions. In the early development of smartphones, protection from apps was

largely seen as a security issue. The two common approaches being used were requiring that apps

be signed by an entity that is vouching for the safety of those apps or prompting the user at runtime

for the capabilities that the app needs. Since Android is an open platform that allows native code,

relying on protection from an external entity was not viable; at the same time, implementations

that prompted for every potentially unsafe operation may lead to a large number of confusing

prompts to the user and quick user prompt-fatigue.

Android initially took an alternative approach of using install-time permissions. In this model,

the user is shown the capabilities that an application will be granted prior to installing it, so they

can look holistically at what the app will be able to do on their device and decide if that makes sense

for what it claims to be. This worked fairly well in the initial mobile world of small, targeted apps:

these apps tended to do a very focused thing (such as a contact manager, a game, a music player,

etc.) and would stand out if they needed other capabilities that didn’t match their functionality.

Over time, two changes happened: First, mobile applications became increasingly complex with

a growing number of secondary features, leading to increasing numbers of install-time permissions

for features a particular person may never use, and for which they were not sufficiently equipped to

make such a decision at installation time (cf. [87, 88, 144, 181]). Second, privacy became a growing

concern for operating systems, resulting in a smaller set of capabilities revolving around the user’s

personal information that are of particular interest.

Privacy changes the user experience with applications from “Is this app safe for me to install?”

to “I want to decide what of my personal information this app gets access to based on what I am

doing with it.” As a result of these changes in application behavior and user needs, Android 6.0

re-arranged its existing raw permissions from a security-oriented organization to privacy-oriented.

This involved two major changes: (1) demoting pure security permissions to be invisible to the

user and used only for auditing of applications; and (2) identifying a small set of types of clearly

identifiable user information (such as location, contacts, camera) that the remaining permissions

can be organized under and introducing runtime prompts the application must perform when

needed for the user to allow that access.

A further refinement in Android permissions was introduced with Android 10 in the form of

non-binary, context dependent permissions: in addition to Allow and Deny , some permissions

(particularly location, and starting with Android 11 others like camera and microphone) can now

be set to Allow only while using the app . This third state only grants the permission when an app

---

## Page 20

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

20 Piqueras Jover, and Michael A. Specter

is in the foreground, i.e. when it either has a visible activity or runs a foreground service with

permanent notification [68]. Android 11 extended this direction with one-time permissions that

are granted until the app loses its foreground state.

At a high level Android permissions fall into one of five classes in increasing order of severity,

whose availability is defined by their protectionLevel attribute [27] with two parts (the protection

level itself and a number of optional flags):

(1) Audit-only permissions : These are install time permissions with protection level normal

that are mostly related to security boundaries for apps and less relevant to user privacy

decision, and which are thus granted automatically at install time. They are primarily used

for auditability of app behavior.

(2) Runtime permissions : These are permissions with protection level dangerous and apps must

both declare them in their manifest as well as request users grant them during use. These

permissions are guarding commonly used sensitive user data, and depending on how critical

they are for the current functioning of an application, different strategies for requesting

them are recommended [22]. While runtime permissions are fairly fine-grained to support

auditing and enforcement in-depth, they are grouped into logical permissions using the

permissionGroup attribute. When requesting runtime permissions, the group appears as a

single permission to avoid over-prompting.

(3) Special permissions : For resources that are either considered higher risk than those protected

by runtime permissions or that are otherwise special cases, there exists a separate class of

permissions with much higher granting friction than the permission dialogs for runtime

permissions. In order for a user to allow an application to use a special access permission,

the user must go to settings and manually grant the permission to the application. Specific

examples to special access permissions are device admin, notification listeners, unrestricted

network data access, or—critically—installing other packages. While the particular special

permissions differ significantly, a commonality is that they are either niche use cases and/or

too complicated to present as a runtime permission in the sense that they are not gating

access to some clear pieces of personal data that users can directly relate to.

(4) Privileged permissions : These permissions are for pre-installed applications only and allow

privileged actions such as modifying secure settings or carrier billing. They typically cannot

be granted by users during run-time but OEMs grant them by allowlisting the privileged

permissions for individual apps [38] in the system image.

Privileged protection level permissions are usually coupled with the signature level.

(5) Signature permissions : These permissions with protection level signature are only available

to components signed with the same key as the component which declares the permission

(i.e., the platform or an application) — which is the platform signing key for platform per-

missions. They are intended to guard internal or highly privileged actions (e.g. configuring

the network interfaces) and are granted at install time if the application is allowed to use

them.

Additionally, there are a number of protection flags that modify the grantability of permissions.

For example, the BLUETOOTH_PRIVILEGED permission has a protectionLevel of “ signature or

privileged ”, with the privileged flag allowing privileged applications to be granted the permis-

sion (even if they are not signed with the platform key).

4.3.3 Application sandbox. Android’s original DAC application sandbox separated apps from each

other and the system by providing each application with a unique UID and a directory owned

by the app. This approach was quite different from the traditional desktop approach of running

---

## Page 21

The Android Platform Security Model (2023) 21

applications using the UID of the physical user. The unique per-app UID simplifies permission

checking and eliminates per-process ID (PID) checks, which are often prone to race conditions.

Permissions granted to an app are stored in a centralized location ( /data/system/packages.xml )

to be queried by other services. For example, when an app requests location from the location

service, the location service queries the permissions service to see if the requesting UID has been

granted the location permission.

Starting with Android 4, UIDs are also used for separating multiple physical device users. As

the Linux kernel only supports a single numeric range for UID values, device users and profiles

are separated through a larger offset ( AID_USER_OFFSET=100000 as defined in AOSP source 19 ) and

apps installed for each user are assigned UIDs in a defined range (from AID_APP_START=10000

to AID_APP_END=19999 ) relative to the device user offset. This combination is referred to as the

Android ID (AID).

Users and profiles. Android allows device sharing through the concept of separate users 20 , gener-

ally mapping to different people using the device. Users inherently do not change anything about

the Android security model: the main security principal is the app sandbox, and access controls are

enforced at that level. Users act as a logical grouping of app sandboxes 21 , guarded by a separate

lock screen (and corresponding key), and treated appropriately by system services. Generally, the

system enforces a few additional security properties on top of the regular app sandbox for apps in

separate users:

• Different users are separated in the system UI. Apps running on behalf of one user are not

able to display alongside apps running on behalf of another user.

• Apps running in different users act as if they run on separate devices: communication

between apps running in different users is not possible, and apps running in different users

are not visible to each other.

A profile , most commonly known in the form of a work profile, is a special case of a user, intended

for separation of different personas belonging to the same person. Contrary to normal users, profiles

are presented directly alongside each other. They share the same system UI, including the launcher,

the notification stream, and most device preferences. A secondary profile can optionally be accessed

directly after unlocking the primary profile, while still having separate storage encryption keys.

Interaction between different profiles is always mediated by the device user:

• Direct communication between two instances of the same app running in separate profiles

is gated by user opt-in.

• Direct communication between different apps running in separate profiles is not possible.

• The device user can explicitly and deliberately share data between profiles by using the

share sheet.

Because of these strong data separation guarantees, enterprise policies are applied only on a

per-profile (per-user) basis. The only exceptions to this are cases that improve the security of the

device as a whole, such as defining a maximum screen timeout or network security requirements.

Historical development. The UID/AID sandbox laid the groundwork and is still the primary

enforcement mechanism that separates apps from each other. It has proven to be a solid foundation

19 See system/core/include/private/android_filesystem_config.h in the AOSP source tree.

20 The term “user” is somewhat overloaded in Android. It can be used to either refer to the person that is using the device, to

the app sandbox (implemented as a Linux user), or to user separation on the device as explained in this section. While the

rest of this paper uses the term to refer to the person using the device, this section uses it to refer to user separation on the

device, calling the person the “device user”.

21 In fact, this is exactly how user separation is implemented in Android: “users” are defined by ranges of UIDs for their apps.

---

## Page 22

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

22 Piqueras Jover, and Michael A. Specter

upon which to add additional sandbox restrictions. However, there are some limitations based

on the traditional UNIX UID model: Processes running as root were essentially unsandboxed

and possessed extensive power to manipulate the system, apps, and private app data. Likewise,

processes running as the system UID were exempt from Android permission checks and permitted

to perform many privileged operations. The use of DAC meant that apps and system processes

could override safe defaults and were more susceptible to dangerous behavior, such as symlink

following or leaking files/data across security boundaries via IPC or fork / exec . Additionally, DAC

mechanisms can only apply to files on file systems that support access controls lists (respectively

simple UNIX access bits). The main implication is that the FAT family of file systems, which is

still commonly used on extended storage such as (micro-) SD cards or media connected through

USB, does not directly support applying DAC. On Android, each app has a well-known directory

on external storage devices, where the package name of the app is included into the path (e.g.

/sdcard/Android/data/com.example ). Since the OS already maintains a mapping from package

name to UID, it can assign UID ownership to all files in these well-known directories, effectively

creating a DAC on a filesystem that doesn’t natively support it. From Android 4.4 to Android 7,

this mapping was implemented through FUSE, while Android 8.0 and later implement an in-kernel

sdcardfs for better performance. Both are equivalent in maintaining the mapping of app UIDs

to implement effective DAC. Android 10 introduced scoped storage , which further limits access to

external storage by allowing apps to access only their own external directory path and the media

files created by themselves in the shared media store.

The primary UID sandbox limitations have been mitigated in a number of ways over subsequent

releases, especially through the addition of MAC policies with SELinux in enforcing mode starting

with Android 5, but also including many other mechanisms such as attack surface reduction (cf.

Tables 2 and 3). In addition to SELinux, seccomp filters complement the MAC policy on a different

level of syscall granularity. While the Chrome app is currently the main user of fine-grained seccomp

filters, others can also use them to internally minimize attack surface for their components.

Another particular example for the interplay between DAC and MAC policies and changes based

on lessons learned are the more recent restrictions to ioctl , /proc , and /sys since Android 7.

As described more generally in Section 4.1, limiting access to such internal interfaces improves

app compatibility between platform versions and supports easier internal refactoring. For these

kernel interfaces, restricting access had another benefit towards user privacy: while few apps used

these kernel interfaces for legitimate purposes that could not be fulfilled with existing Android

APIs, they were also abused by other apps for side-channel attacks [71, 142, 155, 169] on data not

otherwise accessible through their lack of required Android permissions (e.g. network hardware

MAC addresses). Restricting access to these interfaces to follow an allow- instead of block-list

approach is therefore a logical development in line with the defense-in-depth principle.

Rooting, as defined above, has the main aim of enabling certain apps and their processes to break

out of this application sandbox in the sense of granting “root” user privileges [101], which override

the DAC rules (but not automatically MAC policies, which led to extended rooting schemes with

processes intentionally exempt from MAC restrictions). Malware may try to apply these rooting

approaches through temporary or permanent exploits and therefore bypass the application sandbox.

4.3.4 Sandboxing app SDKs. Generally, libraries that are embedded by an app are considered to

be within the app’s security boundary by the platform. Indeed, they are part of the app’s code,

signed by the app developer. One exception to this is the ads SDK runtime, introduced as part of

Android 13. The ads SDK runtime allows an app to load code from third-party libraries, called

“SDKs”, in a secondary bound application sandbox with a separate UID. These third-party libraries

---

## Page 23

The Android Platform Security Model (2023) 23

Threats

Release Improvement

Mitigated

1.0 Core app sandboxing model defined, based on kernel UID separation [T.A2][T.A5]

[T.A6][T.A7]

| 4.1 | Isolated process [21]: Apps may run services in a process with no | [T.A3] access |
| --- | --- | --- |
| Android permissions and access to only two binder services. For | to | [T.N1] |

example, the Chrome browser runs its renderer in an isolated process [T.A2][T.A5]

for untrusted web content. [T.A6][T.A7]

5.x SELinux enabled for all userspace processes, significantly improving [T.A7][T.D2]

the separation between apps and system processes. Boundaries be-

tween apps are still primarily enforced via UID sandbox. This also

increased the auditability of policy, supporting analysis of security

requirements during compatibility testing.

6.x SELinux restrictions on ioctl : 59% of all app reachable kernel vul- [T.A7][T.D2]

nerabilities were through the ioctl() syscall, and these restrictions

limited the reachability of kernel vulnerabilities from user space

code [171, 172].

6.x Removal of app access to debugfs (9% of all app-reachable kernel [T.A7][T.D2]

vulnerabilities).

7.x hidepid=2 : Remove /proc/<pid> side channel used to infer when [T.A4]

apps were started.

7.x perf-event-hardening (11% of app reachable kernel vulnerabilities [T.A7]

were reached via perf_event_open() ).

| 8.x | All apps run with a | seccomp | filter, reducing kernel attack surface. | [T.A7][T.D2] |
| --- | --- | --- | --- | --- |
| 9.0 | Per-app SELinux sandbox (for apps with | targetSdkVersion=P | or | [T.A2][T.A4] |

greater).

Table 2. General Application sandboxing improvements in Android releases

are distributed as separate APKs, listed as dependencies in the app’s manifest, and loaded on request

by the platform at runtime.

Note that this does not change Android’s multi-party authorization model: it only introduces the

SDK 22 as its own security principal, further using the architectural decomposition and containment

strategies described above. Indeed, this is not very different from running the SDK as its own

separate app, bound to the main app, even if the SDKs are loaded by the platform on behalf of the

app. However, the ads SDK runtime environment introduces its own set of restrictions for ads that

are different from regular apps, including a separate SELinux policy that minimizes the ability for

fingerprinting and profiling, and a very limited set of permissions (i.e., audit-only permissions,

which are of the protection level normal ). The platform also introduces restrictions on the ability

for separate sandboxes to interact across apps.

To enable use cases where the ads SDK would need to render part of the app, the platform allows

the app to designate an area within its own view hierarchy in which the SDK is allowed to remotely

render content. The composition of that content is entirely done by the platform, meaning that the

app has no visibility into (or control over) the SDK’s View s, and vice versa.

22 Or, technically, the union of all SDKs for a single app, as we will explain later.

---

## Page 24

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

| 24 | Piqueras Jover, and Michael A. Specter |  |
| --- | --- | --- |
| Release | Improvement | Threats Mitigated |
| 5.x | Webview moved to an updatable APK, independent of a full | [T.A3] |

system update.

6.x Runtime permissions were introduced, which moved the re- [T.A1]

quest for dangerous permissions from install to first use.

6.x Multi-user support: SELinux categories were introduced for a [T.P4]

per-physical-user app sandbox.

6.x Safer defaults on private app data: App home directory moved [T.A2]

from readable by all users, to only the app user ( 0751 UNIX

permissions to 0700 ).

6.x Moving SYSTEM_ALERT_WINDOW, WRITE_SETTINGS, and [T.A1][T.A4]

CHANGE_NETWORK_STATE to special permission category.

| 7.x | OPA/MITM CA certificates are not trusted by default. | [T.N2] |  |  |
| --- | --- | --- | --- | --- |
| 7.x | Safer defaults on | /proc | filesystem access. | [T.A1][T.A4] |
| 8.x | Safer defaults on | /sys | filesystem access. | [T.A1][T.A4] |
| 8.x | Webviews for all apps move into the isolated process. | [T.A3] |  |  |
| 8.x | Apps must opt-in to use cleartext network traffic. | [T.N1] |  |  |
| 10 | Apps can only start a new activity with a visible window, in the | [T.A2][T.A3] |  |  |

foreground activity, or if more specific exceptions apply [49]. [T.A4][T.A7]

| 10 | File access on external storage is scoped to app-owned files. | [T.A1][T.A2] |
| --- | --- | --- |
| 10 | Reading clipboard data is only possible for the app that cur- | [T.A5] |

rently has input focus or is the default input method (e.g. key-

board) app.

10 /proc/net limitations and other side channel mitigations. [T.A1]

11 Legacy access of non-scoped external storage is no longer avail- [T.A1][T.A2]

able.

| 11-13 | Restricted access to the hardware MAC address [34]. | [T.D1] |
| --- | --- | --- |
| 12 | Official support for Rust in AOSP. | [T.A7][T.D2] |
| 12-13 | Restrictions on passthrough touches and occluding windows | [T.A6] |

to prevent Tapjacking attacks.

Table 3. App sandboxing that improved permissions, authorization limitations, and other improvements

With this setup, the platform and the app distribution mechanism can now reason about the app

and its libraries as two separate entities. This additional security boundary brings with it some

desirable properties to the app developer, to the SDK developers, and to users. For app developers,

the largest benefit stems from the fact that the libraries no longer have access to the memory and

private storage of the app (including, for example, its authentication tokens). Due to the way the

platform remotely renders content from the SDK into the app, the app developer can be certain that

the SDK is not able to access any other app content displayed inside its own view hierarchy. It is

also advantageous for the app developer to no longer be considered as the party that is responsible

for the SDK’s code, and that app stores can enforce policies for them as separate entities. As a side

---

## Page 25

The Android Platform Security Model (2023) 25

effect, the SDK runtime helps increase the apps’ stability by ensuring that SDK crashes do not crash

the corresponding app.

SDK developers benefit from the fact that their SDK can now be distributed, and thus updated,

separately from the app (as long as the API contract remains intact). To a lesser extent, they now

have some guarantees that code and memory is not susceptible to tampering by the app developer,

which is especially important for advertising SDKs that want to prevent abuse (e.g. programmatic

clicks).

Users have the benefit of being able to apply a separate set of privacy restrictions to the app

and the SDKs. For example, they can decide to allow the app to access their location, without

inadvertently giving the SDKs that capability as well. As a side effect, the user also benefits from

decreased storage usage, as multiple apps depending on the same SDK can share a dependency on

the same APK.

Note that there is no security boundary between SDKs for the same app . This is a deliberate

tradeoff: while separating every SDK into its own process would provide many additional security

benefits (e.g. preventing different SDKs from inspecting each other’s memory), it would also have

an unreasonable memory overhead. Because of this, the SDK runtime implements a few in-process

mitigations, designed to ensure that SDK developers don’t accidentally handle each others’ resources.

These mitigations include a separate classloader, Context object, and storage location for each SDK,

and restrictions on executing native code. These mitigations are intended to prevent developers

from accidentally sharing resources, and to facilitate policy enforcement on a per-SDK basis. As

mentioned before, Android intentionally does not rely on in-process compartmentalization to

enforce security boundaries.

The platform restricts the ability for SDKs to communicate across different SDK runtimes, or for

them to communicate with apps other than the one they’re loaded by. Note that communication

between the app and its SDKs is not restricted in any way, and is enabled through a generic

communication channel. Generally, collusion between app and SDK developer is out of scope, as

the app developer can just as easily embed the SDK directly, or share a unique ID with the SDK

allowing them to communicate out-of-band.

4.3.5 Sandboxing system processes. In addition to the application sandbox, Android launched with

a limited set of UID sandboxes for system processes. Notably, Android’s architects recognized the

inherent risk of processing untrusted media content and so isolated the media frameworks into UID

AID_MEDIA , and this sandboxing has been strengthened from release to release with continuously

more fine-grained isolation [157]. Figure 2 gives an overview of the sandboxing and isolation

improvements for the media server and codecs. Other processes that warranted UID isolation

include the telephony stack, Wi-Fi, and Bluetooth (cf. Table 4).

4.3.6 Sandboxing specific private data processing. Android 12 introduced Private Compute Core

(PCC) as an isolated environment to maintain separation from apps while enabling users and devel-

opers to maintain control over their data [129]. Its main use case is to provide a safe environment

for deriving less sensitive, potentially pseudonymous (e.g. 𝑘 -anonymous) data from sensitive raw

ambient (sensor captured) or operating system level data.

The whole PCC is sandboxed from Android system services and other apps through framework

APIs provided by the AOSP base, and all data flowing into or out of PCC needs to go through these

open components. Apps running within this PCC sandbox, such as the Google-proprietary “Android

System Intelligence” for processing ambient and other data for on-device machine learning 23 , are

23 Particular services as of Android 12 include Google “Live Caption”, “Now Playing”, “Smart Reply”, and “Screen attention”,

among others.

---

## Page 26

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

26 Piqueras Jover, and Michael A. Specter

Fig. 2. Changes to mediaserver and codec sandboxing from Android 6 to Android 10

prevented from directly accessing any other resources except through the provided PCC APIs. This

includes network access; components running in PCC do not receive the INTERNET permission and

can therefore not open any network sockets. Any communication to external services is required

to go through another open source layer called “Private Compute Services” (PCS) 24 , which is

distributed as an APK and includes standard support for federated learning and analytics, private

information retrieval (PIR) using homomorphic encryption, and secure download of pre-trained

ML models.

While basic data flow is restricted by Android platform permissions available to PCC apps, more

granular control can be implemented by these applications themselves (e.g. for deleting stored data)

and/or additional Android security/privacy controls such as camera, microphone, and other sensor

toggles. All such specific PCC data flows are expected to conform to the multi-party authorization

model. One example demonstrating this granular authorization is the “Content Capture API” 25

introduced in Android 11: it respects developer authorization through the FLAG_SECURE opt-out

flag 26 and user authorization through the PCC privacy settings implemented in AOSP.

For further details on high-level designs and example use cases of PCC, we refer to the separate

whitepaper [129]. PCC applications can benefit from additional confidentiality guarantees for data

storage and processing in protected virtual machines (see Section 4.3.9) even under the assumption

of a compromised Android user space when the particular implementation uses such pVMs for

sandboxing.

24 https://github.com/google/private-compute-services/

25 https://developer.android.com/reference/android/view/contentcapture/ContentCaptureManager

26 https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAGSECURE

---

## Page 27

| The Android Platform Security Model (2023) | 27 |  |
| --- | --- | --- |
| Release | Improvement | Threats Mitigated |
| 4.4 | SELinux in enforcing mode: MAC for 4 root processes | [T.A1][T.A7][T.D2] |

installd , netd , vold , zygote .

| 5.x | SELinux: MAC for all userspace processes. | [T.A1][T.A7] |  |
| --- | --- | --- | --- |
| 6.x | SELinux: MAC for all processes. |  |  |
| 7.x | Architectural decomposition of mediaserver. | [T.A1][T.A7][T.D2] |  |
| 7.x | ioctl | system call restrictions for system components [171]. | [T.A1][T.A7][T.D2] |
| 8.x | Treble | Architectural decomposition: Moved HALs (Hardware | [T.A1][T.A7][T.D2] |

Abstraction Layer components) into separate processes, re-

duced permissions, restrict access to hardware drivers [67, 173].

10 Software codecs (the source of approximately 80% of the crit- [T.A7][T.D2]

ical/high severity vulnerabilities in media components) were

moved into a constrained sandbox.

10 Bounds Sanitizer (BoundSan): Missing or incorrect bounds [T.A7][T.D2]

checks on arrays accounted for 34% of Android’s userspace

security vulnerabilities. Clang’s BoundSan adds bounds check-

ing on arrays when the size can be determined at compile time;

enabled across the Bluetooth stack and in 11 software codecs.

10 Integer Overflow Sanitizer (IOSAN): The process of applying [T.A7][T.D2]

IOSAN to the media frameworks began in Android 7.0 and was

completed in Android 10.

10 Scudo included as a dynamic heap allocator designed to be [T.A7][T.D2]

resilient against heap related vulnerabilities.

10 Shadow Call Stack (SCS, protecting the call graph backwards [T.A7][T.D2]

edge by protecting return addresses) enabled for Bluetooth.

| 12 | Shadow Call Stack enabled for NFC. | [T.A7][T.D2] |
| --- | --- | --- |
| 12 | Memory Tagging Extensions (MTE) [52] software support | [T.A5][T.A6] |
| added | [T.A7][T.D2] |  |
| 13 | Boundsan and IOSAN: Compiler-based sanitizers enabled in | [T.A7][T.D2] |

critical attack surface of the cellular baseband in some devices.

14 Branch Target Identification (BTI) enabled by default on sup- [T.A7][T.D2]

ported hardware, providing forward-edge protection by pre-

venting execution of instructions which are not intended

branch targets.

14 Return Pointer Authentication (PAC-RET) enabled by default [T.A7][T.D2]

on supported hardware. This provides backward-edge protec-

tion by signing the return address stored on the stack.

Table 4. System sandboxing improvements in Android releases

4.3.7 Sandboxing the kernel. Security hardening efforts in Android userspace have increasingly

made the kernel a more attractive target for privilege escalation attacks [172]. Hardware drivers

provided by System on a Chip (SoC) vendors accounted for the vast majority of kernel vulnerabilities

---

## Page 28

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

28 Piqueras Jover, and Michael A. Specter

on Android in 2018 [176]. Reducing app and system access to these drivers was described above,

but kernel-level drivers cannot be sandboxed within the kernel themselves, as Linux still is a

monolithic kernel (as opposed to microkernel approaches). For this reason and others, significant

improvements have been made to mitigate exploitation of weaknesses in all code running within

kernel mode, including the core Linux kernel components and vendor drivers (cf. Table 5).

| Release | Improvement | Threats Mitigated |
| --- | --- | --- |
| 5.x | Privileged eXecute Never (PXN) [182]: Disallow the kernel from | [T.A7][T.D2] |

executing code in userspace memory. Prevents return-to-user

(ret2usr) style attacks.

6.x Kernel threads moved into SELinux enforcing mode, limiting [T.A7][T.D2]

kernel access to userspace files.

8.x Privileged Access Never (PAN) and PAN emulation: Prevent the [T.A7][T.D2]

kernel from accessing any userspace memory without going

through hardened copy-*-user() functions [164].

9.0 Control Flow Integrity (CFI): Ensures that front-edge control [T.A7][T.D2]

flow stays within a precomputed graph of allowed function

calls [165].

10 Shadow Call Stack (SCS): Protects the backwards edge of the [T.A7][T.D2]

call graph by protecting return addresses [166].

11 Require latest long-term support (LTS) kernel with security [T.A7][T.P1]

updates and bug fixes [13].

12 Bounds Sanitizer: The local-bounds part of Bounds Sanitizer is [T.A7][T.D2]

enabled by default in the Android Generic Kernel Image (GKI).

This provides runtime detection of out of bounds accesses when

the allocation size is determinable at compile time.

14 Kernel Control Flow Integrity (KCFI): Providing similar protec- [T.A7][T.D2]

tion to CFI, KCFI has been enabled as part of the Android GKI.

Table 5. Kernel sandboxing improvements in Android releases

4.3.8 Sandboxing below the kernel. In addition to the kernel, the trusted computing base (TCB)

on Android devices starts with the bootloader, which is typically split into multiple stages, and

implicitly includes other components below the kernel, such as the trusted execution environment

(TEE), hardware drivers, and userspace components init , ueventd , and vold [40]. It is clear that

the sum of all these creates sufficient complexity that, given current state of the art, we have to

assume bugs in some of them. For highly sensitive use cases, even the mitigations against kernel

and system process bugs described above may not provide sufficient assurance against potential

vulnerabilities.

Therefore, we explicitly consider the possibility of a kernel or other TCB component failure

as part of the threat model for some select scenarios. Such failures explicitly include compromise

e.g. through directly attacking some kernel interfaces based on physical access in [T.P1], [T.P3],

and [T.P4] or chaining together multiple bugs from user space code to reach kernel surfaces in

[T.A7]; misconfiguration e.g. with incorrect or overly permissive SELinux policies [69]; or bypass

e.g. by modifying the boot chain to boot a different kernel with deactivated security policies. To be

---

## Page 29

The Android Platform Security Model (2023) 29

clear, with a compromised kernel or other TCB parts, Android no longer meets the compatibility

requirements and many of the security and privacy assurances for users and apps no longer hold.

However, we can still defend against some threats even under this assumption:

• Keymint (née Keymaster) implements the Android keystore in TEE to guard cryptographic

key storage and use in the case of a run-time kernel compromise [32]. That is, even with

a fully compromised kernel, an attacker cannot read key material stored in Keymint 27 .

Apps can explicitly request keys to be stored in Keymint, i.e. to be hardware-bound, to

be only accessible after user authentication (which is tied to Gatekeeper/Weaver), and/or

request attestation certificates to verify these key properties [30], allowing verification of

compatibility in terms of rule 3 ○ (compatibility).

• Strongbox , specified starting with Android 9.0, implements the Android keystore in sepa-

rate tamper resistant hardware (TRH) for even better isolation. This mitigates [T.P2] and

[T.P3] against strong adversaries, e.g. against cold boot memory attacks [96] or hardware

bugs such as Spectre/Meltdown [112, 123], Rowhammer [66, 170], or Clkscrew [159] that

allow privilege escalation even from kernel to TEE. From a hardware perspective, the main

application processor (AP) will always have a significantly larger attack surface than ded-

icated secure co-processor. Adding a separate TRH affords another sandboxing layer of

defense in depth.

The Google Pixel 3 was the first device to support Strongbox with a dedicated TRH (Titan M

[185]), and other OEM devices have since started to implement it, often using standard

secure elements that have been available on Android devices for NFC payment and other

use cases.

Note that only storing and using keys in TEE or TRH does not completely solve the

problem of making them unusable under the assumption of a kernel compromise: if

an attacker gains access to the low-level interfaces for communicating directly with

Keymint or Strongbox, they can use it as an oracle for cryptographic operations that

require the private key. This is the reason why keys can be authentication bound and/or

require user presence verification, e.g. by pushing a hardware button that is detectable by

the TRH to assure that keys are not used in the background without user authorization.

• Gatekeeper implements verification of user lock screen factors (PIN/password/pattern) in

TEE and, upon successful authentication, communicates this to Keymint for releasing access

to authentication bound keys [31]. Weaver implements the same functionality in TRH

and communicates with Strongbox. Specified for Android 9.0 and initially implemented

on the Google Pixel 2 and newer phones, we also add a property called Insider Attack

Resistance (IAR): without knowledge of the user’s lock screen factor, an upgrade to the

Weaver/Strongbox code running in TRH will wipe the secrets used for on-device encryp-

tion [132, 183]. That is, even with access to internal code signing keys, existing data cannot

be exfiltrated without the user’s cooperation, directly addressing threat [T.A8].

• Protected Confirmation , also introduced with Android 9.0 [45], partially mitigates [T.A4]

and [T.A6]. In its current scope, apps can tie usage of a key stored in Keymint or Strongbox

to the user confirming that they have seen a message displayed on the screen by pushing

a physical button. Upon confirmation, the app receives a hash of the displayed message,

which can be used to remotely verify that a user has confirmed the message. By controlling

the screen output through TEE when protected confirmation is requested by an app, even

27 Note: This assumes that hardware itself is still trustworthy. Side-channel attacks such as [116] are currently out of scope

of this (software) platform security model, but influence some design decisions on the system level, e.g. to favor dedicated

TRH over on-chip security partitioning.

---

## Page 30

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

30 Piqueras Jover, and Michael A. Specter

a full kernel compromise (without user cooperation) cannot lead to creating these signed

confirmations.

4.3.9 Sandboxing other kernels. Android has mandated the existence of a TEE since version 6.0 [19,

Android 6.0, section 7.3.10.] in order to provide hardware-assisted isolation that has a low attack

surface and is not dependent on the Linux kernel to uphold its security assurances (cf. Section 4.3.8).

Unfortunately, as more and more functionality has moved into the TEE, its attack surface has

increased over time, partially undermining the reason for its existence. A particular concern in

terms of attack surface is that code running in the TEE typically has access to all physical RAM ,

including the Android “normal world” side, and thus vulnerabilities in any of the TEE kernel or

apps result in significantly increased risk.

While some hardware access capabilities still require the TEE in its current form, many TEE apps

do not require this level of privilege and could be compartmentalized into other domains. Much

like it has been done in userspace, ideally we could split the TEE into multiple lower-privilege

TEEs, but that is not currently feasible due to hardware constraints in widely deployed CPUs 28 .

The Android Virtualization Framework [24] was introduced in Android 13 to take advantage of

the separation capabilities that could be provided by a hypervisor outside the TEE in the ARM

architecture. Not only is ARM EL2 already widely deployed across the Android ecosystem, but it

also allows to provide multiple distinct isolation units, solving the scaling problem that we currently

have with TEE-based solutions.

The AOSP reference hypervisor implementation, pKVM, is based on the Linux kernel KVM

hypervisor, but with some important improvements. During early boot, the hypervisor code is split

out of the kernel, which initially runs at EL1, and is installed into EL2. Despite being a part of the

Linux kernel codebase, the component that is installed in EL2 is small 29 , an intentional decision to

harden the hypervisor security by limiting its complexity and attack surface. Unlike normal KVM,

pKVM enforces separation between all VMs, including the host role which is filled by the Android

VM. One major advantage of this design is that the hypervisor code running in EL2 minimizes

hardware dependent driver code, as early hardware initialization is performed by the Linux kernel

code before splitting control between EL2 and EL1, further reducing the hypervisor attack surface.

Note that pKVM in Android 14 delegates scheduling to the standard Android Linux kernel. Denial

of service of virtual machines from a manipulated Android kernel point of view is therefore outside

the threat model of AVF in its current implementation. Dynamic memory management, on the other

hand, is a key piece of the security guarantees provided by pKVM, providing isolation without the

need for physically contiguous carve-outs in physical RAM. To this end, pKVM supports atomic

state changes for virtual machines, including donating pages from the host (Android) to guests

(application VMs) and vice versa and explicit page sharing between host and guests or the TEE. To

minimize attack surface in the early initialization code running within each protected VM (pVM),

the AVF reference implementation of the pVM firmware has been rewritten in Android 14; initially

based on the U-Boot bootloader, the new firmware is written in Rust to benefit from memory safety

guarantees [179]

The system code in Java, including system server and boot classpath, are normally compiled on

the OEM’s server and protected by Verified Boot with a signature. Since Android 10, parts of the

operating system can be updated independently as Modular System Components 30 , meaning that

some of this compilation, including most Java components, need to be compiled on-device. In order

28 Hypervisor based separation in the ARM secure world, i.e. SEL2, is not yet widely available in the Android ecosystem.

29 The open source pKVM hypervisor is smaller than all currently used TEE kernels including the AOSP reference imple-

mentation in the form of Trusty [42].

30 https://source.android.com/docs/core/ota/modular-system

---

## Page 31

The Android Platform Security Model (2023) 31

to ensure the same security properties and prevent persistent attacks, this local compilation needs

to happen in a secure environment.

Before AVF/pKVM, the compilation could only happen at early boot when the device had only

run trusted code protected by Verified Boot. The output was then signed with a key restricted to

early boot to ensure compilation could be skipped in subsequent boots. However, this compilation

process still significantly slowed down the first boot after the Modular System update.

AVF/pKVM enables Isolated Compilation . It allows the compilation to happen safely in the

background (even if Android is significantly compromised) after the Modular System component

has been staged. The isolated environment allows running only trusted code that accepts only

trusted input and flags. The compiled artifacts are signed, together with the information of the

compilation context (e.g., version, flags, etc.). This allows even the first post-update Android boot

to skip the compilation step after checking these artifacts.

4.3.10 Sandboxing firmware on other processors. Securing the platform requires going beyond

the confines of the Application Processor (AP). Android’s defense-in-depth strategy, as well as

the scope of this paper, also applies to the firmware running on bare-metal environments in the

micro-controllers that perform various specialized tasks, such as security functions, image and

video processing, and cellular communication. Separation of concerns and clear interfaces to

communicate between the different processors in the form of HALs (specified in AIDL) are the

primary means of sandboxing on this level.

Many of the exploit mitigations described in Section 4.6 are increasingly applied to non-AP

processors as well. While most of these firmware code bases are chipset/ODM/OEM specific, the

Android platform supports applying sandboxing and exploit mitigation methods initially developed

for AP code on lower level firmware, e.g. through the systematic application of compiler-based

sanitizers in connectivity firmware (Table 4), and with explicit support for memory-safe languages

like Rust [106].

4.4 Encryption of data at rest

A second element of enforcing the security model, particularly rules 1 ○ (multi-party authorization)

and 3 ○ (compatibility), is required when the main system kernel is not running or is bypassed (e.g.

by reading directly from non-volatile storage).

Full Disk Encryption (FDE) uses a credential protected key to encrypt the entire user data

partition. FDE was introduced in Android 5.0, and while effective against [T.P2], it had a number of

shortcomings. Core device functionality, such as incoming calls, accessibility services, and alarms,

were inaccessible until password entry 31 . Multi-user support introduced in Android 6.0 still required

the password of the primary user before disk access.

These shortcomings were mitigated by File Based Encryption (FBE), introduced in Android 7.0.

On devices with TEE or TRH, all keys are derived within these secure environments, entangling the

user knowledge factor with hardware-bound random numbers that are inaccessible to the Android

kernel and components above. FBE allows individual files to be tied to the credentials of different

users, cryptographically protecting per-user data on shared devices [T.P4]. Devices with FBE also

support a feature called Direct Boot which enables access to emergency dialer, accessibility services,

alarms, and receiving calls all before the user inputs their credentials.

Android 10 introduced support for Adiantium [74], a new wide-block cipher mode based on

AES, ChaCha, and Poly1305 to enable full device encryption without hardware AES acceleration

support. While this does not change encryption of data at rest for devices with existing AES support,

31 Note that very limited functionality included only an emergency dialer for outgoing emergency calls, as this did not

depend on availability of the data partition.

---

## Page 32

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

32 Piqueras Jover, and Michael A. Specter

lower-end processors can now also encrypt all data without prohibitive performance impact. The

significant implication is that all devices shipping originally with Android 10 are required to encrypt

all data by default without any further exemptions, homogenizing the Android ecosystem in that

aspect.

Note that encryption of data at rest helps significantly with enforcing rule 4 ○ (safe reset), as

effectively wiping user data only requires to delete the master key material, which is much quicker

and not subject to the complexities of e.g. flash translation layer interactions.

4.5 Encryption of data in transit

Android assumes that all networks are hostile and could be injecting attacks or spying on traffic.

In order to ensure that network level adversaries do not bypass app data protections, Android

takes the stance that all network traffic should be end-to-end encrypted. Link level encryption

is insufficient. This primarily protects against [T.N1] and [T.N2]. However, this is not sufficient

protection against [T.N3] as certain types of user traffic over cellular networks (cf. Section 4.9) are

strictly only protected by link level encryption such as circuit-switched voice and Short Message

Service (SMS).

In addition to ensuring that connections use encryption, Android focuses heavily on ensuring

that the encryption is used correctly. While TLS options are secure by default, we have seen that it

is easy for developers to incorrectly customize TLS in a way that leaves their traffic vulnerable to

OPA/MITM [83, 84, 93]. Table 6 lists platform changes in terms of making network connections

safe by default, which have led to significant improvements of TLS usage in apps [62].

Release Improvement Threats Mitigated

6.x usesCleartextTraffic in manifest to prevent unintentional [T.N1][T.N2]

cleartext connections [63].

7.x Network security config [35] to declaratively specify TLS and [T.N1][T.N2]

cleartext settings on a per-domain or app-wide basis to cus-

tomize TLS connections.

9.0 DNS-over-TLS [111] to reduce sensitive data sent over cleartext [T.N1][T.N2]

and made apps opt-in to using cleartext traffic in their network

security config.

| 9.0 | TLS is the default for all connections [64]. | [T.N1][T.N2] |
| --- | --- | --- |
| 10 | MAC randomization enabled by default for client mode, SoftAP, | [T.P1][T.N1] |

and Wi-Fi Direct [37].

| 10 | TLS 1.3 support. | [T.N1][T.N2] |  |  |
| --- | --- | --- | --- | --- |
| 12 | Option to disable the 2G radio | 32 | [10]. | [T.N3] |
| 11-13 | DNS-over-HTTP/3 [130] introduced as part of Android 13, and | [T.N1][T.N2] |  |  |

added to older platform versions through a Modular System

Update

14 Option to reject null-ciphered cellular connections 33 . [T.N3]

Table 6. Network sandboxing improvements in Android releases

---

## Page 33

The Android Platform Security Model (2023) 33

4.6 Exploit mitigation

A robust security system should assume that software vulnerabilities exist and actively defends

against them. Historically, about 85% of security vulnerabilities on Android result from unsafe

memory access (cf. [113, slide 54]). While this section primarily describes mitigations against

memory unsafety ([T.P1-P4], [T.N2], [T.A1-A3,A7], [T.D2]) we note that the best defense is the

memory safety offered by languages such as Java, Kotlin, or Rust. Much of the Android framework

is written in Java, effectively defending large swathes of the OS from entire categories of security

bugs.

Android mandates the use of a number of mitigations including ASLR [61, 152], RWX memory

restrictions (e.g. 𝑊 ⊕ 𝑋 , cf. [151]), and buffer overflow protections, such as stack-protector for

the stack and allocator protections for the heap. Similar protections are mandated for Android

kernels [164].

In addition to the mitigations listed above, Android is selectively enabling new mitigations,

focusing first on code areas which are remotely reachable (e.g. the media frameworks [53]) or

have a history of high severity security vulnerabilities (e.g. the kernel). Android also strongly

recommends its ecosystem partners similar levels of hardening in over the air remotely reachable

firmware running on other processors within the SoC that perform various specialized tasks (e.g.

cellular communications) [106].

Android has pioneered the use of LLVM undefined behavior sanitizer (UBSAN) and other address

sanitizers [149] in production devices to protect against vulnerabilities in the media frameworks,

kernel, and other security sensitive components.

Android is also rolling out Control Flow Integrity (CFI) [165] in the kernel and security sensitive

userspace components including media, Bluetooth, Wi-Fi, NFC, and parsers [125] in a fine-grained

variant as implemented by current LLVM [163] that improves upon previous, coarse-grained

approaches that have been shown to be ineffective [76]. Starting with Android 10, the common

Android kernel as well as parts of the Bluetooth stack can additionally be protected against

backwards-edge exploitation through the use of Shadow Call Stack (SCS), again as implemented by

current LLVM [157] as the best trade-off between performance overhead and effectiveness [65].

Android 11 started auto-initializing memory in C/C++ code [160].

Android 12 introduced software support for Memory Tagging Extensions (MTE) [52], an ARM

CPU hardware implementation [150] of tagged memory. MTE marks each memory allocation/

deallocation with additional metadata (a “tag” to a memory location), which then can be associated

with pointers that reference that memory location. At runtime, the CPU checks that the pointer

and the metadata tags match on each load and store. Google Pixel 8, originally shipping with

Android 14, is the first device with MTE hardware support enabled and exposed to users as an

optional developer option.

To completely remove many of the memory unsafety bug classes at compile time, Android started

to include support for system components written in Rust instead of C/C++ in 2021 [175], and

Android 12 already featured official support for Rust as platform system programming language.

Android 13 was the first release in which more new code was written in memory safe languages

(Rust, Java, or Kotlin) than memory unsafe languages (C/C++). At the time of this writing, no

memory safety vulnerability has been been discovered in Android Rust code [174], indicating a

significant improvement in platform level mitigations for such bug classes. 34

These code and runtime safety mitigation methods work in tandem with isolation and contain-

ment mechanisms (cf. Tables 2 to 5 for added mitigations over time) to form many layers of defense;

even if one layer fails, other mechanisms aim to prevent a successful exploitation chain. Mitigation

34 Other (including logical) vulnerabilities often have lower impact and severity than memory safety vulnerabilities.

---

## Page 34

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

34 Piqueras Jover, and Michael A. Specter

mechanisms also help to uphold rules 2 ○ (open ecosystem) and 3 ○ (compatibility) without placing

additional assumptions on which languages apps are written in.

There are other types of exploits than apps directly trying to circumvent security controls of

the platform or other apps: malicious apps can try to mislead users through deceptive UI tactics

to either receive authorization grants against users’ interests (including tapjacking [41], the app

equivalent of clickjacking [92]) ([T.A4]–[T.A6], [T.D1]), existing legitimate apps can be repackaged

together with malicious code ([T.A1]–[T.A2]), or look-alike and similarly named apps could try to

get users to install them instead of other well-known apps. Such user deception is not only a problem

in the Android ecosystem but more generally of any UI-based interaction. As deception attacks

tend to develop and change quickly, platform mitigations are often too slow to roll out, making

dynamic blocking more effective. Within the Android ecosystem, mitigations against such kinds of

exploits are therefore based on multiple mechanisms, notably submission-time checks on Google

Play and on-device run-time checks with Google Play Protect. Nonetheless, platform security has

adapted over time to make certain classes of UI deception exploits harder or impossible, e.g. through

restricting SYSTEM_ALERT_WINDOW, background activity limitations, scoped external storage,

or occlusion / touch passthrough prevention (cf. Table 2).

4.7 System integrity

Finally, system (sometimes also referred to as device) integrity is an important defense against

attackers gaining a persistent foothold. AOSP has supported Verified Boot using the Linux kernel

dm-verity support since Android KitKat, providing strong integrity enforcement for the Trusted

Computing Base (TCB) and system components to implement rule 4 ○ (safe reset). Verified Boot [43]

has been mandated since Android Nougat (with an exemption granted to devices which cannot

perform AES crypto above 50MiB/sec. up to Android 8, but no exemptions starting with Android 9.0)

and makes modifications to the boot chain detectable by verifying the boot, TEE, and additional

vendor/OEM partitions, as well as performing on-access verification of blocks on the system

partition [46]. That is, attackers cannot permanently modify the TCB even after all previous layers

of defense have failed, in order to achieve a successful kernel compromise. Note that this assumes

the primary boot loader as root of trust to still be intact. As this is typically implemented in a ROM

mask in sufficiently simple code, critical bugs at that stage are less likely.

Additionally, rollback protection with hardware support (counters stored in tamper-proof persis-

tent storage, e.g. a separate TRH as used for Strongbox or enforced through RPMB as implemented

in a combination of TEE and eMMC controller [18]) prevents attacks from flashing a properly

signed but outdated system image that has known vulnerabilities and could be exploited. Finally,

the Verified Boot state is included in key attestation certificates (provided by Keymint/Strongbox) in

the deviceLocked and verifiedBootState fields, which can be verified by apps as well as passed

onto backend services to remotely verify boot integrity [44] and to support rule 3 ○ (compatibility).

Starting with Android 10, on devices supporting Android Verified Boot 35 version 2, the VBMeta

struct digest (a top-level hash over all parts) is included in key attestation certificates to support

firmware transparency. This is done by verifying that the digest matches that of a released firmware

image [46, 132]. In combination with server side validation, this can be used as a form of remote

system integrity attestation akin to PCR verification with trusted platform modules (TPMs). Integrity

of firmware for other CPUs (including, but not limited to, the various radio chipsets, the GPU,

touch screen controllers, etc.) is out of scope of AVB at the time of this writing, and is typically

handled by OEM-specific boot loaders.

35 AVB, the recommended default implementation for verifying the integrity of read-only partitions [46]

---

## Page 35

The Android Platform Security Model (2023) 35

4.7.1 Verification key hierarchy and updating. While the details for early boot stages are highly

dependent on the respective chipset hardware and low-level boot loaders, Android devices generally

use at least the following keys for verifying system integrity:

(1) The first (and potentially multiple intermediate) boot loader(s) is/are signed by a key K A

held by the hardware manufacturer and verified through a public key embedded in the

chipset ROM mask. This key cannot be changed.

(2) The (final) bootloader responsible for loading the Android Linux kernel is verified through

a key K B embedded in a previous bootloader. Updating this signing key is chipset specific,

but may be possible in the field by updating a previous, intermediate bootloader block.

Android 10 strongly recommends that this bootloader use the reference implementation

of Android Verified Boot [46] and VBMeta structs for verifying all read-only (e.g. system ,

vendor , etc.) partitions.

(3) A VBMeta signing key K C is either directly embedded in the final bootloader or retrieved

from a separate TRH to verify flash partitions before loading the kernel. AVB implemen-

tations may also allow a user-defined VBMeta signing key K ′

C to be set (typically in a

TEE or TRH) — in this case, the Verified Boot state will be set to YELLOW to indicate

that non-manufacturer keys were use to sign the partitions, but that verification with the

user-defined keys has still been performed correctly (see Figure 3).

Updating this key K C used to sign any partitions protected through AVB is supported

through the use of chained partitions in the VBMeta struct (resulting in partition-specific

signing keys K i

D for partition 𝑖 that are in turn signed by K C / K ′

C ), by updating the key used

to sign the VBMeta struct itself (through flashing a new version of the final bootloader in an

over-the-air update), or – in the case of user-defined keys – using direct physical access 36 .

(4) The digest(s) embedded in VBMeta struct(s) are used by the Android Linux kernel to verify

blocks within persistent, read-only partitions on-access using dm-verity (or for small

partitions, direct verification before loading them atomically into memory). Inside the

system partition, multiple public signing keys are used for different purposes, e.g. the

platform signing key mentioned in Section 4.3.1 or keys used to verify the download of

over-the-air (OTA) update packages before applying them. Those keys can be updated by

simply flashing a new system partition.

j

(5) All APKs are individually signed by the respective developer key K E for APK 𝑗 (some

may be signed by the platform signing key to be granted signature permissions for

those components), which in turn are stored on the system or data partition. Integrity of

updateable (system or user installed) apps is enforced via APK signing [47] and is checked

by Android’s PackageManager during installation and update. Every app is signed and

an update can only be installed if the new APK is signed with the same identity or by an

identity that was delegated by the original signer.

For run-time updateable apps, the APK Signature Scheme version 3 was introduced with

Android 9.0 to support rotation of these individual signing keys [47].

4.7.2 Integrity and authenticity of system images. To mitigate against leaks or insider attacks with

resulting control over firmware and system signing keys (questioning if the currently installed

factory image is genuine), public tamper-evident records of released versions such as transparency

logs can be used to clearly declare which system images were officially released for all users, and

therefore to make targeted attacks [T.A8] detectable. E.g., Google Pixel phone firmware has been

36 Google Pixel devices support this through fastboot flash avb_custom_key as documented online at https://source.

android.com/security/verifiedboot/device-state.

---

## Page 36

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

36 Piqueras Jover, and Michael A. Specter

Fig. 3. Verified Boot flow and different states: (YELLOW): warning screen for LOCKED devices with custom

root of trust set; (ORANGE): warning screen for UNLOCKED devices; (RED): warning screen for dm-verity

corruption or no valid OS found [23].

logged into the Pixel Binary Transparency Log since the release of Pixel 6, and this log can be used

to verify that a new firmware update has been created through the official processes and tied to the

version booted through verified boot [103].

4.8 Patching

Orthogonal to all the previous defense mechanisms, vulnerable code should be fixed to close

discovered holes in any of the layers. Regular patching can be seen as another layer of defense.

However, shipping updated code to the huge and diverse Android ecosystem is a challenge [162]

(which is one of the reasons for applying the defense in depth strategy).

Starting in August 2015, Android has publicly released a monthly security bulletin and patches

for security vulnerabilities reported to Google. To address ecosystem diversity, project Treble [186]

launched with Android 8.0, with a goal of reducing the time/cost of updating Android devices [128,

134] and implemented through decoupling of the main system image from hardware-dependent

chipset vendor/OEM customization. This modularization introduced a set of security-relevant

changes:

• The SELinux policy is no longer monolithic, but assembled at boot time from different

partitions (currently system and vendor ). Updating the policy for platform or hardware

components can therefore be done independently through changes within the relevant

partition [48, 67].

• Each of the new Hardware Abstraction Layer (HAL) components (mainly native daemons)

runs in its own sandbox and is permitted access to only the hardware driver it controls;

higher-level system processes accessing this hardware component are now limited to

accessing this HAL instead of directly interacting with the hardware driver [173].

As part of project Treble, approximately 20 HALs were moved out of the system server, including

the HALs for sensors, GPS, fingerprint, Wi-Fi, and more. Previously, a compromise in any of those

HALs would allow gaining privileged system permissions, but in Android 8.0, permissions are

---

## Page 37

The Android Platform Security Model (2023) 37

restricted to the subset needed by the specific HAL. Similarly, HALs for audio, camera, and DRM

have been moved out of audioserver , cameraserver , and drmserver respectively.

In 2018, the Android Enterprise Recommended program as well as general agreements with

OEMs added the requirement of 90-day guaranteed security updates [20].

Starting with Android 10, some core system components can be updated independently 37 through

the Google Play Store (or through a partner-provided OTA mechanism) as standard APK files or —

if required early in the boot process or involving native system libraries/services — as an APEX

loopback filesystem in turn protected through dm-verity [94].

4.9 Cellular network security

While Android as a platform and user-focused operating system does not directly depend on the

security of any network connection layer (cf. Section 4.5), the majority of Android devices use

cellular networks as part of their core functionality. It is therefore important to consider security

aspects of this specific network layer as an important use case dependency. There is no robust

way for a device to verify the legitimacy of a cellular base station or the integrity of messages it

transmits prior to the Authentication and Key Agreement (AKA) handshake [104]. This applies to

2G, 3G, 4G, and 5G, and it is a systemic cellular protocol issue, not an OEM or carrier issue. As a

result, all mobile devices that support cellular connectivity are susceptible to False Base Station

(FBS) attacks [139].

Encrypting data in transit does not protect against all threats derived from an untrusted network.

An adversarial cellular network (e.g. a FBS) can disable link level encryption at the cellular channel,

for example, by silently downgrading the connection to a legacy protocol with weak encryption

and no mutual authentication [153], or by forcing the use of null ciphers. This exposes in the clear

circuit-switched Short Message Service (SMS) and voice user communications regardless of TLS

encryption of data in transit. Even when link level encryption is strictly applied to user traffic,

e.g. Voice over LTE (VoLTE), encryption implementation flaws can allow a passive eavesdropper

to decode the encrypted datagrams [146]. FBS attacks can also extract or intercept user private

identifiers, such as the International Mobile Subscriber Identity (IMSI), regardless of whether all

IP-based traffic is end-to-end encrypted.

Android’s in-depth security model introduces security features that mitigate [T.N3], as listed in

Table 6. For example, the option to disable the 2G radio at the modem level [141] and an option to

refuse null-ciphered connections [107].

Additionally, since 2021 Android has engaged with ecosystem partners to encourage and aid

them in hardening their firmwares with modern exploit mitigations [106] As a result, starting

in Android 13 the platform innovates in leveraging these same compiler-based security features

(UBSAN) in connectivity firmware to harden the security of the cellular baseband in some devices

(Tables 2 and 4).

5 SPECIAL CASES

There are some special cases that require intentional deviations from the abstract security model to

balance specific needs of various parties. This section describes some of these but is not intended

to be a comprehensive list. One goal of defining the Android security model publicly is to enable

researchers to discover potential additional gaps by comparing the implementation in AOSP with

the model we describe, and to engage in conversation on those special cases.

• Listing packages: The ability for one app to discover what other apps are installed on the

device can be considered a potential information leak and violation of user authorization

37 https://source.android.com/docs/core/ota/modular-system

---

## Page 38

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

38 Piqueras Jover, and Michael A. Specter

(rule 1 ○ ). However, app discovery is necessary for some direct app-to-app interaction which

is derived from the open ecosystem principle (rule 2 ○ ). As querying the list of all installed

apps is potentially privacy sensitive and has been abused by malware, Android 11 supports

more specific app-to-app interaction using platform components and limits general package

visibility for apps targeting this API version. While this special case is still supported at the

time of this writing, it requires the QUERY_ALL_PACKAGES permission and may be limited

further in the future.

• VPN apps may monitor/block network traffic for other apps: This is generally a

deviation from the application sandbox model since one app may see and impact traffic from

another app ( developer authorization). VPN apps are granted an exemption because of the

value they offer users, such as improved privacy and data usage controls, and because user

authorization is clear: this is equivalent to the user being responsible for determining the

network over which apps will communicate. For applications that use end-to-end encryption,

clear-text traffic is not available to the VPN application, which makes it equivalent to the

current network operator and keeps the confidentiality of the application sandbox.

• Backup: Data from the private app directory is backed up by default. Android 9 added

support for end-to-end encryption of backups to the Google cloud by entangling backup

session keys with the user lockscreen knowledge factor (LSKF) [108]. Apps may opt out by

setting fields in their manifest.

• Enterprise: Android allows so-called Device Owner (DO) or Profile Owner (PO) policies to

be enforced by a Device Policy Controller (DPC) app. A DO is installed on the primary/main

user account, while a PO is installed on a secondary user that acts as a work profile. Work

profiles allow separation of personal from enterprise data on a single device and are based

on Android multi-user support. This separation is enforced by the same isolation and

containment methods that protect apps and users from each other, with a significantly

stricter divide between the profiles [13].

A DPC introduces a fourth party to the authorization model: only if the policy allows an

action (e.g. within the work profile controlled by a PO) in addition to authorization by all

other parties can it be executed. The distinction of personal and work profile is enhanced

by the recent support for different user knowledge factors (handled by the lockscreen as

explained above in Section 4.2), which lead to different encryption keys for FBE. Note that

on devices with a work profile managed by PO but no full-device control (i.e. no DO),

privacy guarantees for the personal profile still need to hold under this security model.

Users may choose to turn off the work profile at any time, which causes all associated apps

to be stopped and the respective FBE keys to be evicted, ensuring resistance of work profile

data against physical attacks in line with [T.P2] even while the personal (main) profile is

still actively in use.

• Factory Reset Protection (FRP): is an exception to not storing any persistent data across

factory reset (rule 4 ○ ), but is a deliberate deviation from this part of the model to mitigate

the threat of theft and factory reset ([T.P2][T.P3]).

• Widevine: is another exception to rule 4 ○ , as its identifier remains stable across factory

resets. It allows app developers to detect abuse stemming from device resets, and is scoped

to the developer key to prevent cross-app tracking.

6 RELATED WORK

Classical operating system security models are primarily concerned with defining access control

(read/write/execute or more fine grained) by subjects (but most often single users, groups, or roles)

to objects (typically files and other resources controlled by the OS, in combination with permissions

---

## Page 39

The Android Platform Security Model (2023) 39

sometimes also called protection domains [158]). The most common data structures for efficiently

implementing these relations (which, conceptually, are sparse matrices) are Access Control Lists

(ACLs) [147] and capability lists (e.g. [180]). One of the first well-known and well-defined models

was the Bell-LaPadula multi-level security model [57], which defined properties for assigning

permissions and can be considered the abstract basis for Mandatory Access Control and Type

Enforcement schemes like SELinux. Consequently, the Android platform security model implicitly

builds upon these general models and their principle of least privilege.

One fundamental difference is that, while classical models assume processes started by a user

to be a proxy for their actions and therefore executes them directly with user privileges, more

contemporary models explicitly acknowledge the threat of malware started by a user and therefore

aim to compartmentalize their actions. Many mobile OSes (including Symbian as a historical

example) assign permissions to processes (i.e. applications) instead of users, and Android uses a

comparable approach. A more detailed comparison to other mobile OSes is out of scope for this

paper, and we refer to other surveys [80, 115, 135] as well as previous analysis of Android security

mechanisms and weaknesses exploited by malware [14, 82, 86, 118, 119, 122, 188].

7 CONCLUSION

In this paper, we described the Android platform security model and the complex threat model and

ecosystem it needs to operate in. One of the abstract rules is a multi-party authorization model that

is different to most standard OS security models in the sense that it implicitly considers applications

to have equal veto rights over actions in the same sense that the platform implementation and,

obviously, users have. While this may seem restricting from a user point of view, it effectively

limits the potential abuse a malicious app can do on data controlled by other apps; by avoiding

an all-powerful user account with unfiltered access to all data (as is the default with most current

desktop/server OSes), whole classes of threats such as file encrypting ransomware or direct data

exfiltration become impractical.

AOSP implements the Android platform security model as well as the general security principles

of “defense in depth” and “safe by default”. Different security mechanisms combine as multiple

layers of defense, and an important aspect is that even if security relevant bugs exist, they should

not necessarily lead to exploits reachable from standard user space code. While the current model

and its implementation already cover most of the threat model that is currently in scope of Android

security and privacy considerations, there are some deliberate special cases to the conceptually

simple security model, and there is room for future work:

• Keystore already supports API flags/methods to request hardware- or authentication-bound

keys. However, apps need to use these methods explicitly to benefit from improvements like

Strongbox. Making encryption of app files or directories more transparent by supporting

declarative use similar to network security config for TLS connections would make it easier

for app developers to securely use these features.

• It is common for malware to dynamically load its second stage depending on the respective

device it is being installed on, to both try to exploit specific detected vulnerabilities and

hide its payload from scanning in the app store. One potential mitigation is to require all

executable code to: a) be signed by a key that is trusted by the respective Android instance

(e.g. with public keys that are pre-shipped in the firmware and/or can be added by end-users)

or b) have a special permission to dynamically load/create code during runtime that is not

contained in the application bundle itself (the APK file). This could give better control over

code integrity, but would still not limit languages or platforms used to create these apps. It

---

## Page 40

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

40 Piqueras Jover, and Michael A. Specter

is recognized that this mitigation is limited to executable code. Interpreted code or server

based configuration would bypass this mitigation.

• Advanced attackers may gain access to OEM or vendor code signing keys. Even under such

circumstance, it is beneficial to still retain some security and privacy assurances to users.

One recent example is the specification and implementation of Insider Attack Resistance

(IAR) for updateable code in TRH [183], and extending similar defenses to higher-level

software is desirable [132]. Potential approaches could be reproducible firmware builds or

logs of released firmware hashes comparable to e.g. Certificate Transparency [117].

• Hardware level attacks are becoming more popular, and therefore additional (software and

hardware) defense against e.g. RAM related attacks would add another layer of defense,

although, most probably with a trade-off in performance overhead.

However, all such future work needs to be done considering its impact on the wider ecosystem

and should be kept in line with fundamental Android security rules and principles.

ACKNOWLEDGMENTS

Previous versions of this paper were co-authored by Nick Kralevich, and we especially thank

them for their contributions to Android platform security as well as earlier versions of this text.

Additionally, we thank Billy Lau, Joel Galenson, Ivan Lozano, Paul Crowley, Shawn Willden, Jeff

Sharkey, Haining Chen, and Xiaowen Xin for input on various parts, and particularly Vishwath

Mohan for direct contributions to the Authentication section. We also thank the enormous number

of security researchers (https://source.android.com/security/overview/acknowledgements) who

have improved Android over the years and anonymous reviewers who have contributed highly

helpful feedback to earlier drafts of this paper.

REFERENCES

[1] 2015. Stagefright Vulnerability Report . https://www.kb.cert.org/vuls/id/924951

[2] 2017. BlueBorne. https://go.armis.com/hubfs/BlueBorne%20-%20Android%20Exploit%20(20171130).pdf?t=

1529364695784

[3] 2017. CVE-2017-13177. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13177

[4] 2018. CVE-2017-17558: Remote code execution in media frameworks. https://source.android.com/security/bulletin/

2018-06-01#kernel-components

[5] 2018. CVE-2018-9341: Remote code execution in media frameworks. https://source.android.com/security/bulletin/

2018-06-01#media-framework

[6] 2018. SVE-2018-11599: Theft of arbitrary files leading to emails and email accounts takeover. https://security.

samsungmobile.com/securityUpdate.smsb

[7] 2018. SVE-2018-11633: Buffer Overflow in Trustlet. https://security.samsungmobile.com/securityUpdate.smsb

[8] 2019. Android Now FIDO2 Certified. https://fidoalliance.org/android-now-fido2-certified-accelerating-global-

migration-beyond-passwords/

[9] 2020. Personal identification – ISO-compliant driving licence – Part 5: Mobile driving licence (mDL) application.

Draft International Standard: ISO/IEC DIS 18013-5.

[10] 2021. Android 12 and Android 12 release notes. https://source.android.com/docs/setup/about/android-12-release#2g-

toggle

[11] 2022. Hacked documents: how Iran can track and control protesters phones. https://theintercept.com/2022/10/28/iran-

protests-phone-surveillance/

[12] 2022. Vulnerability within the Unisoc baseband opens mobile phone communications to remote hacker attacks.

https://research.checkpoint.com/2022/vulnerability-within-the-unisoc-baseband/

[13] 2023. Android Security White Paper 2023. https://services.google.com/fh/files/misc/android-enterprise-security-

paper-2023.pdf

[14] Y. Acar, M. Backes, S. Bugiel, S. Fahl, P. McDaniel, and M. Smith. 2016. SoK: Lessons Learned from Android

Security Research for Appified Software Platforms. In 2016 IEEE Symposium on Security and Privacy (SP) . 433–451.

https://doi.org/10.1109/SP.2016.33

---

## Page 41

The Android Platform Security Model (2023) 41

[15] Anne Adams and Martina Angela Sasse. 1999. Users Are Not the Enemy. Commun. ACM 42, 12 (Dec. 1999), 40–46.

https://doi.org/10.1145/322796.322806

[16] Andrew Ahn. 2018. How we fought bad apps and malicious developers in 2017. https://android-developers.

googleblog.com/2018/01/how-we-fought-bad-apps-and-malicious.html

[17] Bonnie Brinton Anderson, Anthony Vance, C. Brock Kirwan, Jeffrey L. Jenkins, and David Eargle. 2016. From

Warning to Wallpaper: Why the Brain Habituates to Security Warnings and What Can Be Done About It. Journal of

Management Information Systems 33, 3 (2016), 713–743. https://doi.org/10.1080/07421222.2016.1243947

[18] Anil Kumar Reddy, P. Paramasivam, and Prakash Babu Vemula. 2015. Mobile secure data protection using eMMC

RPMB partition. In 2015 International Conference on Computing and Network Communications (CoCoNet) . 946–950.

https://doi.org/10.1109/CoCoNet.2015.7411305

[19] AOSP. [n.d.]. Android Compatibility Definition Document . https://source.android.com/compatibility/cdd

[20] AOSP. [n.d.]. Android Enterprise Recommended requirements . https://www.android.com/enterprise/recommended/

requirements/

[21] AOSP. [n.d.]. Android isolatedProcess feature. https://developer.android.com/guide/topics/manifest/service-

element#isolated

[22] AOSP. [n.d.]. Android platform permissions requesting guidance . https://material.io/design/platform-guidance/android-

permissions.html#request-types

[23] AOSP. [n.d.]. Android Verified Boot Flow . https://source.android.com/security/verifiedboot/boot-flow

[24] AOSP. [n.d.]. Android Virtualization Framework (AVF) . https://source.android.com/docs/core/virtualization

[25] AOSP. [n.d.]. App hibernation . https://developer.android.com/topic/performance/app-hibernation

[26] AOSP. [n.d.]. App Manifest Overview . https://developer.android.com/guide/topics/manifest/manifest-intro

[27] AOSP. [n.d.]. App Manifest permission element . https://developer.android.com/guide/topics/manifest/permission-

element

[28] AOSP. [n.d.]. Define a custom app permission. https://developer.android.com/guide/topics/permissions/defining

[29] AOSP. [n.d.]. Developer documentation android.security.identity . https://developer.android.com/reference/android/

security/identity/package-summary

[30] AOSP. [n.d.]. Developer documentation android.security.keystore.KeyGenParameterSpec . https://developer.android.

com/reference/android/security/keystore/KeyGenParameterSpec

[31] AOSP. [n.d.]. Gatekeeper . https://source.android.com/security/authentication/gatekeeper

[32] AOSP. [n.d.]. Hardware-backed Keystore . https://source.android.com/security/keystore/

[33] AOSP. [n.d.]. Intents and Intent Filters . https://developer.android.com/guide/components/intents-filters

[34] AOSP. [n.d.]. MAC address availability changes in Android 11 . https://developer.android.com/training/articles/user-

data-ids#mac-11-plus

[35] AOSP. [n.d.]. Network security configuration . https://developer.android.com/training/articles/security-config

[36] AOSP. [n.d.]. Privacy in Android 11. https://developer.android.com/about/versions/11/privacy

[37] AOSP. [n.d.]. Privacy: MAC Randomization . https://source.android.com/devices/tech/connect/wifi-mac-

randomization

[38] AOSP. [n.d.]. Privileged Permission Allowlisting . https://source.android.com/devices/tech/config/perms-whitelist

[39] AOSP. [n.d.]. Restrictions on non-SDK interfaces . https://developer.android.com/distribute/best-practices/develop/

restrictions-non-sdk-interfaces

[40] AOSP. [n.d.]. Security Updates and Resources - Process Types . https://source.android.com/security/overview/updates-

resources#process_types

[41] AOSP. [n.d.]. Tapjacking . https://developer.android.com/topic/security/risks/tapjacking

[42] AOSP. [n.d.]. Trusty TEE . https://source.android.com/docs/security/features/trusty

[43] AOSP. [n.d.]. Verifying Boot . https://source.android.com/security/verifiedboot/verified-boot

[44] AOSP. [n.d.]. Verifying hardware-backed key pairs with Key Attestation . https://developer.android.com/training/

articles/security-key-attestation

[45] AOSP. 2018. Android Protected Confirmation . https://developer.android.com/preview/features/security#android-

protected-confirmation

[46] AOSP. 2018. Android Verified Boot 2.0 . https://android.googlesource.com/platform/external/avb/+/android11-

release/README.md

[47] AOSP. 2018. APK Signature Scheme v3 . https://source.android.com/security/apksigning/v3

[48] AOSP. 2018. SELinux for Android 8.0: Changes & Customizations. https://source.android.com/security/selinux/

images/SELinux_Treble.pdf

[49] AOSP. 2019. Restrictions on starting activities from the background . https://developer.android.com/guide/components/

activities/background-starts

---

## Page 42

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

42 Piqueras Jover, and Michael A. Specter

[50] AOSP. 2020. Android 11 biometric authentication . https://developer.android.com/about/versions/11/features#biometric-

auth

[51] AOSP. 2020. Security and Privacy Enhancements in Android 10 . https://source.android.com/security/enhancements/

enhancements10

[52] ARM. 2019. Memory Tagging Extension: Enhancing memory safety through architecture. https://community.arm.

com/arm-community-blogs/b/architectures-and-processors-blog/posts/enhancing-memory-safety

[53] Dan Austin and Jeff Vander Stoep. 2016. Hardening the media stack. https://android-developers.googleblog.com/

2016/05/hardening-media-stack.html

[54] Adam J. Aviv, Katherine Gibson, Evan Mossop, Matt Blaze, and Jonathan M. Smith. 2010. Smudge Attacks on

Smartphone Touch Screens. In Proceedings of the 4th USENIX Conference on Offensive Technologies (Washington, DC)

(WOOT’10) . USENIX Association, USA, 1–7.

[55] Steve Barker. 2009. The next 700 Access Control Models or a Unifying Meta-Model?. In Proceedings of the 14th

ACM Symposium on Access Control Models and Technologies (Stresa, Italy) (SACMAT ’09) . Association for Computing

Machinery, New York, NY, USA, 187–196. https://doi.org/10.1145/1542207.1542238

[56] David Barrera, Daniel McCarney, Jeremy Clark, and Paul C. van Oorschot. 2014. Baton: Certificate Agility for

Android’s Decentralized Signing Infrastructure. In Proceedings of the 2014 ACM Conference on Security and Privacy in

Wireless and Mobile Networks (Oxford, United Kingdom) (WiSec ’14) . Association for Computing Machinery, New

York, NY, USA, 1–12. https://doi.org/10.1145/2627393.2627397

[57] D. Bell and L. LaPadula. 1975. Secure Computer System Unified Exposition and Multics Interpretation . Technical Report

MTR-2997. MITRE Corp., Bedford, MA.

[58] M. Benantar. 2005. Access Control Systems: Security, Identity Management and Trust Models .

[59] James Bender. 2018. Google Play security metadata and offline app distribution. https://android-developers.

googleblog.com/2018/06/google-play-security-metadata-and.html

[60] Elisa Bertino, Barbara Catania, Elena Ferrari, and Paolo Perlasca. 2003. A Logical Framework for Reasoning about

Access Control Models. ACM Trans. Inf. Syst. Secur. 6, 1 (Feb. 2003), 71–127. https://doi.org/10.1145/605434.605437

[61] Sandeep Bhatkar, Daniel C. DuVarney, and R. Sekar. 2003. Address Obfuscation: An Efficient Approach to Combat a

Board Range of Memory Error Exploits. In Proc. USENIX Security Symposium - Volume 12 (Washington, DC). USENIX

Association, Berkeley, CA, USA, 8–8. http://dl.acm.org/citation.cfm?id=1251353.1251361

[62] Bram Bonné and Chad Brubaker. 2019. An Update on Android TLS Adoption. https://security.googleblog.com/2019/

12/an-update-on-android-tls-adoption.html

[63] Chad Brubaker. 2014. Introducing nogotofail — a network traffic security testing tool. https://security.googleblog.

com/2014/11/introducing-nogotofaila-network-traffic.html

[64] Chad Brubaker. 2018. Protecting users with TLS by default in Android P. https://android-developers.googleblog.

com/2018/04/protecting-users-with-tls-by-default-in.html

[65] N. Burow, X. Zhang, and M. Payer. 2019. SoK: Shining Light on Shadow Stacks. In 2019 IEEE Symposium on Security

and Privacy (SP) . 985–999. https://doi.org/10.1109/SP.2019.00076

[66] Pierre Carru. 2017. Attack TrustZone with Rowhammer. http://www.eshard.com/wp-content/plugins/email-before-

download/download.php?dl=9465aa084ff0f070a3acedb56bcb34f5

[67] Dan Cashman. 2017. SELinux in Android O: Separating Policy to Allow for Independent Updates. https://events.static.

linuxfound.org/sites/events/files/slides/LSS%20-%20Treble%20%27n%27%20SELinux.pdf Linux Security Summit.

[68] Jen Chai. 2019. Giving users more control over their location data. https://android-developers.googleblog.com/2019/

03/giving-users-more-control-over-their.html

[69] Haining Chen, Ninghui Li, William Enck, Yousra Aafer, and Xiangyu Zhang. 2017. Analysis of SEAndroid Policies:

Combining MAC and DAC in Android. In Proceedings of the 33rd Annual Computer Security Applications Conference

(Orlando, FL, USA) (ACSAC 2017) . ACM, New York, NY, USA, 553–565. https://doi.org/10.1145/3134600.3134638

[70] Haining Chen, Vishwath Mohan, Kevin Chyn, and Liz Louis. 2020. Lockscreen and authentication improvements in

Android 11. https://android-developers.googleblog.com/2020/09/lockscreen-and-authentication.html

[71] Qi Alfred Chen, Zhiyun Qian, and Z Morley Mao. 2014. Peeking into your app without actually seeing it: { UI } state

inference and novel android attacks. In 23rd { USENIX } Security Symposium ( { USENIX } Security 14) . 1037–1052.

[72] Erika Chin and David Wagner. 2014. Bifocals: Analyzing webview vulnerabilities in android applications. In

Information Security Applications: 14th International Workshop, WISA 2013, Jeju Island, Korea, August 19-21, 2013,

Revised Selected Papers 14 . Springer, 138–159.

[73] Jiska Classen and Matthias Hollick. 2019. Inside job: diagnosing bluetooth lower layers using off-the-shelf devices.

In Proceedings of the 12th Conference on Security and Privacy in Wireless and Mobile Networks, WiSec 2019, Miami,

Florida, USA, May 15-17, 2019 . ACM, 186–191. https://doi.org/10.1145/3317549.3319727

[74] Paul Crowley and Eric Biggers. 2018. Adiantum: length-preserving encryption for entry-level processors. IACR

Transactions on Symmetric Cryptology 2018, 4 (Dec. 2018), 39–61. https://doi.org/10.13154/tosc.v2018.i4.39-61

---

## Page 43

The Android Platform Security Model (2023) 43

[75] Edward Cunningham. 2017. Improving app security and performance on Google Play for years to come. https:

//android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html

[76] Lucas Davi, Ahmad-Reza Sadeghi, Daniel Lehmann, and Fabian Monrose. 2014. Stitching the Gadgets: On the

Ineffectiveness of Coarse-Grained Control-Flow Integrity Protection. In 23rd USENIX Security Symposium (USENIX

Security 14) . USENIX Association, San Diego, CA, 401–416. https://www.usenix.org/conference/usenixsecurity14/

technical-sessions/presentation/davi

[77] Sabrina De Capitani di Vimercati. 2011. Access Matrix . Springer US, Boston, MA, 14–17. https://doi.org/10.1007/978-

1-4419-5906-5_807

[78] Rachna Dhamija, J. D. Tygar, and Marti Hearst. 2006. Why Phishing Works. In Proceedings of the SIGCHI Conference

on Human Factors in Computing Systems (Montr&#233;al, Qu&#233;bec, Canada) (CHI ’06) . ACM, New York, NY, USA,

581–590. https://doi.org/10.1145/1124772.1124861

[79] Danny Dolev and Andrew Chi chih Yao. 1983. On the security of public key protocols. IEEE Transactions on

Information Theory 29 (1983), 198–208. Issue 2. https://doi.org/10.1109/TIT.1983.1056650

[80] Andre Egners, Björn Marschollek, and Ulrike Meyer. 2012. Hackers in Your Pocket: A Survey of Smartphone Security

Across Platforms . Technical Report 2012,7. RWTH Aachen University. https://itsec.rwth-aachen.de/publications/ae_

hacker_in_your_pocket.pdf

[81] Malin Eiband, Mohamed Khamis, Emanuel von Zezschwitz, Heinrich Hussmann, and Florian Alt. 2017. Understanding

Shoulder Surfing in the Wild: Stories from Users and Observers. In Proceedings of the 2017 CHI Conference on Human

Factors in Computing Systems (Denver, Colorado, USA) (CHI ’17) . Association for Computing Machinery, New York,

NY, USA, 4254–4265. https://doi.org/10.1145/3025453.3025636

[82] W. Enck, M. Ongtang, and P. McDaniel. 2009. Understanding Android Security. IEEE Security Privacy 7, 1 (Jan 2009),

50–57. https://doi.org/10.1109/MSP.2009.26

[83] Sascha Fahl, Marian Harbach, Thomas Muders, Lars Baumgärtner, Bernd Freisleben, and Matthew Smith. 2012. Why

Eve and Mallory Love Android: An Analysis of Android SSL (in)Security. In Proceedings of the 2012 ACM Conference

on Computer and Communications Security (Raleigh, North Carolina, USA) (CCS ’12) . ACM, New York, NY, USA,

50–61. https://doi.org/10.1145/2382196.2382205

[84] Sascha Fahl, Marian Harbach, Henning Perl, Markus Koetter, and Matthew Smith. 2013. Rethinking SSL Development

in an Appified World. In Proceedings of the 2013 ACM SIGSAC Conference on Computer &#38; Communications Security

(Berlin, Germany) (CCS ’13) . ACM, New York, NY, USA, 49–60. https://doi.org/10.1145/2508859.2516655

[85] Hossein Falaki, Ratul Mahajan, Srikanth Kandula, Dimitrios Lymberopoulos, Ramesh Govindan, and Deborah Estrin.

2010. Diversity in Smartphone Usage. In Proc. 8th International Conference on Mobile Systems, Applications, and

Services (San Francisco, California, USA) (MobiSys ’10) . ACM, New York, NY, USA, 179–194. https://doi.org/10.1145/

1814433.1814453

[86] P. Faruki, A. Bharmal, V. Laxmi, V. Ganmoor, M. S. Gaur, M. Conti, and M. Rajarajan. 2015. Android Security: A

Survey of Issues, Malware Penetration, and Defenses. IEEE Communications Surveys Tutorials 17, 2 (2015), 998–1022.

https://doi.org/10.1109/COMST.2014.2386139

[87] Adrienne Porter Felt, Serge Egelman, Matthew Finifter, Devdatta Akhawe, and David A. Wagner. 2012. How to Ask

for Permission. In HotSec .

[88] Adrienne Porter Felt, Elizabeth Ha, Serge Egelman, Ariel Haney, Erika Chin, and David Wagner. 2012. Android

Permissions: User Attention, Comprehension, and Behavior. In Proceedings of the Eighth Symposium on Usable Privacy

and Security (Washington, D.C.) (SOUPS ’12) . ACM, New York, NY, USA, Article 3, 14 pages. https://doi.org/10.1145/

2335356.2335360

[89] Earlence Fernandes, Qi Alfred Chen, Justin Paupore, Georg Essl, J. Alex Halderman, Z. Morley Mao, and Atul Prakash.

2016. Android UI Deception Revisited: Attacks and Defenses. In Financial Cryptography and Data Security (Lecture

Notes in Computer Science) . Springer, Berlin, Heidelberg, 41–59. https://doi.org/10.1007/978-3-662-54970-4_3

[90] Nate Fischer. 2018. Protecting WebView with Safe Browsing. https://android-developers.googleblog.com/2018/04/

protecting-webview-with-safe-browsing.html

[91] Google APIs for Android. [n.d.]. . https://developers.google.com/android/reference/com/google/android/gms/fido/

Fido

[92] Yanick Fratantonio, Chenxiong Qian, Simon Chung, and Wenke Lee. 2017. Cloak and Dagger: From Two Permissions

to Complete Control of the UI Feedback Loop. In Proceedings of the IEEE Symposium on Security and Privacy (Oakland) .

San Jose, CA.

[93] Martin Georgiev, Subodh Iyengar, Suman Jana, Rishita Anubhai, Dan Boneh, and Vitaly Shmatikov. 2012. The most

dangerous code in the world: validating SSL certificates in non-browser software. In ACM Conference on Computer

and Communications Security . 38–49.

[94] Anwar Ghuloum. 2019. Fresher OS with Projects Treble and Mainline. https://android-developers.googleblog.com/

2019/05/fresher-os-with-projects-treble-and-mainline.html

---

## Page 44

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

44 Piqueras Jover, and Michael A. Specter

[95] Marco Grassi and Xingyu Chen. 2021. Gaining remote code execution on 5G smartphones. https:

//i.blackhat.com/USA21/Wednesday-Handouts/us-21-Over-The-Air-Baseband-Exploit-Gaining-Remote-Code-

Execution-On-5G-Smartphones.pdf BlackHat.

[96] J. Alex Halderman, Seth D. Schoen, Nadia Heninger, William Clarkson, William Paul, Joseph A. Calandrino, Ariel J.

Feldman, Jacob Appelbaum, and Edward W. Felten. 2009. Lest We Remember: Cold-boot Attacks on Encryption Keys.

Commun. ACM 52, 5 (May 2009), 91–98. https://doi.org/10.1145/1506409.1506429

[97] Grant Hernandez, Dave (Jing) Tian, Anurag Swarnim Yadav, Byron J. Williams, and Kevin R.B. Butler. 2020. BigMAC:

Fine-Grained Policy Analysis of Android Firmware. In 29th USENIX Security Symposium (USENIX Security 20) . USENIX

Association, 271–287. https://www.usenix.org/conference/usenixsecurity20/presentation/hernandez

[98] Daniel Hintze, Rainhard D. Findling, Muhammad Muaaz, Sebastian Scholz, and René Mayrhofer. 2014. Diversity

in Locked and Unlocked Mobile Device Usage. In Proceedings of the 2014 ACM International Joint Conference on

Pervasive and Ubiquitous Computing: Adjunct Publication (UbiComp 2014) . ACM Press, 379–384. https://doi.org/10.

1145/2638728.2641697

[99] Daniel Hintze, Rainhard D. Findling, Sebastian Scholz, and René Mayrhofer. 2014. Mobile Device Usage Characteristics:

The Effect of Context and Form Factor on Locked and Unlocked Usage. In Proc. MoMM 2014: 12th International

Conference on Advances in Mobile Computing and Multimedia (Kaohsiung, Taiwan). ACM Press, New York, NY, USA,

105–114. https://doi.org/10.1145/2684103.2684156

[100] Daniel Hintze, Philipp Hintze, Rainhard Dieter Findling, and René Mayrhofer. 2017. A Large-Scale, Long-Term

Analysis of Mobile Device Usage Characteristics. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 1, 2, Article

13 (June 2017), 21 pages. https://doi.org/10.1145/3090078

[101] Sebastian Höbarth and René Mayrhofer. 2011. A framework for on-device privilege escalation exploit execution on

Android. In Proc. IWSSI/SPMU 2011: 3rd International Workshop on Security and Privacy in Spontaneous Interaction and

Mobile Phone Use, colocated with Pervasive 2011 (San Francisco, CA, USA).

[102] Michael Hölzl, Michael Roland, and René Mayrhofer. 2017. Real-world Identification for an Extensible and Privacy-

preserving Mobile eID. In Privacy and Identity Management. The Smart Revolution. Privacy and Identity 2017 . IFIP

AICT, Vol. 526/2018. Springer, Ispra, Italy, 354–370. https://doi.org/10.1007/978-3-319-92925-5_24

[103] Jay Hou. 2023. Pixel Binary Transparency: verifiable security for Pixel devices. https://security.googleblog.com/

2023/08/pixel-binary-transparency-verifiable.html

[104] Syed Hussain, Mitziu Echeverria, Ankush Singla, Omar Chowdhury, and Elisa Bertino. 2019. Insecure connection

bootstrapping in cellular networks: the root of all evil. In Proceedings of the 12th Conference on security and privacy in

wireless and mobile networks . ACM, 1–11.

[105] Yeongjin Jang, Chengyu Song, Simon P. Chung, Tielei Wang, and Wenke Lee. 2014. A11Y Attacks: Exploiting Accessibil-

ity in Operating Systems. In Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security

(Scottsdale, Arizona, USA) (CCS ’14) . ACM, New York, NY, USA, 103–115. https://doi.org/10.1145/2660267.2660295

[106] Roger Piqueras Jover, Ivan Lozano, Sudhi Herle, and Stephan Somogyi. 2023. Hardening Firmware Across the Android

Ecosystem. https://security.googleblog.com/2023/02/hardening-firmware-across-android.html

[107] Roger Piqueras Jover, Yomna Nasser, and Sudhi Herle. 2023. Android 14 introduces first-of-its-kind cellular connec-

tivity security features. https://security.googleblog.com/2023/08/android-14-introduces-first-of-its-kind.html

[108] Troy Kensinger. 2018. Google and Android have your back by protecting your backups. https://security.googleblog.

com/2018/10/google-and-android-have-your-back-by.html

[109] Hassan Khan, Urs Hengartner, and Daniel Vogel. 2018. Evaluating Attack and Defense Strategies for Smartphone

PIN Shoulder Surfing. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (Montreal

QC, Canada) (CHI ’18) . Association for Computing Machinery, New York, NY, USA, 1–10. https://doi.org/10.1145/

3173574.3173738

[110] Amin Kharraz, William Robertson, Davide Balzarotti, Leyla Bilge, and Engin Kirda. 2015. Cutting the Gordian Knot:

A Look Under the Hood of Ransomware Attacks. In Detection of Intrusions and Malware, and Vulnerability Assessment ,

Magnus Almgren, Vincenzo Gulisano, and Federico Maggi (Eds.). Springer International Publishing, Cham, 3–24.

[111] Erik Kline and Ben Schwartz. 2018. DNS over TLS support in Android P Developer Preview. https://android-

developers.googleblog.com/2018/04/dns-over-tls-support-in-android-p.html

[112] Paul Kocher, Daniel Genkin, Daniel Gruss, Werner Haas, Mike Hamburg, Moritz Lipp, Stefan Mangard, Thomas

Prescher, Michael Schwarz, and Yuval Yarom. 2018. Spectre Attacks: Exploiting Speculative Execution.

arXiv:1801.01203 [cs] (2018). arXiv:1801.01203 http://arxiv.org/abs/1801.01203

[113] Nick Kralevich. 2016. The Art of Defense: How vulnerabilities help shape security features and mitigations in An-

droid. https://www.blackhat.com/docs/us-16/materials/us-16-Kralevich-The-Art-Of-Defense-How-Vulnerabilities-

Help-Shape-\Security-Features-And-Mitigations-In-Android.pdf BlackHat.

[114] Joshua Kraunelis, Yinjie Chen, Zhen Ling, Xinwen Fu, and Wei Zhao. 2014. On Malware Leveraging the Android

Accessibility Framework. In Mobile and Ubiquitous Systems: Computing, Networking, and Services , Ivan Stojmenovic,

---

## Page 45

The Android Platform Security Model (2023) 45

Zixue Cheng, and Song Guo (Eds.). Springer International Publishing, Cham, 512–523.

[115] Mariantonietta La Polla, Fabio Martinelli, and Daniele Sgandurra. 2013. A Survey on Security for Mobile Devices.

Communications Surveys & Tutorials 15 (01 2013), 446–471.

[116] Ben Lapid and Avishai Wool. 2019. Cache-Attacks on the ARM TrustZone Implementations of AES-256 and AES-256-

GCM via GPU-Based Analysis. In Selected Areas in Cryptography – SAC 2018 , Carlos Cid and Michael J. Jacobson Jr.

(Eds.). Springer International Publishing, Cham, 235–256.

[117] B. Laurie, A. Langley, and E. Kasper. 2013. Certificate Transparency. https://www.rfc-editor.org/info/rfc6962

[118] Li Li, Alexandre Bartel, Jacques Klein, Yves Le Traon, Steven Arzt, Siegfried Rasthofer, Eric Bodden, Damien Octeau,

and Patrick McDaniel. 2014. I know what leaked in your pocket: uncovering privacy leaks on Android Apps with

Static Taint Analysis. arXiv:1404.7431 [cs] (April 2014). http://arxiv.org/abs/1404.7431

[119] Li Li, Tegawendé F. Bissyandé, Mike Papadakis, Siegfried Rasthofer, Alexandre Bartel, Damien Octeau, Jacques

Klein, and Le Traon. 2017. Static analysis of Android apps: A systematic literature review. Information and Software

Technology 88 (2017), 67 – 95. https://doi.org/10.1016/j.infsof.2017.04.001

[120] Rui Li, Wenrui Diao, Zhou Li, Jianqi Du, and Shanqing Guo. 2021. Android custom permissions demystified: From

privilege escalation to design shortcomings. In 2021 IEEE Symposium on Security and Privacy (SP) . IEEE, 70–86.

[121] Eugene Liderman and Sara N-Marandi. 2022. I/O 2022: Android 13 security and privacy (and more). https:

//security.googleblog.com/2022/05/io-2022-android-13-security-and-privacy.html

[122] M. Lindorfer, M. Neugschwandtner, L. Weichselbaum, Y. Fratantonio, V. v. d. Veen, and C. Platzer. 2014. ANDRUBIS

– 1,000,000 Apps Later: A View on Current Android Malware Behaviors. In 2014 Third International Workshop on

Building Analysis Datasets and Gathering Experience Returns for Security (BADGERS) . 3–17. https://doi.org/10.1109/

BADGERS.2014.7

[123] Moritz Lipp, Michael Schwarz, Daniel Gruss, Thomas Prescher, Werner Haas, Stefan Mangard, Paul Kocher, Daniel

Genkin, Yuval Yarom, and Mike Hamburg. 2018. Meltdown. arXiv:1801.01207 [cs] (2018). arXiv:1801.01207 http:

//arxiv.org/abs/1801.01207

[124] T. Lodderstedt, M. McGloin, and P. Hunt. 2013. OAuth 2.0 Threat Model and Security Considerations. https:

//www.rfc-editor.org/info/rfc6819

[125] Ivan Lozano. 2018. Compiler-based security mitigations in Android P. https://android-developers.googleblog.com/

2018/06/compiler-based-security-mitigations-in.html

[126] Ivan Lozano and Roger Piqueras Jover. 2023. Hardening cellular basebands in Android. https://security.googleblog.

com/2023/12/hardening-cellular-basebands-in-android.html

[127] Tongbo Luo, Hao Hao, Wenliang Du, Yifei Wang, and Heng Yin. 2011. Attacks on WebView in the Android system.

In Proceedings of the 27th Annual Computer Security Applications Conference . 343–352.

[128] Iliyan Malchev. 2017. Here comes Treble: A modular base for Android. https://android-developers.googleblog.com/

2017/05/here-comes-treble-modular-base-for.html

[129] Eugenio Marchiori, Sarah de Haas, Sergey Volnov, Ronnie Falcon, Roxanne Pinto, and Marco Zamarato. 2022. Android

Private Compute Core Architecture. https://doi.org/10.48550/ARXIV.2209.10317

[130] Matthew Maurer and Mike Yu. 2022. DNS-over-HTTP/3 in Android . https://security.googleblog.com/2022/07/dns-

over-http3-in-android.html

[131] René Mayrhofer. 2014. An Architecture for Secure Mobile Devices. Security and Communication Networks (2014).

https://doi.org/10.1002/sec.1028

[132] René Mayrhofer. 2019. Insider Attack Resistance in the Android Ecosystem. https://www.usenix.org/conference/

enigma2019/presentation/mayrhofer

[133] René Mayrhofer, Vishwath Mohan, and Stephan Sigg. 2020. Adversary Models for Mobile Device Authentication.

arXiv:2009.10150 [cs.CR]

[134] T. McDonnell, B. Ray, and M. Kim. 2013. An Empirical Study of API Stability and Adoption in the Android Ecosystem.

In 2013 IEEE International Conference on Software Maintenance . 70–79. https://doi.org/10.1109/ICSM.2013.18

[135] I. Mohamed and D. Patel. 2015. Android vs iOS Security: A Comparative Study. In 2015 12th International Conference

on Information Technology - New Generations . 725–730. https://doi.org/10.1109/ITNG.2015.123

[136] Vishwath Mohan. 2018. Better Biometrics in Android P. https://android-developers.googleblog.com/2018/06/better-

biometrics-in-android-p.html

[137] Sara N-Marandi. 2021. What’s new in Android Privacy. https://android-developers.googleblog.com/2021/05/android-

security-and-privacy-recap.html

[138] Vikrant Nanda and René Mayrhofer. 2018. Android Pie à la mode: Security & Privacy. https://android-developers.

googleblog.com/2018/12/android-pie-la-mode-security-privacy.html

[139] Yomna Nasser. 2019. Gotta Catch ’Em All: Understanding How IMSI-Catchers Exploit Cell Networks. https:

//www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks

---

## Page 46

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

46 Piqueras Jover, and Michael A. Specter

[140] Sundar Pichai. 2018. Android has created more choice, not less. https://blog.google/around-the-globe/google-

europe/android-has-created-more-choice-not-less/

[141] Cooper Quintin. 2022. VICTORY: Google Releases “disable 2g” Feature for New Android Smartphones. https:

//www.eff.org/deeplinks/2022/01/victory-google-releases-disable-2g-feature-new-android-smartphones

[142] Joel Reardon, Álvaro Feal, Primal Wijesekera, Amit Elazari Bar On, Narseo Vallina-Rodriguez, and Serge Egelman.

2019. 50 Ways to Leak Your Data: An Exploration of Apps’ Circumvention of the Android Permissions System.

In 28th USENIX Security Symposium (USENIX Security 19) . USENIX Association, Santa Clara, CA, 603–620. https:

//www.usenix.org/conference/usenixsecurity19/presentation/reardon

[143] Peter Riedl, Rene Mayrhofer, Andreas Möller, Matthias Kranz, Florian Lettner, Clemens Holzmann, and Marion Koelle.

2015. Only play in your comfort zone: interaction methods for improving security awareness on mobile devices.

Personal and Ubiquitous Computing (27 March 2015), 1–14. https://doi.org/10.1007/s00779-015-0840-5

[144] Franziska Roesner, Tadayoshi Kohno, Er Moshchuk, Bryan Parno, Helen J. Wang, and Crispin Cowan. 2012. User-

driven access control: Rethinking permission granting in modern operating systems. In Proceedings of the 2012 IEEE

Symposium on Security and Privacy, ser. SP’12 . 224–238. https://doi.org/10.1109/SP.2012.24

[145] Michael Roland, Josef Langer, and Josef Scharinger. 2013. Applying Relay Attacks to Google Wallet. In Proceedings

of the Fifth International Workshop on Near Field Communication (NFC 2013) . IEEE, Zurich, Switzerland. https:

//doi.org/10.1109/NFC.2013.6482441

[146] David Rupprecht, Katharina Kohls, Thorsten Holz, and Christina Pöpper. 2020. Call me maybe: eavesdropping

encrypted LTE calls with REVOLTE. In Proceedings of the 29th USENIX Conference on Security Symposium . 73–88.

[147] R. S. Sandhu and P. Samarati. 1994. Access control: principle and practice. IEEE Communications Magazine 32, 9 (Sept

1994), 40–48. https://doi.org/10.1109/35.312842

[148] N. Scaife, H. Carter, P. Traynor, and K. R. B. Butler. 2016. CryptoLock (and Drop It): Stopping Ransomware Attacks

on User Data. In 2016 IEEE 36th International Conference on Distributed Computing Systems (ICDCS) . 303–312. https:

//doi.org/10.1109/ICDCS.2016.46

[149] Konstantin Serebryany, Derek Bruening, Alexander Potapenko, and Dmitriy Vyukov. 2012. AddressSanitizer: A Fast

Address Sanity Checker. In Presented as part of the 2012 USENIX Annual Technical Conference (USENIX ATC 12) . USENIX,

Boston, MA, 309–318. https://www.usenix.org/conference/atc12/technical-sessions/presentation/serebryany

[150] Kostya Serebryany, Evgenii Stepanov, Aleksey Shlyapnikov, Vlad Tsyrklevich, and Dmitry Vyukov. 2018. Memory

Tagging and how it improves C/C++ memory safety. CoRR abs/1802.09517 (2018). arXiv:1802.09517 http://arxiv.org/

abs/1802.09517

[151] Arvind Seshadri, Mark Luk, Ning Qu, and Adrian Perrig. 2007. SecVisor: A Tiny Hypervisor to Provide Lifetime

Kernel Code Integrity for Commodity OSes. In Proceedings of Twenty-first ACM SIGOPS Symposium on Operating

Systems Principles (Stevenson, Washington, USA) (SOSP ’07) . ACM, New York, NY, USA, 335–350. https://doi.org/10.

1145/1294261.1294294

[152] Hovav Shacham, Matthew Page, Ben Pfaff, Eu-Jin Goh, Nagendra Modadugu, and Dan Boneh. 2004. On the Effective-

ness of Address-space Randomization. In Proceedings of the 11th ACM Conference on Computer and Communications Se-

curity (Washington DC, USA) (CCS ’04) . ACM, New York, NY, USA, 298–307. https://doi.org/10.1145/1030083.1030124

[153] A Shaik, R Borgaonkar, N Asokan, V Niemi, and JP Seifert. 2016. Practical Attacks Against Privacy and Availability

in 4G/LTE Mobile Communication Systems. In Network and Distributed System Security Symposium . Internet Society.

[154] Stephen Smalley and Robert Craig. 2013. Security Enhanced (SE) Android: Bringing Flexible MAC to Android. In

Proc. of NDSS 2013 . 18.

[155] Raphael Spreitzer, Felix Kirchengast, Daniel Gruss, and Stefan Mangard. 2018. Procharvester: Fully automated

analysis of procfs side-channel leaks on android. In Proceedings of the 2018 on Asia Conference on Computer and

Communications Security . 749–763.

[156] Sampath Srinivas and Karthik Lakshminarayanan. 2019. Simplifying identity and access management of your

employees, partners, and customers. https://cloud.google.com/blog/products/identity-security/simplifying-identity-

and-access-management-of-your-employees-partners-and-customers

[157] Jeff Vander Stoep and Chong Zhang. 2019. Queue the Hardening Enhancements. https://android-developers.

googleblog.com/2019/05/queue-hardening-enhancements.html

[158] Andrew S. Tanenbaum and Herbert Bos. 2014. Modern Operating Systems (4th ed.). Prentice Hall Press, Upper Saddle

River, NJ, USA.

[159] Adrian Tang, Simha Sethumadhavan, and Salvatore Stolfo. 2017. CLKSCREW: Exposing the Perils of Security-

Oblivious Energy Management. In 26th USENIX Security Symposium (USENIX Security 17) . USENIX Association,

Vancouver, BC, 1057–1074. https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/

tang

[160] Platform Hardening Team. 2020. System hardening in Android 11. https://security.googleblog.com/2020/06/system-

hardening-in-android-11.html

---

## Page 47

The Android Platform Security Model (2023) 47

[161] Sai Deep Tetali. 2018. Keeping 2 Billion Android devices safe with machine learning. https://android-developers.

googleblog.com/2018/05/keeping-2-billion-android-devices-safe.html

[162] Daniel R. Thomas, Alastair R. Beresford, and Andrew Rice. 2015. Security Metrics for the Android Ecosystem.

In Proceedings of the 5th Annual ACM CCS Workshop on Security and Privacy in Smartphones and Mobile Devices

(Denver, Colorado, USA) (SPSM’15) . Association for Computing Machinery, New York NY USA, 87–98. https:

//doi.org/10.1145/2808117.2808118

[163] Caroline Tice, Tom Roeder, Peter Collingbourne, Stephen Checkoway, Úlfar Erlingsson, Luis Lozano, and Geoff Pike.

2014. Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM. In 23rd USENIX Security Symposium (USENIX

Security 14) . USENIX Association, San Diego, CA, 941–955. https://www.usenix.org/conference/usenixsecurity14/

technical-sessions/presentation/tice

[164] Sami Tolvanen. 2017. Hardening the Kernel in Android Oreo. https://android-developers.googleblog.com/2017/08/

hardening-kernel-in-android-oreo.html

[165] Sami Tolvanen. 2018. Control Flow Integrity in the Android kernel. https://security.googleblog.com/2018/10/posted-

by-sami-tolvanen-staff-software.html

[166] Sami Tolvanen. 2019. Protecting against code reuse in the Linux kernel with Shadow Call Stack. https://security.

googleblog.com/2019/10/protecting-against-code-reuse-in-linux_30.html

[167] Güliz Seray Tuncay, Soteris Demetriou, Karan Ganju, and Carl A Gunter. 2018. Resolving the predicament of android

custom permissions. In Network and Distributed Systems Security (NDSS) Symposium .

[168] Güliz Seray Tuncay, Soteris Demetriou, and Carl A Gunter. 2016. Draco: A system for uniform and fine-grained access

control for web code on android. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications

Security . 104–115.

[169] Güliz Seray Tuncay, Jingyu Qian, and Carl A Gunter. 2020. See no evil: phishing for permissions with false transparency.

In n 29th USENIX Security Symposium (USENIX Security 20) . 415–432.

[170] Victor van der Veen, Yanick Fratantonio, Martina Lindorfer, Daniel Gruss, Clementine Maurice, Giovanni Vigna,

Herbert Bos, Kaveh Razavi, and Cristiano Giuffrida. 2016. Drammer: Deterministic Rowhammer Attacks on Mobile

Platforms. ACM Press, 1675–1689. https://doi.org/10.1145/2976749.2978406

[171] Jeff Vander Stoep. 2015. Ioctl Command Whitelisting in SELinux. http://kernsec.org/files/lss2015/vanderstoep.pdf

Linux Security Summit.

[172] Jeff Vander Stoep. 2016. Android: Protecting the Kernel. https://events.static.linuxfound.org/sites/events/files/slides/

Android-%20protecting%20the%20kernel.pdf Linux Security Summit.

[173] Jeff Vander Stoep. 2017. Shut the HAL up. https://android-developers.googleblog.com/2017/07/shut-hal-up.html

[174] Jeff Vander Stoep. 2022. Memory Safe Languages in Android 13. https://security.googleblog.com/2022/12/memory-

safe-languages-in-android-13.html

[175] Jeff Vander Stoep and Stephen Hines. 2021. Rust in the Android platform. https://security.googleblog.com/2021/04/

rust-in-android-platform.html

[176] Jeff Vander Stoep and Sami Tolvanen. 2018. Year in Review: Android Kernel Security. https://events.linuxfoundation.

org/wp-content/uploads/2017/11/LSS2018.pdf Linux Security Summit.

[177] Peter Visontay and Bessie Jiang. 2021. Making permissions auto-reset available to billions more devices. https:

//android-developers.googleblog.com/2021/09/making-permissions-auto-reset-available.html

[178] W3C. [n.d.]. Web Authentication: An API for accessing Public Key Credentials. https://webauthn.io/

[179] Andrew Walbran. 2023. Bare-metal Rust in Android. https://security.googleblog.com/2023/10/bare-metal-rust-in-

android.html

[180] R. Watson. 2012. New approaches to operatng system security extensibility . Technical Report UCAM-CL-TR-818.

Cambridge University. http://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-818.pdf

[181] Primal Wijesekera, Arjun Baokar, Ashkan Hosseini, Serge Egelman, David Wagner, and Konstantin Beznosov. 2015.

Android Permissions Remystified: A Field Study on Contextual Integrity. In 24th USENIX Security Symposium (USENIX

Security 15) . USENIX Association, Washington, D.C., 499–514. https://www.usenix.org/conference/usenixsecurity15/

technical-sessions/presentation/wijesekera

[182] Linux Kernel Security Subsystem Wiki. 2019. Exploit Methods/Userspace execution . https://kernsec.org/wiki/index.

php/Exploit_Methods/Userspace_execution

[183] Shawn Willden. 2018. Insider Attack Resistance. https://android-developers.googleblog.com/2018/05/insider-attack-

resistance.html

[184] Amy Wilson. 2021. Android 12 simplifies security for work devices. https://blog.google/products/android-

enterprise/android-12-developer-preview/

[185] Xiaowen Xin. 2018. Titan M makes Pixel 3 our most secure phone yet. https://blog.google/products/pixel/titan-m-

makes-pixel-3-our-most-secure-phone-yet/

---

## Page 48

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

48 Piqueras Jover, and Michael A. Specter

[186] Keun Soo Yim, Iliyan Malchev, Andrew Hsieh, and Dave Burke. 2019. Treble: Fast Software Updates by Creating an

Equilibrium in an Active Software Ecosystem of Globally Distributed Stakeholders. ACM Trans. Embed. Comput. Syst.

18, 5s, Article 104 (Oct. 2019), 23 pages. https://doi.org/10.1145/3358237

[187] David Zeuthen, Shawn Willden, and René Mayrhofer. 2020. Privacy-preserving features in the Mobile Driving

License. https://security.googleblog.com/2020/10/privacy-preserving-features-in-mobile.html

[188] Yuan Zhang, Min Yang, Bingquan Xu, Zhemin Yang, Guofei Gu, Peng Ning, X. Sean Wang, and Binyu Zang. 2013.

Vetting Undesirable Behaviors in Android Apps with Permission Use Analysis. In Proceedings of the 2013 ACM SIGSAC

Conference on Computer & Communications Security (Berlin, Germany) (CCS ’13) . ACM, New York, NY, USA, 611–622.

https://doi.org/10.1145/2508859.2516689

---

## Page 49

The Android Platform Security Model (2023) 49

A TOWARDS A FORMAL NOTATION OF ANDROID SECURITY MODEL RULES

Standard access control models are traditionally based on a matrix notation of ( 𝑆, 𝑂, 𝐴 ) triples

with subjects, objects, and a defined set of access permissions 𝐴 [ 𝑠, 𝑜 ] (typically read, write, and

execute) [77]. While the differences in specific implementations of this conceptual matrix (ACLs vs.

capabilities) are superfluous for our discussion, the basic notation is becoming limited [60] and

unfortunately not directly applicable to the Android model of multiple stakeholders and combining

multiple different types of security controls.

Within the scope of this first draft of a notation of the Android platform security meta model,

we define the involved stakeholders as parties 𝑃 ∈ 𝑷 for a set 𝑷 with pre-defined classes 38 :

• 𝑃 𝑈 denotes a user of the system. They may or may not be equivalent to the owner of the

hardware (client device such as a smart phone), where hardware ownership is defined as

out of scope of the security model at this time. However, users are assumed to own their

data.

• 𝑃 𝐷 denotes the developer of an app, which implicitly includes backend services used by

that app. That is, 𝑃 𝐷 is considered owner of the code that is executed by the app as well as

potential owner of data used as part of a service (such as video streaming).

• 𝑃 𝑃 denotes the Android platform or more specifically the set of system components that

are neither third-party apps nor representing user data. Examples are cell communication,

WiFi or Bluetooth services, standard UI elements, or hardware drivers.

• 𝑃 𝑂 denotes an optional organization that can place additional restrictions on the use of a

device, e.g. because it is owned by the organization or internal services are accessed through

the devices that require these security measures. Examples of relevant organizations are

employers or schools.

For a specific interaction, e.g. one particular user using one particular app to take a picture and

store it on the local filesystem of one particular Android system, the relevant stakeholders will be

specific instances of these classes, e.g. 𝑷 𝒑𝒉𝒐𝒕 𝒐𝒂𝒄𝒕 𝒊𝒐𝒏 = { 𝑃 𝑈 1 , 𝑃 𝐷 1 , 𝑃 𝑃 1 } . This set will usually include

3 or 4 (if an organization policy is in place) specific stakeholders, one from each class. The next

interaction may use a different set of specific stakeholders, such as another app, another user (using

the same app on the same platform), or continuing the use of the same app by the same user but on

a different device. To abstract from those specific use cases, we will use the short form ∀ 𝑃 to refer

to all stakeholders of a current interaction without loss of generality.

Each stakeholder 𝑃 has some elements:

• 𝑆 ( 𝑃 ) denotes the internal state of this stakeholder in the form of arbitrary data stored and

controlled by this party. This can take different forms, e.g. files, key/value preferences,

streams, etc. Note that the Android platform security model is primarily concerned with

internal state stored directly within the respective Android system (temporarily in RAM

or permanently on non-volatile storage), and data stored outside the physical system (e.g.

on cloud services) is considered out of scope. However, internal state of one stakeholder

(user account data, an app token, etc.) is often used to directly reference such data, and

some rules of the Android platform security model may therefore transitively apply to such

external data as well.

• 𝐶 ( 𝑃, 𝐴 ) ∈ { 𝑎𝑙𝑙𝑜𝑤, 𝑑𝑒𝑛𝑦 } denotes the run-time authorization decision of this party concern-

ing a specific action 𝐴 , which is generally considered to be the context of an authorization

query. The specific form of an authorization query varies significantly between stakeholder

38 These classes of stakeholders could also be seen as roles in an RBAC notation. However, there is no hierarchical relationship

between these stakeholders – they are intentionally considered to be peers – and therefore the RBAC notation seems less

useful in this case.

---

## Page 50

René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, Dianne Hackborn, Bram Bonné, Güliz Seray Tuncay, Roger

50 Piqueras Jover, and Michael A. Specter

classes (e.g. users will often authorize through a pop-up UI dialog while apps will typically

authorize through policies evaluated automatically in their application code) and between

actions.

The enforcing agent (e.g. platform components acting as security monitors) may cache and

re-apply previous authorization decisions without asking again depending on configured

policy. For example, user authorization expressed through run-time permissions (which

is only one way of users to express consent for a specific class of actions for which such

permissions are defined by the platform) can currently result in 𝐶 ( 𝑃 𝑈 , 𝐴 ) ∈ { 𝑎𝑙𝑙𝑜𝑤 −

𝑎𝑙𝑤𝑎𝑦𝑠, 𝑎𝑙𝑙𝑜𝑤 − 𝑜𝑛𝑐𝑒, 𝑎𝑙𝑙𝑜𝑤 − 𝑖𝑛 − 𝑓 𝑜𝑟𝑒𝑔𝑟𝑜𝑢𝑛𝑑, 𝑑𝑒𝑛𝑦 − 𝑜𝑛𝑐𝑒, 𝑑𝑒𝑛𝑦 − 𝑎𝑙𝑤𝑎𝑦𝑠 } and stored by

the permissions controller for future use. A current 𝑎𝑙𝑙𝑜𝑤 can therefore result from multiple

different responses such as { 𝑎𝑙𝑙𝑜𝑤 − 𝑎𝑙𝑤𝑎𝑦𝑠, 𝑎𝑙𝑙𝑜𝑤 − 𝑜𝑛𝑐𝑒 } .

With these preliminaries, we can more formally specify the access control aspects of Android

platform security model rules:

Rule ○ 1 (multi-party authorization). Authorization for executing an action 𝐴 depends on autho-

rization of all relevant parties.

𝐶 ( 𝐴 ) = 𝑎𝑙𝑙𝑜𝑤 ⇐⇒ ∀ 𝑃 : 𝐶 ( 𝑃, 𝐴 ) = 𝑎𝑙𝑙𝑜𝑤 (1)

Authorization typically grants (partial) access to the internal state of the stakeholder granting this

access.

𝐶 ( 𝑃, 𝐴 ) = 𝑎𝑙𝑙𝑜𝑤 = ⇒ 𝑆 (∀ 𝑃 ) ∋ 𝑓 ( 𝑆 ( 𝑃 ) , 𝐶 ( 𝐴 )) (2)

where 𝑓 ( 𝑆 ( 𝑃 )) denotes the access control function limiting access to the internal state of 𝑃 scoped

to the context of authorization to the current action 𝐴 . That is, the state accessible to all parties ∀ 𝑃

within the current interaction 𝐴 includes this additional state of the authorizing party 𝑃 . The type

of (partial) access, e.g. read or write, depends on the context of an action 𝐴 , but may be explicit in

the authorization query (e.g. read-only or read-write access permission to external storage).

Further, authorization of one party may depend on run-time context of another party such as

𝐶 ( 𝑃 𝑈 , 𝐴 ) = 𝑎𝑙𝑙𝑜𝑤 − 𝑖𝑛 − 𝑓 𝑜𝑟𝑒𝑔𝑟𝑜𝑢𝑛𝑑 ∧ 𝑈 𝐼 − 𝑓 𝑜𝑟𝑒𝑔𝑟𝑜𝑢𝑛𝑑 ∈ 𝑆 ( 𝑃 𝐷 ) = ⇒ 𝐶 ( 𝑃 𝑈 , 𝐴 ) = 𝑎𝑙𝑙𝑜𝑤

where 𝑃 𝑈 authorization depends on the UI state of 𝑃 𝐷 within the current interaction. There

is currently no complete set of all sub-instances of authorization decisions and their contextual

dependencies 39 , and the potential existence of a set sufficient for expressing all necessary conditions

is doubtful.

Within the lattice notation of mandatory access control (MAC) policies, this multi-party authoriza-

tion rule implies trivial lower (no authorization) and upper (all involved stakeholders authorization)

bounds. While the BLP model is still an underlying principle of SELinux policies and used for

Android sandboxing, it is only a part of the higher-level multi-party authorization: namely autho-

rization expressed by the platform components 𝑃 𝑃 𝑥 is internally derived through through BLP flows.

On this level of inter-component permission granting, potential future work could investigate the

applicability of the Take-Grant model [58] for reasoning about collusion issues. Comparison of the

expressive power under a meta model like [60] or [55] is another potential extension, although a

cross-abstraction comparison is at least non-obvious at this point.

39 This is especially true for context dependent authorization by apps 𝑃 𝐷 , which can use arbitrarily complex code to

implement their own decision process.

---

## Page 51

The Android Platform Security Model (2023) 51

Rule ○ 2 (open ecosystem). All stakeholder classes 𝑃 represent unbounded sets, and new specific

instances can be created at any time by any party: new users can be created on the system itself,

new apps can be published and installed without a central gatekeeping instance, and new platforms

(devices) can be created freely as long as they follow these rules (cf. rule 3 ○ ).

Rule ○ 4 (safe reset).

∀ 𝑃 : 𝑆 ( 𝑃 ) : = ∅ (3)

For the developer 𝑃 𝐷 , resetting their state is interpreted as uninstalling the app from a specific

platform and clearing all app data in the process. For user 𝑃 𝑈 and platform 𝑃 𝑃 resetting state implies

removing a user account or invoking reset to factory default. The implication is that this also resets

all authorization from the resetting party, as authorization is defined as (partial) access to internal

state.

Rule ○ 5 (applications as principals). A developer can have multiple apps, which have distinct

internal state. That is, a developer 𝑃 𝐷 actually manages a set of parties 𝑃 𝐴 in the form of all apps

they sign with their developer key.

𝑃 𝐷 ⊃ { 𝑃 𝐴 1 , ..., 𝑃 𝐴 𝑛 } (4)

Apps within a single developer 𝑃 𝐷 can explicitly share each other’s authorization decisions by

requesting to be installed with the same shared UID (which implies signature with the same

developer key). One of the key elements of rule 5 ○ , namely that apps 𝑃 𝐴 do not implicitly represent

users 𝑃 𝑈 is already enforced through keeping their internal state separate (as defined above in

preliminaries).

Rule ○ 3 (compatibility). Compatibility is the most difficult to express formally, and we only

give an intuitive sketch here. As mentioned in Section 3, the Android platform security model by

practical necessity spans multiple layers of abstraction. Compatibility therefore requires a rule on a

meta level: all potential instances of user 𝑃 𝑈 , developer 𝑃 𝐷 , app 𝑃 𝐴 , and organization 𝑃 𝑃 operate

under the other rules and can continuously update their state and authorization decisions, while

the platform 𝑃 𝑃 — specifically as the set of mutually untrusted components enforcing the other

rules on different layers — is pinned to a specific version of AOSP to implement the rules of this

model. If 𝑃 𝑃 fails to fully implement this meta rule, all other rules automatically become invalid.

That is, invalidation of any rule leads to invalidation of all others . Other parties need to learn of

an invalid 𝐷 𝑃 so that they can revoke their own authorization (e.g. users re-installing the system

image to revert to a known-good state). This directly complements (and effectively enables) Rule

○ 2 because it allows other parties to trust 𝑃 𝑃 (which often enforces authorization decisions by these

parties).

On a formal level, enforcement of this rule must necessarily be performed outside the platform

security model (hence the elevation to a meta rule) and therefore assumes a trusted third party

for platform verification. In the current Android ecosystem, this rule is implemented through a

combination of automated test suites (including CTS and VTS, which are available as part of AOSP

itself), platform attestation keys provisioned by OEMs and signed by Google for systems verifiably

passing those test suites, and APIs to query these attestation results that can be used by the other

parties at run-time.

Note that this first formalization only captures the access control implication of the model rules.

It is subject to future work to evaluate if these rules could be formulated under a meta model like

[55] and be expressed in tandem with access control models of underlying security controls such

as MAC policies in the kernel. However, such an endeavour only seems useful if cross-abstraction

validation can then be performed using automated tools.

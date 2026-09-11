---year: 2025

secverify_category: "Category A"
categories:
  - "[[1D.2-密碼學與協議安全審計 (Cryptographic & Protocol Security)]]"
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
title: "KeyDroid: A Large-Scale Analysis of Secure Key Storage in Android Apps"
author: "Jenny Blessing; Ross J. Anderson; Alastair R. Beresford"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 24
source: "KeyDroid (2011) A Large-Scale Analysis of Secure Key Storage in Android Apps.pdf"
---

# KeyDroid: A Large-Scale Analysis of Secure Key Storage in Android Apps

> **文獻存檔**：[PDF 原文](<../../raw-papers/2025/KeyDroid (2025) A Large-Scale Analysis of Secure Key Storage in Android Apps.pdf>) | [Markdown 原文](<../../raw-papers/2025/KeyDroid (2025) A Large-Scale Analysis of Secure Key Storage in Android Apps (Raw).md>)

> **作者**：Jenny Blessing; Ross J. Anderson; Alastair R. Beresford
> **總頁數**：24 頁

---

## Page 1

KeyDroid: A Large-Scale Analysis of

Secure Key Storage in Android Apps

| Jenny Blessing | Ross J. Anderson | Alastair R. Beresford |
| --- | --- | --- |
| University of Cambridge | University of Cambridge | University of Cambridge |

University of Edinburgh

| Abstract | device access. Similarly, sensitive data may be accessed by |
| --- | --- |
| Most contemporary mobile devices offer hardware-backed | an adversary who is able to compromise the main operating |
| storage for cryptographic keys, user data, and other sensitive | system (OS), such as malicious third-party apps which cir- |
| credentials. Such hardware protects credentials from extrac- | cumvented app store vetting processes or were independently |
| tion by an adversary who has compromised the main operat- | downloaded by users [82, 86]. |
| ing system, such as a malicious third-party app. Since 2011, | Modern encryption methods may provide data confidential- |
| Android app developers can access trusted hardware via the | ity and integrity against such threats, but data is only as secure |
| Android Keystore API [24]. In this work, we conduct the first | as the cryptographic keys used. Keys stored in a software key- |
| comprehensive survey of hardware-backed key storage in An- | store (e.g., Java’s Bouncy Castle keystore) are vulnerable to |
| droid devices. We analyze 490,119 Android apps, collecting | memory-extraction attacks [60, 77] where an adversary with |
| data on how trusted hardware is used by app developers (if | full control over the operating system or physical access to |
| used at all) and cross-referencing our findings with sensitive | the device can retrieve the decryption keys or other sensitive |
| user data collected by each app, as self-reported by developers | data through a memory dump of device RAM. |
| via the Play Store’s data safety labels [75]. | Fortunately, mobile device key storage has seen major se- |
| We find that despite industry-wide initiatives to encourage | curity improvements over the past decade: almost all modern |
| adoption, 56.3% of apps self-reporting as processing sensitive | mobile handsets now offer some form of hardware-backed |
| user data do not use Android’s trusted hardware capabilities | credential storage capable of protecting keys against an ad- |
| at all, while just 5.03% of apps collecting some form of sensi- | versary with root permissions [50]. The most common form |
| tive data use the strongest form of trusted hardware, a secure | of hardware-backed storage (commonly called “trusted hard- |
| element distinct from the main processor. To better under- | ware” or “secure hardware”) is the trusted execution environ- |
| stand the potential downsides of using secure hardware, we | ment (TEE), a special mode of operation by the main proces- |
| conduct the first empirical analysis of trusted hardware perfor- | sor (e.g., Arm TrustZone or Intel VT). Keys are generated |
| mance in mobile devices, measuring the runtime of common | and stored within specialized hardware, and all cryptographic |
| cryptographic operations across both software- and hardware- | operations using these keys take place within the hardware |
| backed keystores. We find that while hardware-backed key | component. Provided the TEE is not compromised, these op- |
| storage using a coprocessor is viable for most common cryp- | erations cannot be inspected or interfered with by the Android |

arXiv:2507.07927v1 [cs.CR] 10 Jul 2025

| tographic operations, secure elements capable of preventing | OS (e.g., an attacker who compromises the device cannot |
| --- | --- |
| more advanced attacks make performance infeasible for sym- | extract keys or use them to decrypt data stored off-device). |
| metric encryption with non-negligible payloads and any kind | Android has offered the Android Keystore system [24] as its |
| of asymmetric encryption. | public trusted hardware API for developers since 2011. |

Recent premium models of Android smartphones such as

the Google Pixel devices contain additional hardware in the

1 Introduction form of a separate secure processor, commonly known as a

secure element (SE) [24, 55]. While a TEE is a separate OS

| Mobile devices store highly sensitive user data ranging from | on the main processor, an SE is an entirely separate proces- |  |  |
| --- | --- | --- | --- |
| private health information and payment credentials to per- | sor with its own CPU, memory, and storage. In Android, the |  |  |
| sonal photographs and correspondence. At the same time, | SE is called the | StrongBox Keymaster | [11]. The Android |
| mobile handsets are regularly lost or stolen, making data | Keystore API uses the device’s TEE by default but offers |  |  |
| stored on devices vulnerable to an adversary with physical | developers the option of requesting StrongBox instead. |  |  |

1

---

## Page 2

| Unfortunately, there is currently a lack of empirical ev- | significant performance hit. For instance, encrypting a 1MiB |  |  |
| --- | --- | --- | --- |
| idence on when and how developers use secure hardware | message with AES-GCM takes around 3 seconds and sim- |  |  |
| in practice. Secure hardware is only useful if it is actually | ply | generating | asymmetric keys in StrongBox takes over 9 |
| used, and the Android Security team acknowledges that apps | seconds in Google’s flagship Pixel 8 device, a runtime which |  |  |
| need to explicitly use these APIs in order to see a security | may be prohibitive even for security-conscious apps. Even so, |  |  |
| benefit as Android’s historical Java cryptography APIs use a | StrongBox’s performance has improved significantly since |  |  |
| software-backed keystore by default [61]. Furthermore, while | first introduced by Android in 2018 and is viable for use cases |  |  |
| hardware-backed keystores provide significant security bene- | involving small payloads, such as using StrongBox to encrypt |  |  |
| fits, runtime performance is a critical consideration for mobile | a key generated by a keystore with less overhead. To the |  |  |
| developers. More advanced forms of secure hardware (e.g., | best of our knowledge this is the first time comprehensive |  |  |
| StrongBox), tend to come with an accompanying performance | performance measurements of trusted hardware in mobile |  |  |
| hit, as acknowledged at a high level in Android’s documen- | devices have been published, providing Android developers |  |  |
| tation [11], but to date there has been no publicly available | with empirical evidence to make informed decisions for their |  |  |
| empirical data on hardware keystore performance to the best | particular use case. |  |  |
| of our knowledge. At the same time, however, Android is pur- | Our specific contributions are as follows: |  |  |

suing public initiatives to encourage wider adoption of secure

tematic study of secure credential storage in Android, an-

storage in Android. We find that 56.3% of apps report collect-

ing sensitive data as part of the Play Store’s data safety labels

do not use any form of trusted hardware, and only 5.03% con-

tain a reference to the SE API. Moreover, these usage figures

represent an upper bound on security within the Android app

ecosystem as it is not possible to detect at scale whether apps

which contain at least one reference to the Android Keystore

API are using it to secure all sensitive and relevant credentials.

In particular, of those apps that do use the Android Keystore

API, 94.7% of key initializations are located in third-party

components, indicating that use of the Keystore API may be

due to using a general-purpose library rather than a conscious

choice to use hardware-backed key storage. Furthermore, we

2

2 Key Storage in Android

At a systems level, Android provides three options for storing

cryptographic keys and other sensitive credentials: a software

keystore via long-standing Java APIs, hardware-backed key

storage logically separated from the main Android Operating

System (OS) to protect against OS compromise, and hardware-

backed key storage located on a separate processor to guard

against the most advanced logical and physical attacks. We

discuss security properties and limitations of each below.

| hardware such as the Android Ready SE Alliance (see §2.2.2). | • We design KeyDroid, a tool for static analysis of key |  |  |  |
| --- | --- | --- | --- | --- |
| The lack of empirical evaluation of performance and exist- | storage in Android apps. |  |  |  |
| ing usage patterns is a major barrier to encouraging more | • Conduct large-scale static analysis of | ∼ | 500,000 apps |  |
| widespread adoption: without detailed performance statistics, | to understand how trusted hardware is used, cross- |  |  |  |
| developers cannot make informed choices about the trade-offs | referencing results with user data collection practices. |  |  |  |
| between security and performance for their use case. | • Run comprehensive measurements of key storage perfor- |  |  |  |
| In this work, we conduct the first comprehensive and sys- | mance on all hardware primitives in Android devices. |  |  |  |
| alyzing both the contemporary usage and performance of | • Conduct a developer survey to better understand factors |  |  |  |
| key storage schemes. We compile and analyze a dataset of | influencing developer decisions about trusted hardware. |  |  |  |
| 490,119 Android applications between October 2023 and Au- | • Provide developers with concrete guidance on trusted |  |  |  |
| gust 2024, extracting data from 64 API calls relevant to key | hardware usage patterns and performance. |  |  |  |
| find that 8.5% of keys generated in the Android Keystore | 2.1 | Software-backed Key Storage |  |  |
| explicitly disable Android’s randomized encryption require- | Mobile devices have historically relied on software keystores |  |  |  |
| ment (i.e., IND-CPA), indicating that secure defaults are not | which operate within the mobile OS and use the device’s in- |  |  |  |
| enough to enforce security guarantees. | ternal storage. Java’s Cipher API [10] and the Java Keystore |  |  |  |
| Having measured the usage of secure key storage across | API [14] using a software-backed provider (either Bouncy |  |  |  |
| the Android app ecosystem, we investigate the runtime per- | Castle or AndroidOpenSSL, also known as Conscrypt [27]) |  |  |  |
| formance of common cryptographic operations using the | are both examples of software-backed keystores within An- |  |  |  |
| hardware-backed key storage APIs to consider whether per- | droid that have been available since Android’s inception in |  |  |  |
| formance overhead may discourage adoption. We find that | 2007. On all Android devices today, if no keystore provider |  |  |  |
| the performance of TEE-backed key storage is viable for the | is specified when using Java’s cryptographic APIs (namely |  |  |  |
| vast majority of common app use cases and is noticeably | java.security.* | and | javax.crypto.* | ) Android defaults |
| different from a software-backed keystore only for large pay- | to using a software-backed keystore even if the device sup- |  |  |  |
| loads greater than 5 MiB. StrongBox introduces a far more | ports hardware-backed key storage [41, 81]. |  |  |  |

---

## Page 3

| Software key storage implementations are vulnerable to | string alias. In Android, the TEE is located on the main pro- |  |  |
| --- | --- | --- | --- |
| memory extraction attacks, where an adversary with root per- | cessor, which is divided into the Android OS and the Trusty |  |  |
| missions in the Android operating system can observe the key | OS [22], also commonly referred to as the | normal world | and |
| as it is decrypted in RAM while being used [48, 60]. Mobile | the | secure world | . The hardware used to protect the normal |
| applications are particularly vulnerable to such attacks since | world from the secure world depends on the processor ar- |  |  |
| apps are long-running processes and keys stored in memory | chitecture: TrustZone is used for ARM-based systems and |  |  |
| are not garbage collected until a process has terminated. Mal- | provides dual execution environments [68] while Intel x86 |  |  |
| ware, malicious third-party apps, and other privileged users | uses virtualization technology to provide similar support [52]. |  |  |
| are all capable of compromising the underlying OS, including | The primary security benefit of a TEE is to guard against |  |  |
| kernel access control measures, and launching an attack of | kernel compromise, including malicious applications installed |  |  |
| this sort. | on the device which could request root permissions [61, 71]. |  |  |
| Prior work investigating Java cryptography APIs has also | The Android kernel and applications run in the normal world, |  |  |
| observed that these libraries have an unfortunate tendency to | while the secure world (i.e., the hardware enclave) stores |  |  |
| use the weakest ciphers as defaults (ECB mode with sym- | long-term cryptographic key material and performs opera- |  |  |
| metric encryption being the most pervasive example) [42, 45]. | tions using these keys. Trusted hardware has numerous other |  |  |
| Such choices shift the responsibility for achieving an adequate | benefits for mobile device security, such as enabling hardware |  |  |
| security level from the API provider to the developer. | root of trust schemes to authenticate firmware running on the |  |  |

device, but in this paper we focus on the direct security to app

developers for storing and using cryptographic keys.

2.2 Hardware-backed Key Storage

In Android, a TEE has been available since Android 4.3

| The defining feature of hardware-backed key storage is that | (API level 18) was released in 2013, with new features added |  |  |
| --- | --- | --- | --- |
| keys are stored and used in hardware separate from the main | over the years since [24, 38]. The initial version of the An- |  |  |
| OS. A compromise of the Android operating system, then, | droid Keystore only supported asymmetric cryptographic op- |  |  |
| will not compromise any cryptographic keys or other pro- | erations and did not add support for symmetric keys until |  |  |
| cesses running inside the hardware element. Importantly, se- | Android 6.0 (API level 23) in 2015 (approximately two years |  |  |
| cure hardware ensures that keys will never be revealed in | after the initial release date). Hardware-level key attestation, |  |  |
| memory while they are used (and therefore cannot be viewed | the ability to verify that keys are indeed stored in a hardware- |  |  |
| or extracted even by a privileged user). | backed keystore, and other more advanced features were in- |  |  |
| The vast majority of modern smartphones today contain | troduced in Android 7.0 (API level 24) [23]. |  |  |
| at least some form of secure execution environment [50, 61]. | In addition to hardware-derived security benefits, the Key- |  |  |
| We use the terms “secure hardware”, “trusted hardware”, and | store API makes deliberate design choices that provide an |  |  |
| “hardware enclave” interchangeably throughout this work to | increased level of security in practice when compared with |  |  |
| broadly characterize hardware-backed key storage. | older Java APIs. The API explicitly disallows certain inse- |  |  |
| There are two main forms of hardware-backed key storage | cure key configurations, such as symmetric encryption with a |  |  |
| in the Android ecosystem, each offering different security | constant initialization vector, and offers more secure defaults. |  |  |
| properties: (1) a trusted execution environment (TEE), avail- | While TEEs offer substantial benefits over software-backed |  |  |
| able in Android through the | Android Keystore | API [24] | key storage, including protection from memory extraction, |
| and (2) a secure element (SE), termed ( | StrongBox Keymas- | they are still vulnerable to various physical attacks, including |  |
| ter | [11] and provided as a subset of the Android Keystore | side-channel attacks. There have been several documented |  |
| API. We discuss each of these in turn below as different | attacks on Intel SGX [36, 79, 80], which is an example of a |  |  |
| forms of secure hardware vary in degree of isolation from | TEE; most of these were side-channel attacks [64]. Prior work |  |  |
| the Android OS, and hence the attacks they protect against. | has also discovered several architectural design flaws in ARM |  |  |
| Throughout the rest of the paper, we use the terms “Android | TrustZone implementations leaving data stored even in TEEs |  |  |
| Keystore” and “Keystore” to refer specifically to Android’s | potentially vulnerable to sophisticated threat actors [35, 74]. |  |  |
| trusted hardware API (either TEE or SE). | To protect against the most advanced attacks, a device needs |  |  |

to contain a hardware element entirely separate from the main

2.2.1 Trusted Execution Environment processor: a secure element.

A trusted execution environment (TEE) is a discrete area of

2.2.2 Secure Element

the main processor intended to provide a more secure, logi-

| cally isolated execution environment. It has its own operating | Most premium Android smartphones include a secure element |
| --- | --- |
| system (named Trusty in Android [22]), and communicates | (SE), a form of hardware security module (HSM) which must |
| with the Android OS through requests forwarded through the | have its own CPU and storage, tamper-resistant packaging, |
| Android Keystore interface to the TEE, referencing keys by a | and a true random number generator [11, 24]. An SE provides |

3

---

## Page 4

all the benefits of a TEE and more: the increased isolation

from the main Android OS and processor provides resistance

to various side-channel attacks, including cold-boot memory

attacks and shared-resource attacks [24]. As with a TEE, cryp-

tographic keys are generated and stored within the confines of

the SE, and any operations performed using the key material

take place within the hardware so the key never enters an ap-

plication’s host memory. Different hardware elements are not

mutually exclusive—for instance, a mobile device containing

an entirely separate SE will almost certainly also contain a

TEE as part of its main processor.

Android’s public SE API is termed the StrongBox Key-

chip (SoC) hardware, or integrated secure elements (iSE),

qualify as providing StrongBox support as long as they meet

the requirements above [24]. In 2021, Google’s Pixel 6 intro-

among other features [55]; Google Tensor interfaces with the

novel in mobile handsets, Hugenroth et al. [50] estimated se-

cure element availability in contemporary mobile devices and

found that as of 2023, 96% of iPhones and 45% of Android

devices offer some form of SE. We expect these percentages

will increase in future years as older devices are cycled out.

Spurred on by the advanced security properties SEs can pro-

vide, industry firms have invested significant resources into

encouraging the development and adoption of HSM schemes:

Google launched the Android Ready SE Alliance in 2021,

a “collaboration between Google and Secure Element (SE)

vendors” that aims to make discrete hardware-backed storage

(e.g., StrongBox) “the lowest common denominator for the

Android ecosystem” and to facilitate interoperability and con-

sistency across secure element vendors within the Android

ecosystem [3, 49]. We discuss recommended best practices

and legal mandates in further detail in §A.1.

Despite the industry shift towards SEs as the desirable and

intended outcome, to the best of our knowledge there have

been no prior studies on the usage or performance of this form

of trusted hardware. This is of particular concern since SEs

are widely acknowledged to reduce performance. Google’s

documentation in particular described StrongBox’s perfor-

mance as “a little slower and resource-constrained (meaning

that it supports fewer concurrent operations) compared to

TEE”, and recommends StrongBox for developers who “want

to prioritize higher security guarantees over app resource

efficiency” [24]. Due to these performance drawbacks, the

Android Keystore API is structured so that developers must

4

and call packages.

Trusted hardware is not a panacea: although hardware-backed

key storage prevents keys from being exported off-device or

revealed in memory, the keys can still be used on-device by

an attacker with root privileges, a “fundamental limitation”

of hardware-backed storage [37, 61]. Even so, the adversary

will only be able to decrypt data stored on the device which,

depending on the application, may limit the damage they

can cause if they are unable to use the keys to decrypt data

stored off the device (e.g., data stored on a remote server).

Additional authentication requirements prior to key use can

also substantially mitigate this risk.

Furthermore, the use of hardware-backed protection for

cryptographic key material is “best effort” in the sense that

the Android Keystore API uses the TEE if it is available

on the device (or SE if specially requested), but reverts to a

software-backed keystore otherwise. The default reversion

to a software-backed keystore instead of throwing an error

reflects a desire to support backwards compatibility and a

fragmented Android ecosystem containing many different

device vendors with different price budgets and hardware

specifications. Developers who desire to require hardware-

backed storage as the minimum security level of their product

can add runtime conditional checks hardware availability and

adjust accordingly. A key goal of this work, then, is to ex-

plore whether app developers do indeed request to use trusted

hardware on devices where it is available.

| master | [11] (henceforth abbreviated as StrongBox) and has | Figure 1: KeyDroid Stages: | We (1) scrape Play Store meta- |
| --- | --- | --- | --- |
| been available to external developers since Android 9.0 (API | data and data safety information for all apps in the AndroZoo |  |  |
| level 28) was released in August 2018 [24]. An SE was first in- | dataset with at least 10,000 downloads and (2) decompile |  |  |
| troduced in Pixel devices, Google’s flagship device line, with | each app and pre-screen for any relevant API references. If |  |  |
| the Titan M chip (Google’s in-house secure element proces- | an app contains a reference to the Android Keystore API, we |  |  |
| sor) in the Pixel 3 in 2018 [85]. This was upgraded to the Titan | run KeyDroid, our in-depth static analysis tool, to generate |  |  |
| M2 chip beginning with the Pixel 6 in 2021 [55]. System-on- | the app call graph and extract all API references, arguments, |  |  |
| duced Google Tensor, a system-on-chip (SoC) that is isolated | explicitly opt in to using StrongBox even when the application |  |  |
| from the main processor but also has its own CPU and ROM, | is running on a device that contains a SE. |  |  |
| Titan M2 chip. While secure elements are still comparatively | 2.3 | Key Considerations |  |

---

## Page 5

| 3 | Methodology | 3.3 | Static Analysis |
| --- | --- | --- | --- |
| We begin by describing our process for collecting our dataset | To reduce computational load, we use multiple layered static |  |  |
| of Android apps and analyzing these apps with respect to | analysis techniques to filter for references to Android’s trusted |  |  |
| API usage. Figure 1 provides a high-level overview of all | hardware APIs and extract relevant API calls. We begin by |  |  |
| app analysis stages. We further describe our methodology for | executing a basic keyword search across all APKs in our |  |  |
| testing the runtime performance of different keystores across | dataset, and then perform more in-depth static analysis on any |  |  |
| common cryptographic operations. | APKs flagged as relevant. |  |  |

We use the publicly available AndroZoo dataset [6] as

our source for Android applications. We initially identify

8,804,118 apps in the AndroZoo dataset from the Play Store

marketplace which were crawled on or after July 2013, when

Android’s trusted hardware API was first released to devel-

opers, though this number includes different versions of the

same app and apps no longer available for download. We nec-

essarily only consider free apps since the AndroZoo dataset

does not include paid apps.

For each app provided in the AndroZoo dataset that passed

preliminary filtering, we scrape the Play Store between Octo-

ber 2023 to March 2024 to filter for apps currently available

at the point of scraping with at least 10,000 downloads. We

collect other relevant app metadata at the same time, resulting

in a dataset of 490,119. We were able to successfully down-

load and decompile almost all of these apps, leaving us with a

revised dataset of 486,234. We record the following metadata

for each app: app package ID, title, number of installs, devel-

oper name and email, Play Store genre, release date of the

latest version (release date of initial version is not available),

and version number.

We download the Android Package (.apk) archive file con-

taining the app source code, metadata, and other resource

files for each of these 486,234 apps. When there are multiple

versions of the same app (as identified using Android’s APK

package name) available in the AndroZoo dataset, we use the

most recently crawled version.

App key storage is only a concern if the app processes sensi-

tive or confidential data. Since July 2022 Google has required

each app listed in the Play Store to complete a data safety

form containing self-reported information from the app devel-

opers on what types of user data the app collects and shares

with third-parties, and for what purpose; this includes data

collected by third-party libraries. For instance, the Signal mes-

saging app notes that it collects only a user’s phone number

for “app functionality and account management”, and does

not share data with third parties [76]. We provide further

specifics on what data is considered to be sensitive and dis-

cuss limitations of developer-reported data in §A.2.

5

Keyword Filtering. Since analyzing the call graph is very

pile each .apk file using apktool [28] and run an initial

grep search for any call to the Android KeyStore API

( android.security.keystore ). After filtering out any

apps that do not contain at least one reference to the Key-

store API, we are left with a dataset of 122,305 apps.

Inter-Procedural Call Graph Analysis. To analyze the byte-

code of the 303,948 apps flagged as having at least one rele-

vant API call, we use Soot [2], a well-known framework for

inter-procedural static analysis [57] also used by similar re-

lated work. We experimented with using FlowDroid and other

static analysis tools that more accurately model the Android

lifecycle (e.g., by detecting implicit callback methods such as

onCreate or onClickListener ) but found that the runtime

was sufficiently large as to make it infeasible for a dataset of

our size, in large part due to its iterative callback calculation,

which recomputes the call graph each time a new callback is

encountered. Prior work [84] showed that Flowdroid did not

finish app call graph generation on 24% of apps even with a

timeout of 5 hours, consistent with our own observations, and

so we ultimately determined Soot offered the right balance of

accuracy and efficiency.

We allocate each APK 10GB RAM and set an automatic

timeout of 30 minutes. Our analysis tool begins by generating

the call graph of the APK to determine the context for a

particular API reference. To keep runtime manageable, we

assume that all methods are reachable while generating the

initial call graph, and conduct a custom reachability analysis

(described in more detail below) tracing backwards from a

We search for 64 distinct API calls, including all methods

from the primary KeyStore API as well as other Android

cryptography APIs that in turn call the KeyStore API, such

as androidx.security.crypto.MasterKey [15] and an-

droid.security.keystore.KeyProtection [13], and the

primary methods from the Java KeyStore [14] and Cipher

APIs [10]. The Java cryptographic APIs allow developers

to specify a keystore provider, and so we check these to see

if developers are referencing the Keystore API indirectly.

The full list of specific API methods searched for is avail-

able in our dataset in Table 11 in the Appendix. For each

API call identified, we collect the full method signature of

the calling method, including associated package and class

names, record the object on which the method is called (i.e.,

| 3.1 | Dataset Selection | resource-intensive, to filter candidate apps we first decom- |
| --- | --- | --- |
| 3.2 | Play Store Data Safety Labels | method of interest along the method call chain. |

---

## Page 6

register value), and extract all parameter values by applying 3.4 Performance Measurements

backwards program slicing [83]. As part of our reachability

analysis, we conduct a backwards breadth-first search and

trace each method containing a relevant API call backwards

through the call graph for up to 1,000 nodes, recording all

possible paths.

third-party by checking whether the same package is called by

et al. [67] (described in more detail below). While there are a

developers, we consider it to be third-party; otherwise, if it is

Reachability. Our call-graph generation methodology de-

scribed above errs on the side of favoring false positives over

false negatives (i.e., we would prefer to include a relevant

API call that may be unreachable than to exclude a call that is

used). To reduce the risk of false positives, once we have clas-

sified all packages as first-party or third-party, to determine

whether a particular API call is reachable we trace backwards

through the recorded call paths along the control flow. If there

exists at least one path containing a call to first-party source

code, we consider the API call to be reachable.

6

From the average developer’s perspective, perhaps the most

important consideration when choosing among different key

storage APIs is performance. A natural corollary to surveying

the usage of secure key storage is to investigate key storage

runtime performance, particularly among different forms of

total shown in Table 1.

distinct: if a particular API call is located within a third-party

same method numerous times.

4.1 Overall Usage

Of the 486,234 in our dataset (apps currently in the Play

Store with at least 10,000 downloads) which we were able

to download and decompile, through keyword searching as

described in §3.3 we find 122,305 apps containing a reference

to the Android Keystore API within their source code. This

provides us with an upper bound of 25.15% of apps within the

Play Store using device trusted hardware. If we consider only

the 159,241 apps self-reporting to the Play Store as collecting

| Package Analysis. | We are particularly interested in determin- | hardware-backed key storage. |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing whether a particular API call is located within the main | To conduct systematic performance measurements we |  |  |  |  |  |  |  |  |
| application code or whether it is part of a third-party library. | wrote a benchmarking test application that performs symmet- |  |  |  |  |  |  |  |  |
| First-party usage indicates that developers have consciously | ric and asymmetric key generation, message encryption, and |  |  |  |  |  |  |  |  |
| chosen to store cryptographic key material in trusted hard- | message signing following canonical examples provided in |  |  |  |  |  |  |  |  |
| ware, while for certain third-party libraries developers may | Android documentation and Android’s developer blog [12,53]. |  |  |  |  |  |  |  |  |
| be unaware that this is even occurring. | We use AWS Device Farm [1] to run our test application |  |  |  |  |  |  |  |  |
| To determine call context, we classify packages as first- or | across a variety of Android devices. |  |  |  |  |  |  |  |  |
| other APKs, following similar methodology used by Oltrogge | 4 | Secure Hardware Usage in Android |  |  |  |  |  |  |  |
| small number of public datasets of third-party library signa- | As the first step in our work, we conduct a comprehensive sur- |  |  |  |  |  |  |  |  |
| tures, we find that these are generally too outdated or other- | vey of all Android API calls relevant to key storage or trusted |  |  |  |  |  |  |  |  |
| wise incomplete to be fit for purpose (e.g., LibRadar [59] was | hardware, collecting arguments provided and relevant context |  |  |  |  |  |  |  |  |
| last updated in 2018). | (e.g., class and package name in which the call occurred). |  |  |  |  |  |  |  |  |
| We | collect | all | packages | containing | a | call | to | the | While we make every effort to retrieve the parameter argu- |
| Android | Keystore | key | generation | constructor | an- | ment via constant propagation in cases where static analysis |  |  |  |
| droid.security.keystore.KeyGenParameterSpec. | initially returns the register value, this is not always possible |  |  |  |  |  |  |  |  |
| Builder(String keystoreAlias, int purposes) | . | If | and thus in the results below the parameter total for a particu- |  |  |  |  |  |  |
| a package is referenced by multiple APKs from different | lar API method call is generally lower than the method call |  |  |  |  |  |  |  |  |
| referenced by only a single APK or by multiple APKs from | We further note that unless otherwise specified, statistics for |  |  |  |  |  |  |  |  |
| the same developer, we classify it as a first-party package. | API calls discussed throughout this section are not necessarily |  |  |  |  |  |  |  |  |
| Obfuscation. | We observe a significant amount of obfuscation | library, this call configuration (e.g., parameters) is then dupli- |  |  |  |  |  |  |  |
| of package names where package names are shortened and | cated in our findings for each call to this library (including |  |  |  |  |  |  |  |  |
| anonymized (e.g., | o8 | or | q1.x.a | ), likely due to built-in obfus- | across separate apps). We intentionally consider duplicates |  |  |  |  |
| cation techniques available to developers in Android Studio | in our findings since our purpose is to understand the state |  |  |  |  |  |  |  |  |
| and other widely used development tools. | of Android security and keystore usage in the wild, though |  |  |  |  |  |  |  |  |
| Different packages may share the same obfuscated name, | for certain highly relevant calls we will distinguish between |  |  |  |  |  |  |  |  |
| and so we exclude obfuscated packages from party analysis. | first-party (e.g., unique) calls and third-party library calls. |  |  |  |  |  |  |  |  |
| To identify non-obfuscated package names, if a package name | Similarly, we will frequently distinguish between API usage |  |  |  |  |  |  |  |  |
| has at least one sub-component (i.e., character string separated | as a percentage of total | calls | for a particular API method and |  |  |  |  |  |  |
| by periods) of at least three characters in length, we consider | percentage of individual | apps | containing at least one reference |  |  |  |  |  |  |
| it to be an authentic (non-obfuscated) package name. | to the method in question since a single app can reference the |  |  |  |  |  |  |  |  |

---

## Page 7

| sensitive data, we find 69,583 apps referencing the Android | choices without being hampered by source code obfuscation, |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Keystore API and the upper bound of trusted hardware use | we manually searched for instances of StrongBox disabling |  |  |  |  |
| rises to 43.7%. | on GitHub [47] as of January 2025. Of the 14 unique (i.e., non- |  |  |  |  |
| In practice, these calls may be located within components | fork) repositories which contained a call disabling StrongBox, |  |  |  |  |
| of third-party libraries not referenced by the app, or within | two repositories included a comment citing performance rea- |  |  |  |  |
| unreachable or legacy source code of the app itself. We then | sons while 10 opted out without explanation. The Salesforce |  |  |  |  |
| run our in-depth static analysis tool, KeyDroid, on all 122,305 | Android SDK, for instance, disables StrongBox as the run- |  |  |  |  |
| apps flagged as directly referencing the Android Keystore | time is "too slow" and therefore "not a good fit for [their] use |  |  |  |  |
| API in some capacity to verify which calls are reachable and | case" [72, 73]. The remaining two instances disabled only if |  |  |  |  |
| collect detailed statistics on how the API is used | 1 | . We are | a | StrongBoxUnavailableException | was thrown and were |
| able to successfully analyze 116,555 apps, with the remaining | therefore false positives. |  |  |  |  |
| 2.82% erroring out for various miscellaneous reasons, most | The nested structure of Android key generation makes it |  |  |  |  |
| commonly exceeding the time limit. | difficult to reliably link a key generation call (which speci- |  |  |  |  |
| The Android Keystore API further requires developers to | fies the algorithm to be used) with the Android Keystore’s |  |  |  |  |
| specify an intended purpose at the time of key initialization | parameter specification using call objects, and simply check- |  |  |  |  |
| and enforces this purpose when developers attempt to use the | ing whether both calls are located in the same method is too |  |  |  |  |
| key (e.g., a key specified as being intended for encryption | imprecise since a single method may generate multiple keys. |  |  |  |  |
| cannot later be used to sign). We find that of the 278,056 total | Instead, we can indirectly estimate ciphers used for Strong- |  |  |  |  |
| init calls for which we were able to retrieve the purpose value, | Box specifically by linking key size with Strongbox usage. |  |  |  |  |
| 92.31% of keys are designated as being used for encryption | For the 98 keys which set both StrongBox and the key size |  |  |  |  |
| and decryption only, while 5.60% are used for signing or | and for which we are able to retrieve both parameter values, |  |  |  |  |
| verifying message authentication codes. | we find that 97 of 98 keys used StrongBox with an | AES-256 |  |  |  |
| A full list of all Keystore API endpoints and their total | cipher while just one key used StrongBox to generate an | RSA- |  |  |  |
| usage counts is shown in §A.5. We discuss most methods | 2048 key | , a distribution which again suggests runtime is a |  |  |  |
| in more detail throughout this section. We further describe | major consideration when using StrongBox. |  |  |  |  |

how usage varies by Play Store category in §A.3, and describe

alternative keystores used from a manual review of a subset of

apps flagged as not using the Android Keystore API in §A.4.

StrongBox Usage. We find that 22,875 of the 116,555 apps

with any reference to the Android Keystore API (19.62%) fur-

ther contain a reference to the StrongBox API setIsStrong-

BoxBacked(boolean) , which is 4.7% as a percentage of the

overall dataset (and 5.03% as a percentage of apps collecting

sensitive data). However, since the API takes in a boolean

parameter some of these instances may explicitly request not

to use StrongBox. To calculate how many apps enable Strong-

Box, we are able to retrieve the argument value for 21,022 out

of 24,630 calls and find that while 94.85% of these instances

request to use StrongBox, the remaining 5.15% explicitly

opt out of using StrongBox and storing cryptographic key

material in the device’s secure element. Applying this per-

centage to the 22,875 apps referencing the API, we estimate

that 22,367 apps, or 4.6% of our overall dataset, request to use

StrongBox for at least one key. This percentage rises slightly

to 5.03% if we consider only apps self-reporting collecting

sensitive data. To better understand the context behind these

flagged as containing the string “AndroidKeystore” but did not contain any

cases this is due to requesting the Android Keystore provider via a different

Java API in potentially unreachable code (and so the Keystore API references

7

4.2 First-Party vs. Third-Party Usage

Here we present a package-level analysis of the location con-

text in which trusted hardware is referenced. In particular, we

are interested in determining whether apps flagged as using

trusted hardware are doing so as part of the core applica-

tion source-code or because the hardware API is referenced

indirectly as part of a third-party library. First-party usage in-

dicates that developers have consciously chosen to store cryp-

tographic key material in trusted hardware, while for certain

third-party libraries (such as analytics libraries) developers

may be unaware that this is occurring.

Overall, we find that the vast majority of Keystore API

usages are located in third-party source code (definition pro-

vided in §3.3). Of a total of 199,156 calls to the Keystore

init method located in non-obfuscated packages, we find

that 94.69% of calls originated in third-party libraries, while

5.31% are located in first-party source code. This observed

distribution is also true for SE usage. Of the 17,400 Strong-

Box calls located in non-obfuscated packages, 98.31% are

located in third-party libraries, while only 294 (1.69%) are

API are most commonly used by apps. Table 2 in the Ap-

| 1 | A small number of APKs (2,365, or 0.48% of our overall dataset) were | first-party calls within custom app source code. |  |  |
| --- | --- | --- | --- | --- |
| references to the actual | android.security.keystore | API when searching | Third-Party Libraries. | A natural follow-on question is |
| the source code. After manual investigation we hypothesize that in most | which | third-party libraries referencing the trusted hardware |  |  |
| along the call chain were removed at compilation). We include these APKs | pendix shows the top 10 third-party libraries used by Android |  |  |  |
| in our upper bound percentages reported above but exclude them from more | apps to reference the Keystore API. While several of the top |  |  |  |
| in-depth analysis | 10 are security-focused libraries, four are primarily app de- |  |  |  |

---

## Page 8

velopment and analytics libraries, suggesting that the details 4.4 Implementation Security

of key generation and storage are abstracted from developers

who may be unaware of what data is stored where.

The Android Keystore API allows for a variety of authentica-

tion configurations to determine when a key can be accessed.

The core authentication method setUserAuthentication-

Required(boolean) requires users to authenticate via any

available form of device unlock (device pattern/PIN/password

or biometric credentials) for any cryptographic operations us-

ing a private key [20]. More specialized API methods allow

developers to require a specific form of authentication (e.g.,

biometric authentication only) and to set the duration during

which the authentication is valid.

We find that 15.84% of keys stored in the Android Keystore

require some form of user authentication prior to granting

access, with 2.78% requiring biometric authentication specifi-

cally (and disallowing any other form of authentication, such

as device passcode).

By default, if a key requires any form of authentication

for the user experience. For calls that set a specific duration,

8

Ciphers. Of 232,283 key generation calls to Android cryp-

tographic APIs requesting the Android Keystore as provider,

63.51% requested an AES key, 34.48% requested an RSA key

the Appendix shows the full list of requested ciphers and their

respective usage counts.

As a point of comparison, of the 20,042 calls requesting the

AndroidOpenSSL software-backed provider, 99.74% gener-

ated an RSA key pair with just 51 generating an AES key. We

hypothesize that developers avoid hardware-backed key stor-

age for asymmetric encryption out of performance concerns,

which we discuss further in subsequent sections.

The Android Keystore API also includes legacy ciphers

for backwards compatibility and interoperability, some of

which have since been deprecated. 3DES, for instance, was

simultaneously added and deprecated in API level 28 [25]. In

our analysis, we fortunately find very few instances of apps

using insecure or legacy ciphers. In particular, we find no

instances of 3DES or HMAC-SHA1 even though these ciphers

are available within the Android Keystore [26].

random configuration [16].

Randomized Encryption. It is possible, however, for de-

| 4.3 | Key Authentication | pair, and 0.9% of keys requested an EC key pair. Table 4 in |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| then a user must authenticate each time the key is used. To | Defaults. | Android Keystore API defaults are significantly |  |  |  |  |  |
| provide a more user-friendly configuration, the Keystore API | more secure than those of software-based Java cryptog- |  |  |  |  |  |  |
| allows developers to set a validity duration period in seconds | raphy | APIs | historically | available | in | Android. | For in- |
| during which the key can be reused without any need to reau- | stance, if a developer requests an | AES cipher without |  |  |  |  |  |
| thenticate. 21.75% of keys require the user to authenticate | specifying the accompanying encryption mode(s) as in |  |  |  |  |  |  |
| each time they initiate an operation requiring key access, the | javax.crypto.Cipher.getInstance(“AES”) | , Java’s Ci- |  |  |  |  |  |
| most secure configuration but also one that can use friction | pher API defaults to AES with ECB mode, an insufficiently |  |  |  |  |  |  |
| the most popular durations were 5 seconds (set by 38.53% | Android Keystore, on the other hand, disallows various |  |  |  |  |  |  |
| of keys which set a duration) and 1 hour (set by 4.45% of | insecure cryptographic operations by default, including us- |  |  |  |  |  |  |
| keys). A significant percentage of API calls set very short | ing ECB mode in symmetric encryption, RSA encryp- |  |  |  |  |  |  |
| validity durations: 13.2% of calls that set a duration set it to | tion/decryption without proper padding, and using an insuffi- |  |  |  |  |  |  |
| 3 seconds or less, meaning that the user can only reuse the | ciently random IV [19]. All of the six essential rules in cryp- |  |  |  |  |  |  |
| key within the next few seconds. For some use cases, unless | tography laid out by Egele et al. [42] (e.g., do not use ECB |  |  |  |  |  |  |
| the user proceeds very quickly this is effectively the same as | mode with symmetric encryption, do not use a non-random |  |  |  |  |  |  |
| requiring authentication each time. | IV for CBC) in 2013 are not possible within the Keystore |  |  |  |  |  |  |
| As an alternative to requiring a user to provide information | API by default. Unless the developer explicitly disallows ran- |  |  |  |  |  |  |
| to authenticate, a user can instead approve a pop-up mes- | domized encryption, many of the same configurations that |  |  |  |  |  |  |
| sage via the | setUserConfirmationRequired(boolean) | run smoothly or are even the default in Java’s software APIs |  |  |  |  |  |
| API before proceeding. As a standalone API this does not | will throw an | InvalidKeyException | with the Android Key- |  |  |  |  |
| require the individual approving the message to provide any | store. In addition to disallowing insecure configurations by |  |  |  |  |  |  |
| information indicating that they are indeed the device owner | default, the Android Keystore API is designed such that it |  |  |  |  |  |  |
| (i.e., they need only tap to approve), but it can be used in | requires developers to provide specific configurations instead |  |  |  |  |  |  |
| combination with the authentication APIs described above to | of providing only a high level cipher (e.g., for symmetric |  |  |  |  |  |  |
| provide cryptographic certification that a user has approved a | encryption a developer must specify the block mode(s) and |  |  |  |  |  |  |
| certain action. However, we find that very little use of this fea- | encryption padding at the point of key generation using the |  |  |  |  |  |  |
| ture: of the 26 calls to the | setUserConfirmationRequired | designated | setBlockModes | and | setEncryptionPaddings |  |  |
| API detected where we were able to retrieve the argument | APIS [39, 40]). Android Keystore then verifies that the config- |  |  |  |  |  |  |
| value, only two of them enabled confirmation (with the re- | uration provided is valid, sufficiently secure, and compatible |  |  |  |  |  |  |
| maining 24 disabling). | with the specified key purpose. |  |  |  |  |  |  |

---

## Page 9

| Figure 2: | Performance evolution of encrypting 1 MiB with | Figure 3: | Execution times of AES-GCM-256 encryption as a |
| --- | --- | --- | --- |
| AES-GCM in Pixel devices. Each data point corresponds to | function of message length on the Pixel 8. The x-axis is log- |  |  |
| the Pixel device released in that year (e.g., 2023 represents | scaled. The precise numerical runtimes are shown in Table 5 |  |  |
| measurements taken from the Pixel 8). The y-axis is log- | in the Appendix. |  |  |

scaled.

how this configuration is distributed as a percentage of all

hardware-backed keys, however, given that there were 30,245

references to the randomized encryption API endpoint we

estimate that approximately 8.45% of all Android Keystore-

backed keys disable IND-CPA , a surprisingly high percentage

given that this configuration violates a core cryptographic

security property.

There are a handful of scenarios in which a developer

may deem it necessary to disable this requirement (for

instance, if a custom IV is needed), though the API doc-

umentation suggests alternative workarounds to avoid

cases [19]. To investigate this further, we identify the ten

9

key configuration ( AES/GCM/NoPadding ) but dis-

Key Attestation. Android Keystore allows developers to re-

quire key attestation, which verifies that keys are indeed stored

in device hardware [18]. We find 2,724 calls to setAttesta-

tionChallenge(byte[]) , indicating that 0.98% of all keys

generate an attestation certificate chain. While still a relatively

small percentage, this nonetheless represents a significant in-

crease from Imran et al. [51] who previously scanned a ran-

domly sampled subset of 112,886 Android apps for attestation

in January 2021 and found only 5 apps using key attestation.

| velopers to circumvent Android Keystore’s secure default | ables | randomized | encryption | because | the | API | “does |
| --- | --- | --- | --- | --- | --- | --- | --- |
| settings and implement known insecure configurations by | not work consistently | in | API | levels | 23-28” | [31], (2) |  |
| setting Keystore’s | setRandomizedEncryption(boolean) | com.apptentive.android.sdk.encryption.resolvers | , |  |  |  |  |
| API [19], which mandates configurations must be sufficiently | a customer engagement platform which uses a custom initial |  |  |  |  |  |  |
| randomized to provide indistinguishability between cipher- | vector (IV) and thus is required to disable randomized |  |  |  |  |  |  |
| texts given chosen plaintexts (e.g., | IND-CPA | ), to false. In | encryption [29], and (3) | dev.mcodex.RNSensitiveInfo | , |  |  |
| general, disabling this API means that the same plaintext | a React Native wrapper library which disables randomized |  |  |  |  |  |  |
| encrypted with the generated key may produce similar or | encryption for a basic AES/GCM/NoPadding configuration |  |  |  |  |  |  |
| identical ciphertexts. | as AWS did [62]. Our results are inconclusive as we manually |  |  |  |  |  |  |
| We find that 77.94% of calls to the randomized encryp- | searched Android bug trackers for historical issues with |  |  |  |  |  |  |
| tion API disable the setting (a relatively unsurprising result | randomized encryption API and could not find any relevant |  |  |  |  |  |  |
| given that it is enabled by default, and so referencing the API | results, but these reported issues with consistency may be an |  |  |  |  |  |  |
| with | True | as the argument has no effect). When estimating | area for the Android team to issue public guidance. |  |  |  |  |
| disabling | randomized | encryption | for | several | common | 5 | Key Storage Performance |
| most-used libraries containing a call disabling randomized | Having surveyed the current usage of trusted hardware, in |  |  |  |  |  |  |
| encryption | and manually review each, though we | find | order to judge when hardware-backed key storage | should | be |  |  |
| only three | are | public without significant reverse | engi- | used we must first understand what performance differences, |  |  |  |
| neering: (1) | com.amazonaws.internal.keyvaluestore | , | if any, exist compared with software-backed key storage. Un- |  |  |  |  |
| AWS’s | internal | keystore | which | generates | a | secure | fortunately, to the best of our knowledge Android does not |

---

## Page 10

| currently publish any empirical statistics evaluating the per- | Box performance has improved over time, and so execution |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| formance of software or hardware keystores. | times are even longer in older devices: the initial Pixel 3 (re- |  |  |  |  |
| To conduct our own measurements, we use AWS Device | leased in 2018) has a symmetric encryption runtime of 63 | . | 43 | s |  |
| Farm [1] to measure the runtime performance of key stor- | which held reasonably steady until the release of the Pixel 7 in |  |  |  |  |
| age options across a variety of Android devices. Our test app | 2022 where the performance dropped significantly to 17 | . | 42 | s | . |
| calculates the runtime performance of each individual oper- | The sharp performance improvement between the Pixel 6 |  |  |  |  |
| ation for the following three keystores: the device’s default | and Pixel 7 is somewhat surprising since both devices use |  |  |  |  |
| software-based keystore (Bouncy Castle for the Pixel XL and | Google’s in-house Titan M2 security chip [55]. The Pixel’s |  |  |  |  |
| AndroidOpenSSL for all other devices), the Android Key- | main processor changed from Google Tensor in the Pixel 6 |  |  |  |  |
| store using the default TEE configuration, and the Android | to Google Tensor G2 between the 6 and 7 devices, however, |  |  |  |  |
| Keystore using a SE (StrongBox Keymaster). The numbers | and it is possible that the main Tensor G2 processor is able to |  |  |  |  |
| reported below for each operation represent the average per- | communicate with the Titan M2 chip more efficiently. |  |  |  |  |
| formance across 100 distinct iterations. | For asymmetric encryption, we measure Pixel 8 perfor- |  |  |  |  |

mance across keystores on a very small payload of 256 bits

(i.e., the use case where a software-backed AES key is en-

5.1 Performance Evolution

crypted by a hardware-backed RSA key). We find that asym-

| We first measure how key generation and encryption perfor- | metric encryption incurs very little performance overhead on |  |  |
| --- | --- | --- | --- |
| mance has changed over time using Google’s flagship Pixel | minuscule payloads regardless of keystore, with TEE encryp- |  |  |
| device line from 2016 through 2023. | tion taking an average of 0.0065 | s | and StrongBox encryption |

taking 0.0125 s on average.

| Key Generation. | Our results show that symmetric key gener- | Overall, symmmetric encryption using a SE-backed key |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ation has a negligible performance impact regardless of the | is roughly 35 to 55 times slower than encryption using a |  |  |  |  |
| keystore used. In the most recently released Pixel device, the | TEE-backed key depending on the device, likely due to the |  |  |  |  |
| Pixel 8, generating an AES-GCM-256 key takes 0 | . | 002 | s | in | cost of round-trip communications between the main pro- |
| Android’s software keystore, 0 | . | 021 | s | in Android’s TEE key- | cessor and secure processor. This finding somewhat contra- |
| store, and 0 | . | 071 | s | in Android’s SE keystore, StrongBox. We | dicts Android’s official documentation, which qualitatively de- |
| observe similar runtimes for older Pixel devices. While this | scribes StrongBox as “a little slower” as previously mentioned |  |  |  |  |
| represents a large percentage difference, the real runtime im- | in §2.2.2. On the most recently released Pixel device, how- |  |  |  |  |
| pact is negligible given the small execution times. Runtime | ever, basic symmetric encryption of a 1MiB payload within |  |  |  |  |
| differences are more significant with asymmetric encryption: | StrongBox takes around 37 times (and 15 seconds) longer |  |  |  |  |
| in the Pixel 8, generating an RSA-2048 key takes 0 | . | 21 | s | in | than the same operation within a TEE. |

a software keystore, 1 . 93 s in Android’s TEE keystore, and

9 . 22 s in StrongBox.

5.2 Performance vs. Payload Length

| Key Encryption. | Figure 2 shows the comparative perfor- | We further measure the impact of message length on encryp- |  |  |  |
| --- | --- | --- | --- | --- | --- |
| mance of encrypting a randomly generated 1MiB payload | tion performance. Figure 3 shows the performance of payload |  |  |  |  |
| with AES-GCM-256 with no padding across Pixel devices | sizes between 1MiB and 16MiB for the Pixel 8 (again using |  |  |  |  |
| released between 2016 and 2023. Android introduced a se- | AES-GCM-256 with no padding). In this experiment we used |  |  |  |  |
| cure processor beginning with the Pixel 3, and consequently | the average of 10 iterations for payloads 4MiB and above |  |  |  |  |
| StrongBox measurements are only shown from 2018 on. | (instead of 100 iterations as with other experiments) due to |  |  |  |  |
| The performance impact of software-backed encryption | rapidly increasing execution times. |  |  |  |  |
| and TEE-backed encryption has roughly stayed the same over | While encryption runtime increases linearly with message |  |  |  |  |
| time, with the original Pixel and the most recent Pixel 8 report- | length for all three keystore types, StrongBox runtime quickly |  |  |  |  |
| ing TEE measurements of 0.78 and 0.41 seconds respectively. | becomes unmanageable for large lengths. A relatively small |  |  |  |  |
| For a payload of 1MiB or smaller there is a negligible differ- | payload of 0.1 MiB takes the Android Keystore 0 | . | 08 | s | to en- |
| ence between running cryptographic operations inside a TEE | crypt using the TEE and takes StrongBox 1 | . | 59 | s | . A 4MiB |
| and running them natively in terms of what is observable to | payload, however, will take StrongBox roughly 1 minute to |  |  |  |  |
| the end user, which has been the case since the initial release | encrypt, while the TEE-backed keystore can encrypt the same |  |  |  |  |
| of the Android Keystore API. | payload in just 2 | . | 56 | s | , making the TEE viable even for larger |
| StrongBox encryption, however, is significantly slower than | message lengths. A software-backed keystore provides the |  |  |  |  |
| the other two keystore types. In the Pixel 8, for a 1 MiB | best performance by far as expected, encrypting payloads of |  |  |  |  |
| payload StrongBox symmetric encryption takes an average | up to 16 MiB in just 0.3 seconds given that all operations |  |  |  |  |
| of 15.43 s while TEE encryption takes 0.42 s and encryp- | are in-process with no IPC calls or context switch. Table 5 in |  |  |  |  |
| tion using a software-backed key takes just 0.02 s. Strong- | the Appendix contains the TEE and SE execution times and |  |  |  |  |

10

---

## Page 11

in performance in symmetric encryption. As previously dis-

cussed above the Pixel 8 takes 15 . 43 s to execute AES-GCM

for a 1MiB payload, while the Galaxy S24 takes 26 . 39 s , or

close to twice as long. Curiously, the inverse is true for these

two devices when considering TEE performance as shown in

Figure 4: the Pixel 8 takes 0 . 41 s to execute symmetric encryp-

tion using a TEE-backed key, while the Galaxy S24 takes far

less time at 0 . 06 s , illustrating the nuances and complexities

of each individual device’s processor(s) and other hardware.

6 Developer Survey

To better understand why Android developers opt not to use

hardware APIs, we conducted a large-scale developer survey

| Figure 4: | Runtime duration of encrypting 1 MiB with AES- | in August 2024 for apps flagged as matching either of two |
| --- | --- | --- |
| GCM within a TEE across a range of Android devices recently | trusted hardware configurations of interest. This study was |  |
| released in the past two years. While four of the five devices | approved by our department’s ethics committee (equivalent to |  |
| cluster around 0.1 seconds, the runtime of the Pixel 8 is no- | IRB), and all response data was aggregated and anonymized |  |
| ticeably longer and with a wider range. | (see §12 for an in-depth ethics discussion). The survey ques- |  |

tions are given in §A.5.

We are interested in two broad categories of apps

| standard deviations for all message sizes tested on the Pixel 8 | and conducted separate surveys for each: (1) | Sensitive- |  |  |
| --- | --- | --- | --- | --- |
| (shown visually in Figure 3). | NonKeystore | : apps that self-reported as collecting sensi- |  |  |
| Execution times for message signing are similarly cost- | tive user data but did not use Android’s trusted hardware |  |  |  |
| prohibitive using StrongBox. As shown in Table | 6 in the | APIs (either in first-party | or | third-party components) and |
| Appendix, while StrongBox needs only 1 second to sign a | (2) | StrongBox-Disabled | : apps that referenced the Android |  |
| small payload of 0.1 MiB, this runtime increases to 9 seconds | Keystore API in a first-party context but explicitly disabled |  |  |  |
| for a payload of 1 MiB and 35.91 seconds for a 4 MiB payload. | StrongBox for at least one key (e.g., they requested to only |  |  |  |
| In contrast, a TEE is able to sign a 4 MiB message in 1.76 | use TEE-backed key storage). Both of these high-level config- |  |  |  |
| seconds, making it roughly | 20x | faster than StrongBox. | urations indicated that the app developers may have made a |  |

conscious decision not to use some form of trusted hardware.

5.3 Cross-Provider Performance For the first ( Sensitive-NonKeystore ) configuration, we

surveyed a random sample of 10,000 developers via email

| We further investigate how Pixel performance compares with | using the contact information given on the Play Store, and |  |  |  |
| --- | --- | --- | --- | --- |
| other commonly used mobile devices in the Android ecosys- | have received | n | = | 42 responses at the time of writing. We |
| tem. Figure 4 shows TEE performance for symmetric encryp- | attribute the low response rate in large part to the use of Play |  |  |  |
| tion across a range of Android devices, including Samsung | Store app support email addresses, which are often read by a |  |  |  |
| and Xiaomi. The five devices measured were chosen by select- | customer service team (if one exists) and who may not pass |  |  |  |
| ing the most recently released device across all device lines | on our survey request to developers. |  |  |  |
| available through AWS Device Farm. Four of the five devices | Of the 42 responses, 18 respondents reported that one fac- |  |  |  |
| measured (Samsung Galaxy A15, Samsung Galaxy A35, Sam- | tor in opting not to use trusted hardware APIs is that their |  |  |  |
| sung Galaxy S24, and Xiaomi 13) consistently report runtimes | app does not store credentials and/or deemed the security |  |  |  |
| around 0.1 seconds for TEE-backed symmetric encryption, | benefits unnecessary given the type of user data collected. |  |  |  |
| while the Pixel 8’s average runtime is 0.41 seconds. | Three respondents reported general performance concerns, |  |  |  |
| While the Galaxy A15, Galaxy A35, and Xiaomi 13 devices | while 14 respondents indicated that legacy development or |  |  |  |
| do not include a secure element | 2 | , we compare StrongBox per- | compatibility reasons were prohibitive factors, reporting ei- |  |
| formance between the Pixel 8 and the Samsung Galaxy S24 | ther a desire to maximize devices the app can run on or that |  |  |  |
| (released in January 2024) and find a noticeable difference | the app was developed prior to the Android Keystore API |  |  |  |
| 2 | Samsung first introduced a secure processor in 2020 but only within its | release date in 2013. One such developer specified that their |  |  |
| Galaxy S series [63]. Devices recently released as part of other series (such as | app uses SQLite due to “lack of knowledge [of the Android |  |  |  |
| the Galaxy A15 and Galaxy A35 devices, introduced in December 2023 and | Keystore API] at the time of development and difficulties for |  |  |  |

March 2024, respectively) do not include a secure processor (and thus throw

migrating later.” Notably, API usability did not appear to be a

a StrongBoxUnavailableException if a developer attempts requests to

store keys in the StrongBox). We confirmed this through our own tests. widespread concern—just two of the 42 respondents indicated

they had found the Keystore API difficult to use.

11

---

## Page 12

| For the | StrongBox-Disabled | configuration, after filter- | apps that, by their own admission, collect potentially sensitive |  |
| --- | --- | --- | --- | --- |
| ing out third-party StrongBox calls we identified | n | = | 25 apps | user data. Just 43.7% of apps processing sensitive data use |
| matching a StrongBox-disabled configuration. Unfortunately | any form of trusted hardware, and almost all of this usage |  |  |  |
| we received no responses for our | StrongBox-Disabled | sur- | comes from third-party components. While some of these |  |
| vey, a relatively unsurprising response rate given our restric- | apps may be collecting relatively benign data (such as a user’s |  |  |  |
| tion of the dataset to first-party disabled calls limited our sam- | name) or may rely primarily on a remote server to handle |  |  |  |
| ple size. Even so, our manual review of disabled StrongBox | most cryptographic operations instead of storing data on de- |  |  |  |
| configurations on GitHub described in §4.1 has also provided | vice, this is still a comparatively low rate given there is little |  |  |  |
| a window into developers’ thought processes. | to no performance drawback for common cryptographic use |  |  |  |

cases in a TEE-backed keystore.

Additionally, the vast majority of apps using hardware-

7 Limitations

backed storage use a TEE instead of an SE (43.7% compared

| Here we acknowledge the following limitations of our analy- | to 5.03%). Put another way, while Google’s public goal is to |
| --- | --- |
| sis and describe steps taken to mitigate these limitations. | make the SE the "lowest common denominator" in credential |

storage [3], as of 2024 we observe that only around 10% of

| Accuracy of static analysis: | As with prior work in Android | apps using trusted hardware at all are using the SE at least |
| --- | --- | --- |
| app analysis, our research is subject to the inherent technical | once. As side-channel attacks become ever more sophisticated |  |
| limitations of static analysis. Given that we only have access | and effective [34], it is even more important for applications |  |
| to packaged bytecode instead of the original source code, we | to use the most advanced storage available to protect data. |  |

cannot guarantee that certain source code components have

| not been obfuscated, though it is unlikely that this would be | Android Keystore API provides more secure defaults: | In |  |
| --- | --- | --- | --- |
| the case for Android system APIs. Static analysis cannot re- | addition to the protection secure hardware provides against |  |  |
| liably detect whether a particular component is executed at | OS compromise, the Android Keystore API also offers signif- |  |  |
| runtime (i.e., dead or legacy code), but this is a natural trade- | icantly more secure defaults than similar Java cryptographic |  |  |
| off with the scale of our work. Modern compilers and widely | APIs. Android Keystore mandates an | IND-CPA | -secure config- |
| used app optimization tools are highly effective at removing | uration by default, disallowing insecure configurations that |  |  |
| unused source code and so we anticipate app bytecode is un- | have plagued other cryptographic APIs [42, 45]. Android also |  |  |
| likely to contain unreachable code at the point of our analysis. | runs checks to ensure the security and validity of a config- |  |  |
| Dynamic analysis would further preclude studying certain | uration, including cross-referencing the stated purpose of a |  |  |
| categories of apps, such as financial apps, since we cannot | key with which it is generated (e.g., EC keys cannot be used |  |  |
| create test financial accounts for regulatory reasons. | for encryption and decryption, only signing). While it is still |  |  |

possible for developers to circumvent this default (as 8.45%

| Necessity of high-level analysis: | The scale of our work | of them do), this nonetheless requires a conscious decision by |
| --- | --- | --- |
| (downloading and analyzing around half a million apps) nec- | the developer. Android Keystore’s default settings alone make |  |
| essarily means that our analysis will be comparatively high- | it a security improvement over other cryptographic APIs. |  |

level. In particular, static analysis is unable to automatically

| detect the semantic application context in which a trusted | TEE-backed storage performance is viable for small-to- |  |
| --- | --- | --- |
| hardware API call occurs, including what particular data is | medium message sizes | : We find a negligible difference (<0.5 |
| being stored within the hardware element and how keys gen- | seconds) between TEE-backed and software-backed crypto- |  |
| erated are being used, or to guarantee that the flagged API | graphic operations for payloads less than 1MiB, empirically |  |
| call is used to protect sensitive data at runtime (e.g., an app | confirming that in common scenarios hardware key storage |  |
| might import a marketing analytics API that in turn references | runtime is not a prohibitive factor when using the Android |  |
| the Keystore API for processing analytics data). However, in | Keystore API. A TEE keystore can thus provide significant |  |
| our work we are primarily interested in which apps choose | security benefits with minimal performance impact, providing |  |
| not | to use trusted hardware, particularly SEs, and why. Our | an ideal trade-off between enhanced security and performance |
| results provide an empirical upper bound on secure key stor- | overhead for most app use cases. |  |
| age usage and provide comprehensive data on API usage and | Need for public performance evaluations of StrongBox: | In |
| performance across the Android ecosystem as a whole. | comparison to the TEE, Android’s SE demonstrates signifi- |  |

cantly worse processing time for all but the smallest payloads.

8 Discussion If we consider acceptable processing times to be less than

three seconds, StrongBox can only encrypt message sizes of

| Trusted hardware usage is still comparatively low | : While | roughly 0.2 MiB or less even in the most recently released |
| --- | --- | --- |
| both industry and government have launched various initia- | Pixel devices. For comparison, a TEE can encrypt message |  |
| tives encouraging developers to move towards trusted hard- | sizes of up to around 2 MiB within the same time frame. Our |  |
| ware [3, 5, 78], usage remains stubbornly low even among | performance measurements, static analysis of symmetric ver- |  |

12

---

## Page 13

| sus asymmetric usage patterns, and manual review of calls | on a randomly sampled subset of Play Store apps and found |
| --- | --- |
| disabling StrongBox all strongly suggest that performance is | that 32.0% of apps analyzed contained a call to the Keystore |
| a prohibitive factor in using SEs in practice. 5.15% of devel- | API (excluding gaming apps), but only measured the binary |
| opers referencing the Android Keystore API explicitly opt out | question of whether an app contained any Keystore API call |
| of using StrongBox (as in the Salesforce example in §4.1). | without investigating usage specifics. Additionally, a particu- |
| Even so, StrongBox’s execution time may be entirely rea- | lar focus of our work is comparing TEE and SE APIs in both |
| sonable in cases with very small payloads: for instance, an app | usage and performance. |
| may use StrongBox to encrypt a different cryptographic key. | Coojimans et al. [37] systematized high-level security prop- |
| Equally, developers may evaluate overhead cost differently | erties of Android key storage options in 2014, observing that |
| depending on whether it is a one-time operation (e.g., initial | while Android’s TEE-backed key storage provides device |
| login) or a repeated process. Developers need quantitative | binding (i.e. prevents keys from being extracted from the |
| information in order to make case-by-case decisions, a gap | device) where software keystores are vulnerable, the imple- |
| which our work fills. Most importantly, Android’s documenta- | mentation of the TEE keystore made it possible for an attacker |
| tion arguably understates the depth of the performance draw- | with root permissions to use other apps’ keys (i.e. did not ef- |
| backs of SEs, making it more challenging for developers to | fectively provide app-binding). Our work expands on this |
| make an informed decision. Updated, empirical performance | discussion to consider new forms of hardware (namely, SEs) |
| measurements based on contemporary device measurements | that were not available when Coojimans et al. surveyed An- |
| should be publicly available and easily accessible to develop- | droid key storage in 2014. |

ers in place of the ambiguous language currently used in the

documentation., which may also have led developers to opt

out of using StrongBox as a precautionary measure.

API was only released in 2013). They noted at the time that

both Java and Android JCA APIs allowed a developer to spec-

ify only the encryption algorithm (e.g., AES), in which case

Java and Android used ECB mode with PKCS7Padding as the

default. Focardi et al. [45] similarly analyzed the confiden-

tiality and integrity properties provided by various software-

backed Java keystores in 2018.

There have been a handful of studies focusing on particular

subsets of hardware-related API usage in Android. Bianchi et

al. [32] conducted an empirical survey of Android’s Finger-

print API and found very low adoption rates, with just 424 of

30,459 popular apps scanned using the API. Imran et al. [51]

ran a keyword search for the key attestation API on a subset

of apps in sensitive categories (e.g., finance, communication,

medical), finding that of 112,886 apps only five use key at-

testation. Concurrently to our work, Bove [33] conducted a

high-level study on various TEE-based Android APIs (includ-

ing the Biometrics and Digital Rights Management APIs)

13

Trusted Hardware Performance: To the best of our knowl-

edge, Android does not provide official quantitative assess-

ments of trusted hardware performance. There has been a

small amount of prior work measuring specific aspects of

periments demonstrating the viability of a proposed crypto-

10 Conclusion

This work presents the first comprehensive, large-scale sur-

vey of trusted hardware usage and performance in Android

devices. While even the most secure trusted hardware config-

uration is ultimately best-effort as developers have to contend

with available device hardware, we find that a significant per-

centage of apps, including those self-reporting to the Play

Store as collecting sensitive user data, do not make use of the

Android Keystore trusted hardware API. Our performance

results show that TEE-backed key storage is viable for all

but very large payloads, removing one of the most significant

barriers to adoption. Our results provide app developers with

concrete performance data to encourage adoption and ulti-

mately to enable them to make an informed decision for their

individual use case(s).

| 9 | Related Work | trusted hardware performance in Android as supporting ex- |
| --- | --- | --- |
| Android App Analysis: | Most prior work studying security | graphic scheme. Hugenroth et al. [50] measured the perfor- |
| and privacy in Android apps has used metrics such as permis- | mance of HMAC execution in SEs on Android and iPhone |  |
| sions requested [44,58,70] and traffic analysis [43,67,69] and | devices to confirm their proposed key stretching scheme was |  |
| has often overlooked data storage, even when investigating | feasible on contemporary devices, observing that time elapsed |  |
| overall app security [56]. For instance, Gilsenan et al. [46] | increases linearly with input length and that a 10 KiB payload |  |
| studied security issues in two-factor authentication (2FA) apps | takes approximately 1 second to execute in the Pixel 3 SE. |  |
| and recommended that apps use the Android Keystore, but | In our work, we present the first comprehensive, longitudinal |  |
| did not investigate how apps actually do store their keys. | analysis of the performance of various key storage schemes, |  |
| Egele et al. [42] studied cryptographic misuses in Android | measuring the comparative performance of all widely used |  |
| applications in 2014, but looked only at the software-backed | ciphers across the three major key storage options for de- |  |
| Java Cryptographic Architecture APIs (presumably due to the | velopers (a software-backed Java Keystore, Android’s TEE |  |
| timing of the work, since the initial Android trusted hardware | Keystore, and Android’s StrongBox SE API). |  |

---

## Page 14

| 11 | Open Science | Acknowledgments |
| --- | --- | --- |
| In compliance with the open science policy and in the inter- | Jenny Blessing is funded by Entrust and Nokia Bell Labs. |  |
| est of open access, we have open sourced all data used in | Ross Anderson made important contributions to the ideas |  |
| our analysis, including our APK dataset, keyword search and | contained in this paper. Unfortunately he died on 28th March |  |
| call graph analysis results files for all individual APKs, and | 2024 before the final version was written; any errors remain |  |
| all source code and testing scripts used. Our performance | our own. |  |

benchmarking test app and all runtime logs are also publicly

released. Our dataset can be accessed here: <redacted for

review>.

12 Ethics Considerations

We carefully considered the ethics of all components of our

gated and comparatively high-level to avoid the perception

Developer survey. As part of our developer survey, we sent

ensure that we only selected one app from each developer

Our email clearly identified ourselves as academic re-

searchers, including institutional affiliation, in the first sen-

tence and emphasized that we were conducting a voluntary

research study in which all responses were anonymous. If

recipients clicked on the survey link, we further included an

informed consent statement at the beginning of the survey

that included similar information in greater detail, and invited

ence department’s ethics committee (the effective equivalent

consent statement appearing at the beginning of the survey.

Additional specifics of the methodology are described in §6.

We opted not to financially compensate participants in order

to adequately preserve anonymity in line with similar work

14

References

[1] AWS Device Farm. https://aws.amazon.com/dev

ice-farm/ .

[2] Soot. https://soot-oss.github.io/soot/ .

4g-testing-cryptography , 2024.

[7] Android. AndroidKeyStoreBCWorkaround-

Provider.java. https://android.googlesour

ce.com/platform/frameworks/base/+/marshmal

low-mr1-release/keystore/java/android/sec

urity/keystore/AndroidKeyStoreBCWorkaround

Provider.java .

ity/googleplay-asi .

[10] Android. Cipher. https://developer.android.co

m/reference/javax/crypto/Cipher .

[12] Android. KeyGenParameterSpec. https://develope

r.android.com/reference/android/security/k

eystore/KeyGenParameterSpec .

| research. All static analysis is conducted on publicly available | [3] Android Ready SE. | https://developers.google. |  |
| --- | --- | --- | --- |
| data, including both published apps and Play Store metadata. | com/android/security/android-ready-se | , 2021. |  |
| We intentionally keep our discussion of usage analysis aggre- | Last accessed August 25th 2024. |  |  |
| of targeting specific apps for potentially insecure configura- | [4] Cryptography in Mobile Apps. | https://mobile-sec |  |
| tions, though we open-source all analysis results as described | urity.gitbook.io/mobile-security-testing-g |  |  |
| in §11. | uide/general-mobile-app-testing-guide/0x0 |  |  |
| a single initial email to each app developer in our random | [5] Shifting the Balance of Cybersecurity Risk: Principles |  |  |
| sample of 10,000 apps, after filtering the random sample to | and Approaches for Secure by Design, October 2023. |  |  |
| (i.e., a developer would not receive more than one email). All | [6] Kevin Allix, Tegawendé F Bissyandé, Jacques Klein, |  |  |
| email addresses were retrieved by scraping the Play Store | and Yves Le Traon. | Androzoo: Collecting millions |  |
| and were intentionally provided as a point of contact for the | of android apps for the research community. | In | Pro- |
| public. We did not send follow-up or reminder emails to avoid | ceedings of the 13th international conference on mining |  |  |
| spam. | software repositories | , pages 468–471, 2016. |  |
| respondents to reach out directly over email with any ques- | [8] Android. androidx.security.crypto. | https://develo |  |
| tions. | per.android.com/reference/androidx/securit |  |  |
| Our developer survey was approved by our computer sci- | y/crypto/package-summary | . |  |
| of an Institutional Review Board) after the committee re- | [9] Android. App Security Improvement Program. | https: |  |
| viewed the proposed survey questions, email, and informed | //developer.android.com/privacy-and-secur |  |  |
| involving large-scale surveying of Play Store developers but | [11] Android. Hardware security module. | https://develo |  |
| took care to keep the survey length to a minimum (estimated | per.android.com/privacy-and-security/keys |  |  |
| 2-3 minutes) to be respectful of developers’ time. | tore#HardwareSecurityModule | . |  |

---

## Page 15

| [13] Android. KeyProtection. | https://developer.andr | [27] Android Developers. Conscrypt. | https://source.a |  |
| --- | --- | --- | --- | --- |
| oid.com/reference/android/security/keystor | ndroid.com/docs/core/ota/modular-system/co |  |  |  |
| e/KeyProtection | . | nscrypt | . |  |
| [14] Android. KeyStore. | https://developer.android. | [28] Apktool. Apktool. | https://apktool.org/ | , 2024. |

com/reference/java/security/KeyStore .

[16] Android. Remediation for unsafe encryption mode us-

age. https://support.google.com/faqs/answer

/10046138 .

[17] Android. Security guidelines. https://developer.

android.com/privacy-and-security/security

-tips .

security/keystore/KeyGenParameterSpec.Buil

[22] Android. Trusty TEE. https://source.android.c

om/docs/security/features/trusty .

[23] Android. Verify hardware-backed key pairs with Key

Attestation. https://developer.android.com/pr

ivacy-and-security/security-key-attestati

on .

per.android.com/privacy-and-security/keys

tore , 2024.

ES , 2024.

15

[29] Apptentive. appten-

1be4f12683/apptentive/src/main/java/com/ap

ptentive/android/sdk/encryption/resolvers/

KeyResolver23.java#L70 .

[30] American Medical Association. HIPAA security rule &

risk analysis. https://www.ama-assn.org/practi

ce-management/hipaa/hipaa-security-rule-r

isk-analysis .

Provider23.java#L91 .

Generic attacks against cryptographic hardware

through long-range deep learning. arXiv preprint

arXiv:2306.07249 , 2023.

[35] David Cerdeira, Nuno Santos, Pedro Fonseca, and San-

dro Pinto. SoK: Understanding the Prevailing Security

Vulnerabilities in TrustZone-Assisted TEE Systems. In

2020 IEEE Symposium on Security and Privacy (SP) ,

[36] Guoxing Chen, Sanchuan Chen, Yuan Xiao, Yinqian

Zhang, Zhiqiang Lin, and Ten H Lai. Sgxpectre: Steal-

[37] Tim Cooijmans, Joeri de Ruiter, and Erik Poll. Analysis

| [15] Android. MasterKey. | https://developer.android. | tive/android/sdk/encryption/resolvers/KeyResolver23.java. |  |  |  |
| --- | --- | --- | --- | --- | --- |
| com/reference/androidx/security/crypto/Mas | https://github.com/apptentive/apptentive-a |  |  |  |  |
| terKey | . | ndroid/blob/91aebf3fa758edddd40924f06aecdf |  |  |  |
| [18] Android. setAttestationChallenge. | https://develope | [31] AWS-SDK-Android. | amazon- |  |  |
| r.android.com/reference/android/security/k | aws/internal/keyvaluestore/KeyProvider23.java. |  |  |  |  |
| eystore/KeyGenParameterSpec.Builder#setAtt | https://github.com/aws-amplify/aws-sdk-and |  |  |  |  |
| estationChallenge(byte[]) | . | roid/blob/8fd69db5e22d13973ddebf6521f5663a |  |  |  |
| [19] Android. setRandomizedEncryptionRequired. | https: | e2275c4c/aws-android-sdk-core/src/main/jav |  |  |  |
| //developer.android.com/reference/android/ | a/com/amazonaws/internal/keyvaluestore/Key |  |  |  |  |
| der#setRandomizedEncryptionRequired(boolea | [32] Antonio Bianchi, Yanick Fratantonio, Aravind Machiry, |  |  |  |  |
| n) | . | Christopher Kruegel, Giovanni Vigna, Simon Pak Ho |  |  |  |
| [20] Android. setUserAuthenticationRequired. | https://de | Chung, and Wenke Lee. Broken Fingers: On the Usage |  |  |  |
| veloper.android.com/reference/android/secu | of the Fingerprint API in Android. In | NDSS | , 2018. |  |  |
| rity/keystore/KeyGenParameterSpec.Builder# | [33] Davide Bove. A Large-Scale Study on the Prevalence |  |  |  |  |
| setUserAuthenticationRequired(boolean) | . | and Usage of TEE-based Features on Android. | arXiv |  |  |
| [21] Android. SharedPreferences. | https://developer.an | preprint arXiv:2311.10511 | , 2023. |  |  |
| droid.com/reference/android/content/Shared | [34] Elie Bursztein, Luca Invernizzi, Karel Král, Daniel |  |  |  |  |
| Preferences | . | Moghimi, Jean-Michel | Picod, and | Marina | Zhang. |
| [24] Android. Android Keystore system. | https://develo | pages 1416–1432. IEEE, 2020. |  |  |  |
| [25] Android. KEY_ALGORITHM_3DES. | https://deve | ing intel secrets from sgx enclaves via speculative exe- |  |  |  |
| loper.android.com/reference/android/securi | cution. In | 2019 IEEE European Symposium on Security |  |  |  |
| ty/keystore/KeyProperties#KEY_ALGORITHM_3D | and Privacy (EuroS&P) | , pages 142–157. IEEE, 2019. |  |  |  |
| [26] Android. KeyProperties. | https://developer.andr | of secure key storage solutions on android. In | Proceed- |  |  |
| oid.com/reference/android/security/keystor | ings of the 4th ACM Workshop on Security and Privacy |  |  |  |  |
| e/KeyProperties | , 2024. | in Smartphones & Mobile Devices | , pages 11–20, 2014. |  |  |

---

## Page 16

[38] Android Developers. Jelly Bean. https://develope [49] Sudhi Herle and Jason Wong. Announcing the Android

r.android.com/about/versions/jelly-bean . Ready SE Alliance. https://security.googleb

loper.android.com/reference/android/securi

loper.android.com/reference/android/securi

per.android.com/privacy-and-security/cryp

tography , Last Accessed September 4 2024.

graphic misuse in android applications. In Proceedings

of the 2013 ACM SIGSAC conference on Computer &

communications security , pages 73–84, 2013.

Baumgärtner, Bernd Freisleben, and Matthew Smith.

Why Eve and Mallory love Android: An analysis of

Android SSL (in)security. In Proceedings of the 2012

ACM conference on Computer and communications se-

curity , pages 50–61, 2012.

2011.

sium , pages 1–15. The Internet Society, 2018.

[48] J Alex Halderman, Seth D Schoen, Nadia Heninger,

William Clarkson, William Paul, Joseph A Calandrino,

16

log.com/2021/03/announcing-android-ready-s

able encryption using secure elements on smartphones.

Android Remote Authorization. In 31st USENIX Se-

1578, 2022.

[52] Intel. What Is Virtualization Security? https://www.

ecurity.html .

[53] Trevor Johns. Using Cryptography to Store Credentials

Safely. https://android-developers.googlebl

-credentials.html .

[54] Rishabh Khandelwal, Asmit Nayak, Paul Chung, and

Kassem Fawaz. Unpacking privacy labels: A measure-

ment and developer perspective on google’s data safety

section. arXiv preprint arXiv:2306.08111 , 2023.

-mobile.html , 2021.

[57] Li Li, Tegawendé F Bissyandé, Mike Papadakis,

IEEE Symposium on Security and Privacy (SP) , pages

70–86. IEEE, 2021.

international conference on software engineering com-

panion , pages 653–656, 2016.

| [39] Android Developers. setBlockModes. | https://deve | e-alliance.html | , 2021. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ty/keystore/KeyGenParameterSpec.Builder#se | [50] Daniel Hugenroth, Alberto Sonnino, Sam Cutler, and |  |  |  |  |  |  |
| tBlockModes(java.lang.String[]) | . | Alastair R Beresford. Sloth: Key stretching and deni- |  |  |  |  |  |
| [40] Android Developers. setBlockModes. | https://deve | Cryptology ePrint Archive | , 2023. |  |  |  |  |
| ty/keystore/KeyGenParameterSpec.Builder#se | [51] Abdullah Imran, Habiba Farrukh, Muhammad Ibrahim, |  |  |  |  |  |  |
| tEncryptionPaddings(java.lang.String[]) | . | Z Berkay Celik, and Antonio Bianchi. SARA: Secure |  |  |  |  |  |
| [41] Android Developers. Cryptography. | https://develo | curity Symposium (USENIX Security 22) | , pages 1561– |  |  |  |  |
| [42] Manuel Egele, David Brumley, Yanick Fratantonio, and | intel.com/content/www/us/en/business/enter |  |  |  |  |  |  |
| Christopher Kruegel. | An empirical study of crypto- | prise-computers/resources/virtualization-s |  |  |  |  |  |
| [43] Sascha Fahl, Marian Harbach, Thomas Muders, Lars | og.com/2013/02/using-cryptography-to-store |  |  |  |  |  |  |
| [44] Adrienne Porter Felt, Erika Chin, Steve Hanna, Dawn | [55] Dave Kleidermacher, Jesse Seed, Brandon Barbello, and |  |  |  |  |  |  |
| Song, and David Wagner. Android permissions demys- | Stephan Somogyi. Pixel 6: Setting a new standard for |  |  |  |  |  |  |
| tified. In | Proceedings of the 18th ACM conference on | mobile security. | https://security.googleblog.co |  |  |  |  |
| Computer and communications security | , pages 627–638, | m/2021/10/pixel-6-setting-new-standard-for |  |  |  |  |  |
| [45] Riccardo Focardi, Francesco Palmarini, Graham Steel, | [56] Konrad Kollnig, Anastasia Shuba, Reuben Binns, Max |  |  |  |  |  |  |
| M Squarcina, Mauro Tempesta, et al. Mind your keys? | Van Kleek, and Nigel Shadbolt. Are iphones really better |  |  |  |  |  |  |
| a security evaluation of java keystores. In | Proceedings | for privacy? comparative study of ios and android apps. |  |  |  |  |  |
| of the Network and Distributed System Security Sympo- | arXiv preprint arXiv:2109.13722 | , 2021. |  |  |  |  |  |
| [46] Conor Gilsenan, Fuzail Shakir, Noura Alomar, and Serge | Siegfried Rasthofer, Alexandre Bartel, Damien Octeau, |  |  |  |  |  |  |
| Egelman. | Security and privacy failures in popular | Jacques Klein, and Le Traon. Static analysis of android |  |  |  |  |  |
| { | 2FA | } | apps. | In | 32nd USENIX Security Symposium | apps: A systematic literature review. | Information and |
| (USENIX Security 23) | , pages 2079–2096, 2023. | Software Technology | , 88:67–95, 2017. |  |  |  |  |
| [47] GitHub. GitHub Search Results. | https://github.com | [58] Rui Li, Wenrui Diao, Zhou Li, Jianqi Du, and Shanqing |  |  |  |  |  |
| /search?q=%22setIsStrongBoxBacked%28false% | Guo. Android custom permissions demystified: From |  |  |  |  |  |  |
| 29%22+language%3AJava&type=code&l=Java&p=1 | . | privilege escalation to design shortcomings. In | 2021 |  |  |  |  |
| Ariel J Feldman, Jacob Appelbaum, and Edward W Fel- | [59] Ziang Ma, Haoyu Wang, Yao Guo, and Xiangqun Chen. |  |  |  |  |  |  |
| ten. Lest we remember: cold-boot attacks on encryption | Libradar: Fast and accurate detection of third-party li- |  |  |  |  |  |  |
| keys. | Communications of the ACM | , 52(5):91–98, 2009. | braries in android apps. | In | Proceedings of the 38th |  |  |

---

## Page 17

| [60] Carsten Maartmann-Moe, Steffen E Thorkildsen, and | [71] Mohamed Sabt and Jacques Traoré. Breaking into the |  |  |
| --- | --- | --- | --- |
| André Årnes. The persistence of memory: Forensic iden- | keystore: A practical forgery attack against android key- |  |  |
| tification and extraction of cryptographic keys. | digital | store. In | Computer Security–ESORICS 2016: 21st Eu- |
| investigation | , 6:S132–S140, 2009. | ropean Symposium on Research in Computer Security, |  |

[61] René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker,

and Nick Kralevich. The Android Platform Security

thub.com/mCodex/react-native-sensitive-inf

with Galaxy S20’s Secure Processor. https://news.s

amsung.com/global/strengthening-hardware-s

Brorsson. A Survey of Published Attacks on Intel SGX.

ance to render unsecured protected health information

unusable, unreadable, or indecipherable to unauthorized

Matthew Smith, and Sascha Fahl. To pin or not

TrustZone: A Comprehensive Survey. ACM computing

[70] Joel Reardon, Álvaro Feal, Primal Wijesekera, Amit

19) , pages 603–620, 2019.

17

Heraklion, Greece, September 26-30, 2016, Proceedings,

Part II 21 , pages 531–548. Springer, 2016.

rceMobileSDK-Android/commit/4b074b7c744f44

5701af/libs/SalesforceSDK/src/com/salesfor

a#L247 .

Zone Keymaster Design. In 31st USENIX Security Sym-

Play’s Data safety section. https://support.goog

10787469?hl=en .

10th USENIX Symposium on Operating Systems Design

ent/publications/code-of-practice-for-app

Genkin, Baris Kasikci, Frank Piessens, Mark Silberstein,

pages 991–1008, 2018.

354. IEEE, 2021.

| Model. | ACM Transactions on Privacy and Security | [72] Salesforce. Commit 4b074b7: Refactoring StrongBox |  |  |  |
| --- | --- | --- | --- | --- | --- |
| (TOPS) | , 24(3):1–35, 2021. | code. | https://github.com/forcedotcom/Salesfo |  |  |
| [62] mCodex. RNSensitiveInfoModule.java. | https://gi | 129486029a7df6481d0d7c3eb2 | . |  |  |
| o/blob/495dd7f08c077f5744e56803e45f54787df | [73] Salesforce. KeyStoreWrapper.java. | https://github |  |  |  |
| 3dab3/android/src/main/java/dev/mcodex/RNS | .com/forcedotcom/SalesforceMobileSDK-Andro |  |  |  |  |
| ensitiveInfoModule.java#L313 | . | id/blob/1a11e225b20968cc88ed08cf3304ede28b |  |  |  |
| [63] Samsung Newsroom. Strengthening Hardware Security | ce/androidsdk/security/KeyStoreWrapper.jav |  |  |  |  |
| ecurity-with-galaxy-s20s-secure-processor | , | [74] Alon Shakevsky, Eyal Ronen, and Avishai Wool. Trust |  |  |  |
| May 2020. | Dies in Darkness: Shedding Light on Samsung’s Trust- |  |  |  |  |
| [64] Alexander Nilsson, Pegah Nikbakht Bideh, and Joakim | posium (USENIX Security 22) | , pages 251–268, 2022. |  |  |  |
| arXiv preprint arXiv:2006.13598 | , 2020. | [75] Google Play Store. | Provide information for Google |  |  |
| [65] U.S. Department of Health and Human Services. Guid- | le.com/googleplay/android-developer/answer/ |  |  |  |  |
| individuals. | https://www.hhs.gov/hipaa/for-pro | [76] Google Play Store. Signal Private Messenger. | https: |  |  |
| fessionals/breach-notification/guidance/i | //play.google.com/store/apps/datasafety?id |  |  |  |  |
| ndex.html | . | =org.thoughtcrime.securesms&hl=en&gl=US | . |  |  |
| [66] U.S. Department of Health and Human Services. The | [77] Yang Tang, Phillip Ames, Sravan Bhamidipati, Ashish |  |  |  |  |
| security rule. | https://www.hhs.gov/hipaa/for-p | Bijlani, Roxana Geambasu, and Nikhil Sarda. CleanOS: |  |  |  |
| rofessionals/security/index.html | . | Limiting Mobile Data Exposure with Idle Eviction. In |  |  |  |
| [67] Marten | Oltrogge, Yasemin | Acar, Sergej | Dechand, | and Implementation (OSDI 12) | , pages 77–91, 2012. |
| to | { | Pin—Helping | } | app developers bullet proof their | [78] United Kingdom Department for Science, Innovation |
| { | TLS | } | connections. In | 24th USENIX Security Sympo- | and Technology. Code of practice for app store operators |
| sium (USENIX Security 15) | , pages 239–254, 2015. | and app developers. | https://www.gov.uk/governm |  |  |
| [68] Sandro Pinto and Nuno Santos. | Demystifying ARM | -store-operators-and-app-developers | . |  |  |
| surveys (CSUR) | , 51(6):1–36, 2019. | [79] Jo Van Bulck, Marina Minkin, Ofir Weisse, Daniel |  |  |  |
| [69] Andrea Possemato and Yanick Fratantonio. Towards | Thomas F Wenisch, Yuval Yarom, and Raoul Strackx. |  |  |  |  |
| HTTPS everywhere on android: We are not there yet. In | Foreshadow: Extracting the keys to the Intel SGX king- |  |  |  |  |
| 29th USENIX Security Symposium (USENIX Security | dom with transient Out-Of-Order execution. | In | 27th |  |  |
| 20) | , pages 343–360, 2020. | USENIX Security Symposium (USENIX Security 18) | , |  |  |
| Elazari Bar On, Narseo Vallina-Rodriguez, and Serge | [80] Stephan Van Schaik, Marina Minkin, Andrew Kwong, |  |  |  |  |
| Egelman. 50 ways to leak your data: An exploration of | Daniel Genkin, and Yuval Yarom. Cacheout: Leaking |  |  |  |  |
| apps’ circumvention of the android permissions system. | data on intel cpus via cache evictions. In | 2021 IEEE |  |  |  |
| In | 28th USENIX security symposium (USENIX security | Symposium on Security and Privacy (SP) | , pages 339– |  |  |

---

## Page 18

[81] Adam Vartanian. Cryptography Changes in Android P.

https://android-developers.googleblog.com

/2018/03/cryptography-changes-in-android-p

.html , March 8 2018.

[82] Wei Wang, Xing Wang, Dawei Feng, Jiqiang Liu, Zhen

Han, and Xiangliang Zhang. Exploring permission-

induced risk in android applications for malicious ap-

plication detection. IEEE Transactions on Information

Forensics and Security , 9(11):1869–1882, 2014.

[83] Mark Weiser. Program slicing. IEEE Transactions on

software engineering , (4):352–357, 1984.

[84] Daoyuan Wu, Debin Gao, Robert H Deng, and

Chang Rocky KC. When program analysis meets byte-

code search: Targeted and efficient inter-procedural anal-

ysis of modern android apps in backdroid. In 2021

51st Annual IEEE/IFIP International Conference on De-

pendable Systems and Networks (DSN) , pages 543–554.

IEEE, 2021.

[85] Xiaowen Xin. Titan M makes Pixel 3 our most secure

phone yet. https://blog.google/products/pixel

/titan-m-makes-pixel-3-our-most-secure-pho

ne-yet/ , 2018.

[86] Wu Zhou, Yajin Zhou, Xuxian Jiang, and Peng Ning.

Detecting repackaged smartphone applications in third-

party android marketplaces. In Proceedings of the sec-

ond ACM conference on Data and Application Security

and Privacy , pages 317–326, 2012.

18

---

## Page 19

A Appendix Published data safety information. According to Google’s

Legal Mandates: In certain industries, developers have to

abide by a heavy patchwork of regulatory standards govern-

ing data collection and processing. In the U.S. (the region

in which our application dataset and ranking information are

collected) since 1996 the medical sector has been governed

by the Health Insurance Portability and Accountability Act

(HIPAA)’s Security Rule [66], which specifies minimum se-

curity standards that health service providers must meet. The

financial sector has a variety of SEC regulations and long-

standing laws they must comply with, such as the global

Payment Card Industry Data Security Standard (PCI DSS)

that governs processing and storage of credit card data.

Regulatory standards in the financial and medical indus-

tries generally require that data is encrypted at rest. Specific

implementations, such as use of secure hardware to store cre-

dentials, are usually not mandated directly. For instance, the

American Medical Association acknowledges that since secu-

rity is an “evolving target, and so HIPAA’s security require-

ments are not linked to specific technologies or products” [30].

Rather, regulation often encourages adoption indirectly, such

as a law that mandates a security standard only provided by

the hardware-backed storage mechanism. For instance, an

industry may be required to use a FIPS-compliant random

number generator [65], which on a particular mobile device

is only available via the HSM API. Moreover, even in cases

where regulations provide little specific guidance, providers

secure hardware to store and use encryption keys. To audit app

A.2 Play Store Data Safety Labels

19

developer documentation, “all developers that have an app

(including apps that self-report not collecting user data) [75].

In practice, we find that only 74.47% (342,872/460,362) of

apps have submitted a data safety form at the time of scraping

in March through April 2024 3 . Khandelwal et al. [54] had

previously conducted a large-scale analysis of Play Store data

safety labels in May 2023 (approximately one year earlier)

and found that only 46.8% of apps reported any data, so we

note the percentage of apps providing a data safety label

has increased significantly from approximately a year earlier,

though it is still noticeably far from satisfying the Play Store

mandate.

For apps that have data safety information, we classify each

app as “sensitive” or “benign” based on the types of data the

developer has reported. Google uses 14 high-level data type

categories, such as location, financial information, audio files,

etc. [75] We consider an app to be sensitive if it collects any

information from 12 of these 14 data types. We exclude the

final two categories, “App info and performance” (defined

by Google as crash logs and other app performance data)

and “Device or other IDs” (e.g. MAC address or Firebase ID),

since we are interested in whether developers are intentionally

collecting sensitive user data relating to specific individuals,

which we broadly define as user-provided data. Based on

this classification, we find that of the 342,872 apps reporting

data safety information, 46.75% are sensitive (and therefore

53.25% are benign).

sensitive data.

we hypothesize that it is unlikely that those apps which do

process sensitive data, but do not declare it in their data safety

label, process such data securely.

removed by the time we began scraping app data safety pages in March 2024.

| A.1 | Trusted Hardware Best Practices | published on Google Play must complete the data safety form” |
| --- | --- | --- |
| operating in heavily-regulated sectors are generally motivated | Developer self-reporting. | Google uses a somewhat counter- |
| to prioritize security within their product to keep pace with | intuitive notion of what constitutes data collection: instruc- |  |
| the sector in which they operate and minimize the risk that | tions to developers state data is considered to be collected |  |
| they could be charged with running afoul of the law. | if it is transmitted “from your app off a user’s device” [75], |  |
| Developer Guidelines: | Android’s published security guide- | and user data that is only processed and stored locally does |
| lines for developers [17] recommends developers use the | not need to be reported as “collected”. In short, it is possible |  |
| Android Keystore for long-term or multi-use keys, and the | that an app that processes sensitive user data locally (and may |  |
| OWASP Mobile Application Security Testing Guide [4] rec- | therefore be expected to use some form of hardware-backed |  |
| ommends that developers “should always rely on” available | key storage) yet this app would not be listed as collecting |  |
| security, Android’s “app security improvement program” [9] | Therefore, by using the information in the data safety labels |  |
| further scans all applications for various potential security | there is a risk our analysis excludes apps which do in fact |  |
| issues upon initial submission and subsequent updates, in- | process sensitive data. Nevertheless, we argue that there is |  |
| cluding well-known vulnerabilities (e.g., Logjam), unsafe en- | much to be gained from understanding how the Keystore API |  |
| cryption modes, and insecure connection issues. We are not | is used by those apps which state they process sensitive data: if |  |
| aware of any analysis of key storage. | these apps do not make use of hardware-based secure storage, |  |
| In this paper we use the Play Store’s data safety label infor- | 3 | The slight difference in number of apps for which we attempted to |
| mation to determine which apps process sensitive data, and | retrieve a data safety label (460,263) vs. number of apps downloaded and |  |
| therefore which apps may be expected to make use of secure | decompiled (486,234) is due to apps that were available in the Play Store at |  |
| key storage. | the time we began scraping apps themselves in October 2023 but had been |  |

---

## Page 20

Figure 5: Percentages of Android apps using TEE and SE

APIs, respectively, across major categories within the Google

Play Store. StrongBox usage is shown here as a subset of An-

droid Keystore API usage (i.e., any app that uses StrongBox

necessarily uses the Android Keystore API).

There are both benign and malicious reasons for developers

inaccurately reporting their use of sensitive data. For example,

developers may be unaware of the data collected by third-

party libraries or wish to avoid highlighting the data their app

collects in their submission, and thus may understate data col-

lected. Conversely, it is also possible that developers may err

on the side of overstating the sensitivity of the data they col-

lect to ensure they are in compliance with Play Store policies.

In principle, Google can often verify whether an app collects

sensitive data (or not) and spot any differences between app

behavior and reported collection. If discrepancies are found,

Google has the ability to block app updates or remove the app

from the Play Store altogether. We are unable to determine

the extent to which such verification and enforcement takes

place and therefore validate the correctness (or otherwise) of

the data safety label information.

egories in the Google Play Store. We show a representative

sample of categories here due to space limitations, but data for

demonstrate the highest rates of trusted hardware usage, with

over 60% of apps referencing the broader Android Keystore

hypothesize is due to the fact that the vast majority of Strong-

20

Box references come from third-party APIs, but gaming app

development teams are less likely to use high-level app de-

velopment toolkits given the more advanced functionality

required to create the app.

A.4 Manual Analysis

We select a subset of applications flagged as not using An-

droid’s trusted hardware API for further examination to verify

our static analysis results and to better understand which key

storage schemes are used instead. We scraped the top 200

most-downloaded apps in the Play Store as of April 1, 2024,

and then selected the ten most highly-ranked apps which

self-reported collecting sensitive data but had been flagged

in our initial keyword search as not referencing the Android

Keystore API. We decompiled each app using Apktool and

manually searched for relevant keywords relating to widely

used software-backed keystores provided as part of Android,

such as Android’s SharedPreferences API [21].

We verified that each of these ten apps were indeed not

using Android’s trusted hardware API anywhere and found

that they instead generally made use of some combination

of Android’s SharedPreferences, Android’s default software-

backed keystore (i.e., AndroidOpenSSL ), or a local SQLite

database such as SQLCipher. SharedPreferences is a bit more

concerning than other software-backed keystores as it offers

very different security properties: some Android keystores

(namely SharedPreferences and KeyChain are intended as

systemwide credential storage, where keys are accessible to

any app on the device. While it is challenging to make any

definitive statements on individual app use cases due to the

high-level nature of our analysis and obfuscation of internal

variable names, developers should always exercise caution

when using a systemwide keystore.

It is also possible that some apps hardcode encryption keys

after obfuscating the keys using Dexguard or a similar tool,

but this was not possible to detect given our manual review is

relatively cursory and intended primarily to verify our static

analysis results and identify other APIs used.

A.5 Developer Survey Questions

c. Project Manager

f. Other

the app?

| A.3 | Usage by Category | 1. Which of the following best describes your role? |
| --- | --- | --- |
| Figure 5 shows the comparative usage of the Android Key- | a. Programmer/Developer |  |
| store (TEE) and StrongBox (SE) APIs across a range of cat- | b. Software Tester/Quality Assurance |  |
| all categories can be found in the accompanying code repos- | d. Software Design/Architecture |  |
| itory (see §11). Unsurprisingly, we find that financial apps | e. Administration (Non-Technical) |  |
| API and 12.8% referencing the StrongBox API. Gaming apps | 2. Approximately how many people (including project man- |  |
| have an exceptionally low rate of StrongBox usage, which we | agers, developers, testers, etc.) are involved in developing |  |

---

## Page 21

| a. 1 | b. Agree |
| --- | --- |
| b. 2 - 5 | c. Neither agree nor disagree |
| c. 6 - 20 | d. Disagree |
| d. 21 - 50 | e. Strongly disagree |

e. 50+

a. None

b. Less than 1 year

c. 1 - 5 years

d. 5 - 10 years

c. Neither agree nor disagree

d. Disagree

e. Strongly disagree

following statement: Our app collects and processes

potentially sensitive user data (e.g., name, other demo-

a. Strongly agree

b. Agree

d. Disagree

6. On a five-point scale, how much do you agree with the

b. Agree

e. Strongly disagree

following statement: I am familiar with the Android Key-

store trusted hardware API, commonly used in Android

a. Strongly agree

21

8. [ If app did not reference Android Keystore API at all. ]

Which of the following reasons best describe the main

considerations behind this decision? Please select all that

apply.

• Security benefits were unclear

• Security benefits were not needed given type of

versions of Android)

• App was developed prior to Android’s Keystore

API release date in 2013

• Found Keystore API difficult to use

• Don’t know/don’t remember

rect: [open text]

• Other: [open text]

To the best of your knowledge, what libraries, if any,

does your app use within Android for credential storage

such as cryptographic keys)? [Open text]

our static analysis of your app from November 2023,

we determined your app used the Android Keystore API

described in the link above was set to false). Which of the

following reasons best describe the main considerations

• Security benefits were unclear

• Performance concerns

| 3. How many years of experience do you have working | Based on our static analysis as of November 2023, your |  |  |
| --- | --- | --- | --- |
| with Android app development? | app was recorded as not using the Android Keystore API. |  |  |
| e. 10 years or more | data (if any) collected by app |  |  |
| 4. On a five-point scale, how much do you agree with the | • Performance concerns |  |  |
| following statement: Our development team prioritizes | • Lack of features: Desired algorithm and/or key size |  |  |
| security as part of the development process. | was unavailable with Android Keystore |  |  |
| a. Strongly agree | • We wanted to maximize our app’s ability to run on |  |  |
| b. Agree | many different devices (potentially running older |  |  |
| 5. On a five-point scale, how much do you agree with the | • Unaware this API existed |  |  |
| graphic information, health data, financial data, etc.). | • We believe your static analysis result to be incor- |  |  |
| c. Neither agree nor disagree | 9. [ | If app did not reference Android Keystore API at all. | ] |
| e. Strongly disagree | (either user login credentials or developer credentials |  |  |
| following statement: I am familiar with the concept of | 10. [ | If app was recorded as disabling StrongBox. | ] A secure |
| trusted hardware (e.g., Intel SGX and Arm TrustZone). | element (called the StrongBox Keymaster in Android) |  |  |
| a. Strongly agree | is a more advanced form of trusted hardware. Based on |  |  |
| c. Neither agree nor disagree | but disabled usage of the secure element in at least one |  |  |
| d. Disagree | instance. (Specifically, the setIsStrongBoxBacked API |  |  |
| 7. On a five-point scale, how much do you agree with the | behind this decision? Please select all that apply. |  |  |
| development for credential storage (e.g., storing crypto- | • Security benefits were not needed given type of |  |  |
| graphic keys). | data (if any) collected by app |  |  |

---

## Page 22

• Lack of features: desired cryptographic algorithm

and/or key size was unavailable with StrongBox

Keymaster

• We wanted to maximize our app’s ability to run on

many different devices (potentially running older

versions of Android)

• Don’t know/don’t remember

• We believe your static analysis result to be incor-

rect: [open text]

• Other: [open text]

22

---

## Page 23

| Keystore API Method | Count |
| --- | --- |
| void <init>(java.lang.String,int) | 278,567 |
| android.security.keystore.KeyGenParameterSpec$Builder setEncryptionPaddings(java.lang.String[]) | 235,719 |
| android.security.keystore.KeyGenParameterSpec$Builder setBlockModes(java.lang.String[]) | 224,169 |
| android.security.keystore.KeyGenParameterSpec$Builder setKeySize(int) | 166,379 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserAuthenticationRequired(boolean) | 48,150 |
| android.security.keystore.KeyGenParameterSpec$Builder setDigests(java.lang.String[]) | 48,095 |
| android.security.keystore.KeyGenParameterSpec$Builder setCertificateNotAfter(java.util.Date) | 44,087 |
| android.security.keystore.KeyGenParameterSpec$Builder setCertificateNotBefore(java.util.Date) | 44,062 |
| android.security.keystore.KeyGenParameterSpec$Builder setRandomizedEncryptionRequired(boolean) | 30,245 |
| android.security.keystore.KeyGenParameterSpec$Builder setIsStrongBoxBacked(boolean) | 24,656 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserAuthenticationValidityDurationSeconds(int) | 23,946 |
| android.security.keystore.KeyGenParameterSpec$Builder setKeyValidityForOriginationEnd(java.util.Date) | 15,334 |
| android.security.keystore.KeyGenParameterSpec$Builder setSignaturePaddings(java.lang.String[]) | 9,313 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserAuthenticationParameters(int,int) | 8,974 |
| android.security.keystore.KeyGenParameterSpec$Builder setInvalidatedByBiometricEnrollment(boolean) | 6,629 |

android.security.keystore.KeyGenParameterSpec$Builder setAlgorithmParameterSpec

| (java.security.spec.AlgorithmParameterSpec) | 5,531 |
| --- | --- |
| android.security.keystore.KeyGenParameterSpec$Builder setAttestationChallenge(byte[]) | 2,724 |
| android.security.keystore.KeyGenParameterSpec$Builder setKeyValidityEnd(java.util.Date) | 1,295 |
| android.security.keystore.KeyGenParameterSpec$Builder setKeyValidityStart(java.util.Date) | 1,088 |
| android.security.keystore.KeyGenParameterSpec$Builder setUnlockedDeviceRequired(boolean) | 383 |
| android.security.keystore.KeyGenParameterSpec$Builder setKeyValidityForConsumptionEnd(java.util.Date) | 230 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserAuthenticationValidWhileOnBody(boolean) | 93 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserConfirmationRequired(boolean) | 47 |
| android.security.keystore.KeyGenParameterSpec$Builder setUserPresenceRequired(boolean) | 38 |

Table 1: Usage count of Android Keystore API methods across all apps in the Play Store.

| Package Name | Call Count | Package Name | Call Count |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| com.google.android.gms.internal | androidx.security.crypto | 11,424 |  |  |  |  |  |  |
| .firebase-auth-api | 30,055 | com.oblador.keychain.cipherStorage | 2,161 |  |  |  |  |  |
| androidx.security.crypto | 26,345 | com.microsoft.identity.common.internal |  |  |  |  |  |  |
| com.appsflyer | 23,566 | .platform | 1,019 |  |  |  |  |  |
| androidx.biometric | 15,960 | com.salesforce.marketingcloud.sfmcsdk |  |  |  |  |  |  |
| com.microsoft.appcenter.utils.crypto | 12,282 | .components.encryption | 758 |  |  |  |  |  |
| com.google.crypto.tink.integration.android | 11,656 | com.iproov.sdk.crypto | 179 |  |  |  |  |  |
| com.flurry.sdk | 7,806 | androidx.tracing | 136 |  |  |  |  |  |
| com.amazonaws.internal.keyvaluestore | 4,138 | com.ionicframework.IdentityVault | 129 |  |  |  |  |  |
| com.oblador.keychain.cipherStorage | 4,073 | com.oblador.keychain.g | 108 |  |  |  |  |  |
| com.huawei.secure.android.common | com.epicshaggy.biometric | 76 |  |  |  |  |  |  |
| .encrypt .keystore.aes | 2,794 | com.it_nomads.fluttersecurestorage.ciphers | 66 |  |  |  |  |  |
| Table | 2: | Top | 10 | third-party | libraries | referenc- | Table 3: | Top 10 third-party libraries referencing Android’s |
| ing | the | Android | Keystore | key | initialization | API | secure element StrongBox Keymaster API.. We chose to clas- |  |
| <init>(java.lang.String, int) | . | We | chose | to | clas- | sify | androidx.security.crypto | [8] as a third-party library |
| sify | androidx.security.crypto | [8] as third party after | after finding that the majority of references were to the | En- |  |  |  |  |
| finding that the majority of references were to the | Encrypt- | cryptedFile | and | EncryptedSharedPreferences | classes |  |  |  |
| edFile | and | EncryptedSharedPreferences | classes which | which abstract the details of key generation and storage from |  |  |  |  |
| abstract the details of key generation and storage. | the developer. |  |  |  |  |  |  |  |

23

---

## Page 24

Cipher Usage Count Message Avg. Runtime (s)

| RSA | 80,096 |
| --- | --- |
| HMAC-SHA256 | 2,321 |
| EC | 2,233 |
| HMAC-SHA512 | 100 |

Table 4: List of ciphers requested for the Android Keystore

provider through the javax.crypto.KeyGenerator,

java.security.KeyPairGenerator,

javax.crypto.Cipher and java.security.KeyStore

APIs along with respective usage counts. We include results

from both the “AndroidKeyStore” and “AndroidKeyStoreBC-

Workaround” providers due to an Android bug dating back to

2015 [7].

Message Avg. Runtime (s)

Size (MiB)

| TEE | SE |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0.01 | 0.03 | ± | 0.01 | 0.21 | ± | 0.01 |
| 0.1 | 0.08 | ± | 0.01 | 1.59 | ± | 0.02 |
| 0.2 | 0.12 | ± | 0.02 | 3.11 | ± | 0.02 |
| 1 | 0.42 | ± | 0.06 | 15.43 | ± | 0.10 |
| 2 | 1.13 | ± | 0.09 | 30.88 | ± | 0.16 |
| 4 | 2.56 | ± | 0.19 | 62.23 | ± | 0.33 |
| 6 | 4.25 | ± | 0.74 | 94.68 | ± | 0.37 |
| 8 | 7.67 | ± | 1.02 | 159.61 | ± | 0.72 |
| 10 | 5.83 | ± | 0.63 | 127.01 | ± | 0.69 |
| 12 | 9.24 | ± | 0.83 | 192.37 | ± | 0.80 |
| 14 | 10.87 | ± | 1.14 | 223.44 | ± | 1.02 |
| 16 | 13.10 | ± | 1.44 | 257.69 | ± | 1.09 |

Table 5: Execution times of AES-GCM-256 encryption as a

function of message length. These measurements were taken

from the TEE and SE in Google’s Pixel 8 device.

24

Size (MiB)

| 0.01 | 0.02 | ± | 0.01 | 0.15 | ± | 0.02 |
| --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 0.06 | ± | 0.01 | 0.99 | ± | 0.07 |
| 0.2 | 0.14 | ± | 0.02 | 1.89 | ± | 0.02 |
| 1 | 0.48 | ± | 0.03 | 9.05 | ± | 0.05 |
| 2 | 0.89 | ± | 0.04 | 17.99 | ± | 0.06 |
| 4 | 1.76 | ± | 0.05 | 35.91 | ± | 0.09 |

Table 6: Execution times of generating an Elliptic Curve

Digital Signature Algorithm (ECDSA) signature with SHA-

256. These measurements were taken from the TEE and SE

in Google’s Pixel 8 device.

AES 147,529 TEE SE

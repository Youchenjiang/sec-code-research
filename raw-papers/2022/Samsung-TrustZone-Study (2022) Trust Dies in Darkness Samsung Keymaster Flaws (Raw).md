---
title: "45_Shakevsky_et_al.,_Trust_Dies_in_Darkness_Samsung_TrustZone"
creator: "LaTeX with hyperref"
pages: 19
---

# 45_Shakevsky_et_al.,_Trust_Dies_in_Darkness_Samsung_TrustZone

> **總頁數**：19 頁

---

## Page 1

Trust Dies in Darkness: Shedding Light on

Samsung’s TrustZone Keymaster Design

Alon Shakevsky, Eyal Ronen, and Avishai Wool, Tel-Aviv University

https://www.usenix.org/conference/usenixsecurity22/presentation/shakevsky

This paper is included in the Proceedings of the

31st USENIX Security Symposium.

August 10–12, 2022 • Boston, MA, USA

978-1-939133-31-1

Open access to the Proceedings of the

31st USENIX Security Symposium is

sponsored by USENIX.

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

Trust Dies in Darkness:

Shedding Light on Samsung’s TrustZone Keymaster Design

| Alon Shakevsky | Eyal Ronen | Avishai Wool |
| --- | --- | --- |
| shakevsky@mail.tau.ac.il | eyal.ronen@cs.tau.ac.il | yash@eng.tau.ac.il |

Tel-Aviv University

Abstract Simultaneously, smartphones are becoming more and more

ARM-based Android smartphones rely on the TrustZone

hardware support for a Trusted Execution Environment (TEE)

to implement security-sensitive functions. The TEE runs a

separate, isolated, TrustZone Operating System (TZOS), in

parallel to Android. The implementation of the cryptographic

functions within the TZOS is left to the device vendors, who

create proprietary undocumented designs.

In this work, we expose the cryptographic design and imple-

mentation of Android’s Hardware-Backed Keystore in Sam-

sung’s Galaxy S8, S9, S10, S20, and S21 flagship devices.

We reversed-engineered and provide a detailed description of

the cryptographic design and code structure, and we unveil

severe design flaws. We present an IV reuse attack on AES-

GCM that allows an attacker to extract hardware-protected

key material, and a downgrade attack that makes even the

latest Samsung devices vulnerable to the IV reuse attack. We

demonstrate working key extraction attacks on the latest de-

vices. We also show the implications of our attacks on two

higher-level cryptographic protocols between the TrustZone

and a remote server: we demonstrate a working FIDO2 We-

bAuthn login bypass and a compromise of Google’s Secure

Key Import.

We discuss multiple flaws in the design flow of TrustZone

based protocols. Although our specific attacks only apply to

the ≈ 100 million devices made by Samsung, it raises the

much more general requirement for open and proven stan-

Beyond their usage in many and various daily activities, smart-

files), cryptographic key management [24], FIDO2 web au-

complex and present an increasingly larger attack surface. The

result is that they have become a major target for malware and

malicious attackers. There have been many public exploits

that allow an attacker to escalate privileges in the Android OS,

gaining execution as root or even as the OS kernel [9, 14, 20,

21,39]. Ideally, such attacks should not be able to compromise

the devices’ security-critical tasks.

Trusted Execution Environments (TEEs) are largely used

in modern mobile devices to provide an isolated environment

for execution of Trusted Applications (TAs) that can securely

perform security-critical tasks. They have a relatively small

codebase and limited APIs.

In contrast, the Rich Execution Environments (REEs), such

as Android OS, cannot be fully audited and trusted (due to

their complexity). An isolated TEE can be used alongside the

REE to implement security-sensitive functions. This makes

it harder for an attacker to compromise these functions, as

the attack surface is significantly reduced and is limited to

communication with the TEE.

In other words, the goal of the TEE is to withstand attacks

from a fully compromised REE, including by privileged ad-

versaries with kernel or root capabilities.

ARM is the most widely used processor in the mobile

and embedded markets [46], and it provides TEE hardware

support with ARM TrustZone [3, 8]. TrustZone separates the

device into two execution environments:

system runs.

tem runs.

World.

| dards for critical cryptographic and security designs. | 1. A non-secure REE where the “Normal World” operating |  |
| --- | --- | --- |
| 1 | Introduction | 2. A secure TEE where the “Secure World” operating sys- |
| phones are increasingly used for many security-critical tasks, | The REE and TEE use separate resources (e.g., memory, pe- |  |
| such as the protection of sensitive data (messages, images, | ripherals), and the hardware enforces the protection of Secure |  |
| thentication [65], Digital Rights Management [64] (DRM), | In most mobile devices, the Android OS runs the non- |  |
| mobile payment services [53] (e.g., Samsung Pay) and enter- | secure Normal World. As for the Secure World, there are |  |
| prise identity management [53]. | more choices. Even among Samsung devices, there are at |  |
| USENIX Association | 31st USENIX Security Symposium | 251 |

---

## Page 3

| least three different TrustZone Operating Systems (TZOS) in | Zone and a remote server. We demonstrate working Proof-of- |
| --- | --- |
| use (see Section 2.2). | Concept attacks on Galaxy S9, S10, and the latest S21 model. |
| The Android Keystore [28] provides hardware-backed cryp- | To summarise our contributions: |

tographic key management services through a Hardware Ab-

and key usage (e.g., encryption or signing actions). Samsung

implements the HAL through a Trusted Application (TA)

The

Keymaster TA performs the cryptographic operations in the

Secure World using hardware peripherals, including a crypto-

are “wrapped” (encrypted) keys that are stored on the REE’s

file system. The “wrapping”, “unwrapping”, and usage of

Although it is crucial to rigorously verify and test such

cryptographic designs, real-world TrustZone implementations

received relatively little attention in the literature. We believe

that this is mainly due to the fact that most device vendors

do not provide detailed documentation of their TZOS and

Samsung’s Keymaster TA, and asked the following questions:

Does the hardware-based protection of cryptographic keys

remain secure even when the Normal World is compromised?

1.1 Our Contribution

and a downgrade attack that makes even the latest Samsung

flagship devices vulnerable to our IV reuse attack. As sum-

vices [66].

We also show the implications of these vulnerabilities

on bypassing key usage restrictions and on the security of

two higher-level cryptographic protocols between the Trust-

2. We show that the hardware protection in Samsung

on AES-GCM, allowing the extraction of protected key

material.

reuse attack.

5. We discuss the root causes leading to each of the vulner-

abilities we identified, focusing on possible countermea-

sures and problems in the closed cryptographic design

methodology.

1.2 Responsible Disclosure

CVE-2021-25444 with High severity to the issue and released

a patch that prevents malicious IV reuse by removing the

option to add a custom IV from the API. According to Sam-

key blob implementation.

Section 2 provides some background on TrustZone. In Sec-

tion 3 we dissect the Keymaster TA in Samsung Galaxy S8,

S9, S10, S20, and S21 devices. In Section 4 we present an

IV reuse attack against hardware-protected keys as well as

| straction Layer (HAL) that vendors such as Samsung imple- | 1. We expose the proprietary Keymaster TA implementa- |  |  |
| --- | --- | --- | --- |
| ment. The Keystore exposes an API to Android applications, | tion in Samsung devices, focusing on its key derivation |  |  |
| including cryptographic key generation, secure key storage, | and blob encryption implementation. |  |  |
| called the Keymaster TA, which runs in the TrustZone. | 1 | Galaxy S9 devices is vulnerable to an IV reuse attack |  |
| graphic engine. | 3. We show a downgrade attack on Samsung Galaxy S10, |  |  |
| The Keymaster TA’s secure key storage uses | blobs | : these | S20, and S21 devices, making them vulnerable to our IV |
| the keys are done inside the Keymaster TA using a device- | 4. We evaluate the impact of our attacks and describe how |  |  |
| unique hardware AES key. Only the Keymaster TA should | to exploit them to misuse the Keystore key attestation |  |  |
| have access to the secret key material; the Normal World | to bypass FIDO2 WebAuthn login and compromise |  |  |
| should only see opaque key blobs. | Google’s Secure Key Import. |  |  |
| proprietary TAs and share little-to-no information regarding | In order to implement our attacks, we developed an open- |  |  |
| how the sensitive data is protected. To advance and motivate | source Keymaster client that we will make available on [58]. |  |  |
| this research area, we decided to use the leading Android | Our client interacts with the Keymaster TA without passing |  |  |
| vendor Samsung as a test case. We reversed-engineered the | through the Keymaster HAL API, which allows us full control |  |  |
| full cryptographic design and API of several generations of | of the input passed to the Trusted Application. |  |  |
| How does the cryptographic design of this protection affect | We reported our IV reuse attack on S9 to Samsung Mobile |  |  |
| the security of various protocols that rely on its security? | Security in May 2021. In August 2021 Samsung assigned |  |  |
| In this work, we focus on the Keymaster TA used by Sam- | sung [57], the list of patched devices includes: S9, J3 Top, J7 |  |  |
| sung’s flagship devices, including the Samsung Galaxy S8, | Top, J7 Duo, TabS4, Tab-A-S-Lite, A6 Plus, A9S. |  |  |
| S9, S10, S20, and S21. For the first time, we expose its crypto- | We reported the downgrade attack on S10, S20 and S21 in |  |  |
| graphic design, and unveil severe design flaws that can allow | July 2021. In October 2021 Samsung assigned CVE-2021- |  |  |
| an attacker to extract hardware-protected key material. We | 25490 with High severity to the downgrade attack and patched |  |  |
| present an IV reuse attack on AES-GCM that allows the at- | models that were sold with Android P OS or later, including |  |  |
| tackers to extract keys from hardware-protected key blobs; | S10, S20, and S21. The patch completely removes the legacy |  |  |
| marised in Table 1, our attacks affect over 100 million de- | 1.3 | Structure of the Paper |  |
| 1 | For brevity, we refer to TrustZone-based TEEs simply as “TrustZone”. | a downgrade attack. In Section 5 we show how our attacks |  |
| 252 | 31st USENIX Security Symposium | USENIX Association |  |

---

## Page 4

| Table 1: Susceptibility of Samsung Galaxy devices to IV reuse | As the implementation of the TZOS is left to vendors, there |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| and downgrade attack - | 3 | means vulnerable and | 7 | means not. | are multiple implementations by various vendors, including: |
| Device | IV reuse attack | Downgrade attack | • Qualcomm Secure Execution Environment (QSEE) by |  |  |

| S8 | 7 | 7 |
| --- | --- | --- |
| S9 | 3 | 3 |
| S10 | 7 | 3 |
| S20/S21 | 7 | 3 |

break the composability of higher-level cryptographic proto-

cols, focusing on Google’s Secure Key Import and FIDO2

2 Background

The Advanced Encryption Standard (AES) is the most widely

used symmetric block cipher. Galois Counter Mode (GCM)

is a mode of operation for block ciphers that provides Authen-

ticated Encryption. AES-GCM is a stream cipher that uses

AES-CTR (Counter Mode) and the Galois Message Authenti-

cation Code (GMAC) internally.

tialization Vector (IV) reuse attacks. When an IV is reused

while encrypting with the same key, the resulting keystream

is identical. In that case, knowledge of one plaintext immedi-

ately reveals the other. Furthermore, in AES-GCM, Joux [38]

showed how IV reuse could be exploited to break authentica-

tion and create new valid messages.

The ARM TrustZone technology [7] adds an additional virtual

and ARM exception levels.

Qualcomm: used in Google Pixel devices and in Snap-

dragon models of Samsung Galaxy devices.

• Kinibi by Trustonic: used in older Exynos models of

Samsung Galaxy devices, prior to S10.

• TrustedCore (TC) by Huawei.

• TEEGRIS by Samsung (used in newer Exynos models

of Samsung Galaxy devices).

TA parses the commands input, performs required processing

and sends a response back to the client. See the extended

version of this paper [59] for more details on the TEE client

API. Control is transferred to the TA via the dedicated SMC

World application usually exchange arguments and output

using a shared memory buffer called World Shared Memory.

As performing SMCs requires EL1 privileges, a device driver

in the Android kernel handles the communication with the

TA and exposes an API for Normal World applications.

The Android Keystore [24] allows Normal World applica-

tions to perform cryptographic operations while protecting

the cryptographic keys from extraction or unauthorized use.

On devices with TrustZone technology, Keystore utilizes the

TEE to perform cryptographic operations. This Hardware-

Backed Keystore implementation is called the Keymaster TA.

The Keystore’s main functions are: key generation and im-

symmetric encryption/decryption and generation/verification

of symmetric MACs.

follows:

| WebAuthn. In Section 6 we discuss the root causes of the | 2.3 | Trusted Applications |
| --- | --- | --- |
| attacks and gaps in the higher-level protocols’ design. In Sec- | A Trusted Application (TA) is a program that runs in the TEE |  |
| tion 7 we survey related work in TrustZone research, and we | and exposes security services to Android client applications. |  |
| conclude our work in Section 8. Multiple appendices provide | The application can open a session with the TA and invoke |  |
| technical details. | commands within the session. After receiving a command, a |  |
| 2.1 | AES GCM | (Secure Monitor Call) instruction, and the TA and Normal |
| Like every stream cipher, AES-GCM is vulnerable to Ini- | 2.4 | Android Hardware Backed Keystore |
| 2.2 | ARM TrustZone | port, asymmetric encryption/decryption/signing/verification, |
| processor mode called “Secure World” that complements the | Keys can be generated and used inside the TrustZone by |  |
| “Normal World”. The two modes are separated and can com- | the Keymaster TA, and are thus protected from any Normal |  |
| municate using the “Secure Monitor” (running in the high- | World attacker. However, the Keymaster TA relies on the |  |
| est EL3 execution level) or by memory mapping of “World | Normal World application to store the keys [28]. To protect |  |
| Shared Memory”. The separation allows to implement a TEE, | the key material, the keys are encrypted or “wrapped” with |  |
| since a compromised Normal World will not be able to access | a hardware-derived key inside the TrustZone. The encrypted |  |
| the memory of the Secure World. Fig. 1 shows the compo- | key “blobs” are then passed to the Normal World to be stored. |  |
| nents in each exception level in the TrustZone architecture. | Fig. 2 shows a simplified overview of an Android appli- |  |
| See Appendix A for a detailed overview of ARM TrustZone | cation using the Keymaster TA. The general flow runs as |  |
| USENIX Association | 31st USENIX Security Symposium | 253 |

---

## Page 5

Normal World Secure World

EL0

Application 1 Application 2

Usermode

EL1 Android Kernel

Kernelmode

EL2 Hypervisor

EL3

Figure 1: The TrustZone software and hardware isolation architecture

Keymaster TA in

Android

TrustZone

Generate key

B = wrap(key)

Generate attestation cert

cert

(e.g., encrypt/sign)

key = unwrap( B )

result = operation(key)

Figure 2: A usage example of an Android application using

1. The Android application requests a new key to be gen-

application.

2. The Android application saves the blob B in the Normal

World’s file system.

3. Some protocols such as WebAuthn [65] require that the

Android application must prove that a specific key was

generated securely by the Keymaster TA. In these cases,

the application can pass the encrypted blob B to the Key-

Trusted App 1 Trusted App 2

TZOS kernel

Secure Monitor

2

For details on the attestation process see Section 2.5.

4. The application can ask the Keymaster TA to perform

a cryptographic operation on its behalf. For example,

TA. The Keymaster TA decrypts the blob to recover the

return the resulting signature to the application in the

Normal World.

lowing measures:

hence compromising the application will not lead to key

material extraction.

date, rate-limiting, or requiring user authentication (e.g.,

passing biometric authentication/unlocking the screen).

In order to support multiple TZOS implementations, the

Android Keystore uses a HAL, as we shall describe in Sec-

tion 3.2. Every TZOS implements the HAL for Android ser-

vices that require hardware support, usually by having a TA

that performs the needed operations. This is the case for Sam-

sung’s Keymaster TA, which is used to implement Android

Hardware-Backed Keystore and is the main focus of our re-

search.

| Request key generation | to sign a message, the application passes the encrypted |  |  |
| --- | --- | --- | --- |
| B | blob | B | and the message to be signed to the Keymaster |
| Request attestation for | B | signing key. It then uses the key to sign the message and |  |
| Request operation for | B | The Keystore protects keys from extraction using the fol- |  |
| result | 1. Key material is not present in the application memory, |  |  |
| a Hardware-Backed Keystore (i.e., the Keymaster TA) for | 2. The Keystore can provide access control that restricts the |  |  |
| cryptographic key management: key generation, attestation, | usage of keys in various ways, such as restricting a key’s |  |  |
| and encryption/signature. | 2 | purpose (e.g., encryption only), setting an expiration |  |
| erated. The Keymaster TA generates a new key, and | 3. Hardware binding: Supported devices can bind keys to |  |  |
| encrypts it using a hardware-derived key. The result- | the secure hardware (i.e., the TEE), so they cannot be |  |  |
| ing encrypted key blob | B | is passed back to the Android | used outside of the secure hardware on that device. |
| master TA and ask it to generate an attestation certificate. | 2 | Designed using resources from Flaticon.com |  |
| 254 | 31st USENIX Security Symposium | USENIX Association |  |

---

## Page 6

2.5 Android Key Attestation other TZOSs and TAs, Samsung’s implementation is vendor-

the Normal World, despite the fact that all the communications

with the Keymaster TA go through the Normal World. As we

show in Section 5, Secure Key Import and FIDO2 WebAuthn

use key attestation (using Google’s root certificate) exactly

for this purpose.

In this paper, we assume that an attacker can fully compro-

mise the Normal World, e.g., an attacker with root or even

kernel privileges. Moreover, we assume that the attacker is

able to compromise the Normal World without setting the

bootloader fuses that are attested by the Keymaster (e.g., boot-

loader unlocked, Samsung’s warranty bit). Such attacks were

shown by [21,44]. The attacker aims to compromise data that

is secured by the Trusted World, such as Keystore hardware-

protected keys, or higher-level protocols that rely on remote

attestation (e.g., cloning a FIDO2 token or by stealing a key

that was securely imported).

We follow the Android Platform Security Model by

Mayrhofer et al. [42] that states that the hardware protection

and isolation of cryptographic keys offered by TrustZone and

the Keymaster TA should prevent any key compromise even

by such an attacker. This is consistent with the attack model

used by Harrison et al. [36] as well as Lapid and Wool [40].

Note that the attacks described in Sections 4 and 5 do not

require us to actually run code in the Android Kernel. For

our attack, we only require code execution in EL0 (Android

user mode) with sufficient privileges to read key blobs, and

appropriate SELinux permissions to communicate with the

TZOS drivers. For instance, a vulnerability in the Android

Keystore user mode daemon/HAL (such as [37]) would likely

suffice. Alternatively, a root malware or a supply-chain attack

that patches the Keymaster HAL can be used for both attacks.

3 Dissecting the Keymaster TA

Keymaster TA and its new TZOS named TEEGRIS. Like

specific and is a proprietary closed-source system with little-

Overall, we evaluated 26 firmwares for both Exynos and

Snapdragon models of S8, S9, S10, S20, and S21 (including

variants such as S9+, Note9, S10+, S20+, etc.) published be-

tween 2018 and 2021. We found that Keymaster TA’s code

base is extremely similar in theses firmwares (except the S8),

even across TZOSs (Kinibi/QSEE/TEEGRIS).

ference between the Keymaster TA in S8 and in the newer

models. As we shall see in Section 4, one specific code change

introduced in the S9 makes it and all the newer models vul-

nerable to attacks. Although S20 and S21 models include

the more secure Strongbox Keymaster functionality (using a

dedicated tamper-resistant hardware security module), they

are still vulnerable to our attacks as they share the same vul-

nerable cryptographic design and API.

As Kinibi and QSEE have been more thoroughly studied

by the security community [12, 48, 49], when we discuss

details we refer to TEEGRIS unless otherwise noted. See the

extended version of this paper [59] for details on firmware

analysis.

3.2 The Keymaster HAL

The Keymaster HAL is an interface between Android and the

vendor-specific Keymaster implementation. The Android doc-

umentation provides reference guidelines for implementers of

Keymaster HALs [30]. It is implemented in the Android user

mode and communicates with the Keymaster TA using kernel

drivers and World Shared Memory buffers (see Fig. 3). The

extended version of this paper [59] contains a more detailed

overview of the Keymaster HAL in TEEGRIS.

The Keymaster HAL API in TEEGRIS is implemented in

a number of undocumented shared-objects that use TEEGRIS

kernel drivers. To explore the Keymaster TA we reversed

Keymaster client—an Android process that sends our custom

filtering.

| Keystore Key Attestation [33, 67] allows remote parties to | to-no documentation available. To understand the crypto- |  |
| --- | --- | --- |
| verify that a key was generated within the secure hardware by | graphic design implemented by the Keymaster TA, we stati- |  |
| having the Keymaster TA generate a certificate chain whose | cally analyzed the binaries of firmwares and TAs in 3 TZOS’s |  |
| root certificate is Google (or Samsung, for applications such | (TEEGRIS, Kinibi and QSEE) using Ghidra [45]. Addition- |  |
| as KNOX attestation). This allows the remote party to trust | ally, we used the Samsung Open Source [55] website to down- |  |
| public-keys generated within the TrustZone without trusting | load the Android kernel sources for our device. |  |
| 2.6 | The Attack Model | In our analysis, we noticed that there is a significant dif- |
| In our experiments, we used Samsung Galaxy S9, S10, and | Android provides an open-source API for functions that |  |
| S21 devices, rooted using Magisk [68]. Note that when we | the Keymaster should implement [29]. This API includes |  |
| rooted the devices, the Samsung KNOX warranty fuse was | many functionalities such as key generation, key import, and |  |
| set. This does not affect our attacks as we don’t target any | cryptographic operations such as encrypt/decrypt/sign/verify |  |
| KNOX functionality. | using the keys stored in the encrypted blobs. |  |
| 3.1 | Survey of the Keymaster TA Family | engineered the Keymaster HAL and implemented our own |
| In this paper we focus on Samsung’s implementation of the | requests to the Keymaster TA without any input validation or |  |
| USENIX Association | 31st USENIX Security Symposium | 255 |

---

## Page 7

Normal World Secure World

keystore daemon Binder Application

EL0

Usermode

| Keymaster HAL | TEE Interface |
| --- | --- |
| EL1 | TrustZone device drivers |

Kernelmode

SMC

EL3

Figure 3: Overview of the Hardware backed keystore

| v15 blob | v20-s9 blob |
| --- | --- |
| "MDFPP HW Keymaster HEK v15\x00" | "MDFPP HW Keymaster HEK v20\x00" |

.

root_of_trust

| "ID" | "ID" |
| --- | --- |
| "\x02\x00\x00\x00" | "\x02\x00\x00\x00" |
| "id" | "id" |
| "DATA" | "DATA" |
| "\x04\x00\x00\x00" | "\x04\x00\x00\x00" |
| "data" | "data" |

integrity_flags

in green are new to that version.

in Section 2.4, the Keymaster TA encrypts key material inside

a blob. This protects the key material from extraction while

allowing it to be stored by the Normal World application.

As we discovered during our research, each blob contains an

AES key called the Root Encryption Key (REK) [61]. This

World Keymaster TA

Shared

Memory

TEEGRIS kernel

SMC

Secure Monitor

2

v20-s10 blob

"MDFPP HW Keymaster HEK v20\x00"

root_of_trust

"ID"

"\x02\x00\x00\x00"

"id"

"DATA"

"\x04\x00\x00\x00"

"data"

integrity_flags

hek_randomness

derived using a Key Derivation Function (KDF) that mixes

we discuss next.

3.4 KDF Versions of Key Blobs

certified.

Figure 4: The three KDF versions for HDK salt derivation, assuming the Application ID is “id” and the Application Data is

“data”. The salt value is the SHA256 digest of the concatenation of the values. Values shaded in blue are optional, values shaded

| 3.3 | Key Blob Encryption | Key (HDK) that is derived from the REK. A blob’s HDK is |
| --- | --- | --- |
| The main focus of our research is how key blobs are decrypt- | the REK with a blob-specific salt value. The KDF itself is |  |
| ed/encrypted. Based on our analysis and reverse engineering | accessed by the Keymaster TA through a TZOS-internal ioctl |  |
| of the proprietary Keymaster TA, we will now describe the | API. The salt for deriving the HDK is computed as the SHA- |  |
| process at a high level. For a detailed description of the control | 256 digest of a concatenation of several values. Samsung’s |  |
| flow inside the Keymaster TA, see Appendix B. As mentioned | salt-generation method evolved between device models, as |  |
| encrypted part that includes the key material and various pa- | The National Information Assurance Partnership (NIAP) cre- |  |
| rameters. The blob also contains a clear-text part containing | ated the Mobile Device Fundamentals Protection Profile |  |
| the information required for decryption, such as the IV and | (MDFPP) that includes core security requirements for de- |  |
| AAD used in the encryption. | vices. The constant string used in the salt derivation (in all |  |
| The cryptographic foundation which the Keymaster TA | key blobs flavors) suggests that Samsung complies with the |  |
| relies upon is a permanent, hardware, device-unique 256-bit | certification, and indeed Samsung devices are MDFPP CC |  |
| key is only present in the secure hardware cryptographic | In our analysis, we identified three different blob salt- |  |
| engine—the Keymaster TA cannot access it directly. | derivation versions, which we call v15, v20-s9, and v20-s10. |  |
| Each key blob is encrypted using its own Hardware Derived | The differences between the versions are the values used in |  |
| 256 | 31st USENIX Security Symposium | USENIX Association |

---

## Page 8

| the string that is hashed to generate the salt for the key deriva- | Surprisingly, we discovered that the Android client is al- |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tion. All versions can include optional values that are called | lowed to | set | the IV when generating or importing a key. All |  |  |  |  |  |  |  |
| Application ID and Application Data. These values are set by | that is necessary is to place an attacker-chosen IV as part |  |  |  |  |  |  |  |  |  |
| the Normal World. Fig. 4 shows example strings for each of | of the key parameters, and it is used by the Keymaster TA |  |  |  |  |  |  |  |  |  |
| the three blob versions. | instead of a random IV. As the Normal World also controls |  |  |  |  |  |  |  |  |  |
| The first blob key version, which we call v15, is the version | the application ID and application data, this means that an |  |  |  |  |  |  |  |  |  |
| used in Galaxy S8. The salt in v15 key blobs only depends | attacker can force the Keymaster TA to reuse the same key |  |  |  |  |  |  |  |  |  |
| on the application ID and data set by the Normal World (and | and IV that were previously used to encrypt some other v15 or |  |  |  |  |  |  |  |  |  |
| a constant string). | v20-s9 blobs. Since AES-GCM is a stream cipher, the attacker |  |  |  |  |  |  |  |  |  |
| Galaxy S9 introduced a new version which we call v20-s9. | can now recover hardware-protected keys from key blobs. |  |  |  |  |  |  |  |  |  |
| This version adds two new values to the SHA-256 digest, | Given a key blob | B | A | wrapping an unknown key | K | A | , an |  |  |  |
| which we call | root_of_trust | and | integrity_flags | . This | attacker can import another key blob | B | B | with a known (suf- |  |  |
| might be due to a new MDFPP regulation that requires derived | ficiently long) key | K | B | that was encrypted using the same IV |  |  |  |  |  |  |
| keys to be bound to the device’s integrity. | and the same salt. To do so the attacker first extracts the IV |  |  |  |  |  |  |  |  |  |
| The | root_of_trust | is “a collection of values that defines | from the key blob | B | A | , and passes this IV and the same appli- |  |  |  |  |
| key information about the device’s status” [33]. The Keymas- | cation ID and data to the Keymaster TA’s import key function. |  |  |  |  |  |  |  |  |  |
| ter TA computes | integrity_flags | based on the integrity | The known | K | B | will be encrypted using the same blob encryp- |  |  |  |  |
| status of the device (a normal device should have 0, a rooted | tion key HDK (as the salt only depends on the application ID |  |  |  |  |  |  |  |  |  |
| device has value 7). | and data) and the same IV (by construction) as was used to |  |  |  |  |  |  |  |  |  |
| In our analysis, we noticed that although S9 uses the new | encrypt | K | A | . |  |  |  |  |  |  |
| salt version v20-s9 by default, it still includes code that im- | As with any stream-cipher encryption, we can now use our |  |  |  |  |  |  |  |  |  |
| plements the older v15 blob version. The Keymaster TA API | knowledge of | K | B | together with the ciphertexts | B | A | and | B | B | to |
| exposed the option to use this older version to the Normal | recover | K | A | . Let us denote the key-stream created from key |  |  |  |  |  |  |
| World. As we were not able to find any use for this option by | HDK with a given IV as | E | ( | HDK | , | IV | ) | , then: |  |  |
| the Normal World, we believe that this is latent code that is | B | A | ⊕ | B | B | ⊕ | K | B |  |  |

never used.

On S10, S20, and S21 devices, we found a revised KDF that

is very similar to the v20-s9: it uses exactly the same strings,

4 Attacking the Keymaster TA

This section describes two attacks against the Keymaster TA

that allow us to extract hardware-protected key material. Table

2 includes a summary of the Samsung Galaxy devices that

we’ve examined and their susceptibility to IV reuse.

As we discussed in Section 3, the wrapping key used to en-

crypt the key blobs (HDK) is derived using a salt value com-

depends on its IV values never being reused.

= ( E ( HDK , IV ) ⊕ K A ) ⊕ ( E ( HDK , IV ) ⊕ K B ) ⊕ K B

= K A ⊕ K B ⊕ K B = K A

encryption key. Although the attacker can still cause IV reuse,

this reuse is not exploitable. We note that, although S8 can

create only blobs with version v15, its Keymaster TA ignores

the IV parameter in key generation and key import functions,

i.e., it does not allow us to set the IV and is thus not vulnerable

to any of our attacks.

To demonstrate our IV reuse attack, we implemented it on

Galaxy S9 (all key blobs), S10, and S21 (by forcing the cre-

ation of v15 key blobs), and we were able to recover securely

4.2 The Downgrade Attack

version v15.

| root of trust and integrity flags, with one crucial addition: in | All key blobs created on the Galaxy S9 are vulnerable, as |  |  |
| --- | --- | --- | --- |
| v20-s10 the salt also includes a fresh per-blob 16-byte ran- | its default blob version is the vulnerable v20-s9. However, on |  |  |
| dom value | hek_randomness | generated inside the TrustZone. | S10, S20, and S21 devices, the default version is v20-s10, and |
| Similar to S9, we also found latent code that implements v15 | its salt is randomised by the | hek_randomness | field (recall |
| and is exposed to the Normal World. | Fig. 4), hence each blob is encrypted with a uniquely derived |  |  |
| 4.1 | IV Reuse Attack on v15 and v20-s9 Blobs | generated AES, RSA, and ECDSA keys from encrypted blobs. |  |
| puted by the Keymaster TA. In v15 and v20-s9 blobs, the | On S10 and later models, the default blob version is v20-s10. |  |  |
| salt is a deterministic function that depends only on the appli- | However, to our surprise, we discovered the existence of latent |  |  |
| cation ID and application data (and constant strings), which | code that allows the Normal World to request the creation of |  |  |
| the Normal World client fully controls. This means that for a | v15 blobs by simply passing an “encryption version” parame- |  |  |
| given application, all key blobs will be encrypted using the | ter with a specific value. Although the Keymaster HAL API |  |  |
| same key | . As the blobs are encrypted in AES-GCM mode- | does not normally pass this parameter, its existence can be |  |
| of-operation, the security of the resulting encryption scheme | exploited by a privileged attacker to force all new blobs to |  |  |
| USENIX Association | 31st USENIX Security Symposium | 257 |  |

---

## Page 9

Table 2: Summary of Samsung Galaxy devices Keymaster features that make them vulnerable to IV reuse - 3 means true and

7 means false

(after the Normal World is compromised). In Section 5 we

show that this can be exploited to attack security-critical pro-

tocols such as Google’s Secure Key Import and FIDO2 We-

bAuthn.

To demonstrate our findings, we wrote a GDB script (see

the extended version of this paper [59]) that intercepts the call

to the Keymaster HAL in the Normal World. We hooked the

key generation function and modified the passed parameters

in flight to add the encryption version parameter with the

value 0 x f indicating v15. This caused the Keymaster TA to

always generate v15 key blobs and allowed us to recover the

encrypted keys using the IV reuse attack. Creative malware

authors could achieve a similar effect in other ways, such as

always returning a pre-computed v15 key blob, or possibly

patching the Keymaster HAL so that it always downgrades to

v15 blobs.

that indicates that the key must be “upgraded”. The Key-

master API exposes the upgradeKey method which unwraps

(decrypts) the key, examines the OS versions inside the key

parameters and compares them to the current OS version. If

However, we found that the key parameters that are used in

5 Implications of the Attacks

In this section, we explore the possible implications of the

attacks described in Section 4. Naturally, an attacker that

controls the Normal World can simply ask the TrustZone

to locally perform any permitted individual cryptographic

operation on their behalf. However, we shall see that by ex-

tracting the keys, the attacker is able to bypass key usage

limitations. Moreover, they can perform advanced attacks that

break cryptographic protocols with remote parties, protocols

specifically designed to utilize the security guarantees offered

by the Secure World.

As we have seen in the recent line of exploits observed

in the wild [14, 23], such normal-world compromises can be

done remotely, covertly, and without changing the state of

the bootloader fuses. The attacker then aims to compromise

WebAuthn and Secure Key Import. While our attacks can-

compromise.

5.1 Authentication and Confirmation Bypass

controlling the Normal World).

| Device | Default blob version | Deterministic HDK | Can attacker set IV | Vulnerable to IV reuse | Can attacker downgrade to v15 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S8 | v15 | 3 | 7 | 7 | N/A |  |  |  |  |  |  |
| S9 | v20-s9 | 3 | 3 | 3 | v15, | 3 | v20-s9 | 3 |  |  |  |
| S10 | v20-s10 | 3 | v15, | 7 | v20-s10 | 3 | 3 | v15, | 7 | v20-s10 | 3 |
| S20/S21 | v20-s10 | 3 | v15, | 7 | v20-s10 | 3 | 3 | v15, | 7 | v20-s10 | 3 |
| This downgrade attack makes newer devices, including | ever, this behavior of the | upgradeKey | function allows our |  |  |  |  |  |  |  |  |
| Galaxy S10, S20, and S21 vulnerable to the IV reuse attack | downgrade to persist through firmware updates. |  |  |  |  |  |  |  |  |  |  |
| 4.3 | Persistence of v15 Blobs | the security properties of the higher-level protocols such as |  |  |  |  |  |  |  |  |  |
| According to the Keymaster API [29], key blobs become “old” | not decrypt v20-s10 keys generated before the compromise, |  |  |  |  |  |  |  |  |  |  |
| when the Keymaster device is updated or when the Normal | the downgrade attack can break the security of remote at- |  |  |  |  |  |  |  |  |  |  |
| World OS is upgraded to a newer version. When a key be- | testation on the latest devices (including S10, S20, and S21) |  |  |  |  |  |  |  |  |  |  |
| comes “old”, the API functions return a special error code | by compromising any key that is generated after the covert |  |  |  |  |  |  |  |  |  |  |
| the current OS version is higher it “upgrades” the key by | The Keymaster TA can be used to enforce restrictions on |  |  |  |  |  |  |  |  |  |  |
| wrapping (encrypting) it again (and adding the current OS | the use of cryptographic keys to prevent misuse of the keys |  |  |  |  |  |  |  |  |  |  |
| version to the key parameters list). | without the user’s consent or knowledge (e.g., by an attacker |  |  |  |  |  |  |  |  |  |  |
| the new blob’s wrapping are the same as those in the old key. | For example, keys | can | be | limited | for specific | use, |  |  |  |  |  |
| As any key blob created by our downgrade attack includes | such as signature only. Moreover, applications can create |  |  |  |  |  |  |  |  |  |  |
| the encryption version parameter, “upgrading” such a down- | “authentication-bound” keys that require the user to be re- |  |  |  |  |  |  |  |  |  |  |
| graded v15 key blob will result in a new but still vulnerable | cently authenticated in order to use the key, e.g., by specifying |  |  |  |  |  |  |  |  |  |  |
| v15 blob. | a timeout since the last time the user entered their passcode, |  |  |  |  |  |  |  |  |  |  |
| According to Samsung [57], this is the intended behavior, | or requiring a biometric prompt authentication [27]. |  |  |  |  |  |  |  |  |  |  |
| and since the S10 and newer devices have v20-s10 as the | The usage and authentication requirements are enforced by |  |  |  |  |  |  |  |  |  |  |
| default version, no v15 key should exist “in the wild”. How- | the Keymaster TA when it is attempting to use the blob. This |  |  |  |  |  |  |  |  |  |  |
| 258 | 31st USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |

---

## Page 10

| prevents attackers from using the keys on a device without | Cert | , the server uses | Pub | to encrypt | K | , generating | C | = |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the user’s consent — e.g., the secure hardware can refuse to | Enc | Pub | ( | K | ) | , and sends | C | to the device. |

use the key if the user is not authenticated. For instance, the

to be signed (via a trusted UI interface). Google discussed

some use cases for Protected Confirmation [19], including

Medical applications, such as an injection of insulin by Big-

foot Biomedical [13], and Enterprise applications such as

Two-Factor Authentication including Duo Mobile [10].

However, the security of these restrictions is based on the

assumption that the protected keys cannot be extracted from

inside the TrustZone. An attacker can use our attacks to ex-

tract the keys and completely bypass any restrictions. For

example, they can use “authentication-bound” without knowl-

edge of the user’s password or sign payment transactions

without user interaction or consent. Moreover, they can con-

tinue to use the keys even if they no longer have access to

the device. This is especially useful if the attacker has only

limited-time physical access to the device (e.g., search by

border agents, law enforcement, evil housekeeping).

The Keymaster TA supports Secure Key Import [69] which

allows applications to securely provision existing keys into

Keystore. The protocol’s goal is to allow servers to securely

share a secret key with an Android device while preventing the

key from being intercepted or extracted from the device, even

if the device is compromised. The key is encrypted by the

server and only decrypted inside the secure hardware. Thus

it is bound to the device, allowing it to be used in various

scenarios such as SSH/RDP, DRM, secure payment, etc. For

example, Google Pay uses Secure Key Import to provision

some of its keys [69].

Secure Key Import allows a server to securely send some

key material K to the device. A simplified version of the pro-

tocol and our attacks is shown in Fig. 5. For the full protocol

follows:

RSA that contains Priv .

accessible inside the TrustZone, and its corresponding

contains K .

While Secure Key Import protects the keys in transit, after

importing, they are encrypted inside a key blob as other im-

ported keys. Therefore, an attacker that can recover the key

material (as in our attack) can decrypt securely imported keys

and break the security of applications that use Secure Key

Import.

As before, any key K imported into Galaxy S9 can be

extracted using our IV reuse attack on the encrypted blob B K .

However, unlike the regular key import and key generation

functionalities, the Secure Key Import API call does not allow

us to specify the version of the key blob, making it resilient

to our downgrade attack. To be able to break Secure Key

Import on the newer S10, S20, and S21, we need to use a

different approach: Instead of extracting the key from B K ,

we performed our downgrade and IV reuse attacks against

B RSA and used the recovered private key Priv to decrypt C

Since B RSA was securely generated in the TrustZone — as

a v15 blob — the Keymaster TA function will happily attest

to its validity and generate a valid Cert that will allow us to

continue with the Secure Import process. When we receive the

encrypted key C from the server, we can use Priv to perform

the same decryption process as the Keymaster does to extract

the imported key K .

We demonstrate this attack in our proof-of-concept on

Galaxy S10 and S21 by performing the downgrade attack

from Section 4.2 on the wrapping key B RSA . We intercept the

request to generate the RSA keys and modify it to wrap the

generated RSA keys in blob B RSA with version v15. We then

continue to recover Priv with the IV reuse attack.

FIDO2 WebAuthn [65] is a specification by W3C and FIDO

an internal secure element called a “platform authenticator”

the secure element. Meaning that authentication is only

| attacks shown by Cooijmans et al. [18] and by Bre´ | nski et | 4. To finish the import process, the application passes | C | and |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| al. [15] fail when the restrictions are enforced. | B | RSA | to the Keymaster TA. The Keymaster TA decrypts |  |  |  |  |  |  |
| Similarly, Protected Confirmation [19] allows signing keys | B | RSA | , and uses | Priv | to decrypt | C | and recover | K | . Then it |
| to be used only if the user provides confirmation of the data | returns to the application an encrypted key blob | B | K | that |  |  |  |  |  |
| 5.2 | Extracting Keys from Secure Key Import | and recover the encrypted key in transit, as shown in Fig. 5. |  |  |  |  |  |  |  |
| details, see [25]. In high-level, Secure Key Import works as | 5.3 | Bypassing FIDO2 WebAuthn |  |  |  |  |  |  |  |
| 1. The application requests the Keymaster TA to generate | that allows the creation and use of public-key cryptography |  |  |  |  |  |  |  |  |
| an RSA private-public key pair | ( | Pub | , | Priv | ) | , and receives | to register and authenticate to websites instead of passwords. |  |  |
| an encrypted key blob | B | The authentication keys can be generated and used inside |  |  |  |  |  |  |  |
| 2. The application also requests the Keymaster TA for the | (e.g., TrustZone, Trusted Platform Module (TPM) [34]) or |  |  |  |  |  |  |  |  |
| attestation certificate | Cert | that verifies that | B | RSA | was | an external secure element called a “roaming authenticator” |  |  |  |
| generated inside the secure hardware. | Cert | is signed by | (e.g., Yubikey [70] and Solo [60]). Such secure elements aim |  |  |  |  |  |  |
| asymmetrically using a dedicated private key that is only | to provide two main security guarantees: |  |  |  |  |  |  |  |  |
| public key is signed by Google. | 1. An attacker should not be able to extract the keys from |  |  |  |  |  |  |  |  |
| 3. The application sends | Cert | to the server. After verifying | possible using the secure element, and it can’t be cloned. |  |  |  |  |  |  |
| USENIX Association | 31st USENIX Security Symposium | 259 |  |  |  |  |  |  |  |

---

## Page 11

Trusted Server Android Keymaster TA in

Verify

certificate cert

C = Enc Pub ( K )

C

Attacker decrypts K

from C using Priv

and authentication (e.g., a Biometric Prompt) and after

Hardware-Backed Android Keystore for key generation and

key attestation during registration, and for performing asser-

tions (signing with a key blob) that require user confirmation

(Section 5.2), the ( Pub , Priv ) key pair is generated by the

TrustZone

Request key generation

(attacker downgrades to

v15 blob)

B RSA Generate ( Pub, Priv )

B RSA = wrap( Pub, Priv )

IV reuse:

recover Priv from B RSA

Request attestation for B RSA

Generate attestation cert

cert

(C, B RSA ) Import wrapped key

in secure hardware

B K

used for authentication and to violate the expected security

website without the user’s presence or consent. Our attack

S20, and S21 we must first perform a downgrade attack. A

keys and modify it to force the generated keys in blob

2. The attacker uses the IV reuse attack to extract the private

key material of the key blob.

Figure 5: Simplified Secure Key Import: the “hacker” icons indicate the interception points used in our attack 2

| 2. Authentication can require user presence. For example, | required, the application passes the server’s challenge and |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| the user can be required to press a button or authenticate | B | AUT H | to the Keymaster TA, asking it to sign it with | Priv | . |  |
| using a biometric scan. | However, we can use our attacks to extract the private key |  |  |  |  |  |
| Android devices can use the Android hardware-backed Key- | guarantees. This may allow attackers to clone the “platform |  |  |  |  |  |
| store to provide similar security guarantees, using TrustZone | authenticator” and allow attestation from other devices with- |  |  |  |  |  |
| instead of a dedicated external hardware secure element. | out having further access to the target smartphone. Moreover, |  |  |  |  |  |
| WebAuthn includes two main stages (see Fig. 6): | we can use the recovered private keys to authenticate to a |  |  |  |  |  |
| 1. Registration: the device creates a key pair and sends an | is similar to our previous attack against Secure Key Import |  |  |  |  |  |
| attestation to the web server. If the attestation is verified, | (Section 5.2): On Galaxy S9 we use our IV reuse attack to |  |  |  |  |  |
| the server associates the public key with the user. | extract | Priv | from the | B | AUT H | key blob; and on Galaxy S10, |
| 2. Assertion: when the user tries to login, the server sends a | simplified version of the protocol and our attack is shown in |  |  |  |  |  |
| challenge to the device, the device requires user presence | Fig. 6. At a high-level, out attack works as follows: |  |  |  |  |  |
| receiving user consent the device signs the challenge | 1. When the device is registered to a website (e.g., Pay- |  |  |  |  |  |
| with the private key. If the server verifies the signature | pal.com), the attacker uses the downgrade attack from |  |  |  |  |  |
| (with the public key) - the user is logged in. | Section 4.2. They intercept the request to generate the |  |  |  |  |  |
| FIDO2 WebAuthn implementations for Android use the | B | AUT H | to use the v15 KDF method. |  |  |  |
| at login time. When using a Hardware-backed Keystore, We- | 3. The attacker can now silently authenticate to the website |  |  |  |  |  |
| bAuthn is supposed to withstand a compromise of the Nor- | by signing the Assertion challenge with the private key— |  |  |  |  |  |
| mal World. Similarly to what is done in Secure Key Import | without user confirmation. |  |  |  |  |  |
| Keymaster inside the TrustZone, and the application receives | We demonstrate this attack on Samsung Galaxy S10 us- |  |  |  |  |  |
| only an encrypted key blob | B | AUT H | that contains the key pair. | ing StrongKey FIDO sample Android native application and |  |  |
| The application sends the attestation certificate (including | client for FIDO [62]. The StrongKey system has two com- |  |  |  |  |  |
| the public key) to the FIDO server. When authentication is | ponents: a Linux server that runs the FIDO(R) Certified |  |  |  |  |  |
| 260 | 31st USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 12

FIDO2

Trusted Server

Registration

Registration Request

Verify certificate, cert

associate the

public key with the user

Authentication Request

Generate Challenge

Assertion A

Verify assertion A,

if successful

the user is signed-in

Authentication Request

Challenge

Assertion

Bypass Attacker

A C using

reuse attack on

the application on the device without modifications, and used

application requests to generate a key through the Keymaster

HAL. Using the downgrade attack (recall Section 4.2 and the

extended version of this paper [59]), the call to the function

nwd_generate_key is intercepted by our debugger and the

generated blob is forced to be a v15 blob B AUT H . We then

use the IV Reuse attack to on this blob and recover its private

key Priv . As in the Secure Key Import, the attestation works

seamlessly.

To validate our attack, we verified the recovered private

key Priv against the public key in the attestation certificate.

Using this private key an attacker is able to forge signatures

created an alternative, modified version of the sample applica-

Android Keymaster TA in

TrustZone

Request key generation

(attacker downgrades to

v15 blob) Generate ( Pub, Priv )

B AUTH B AUTH = wrap( Pub, Priv )

Request attestation for B AUTH

Create attestation

cert certificate chain for blob

Request user consent then

Ask to sign challenge with B

Sign Challenge with Priv in

A

After registration,

forges assertions by signing

Priv (recovered from the IV

B AUTH ) and successfully

logs in (from Android or another device)

action.

Note that in our demo, we did not make changes to the

Android sample application by StrongKey: the interception is

done outside the application, and the alternative application

(for the assertion during login) required a minimal change

to use the recovered key. The registration and authentication

was done against StrongKey’s own demo server.

6 Discussion

fast and parallelizable, seem less critical for blob encryption—

demonstrated. If the designers choose to retain AES-GCM as

such as AES-GCM-SIV [35] should prevent IV reuse attacks.

FIDO2 Challenge secure hardware

Figure 6: FIDO2 WebAuthn: the “hacker” icons indicate the interception points used in our attack 2

| StrongKey FIDO Server, and the client application, which | 4. Fig. 7d shows that the attacker successfully authenticates |  |  |  |
| --- | --- | --- | --- | --- |
| in our case is the sample Android application. We installed | using the alternative application. |  |  |  |
| it to register and authenticate against StrongKey’s demo server. | 5. Fig. 7e and Fig. 7f show an example of re-authentication |  |  |  |
| When the user registers to a website the Android StrongKey | in the alternative application in order to approve a trans- |  |  |  |
| and bypass the Assertion stage. To complete our demo, we | 6.1 | Low-Level Cryptographic Issues |  |  |
| tion, which signs the website’s challenge using the recovered | A fundamental issue in the Keymaster design is the choice of |  |  |  |
| private key | K | P | instead of using Keystore—see Fig. 7: | a stream cipher, AES-GCM. The advantages of GCM, being |
| 1. Fig. 7a shows how we attach a debugger to the Keymas- | which is always coupled with slow I/O operations; whereas its |  |  |  |
| ter HAL process. | susceptability to keystream reuse is a cause for concern, as we |  |  |  |
| 2. Fig. 7b shows the GDB output of the downgrade attack. | a building block then using a nonce-misuse resistant AEAD |  |  |  |
| 3. Fig. 7c shows that we are successfully registered against | The root cause of the IV reuse attack is that the API offered |  |  |  |
| the FIDO server—in the unmodified application. | by Keymaster TA allows the Normal World to | set | the value |  |
| USENIX Association | 31st USENIX Security Symposium | 261 |  |  |

---

## Page 13

(a) Attaching a GDB debugger to the Keymaster HAL process

(b) During registration, the GDB script performs the downgrade attack

| (c) Registration | (d) Authentication | (e) Checkout | (f) Re-authentication |
| --- | --- | --- | --- |
| success | success | example | success |

Figure 7: Screenshots from bypasing of the FIDO2 WebAuthn Sample Application by StrongKey Demo. (7c) shows the

successful registration of the legitimate application; (7d)-(7f) show the successful re-authentication of the alternative application.

| of the IV. The Keymaster API should not allow the user to | grade” old encryption blobs is already supported, it should |
| --- | --- |
| set the IV and instead always generate a random 12 byte IV. | also encrypt the new blobs with the latest (and hopefully |
| Modern encryption libraries such as Tink [31] and Google’s | safest) encryption option. A properly designed “upgrade” can |
| Trusty Keymaster implementation [32] handle the IV inter- | mitigate many downgrade attacks. |
| nally without exposing it in the API, thus protecting the user | On the positive side, using internal randomness as part of |
| from known pitfalls. | the key derivation process in the Keymaster TA makes the |
| The root cause of the downgrade attack is that the API | encryption process more robust and actually blocks our attack, |
| allows the user to choose the blob version. The user should | despite the fact that the API still allows the IV to be set. The |
| not be given a choice over any option that might affect the | reason the latest Samsung devices were still vulnerable is our |
| security of the encrypted blobs, especially if the user might be | ability to downgrade the blob version to a version that does |
| malicious. Moreover, the existence of latent code in a security- | not randomize the key derivation. |

critical application such as the Keymaster TA increases the

size of the attack surface on the application and should be

6.2 Composability: The Gap in Attestation

avoided. As we have shown, exposing such latent code to an

| external API invites exploitation by attackers. | In protocols such as FIDO2 WebAuthn and Secure Key Im- |  |
| --- | --- | --- |
| Furthermore, the persistence of our downgrade to v15 in | port, a trusted remote server uses key attestation to verify that |  |
| blobs should not have been allowed. As the process to “up- | a key was generated in secure hardware. As we’ve shown |  |
| 262 | 31st USENIX Security Symposium | USENIX Association |

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

---

## Page 14

| for Samsung devices, and Busch et al. [16] have shown for | of the security of the overall design. This should include a |  |
| --- | --- | --- |
| Huawei, the TEE implementation can be flawed, which allows | fine-grain threat model that will motivate breakdown resilient |  |
| attackers to compromise the keys. The protocol step of key | designs. |  |
| attestation is supposed to mitigate such scenarios. | For example, if several key encryption options are available, |  |
| The problem is that the attestation, as defined in the Key- | the attestation certificate should provide details on the encryp- |  |
| master HAL, | does not commit to the cryptographic method | tion method that was used for the key. This will allow servers |
| used to secure the key | . In fact it does not even commit to the | to block requests using vulnerable encryption methods and |
| version number of the Keymaster TA. This gap means that | mitigate attacks similar to our downgrade attack. Moreover, |  |
| the remote server that receives the attestation cannot set a | formal analysis that includes the full API and key encryption |  |
| policy such as “only accept attestations for keys secured with | schemes could detect issues like the IV reuse vulnerability |  |
| non-vulnerable KDF versions”. | early in the standardization process. |  |

The attestation data that is accessible to the remote

server [33, 67] includes general information about the

7 Related Work

key ( KeyDescription ), whether the key is protected

| by | a | TEE | or HSM | ( | SecurityLevel | ), key | properties | Despite their prevalence and importance, there have been very |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ( | AuthorizationList | ), and information about the device’s | few studies of the cryptographic design of TrustZone instan- |  |  |  |  |  |
| status ( | RootOfTrust | and | VerifiedBootState | ) - e.g., if the | tiations and their composability with higher-level protocols. |  |  |  |
| bootloader is locked. As recent attacks showed [14, 23], the | One exception is the review of the Huawei TrustedCore TZOS |  |  |  |  |  |  |  |
| device can be remotely compromised without changing the | by Busch et al. [16]. They have shown that, in fact, it does |  |  |  |  |  |  |  |
| bootloader state. | not provide any hardware protection at all, as it uses | hard- |  |  |  |  |  |  |
| The attestation certificate does contain a field called | coded fixed keys | . To the best of our knowledge, our work is the |  |  |  |  |  |  |
| osPatchLevel | , which could possibly allow a server to iden- | first to target and break the cryptographic design of a mature |  |  |  |  |  |  |
| tify vulnerable devices. However, as we’ve shown, Sam- | hardware protection instantiation of TrustZone. |  |  |  |  |  |  |  |
| sung’s latest Keymaster simultaneously supports | two | KDF | There have been several works showing protected keys |  |  |  |  |  |
| methods: the insecure v15 and the secure v20-s10, and the | extraction using side-channels attacks. Lapid and Wool [40] |  |  |  |  |  |  |  |
| osPatchLevel | field does not indicate which method was | showed that the Kinibi TZOS’s AES-GCM implementation |  |  |  |  |  |  |
| used. Therefore, relying on the Keymaster TA’s software patch | is vulnerable to cache timing side-channel attacks, allowing |  |  |  |  |  |  |  |
| level may still leave opportunities for misuse. | Key Encryption Key (KEK) to be compromised. Keegan [51] |  |  |  |  |  |  |  |
| The security of protocols such WebAuthn depends on its | showed that the ECDSA implementation in the QSEE’s Key- |  |  |  |  |  |  |  |
| composition with the implementation and cryptographic de- | master TA was vulnerable to a cache timing side-channel |  |  |  |  |  |  |  |
| sign of the Keymaster TA. The current approach of using | attack that can be exploited to leak a hardware-protected EC |  |  |  |  |  |  |  |
| vendor specific black-box designs makes it impossible to ana- | key. In contrast, as we target the cryptographic design, we |  |  |  |  |  |  |  |
| lyze the security of the composition. As we have shown, this | were able to extract keys even when side-channels mitiga- |  |  |  |  |  |  |  |
| provides ample room for vulnerabilities. | tions such as Samsung’s Strongbox security processor were |  |  |  |  |  |  |  |

implemented.

There have been several previous works analyzing the us-

6.3 TrustZone-based Keystore Standard

age of Keystore-protected keys in applications and higher-

| The attacks we described in this paper highlight the critical | level protocols. Sabt et al. [52] showed a forgery attack against |  |  |
| --- | --- | --- | --- |
| vulnerabilities that can arise from problems in the crypto- | the | software-only | Keymaster provided by Google. In compar- |
| graphic design of Trustzone-based Keystore. However, so far, | ison, our attacks work against | hardware-backed | Keymaster |
| these cryptographic designs and protocols have not received | on the latest Samsung devices. Cooijmans et al. [18], and |  |  |
| much attention in the academic literature. We believe that this | Bre´ | nski et al. [15] showed that a privileged attacker could |  |
| is mainly due to the fact that the current ecosystem is based on | simply use Keystore keys without user consent if the keys |  |  |
| blackbox designs, with an API that is inconsistent and frag- | are not authentication-bound. In contrast, our attack recov- |  |  |
| mented between different vendors. Indeed, uncovering the | ers the full keying material, allowing an attacker to use even |  |  |
| vulnerabilities presented in this paper required a significant | authentication-bound keys in unauthorized ways (bypassing |  |  |
| amount of time-consuming reverse-engineering effort. | authentication/Protected Confirmation/Cloning). Prünster et |  |  |
| We hope that our work will motivate further research on | al. [47] explored the usage of key attestation in the Android |  |  |
| Keystore security and lead to a uniform open standard for | Keystore for sensitive operations. Our attacks on FIDO2 We- |  |  |
| the Keymaster HAL and TA. Such a standard can reduce the | bAuthn and Google’s Secure Key Import bypass attestation |  |  |
| current barriers preventing researchers from analyzing the | because the key is indeed generated in secure hardware (and |  |  |
| security of the cryptographic designs and protocols. Similar | the attacker recovers it). |  |  |
| to the standardization process of TLS 1.3 [50], a collaboration | Software vulnerabilities in TrustZone-based TEEs were |  |  |
| between academia and industry will allow for formal analysis | studied by many: Pinto and Santo [46] surveyed research on |  |  |
| USENIX Association | 31st USENIX Security Symposium | 263 |  |

---

## Page 15

| TrustZone and weaknesses of existing systems, Cerdeira et | tivate the need for an open and standardized cryptographic |
| --- | --- |
| al. [17] classified different software vulnerabilities in TEEs | design. |

and analyzed their architectural flaws, and Fleischer et al. [22]

evaluated the exploitability of memory corruptions in TEEs.

Alendal [1] exploited a stack-based buffer overflow to com-

language is used or if a separate hardware security model is

deployed.

When our research began, there were few resources avail-

design.

8 Conclusions

Vendors including Samsung and Qualcomm maintain secrecy

around their implementation and design of TZOSs and TAs.

As we have shown, there are dangerous pitfalls when dealing

with cryptographic systems. The design and implementation

details should be well audited and reviewed by independent

researchers and should not rely on the difficulty of reverse

engineering proprietary systems.

In this work, we examined the cryptographic design and

implementation of Android’s Hardware-Backed Keystore in

Samsung’s Galaxy S8, S9, S10, S20, and S21 flagship devices.

By an extensive reverse engineering effort, we were able to

analyze the Keymaster TA in multiple TZOSs (TEEGRIS,

Kinibi, and QSEE). To the best of our knowledge, we are the

first to explore the details of the Keymaster TA implementa-

tion in TEEGRIS.

Through our analysis we unveiled severe cryptographic de-

sign flaws. We identified an IV reuse attack on AES-GCM that

allows an attacker to extract hardware-protected key material,

and a downgrade attack that makes even the latest Samsung

devices vulnerable to the IV reuse attack. We demonstrated a

working key extraction attacks on the latest devices. We also

server: we demonstrated a working FIDO2 WebAuthn login

Acknowledgement

References

forensics-23566 .

[2] ARM. ARM trusted firmware design. URL: https:

//chromium.googlesource.com/external/github.

com/ARM-software/arm-trusted-firmware/+/v0.4-

rc1/docs/firmware-design.md .

[3] ARM. ARM TrustZone. URL: https://developer.arm.

com/ip-products/security-ip/trustzone .

[4] ARM. Privilege and exception levels. URL:

https://developer.arm.com/documentation/102412/

0100/Privilege-and-Exception-levels .

[5] ARM. SMC calling convention (SMCCC). URL: https://

developer.arm.com/documentation/den0028/latest .

[6] ARM. Trusted Firmware-A. URL: https://github.com/

ARM-software/arm-trusted-firmware .

[7] ARM. The TrustZone hardware architecture. URL:

https://developer.arm.com/documentation/100935/

0100/The-TrustZone-hardware-architecture- .

[8] ARM. ARM security technology: Building a secure system us-

ing TrustZone technology, 2009. URL: https://developer.

arm.com/documentation/PRD29-GENC-009492/c .

[9] Brandon Azad. An iOS hacker tries Android, 2020. from

Project Zero. URL: https://googleprojectzero.

blogspot.com/2020/12/an-ios-hacker-tries-

android.html .

[10] James Barclay, Robbie Small, and Taylor Mccaslin. Humans

only: Duo mobile and android protected confirmation. Duo

[11] Gal Beniamini. Extracting Qualcomm’s KeyMaster keys -

| promise the secure element of Samsung S20 Exynos devices. | The authors would like to thank Federico Menarini and |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Other attacks against Trustonic Kinibi and Qualcomm QSEE | Alexander Tarasikov for their interesting insights. |  |  |  |  |  |  |
| include Sang et al. [48], Adamski, Guilbon and Peterlin [49], | This work was supported by the Robert Bosch Founda- |  |  |  |  |  |  |
| Beniamini [11, 12], and Machiry et al. [41]. Our work shows | tion; Len Blavatnik and the Blavatnik Family foundation and |  |  |  |  |  |  |
| cryptographic design flaws that are not implementation flaws | Blavatnik ICRC at Tel-Aviv University; The second and third |  |  |  |  |  |  |
| and will therefore persist even if a memory-safe programming | authors are members of CPIIS. |  |  |  |  |  |  |
| able on the TEEGRIS TZOS. One exception is a blog by | [1] Gunnar Alendal. | Chip | chop | - | smashing | the | mobile |
| Tarasikov [63] which provided useful insight for reverse- | phone secure chip for fun and digital forensics. | BlackHat |  |  |  |  |  |
| engineering TEEGRIS. Later, Menarini et al. [43] published a | USA, 2021. | URL: | https://www.blackhat.com/us- |  |  |  |  |
| detailed blog on exploiting TEEGRIS. However, both are fo- | 21/briefings/schedule/#chip-chop---smashing-the- |  |  |  |  |  |  |
| cused on software vulnerabilities and not on the cryptographic | mobile-phone-secure-chip-for-fun-and-digital- |  |  |  |  |  |  |
| showed the implications of our attacks on two higher-level | blog, 2018. URL: | https://duo.com/blog/humans-only- |  |  |  |  |  |
| cryptographic protocols between the TrustZone and a remote | duo-mobile-and-android-protected-confirmation | . |  |  |  |  |  |
| bypass and a compromise of Google’s Secure Key Import. | breaking Android full disk encryption, 2016. Accessed: 2019- |  |  |  |  |  |  |
| Finally, we note that our attacks on the higher-level crypto- | 11-01. URL: | https://bits-please.blogspot.com/2016/ |  |  |  |  |  |
| graphic protocols work on new devices due to subtle attacks | 06/extracting-qualcomms-keymaster-keys.html | . |  |  |  |  |  |
| arising from their composability with the lower-level key- | [12] Gal Beniamini. | QSEE privilege escalation vulnerability |  |  |  |  |  |
| encryption. Furthermore, we argue that the design choice of | and exploit (CVE-2015-6639), 2016. Accessed: 2019-11- |  |  |  |  |  |  |
| using the fragile AES-GCM stream cipher for authenticated | 01. URL: | http://bits-please.blogspot.com/2016/05/ |  |  |  |  |  |
| blob encryption deserves discussion. These issues further mo- | qsee-privilege-escalation-vulnerability.html | . |  |  |  |  |  |
| 264 | 31st USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 16

| [13] Bigfoot | Biomedical, | 2018. | URL: | https://www. | [29] Google. | Ikeymasterdevice.hal. | URL: | https: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bigfootbiomedical.com/about/press-room/press- | //android.googlesource.com/platform/hardware/ |  |  |  |  |  |  |  |
| releases/google-io-2018 | . | interfaces/+/master/keymaster/4.0/ | . |  |  |  |  |  |
| [14] Mark Brand. | In-the-wild series: Android exploits, 2021. | [30] Google. | Keymaster functions. | URL: | https://source. |  |  |  |
| from Project Zero. | URL: | https://googleprojectzero. | android.com/security/keystore/implementer-ref | . |  |  |  |  |
| blogspot.com/2021/01/in-wild-series-android- | [31] Google. | Tink cryptographic library. | URL: | https:// |  |  |  |  |
| exploits.html | . | developers.google.com/tink | . |  |  |  |  |  |
| [15] Kamil Bre´ | nski, Krzysztof Pranczk, and Mateusz Fruba. How | [32] Google. | generate_nonce | . | URL: | https://android. |  |  |
| secure is your Android keystore authentication? F-Secure Labs, | googlesource.com/platform/system/keymaster/+/ |  |  |  |  |  |  |  |
| 2019. | URL: | https://labs.f-secure.com/blog/how- | master/key_blob_utils/auth_encrypted_key_blob. |  |  |  |  |  |
| secure-is-your-android-keystore-authentication/ | . | cpp#40 | . |  |  |  |  |  |
| [16] Marcel Busch, Johannes Westphal, and Tilo Mueller. | Un- | [33] Google. Verifying hardware-backed key pairs with key attesta- |  |  |  |  |  |  |
| earthing the TrustedCore: A critical review on Huawei’s trusted | tion. URL: | https://developer.android.com/training/ |  |  |  |  |  |  |
| execution environment. In | 14th USENIX Workshop on Offen- | articles/security-key-attestation | . |  |  |  |  |  |

sive Technologies (WOOT’20) , 2020.

[17] David Cerdeira, Nuno Santos, Pedro Fonseca, and Sandro Pinto.

Sok: Understanding the prevailing security vulnerabilities in

trustzone-assisted TEE systems. In 2020 IEEE Symposium on

Security and Privacy (SP) , pages 1416–1432. IEEE, 2020.

[18] Tim Cooijmans, Joeri de Ruiter, and Erik Poll. Analysis of

secure key storage solutions on Android. In Proceedings of the

4th ACM Workshop on Security and Privacy in Smartphones

[19] Janis Danisevskis. Android protected confirmation: Tak-

ing transaction security to the next level, 2018. URL:

https://android-developers.googleblog.com/2018/

10/android-protected-confirmation.html .

[20] Dirty cow, 2016. Accessed: 2019-11-01. URL: https://

dirtycow.ninja/ .

https://github.com/vngkv123/articles/blob/main/

Galaxy’sMeltdown-ExploitingSVE-2020-18610.md .

[22] Fabian Fleischer, Marcel Busch, and Phillip Kuhrt. Memory

corruption attacks within Android TEEs: A case study based on

OP-TEE. In Proceedings of the 15th International Conference

on Availability, Reliability and Security , pages 1–9, 2020.

ern android devices. BlackHat USA, 2020. URL:

https://i.blackhat.com/USA-20/Thursday/us-20-

Gong-TiYunZong-An-Exploit-Chain-To-Remotely-

Root-Modern-Android-Devices.pdf .

[24] Google. Android keystore system. URL: https:

//developer.android.com/training/articles/

keystore .

android.com/training/articles/keystore#

ImportingEncryptedKeys .

googlesource.com/boringssl/ .

android.com/security/keystore .

[34] Trusted Computing Group. Trusted platform module (tpm)

summary, 2007. URL: https://trustedcomputinggroup.

org/wp-content/uploads/Trusted-Platform-Module-

Summary_04292008.pdf .

[35] Shay Gueron, Adam Langley, and Yehuda Lindell. AES-GCM-

SIV: Specification and analysis. IACR Cryptol. ePrint Arch. ,

2017:168, 2017.

Koushik Sen, and Michael Grace. PARTEMU: Enabling dy-

namic analysis of real-world TrustZone software using emu-

lation. In 29th USENIX Security Symposium (USENIX Secu-

rity’20) , pages 789–806, 2020.

[37] Roee Hay and Avi Dayan. Android keystore stack

buffer overflow. CVE-2014-3100, 2014. URL:

https://securityintelligence.com/android-

[38] Antoine Joux. Authentication failures in NIST version of

GCM. NIST Comment , page 3, 2006.

[39] Mateusz Jurczyk. Samsung android multiple interac-

tionless rces and other remote access issues in qmage

image codec built into skia, 2020. from Project

Zero. URL: https://bugs.chromium.org/p/project-

[40] Ben Lapid and Avishai Wool. Navigating the Samsung Trust-

Zone and cache-attacks on the keymaster trustlet. In European

Symposium on Research in Computer Security , pages 175–196.

Springer, 2018.

[41] Aravind Machiry, Eric Gustafson, Chad Spensky, Christo-

pher Salls, Nick Stephens, Ruoyu Wang, Antonio Bianchi,

Yung Ryn Choe, Christopher Kruegel, and Giovanni Vigna.

[42] René Mayrhofer, Jeffrey Vander Stoep, Chad Brubaker, and

Nick Kralevich. The Android platform security model. ACM

2021.

investigation-part1 .

| & Mobile Devices | , pages 11–20, 2014. | [36] Lee | Harrison, Hayawardh | Vijayakumar, Rohan | Padhye, |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [21] ENKI. | Galaxy’s | meltdown | - | exploiting | SVE- | keystore-stack-buffer-overflow-to-keep-things- |  |
| 2020-18610, 2020. | Accessed: | 2021-02-01. | URL: | simple-buffers-are-always-larger-than-needed/ | . |  |  |
| [23] Guang Gong. | An exploit chain to remotely root mod- | zero/issues/detail?id=2002 | . |  |  |  |  |
| [25] Google. | Android keystore | system | - | import encrypted | BOOMERANG: Exploiting the semantic gap in trusted execu- |  |  |
| keys | more | securely. | URL: | https://developer. | tion environments. In | NDSS | , 2017. |
| [26] Google. | Boringssl. | URL: | https://boringssl. | Transactions on Privacy and Security (TOPS) | , 24(3):1–35, |  |  |
| [27] Google. Gatekeeper. URL: | https://source.android.com/ | [43] Federico | Menarini. | Samsung | investigation | part | 1: |
| security/authentication/gatekeeper | . | TEEs, TrustZone and TEEGRIS, 2021. | Accessed: | 2021- |  |  |  |
| [28] Google. Hardware-backed keystore. URL: | https://source. | 02-23. URL: | https://www.riscure.com/blog/samsung- |  |  |  |  |
| USENIX Association | 31st USENIX Security Symposium | 265 |  |  |  |  |  |

---

## Page 17

[44] Gyorgy Miru. [bugtales] a nerve-racking bug colli- [60] SoloKeys. The first open-source fido2 security key. URL:

sion in samsung’s npu driver, 2021. from TASZK. https://solokeys.com/ .

URL: https://labs.taszk.io/articles/post/bug_

collision_in_samsungs_npu_driver/ .

ghidra .

samsungs-trustzone-part-1.html .

ACM SIGSAC Conference on Computer and Communications

Security , pages 181–194, 2019.

531–548. Springer, 2016.

[53] Samsung. KNOX white paper: Root of trust. URL:

https://docs.samsungknox.com/admin/whitepaper/

kpe/hardware-backed-root-of-trust.htm .

[54] Samsung. Real-time kernel protection (RKP). URL:

https://www.samsungknox.com/en/blog/real-time-

kernel-protection-rkp .

opensource.samsung.com/uploadList .

cryptographic-module-validation-program/

documents/security-policies/140sp3027.pdf .

[61] Gossamer Security Solutions. Samsung Electronics Co., Ltd.

Samsung Galaxy devices on Android 10 – spring security

[62] StrongKey. Strongkey FIDO server (skfs), community edition.

selling_mobile_phones .

[69] Lilian Young, Shawn Willden, and Frank Salim. New

keystore features keep your slice of Android pie

[70] Yubico. Yubikey: Built for high security. URL: https://www.

yubico.com/ .

A ARM TrustZone Overview

ARM provides a reference implementation of secure world

software called ARM Trusted Firmware [6] (ATF), and the

(e.g., Qualcomm, Trustonic, Samsung) based on ATF. ATF is

To achieve the isolation of the TEE and the REE, TrustZone

uses the NS (Non-Secure) bit which is set to 0 if the processor

| [45] NSA. | Ghidra software reverse engineering framework. | target, 2020. | URL: | https://www.niap-ccevs.org/MMO/ |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| URL: | https://github.com/NationalSecurityAgency/ | Product/st_VID11042-st.pdf | . |  |  |  |  |  |
| [46] Sandro Pinto and Nuno Santos. Demystifying ARM TrustZone: | URL: | https://github.com/StrongKey/fido2 | . |  |  |  |  |  |
| A comprehensive survey. | ACM Computing Surveys (CSUR) | , | [63] Alexander Tarasikov. | Reverse-engineering Samsung S10 |  |  |  |  |
| 51(6):1–36, 2019. | TEEGRIS | TrustZone | OS, 2019. | Accessed: | 2019-11-03. |  |  |  |
| [47] Bernd Prünster, Gerald Palfinger, and Christian Kollmann. | URL: | https://allsoftwaresucks.blogspot.com/2019/ |  |  |  |  |  |  |
| Fides: Unleashing the full potential of remote attestation. In | 05/reverse-engineering-samsung-exynos-9820.html | . |  |  |  |  |  |  |
| ICETE (2) | , pages 314–321, 2019. | [64] Robert Triggs. | Widevine digital rights management ex- |  |  |  |  |  |
| [48] Quarkslab. | Reverse | engineering | Samsung | s6 | plained. | Android Authority, 2019. | URL: | https://www. |
| sboot | - | part | i, 2017. | Accessed: | 2019-11-01. | URL: | androidauthority.com/widevine-explained-821935/ | . |
| https://blog.quarkslab.com/reverse-engineering- | [65] W3C. Web authentication: An API for accessing public key |  |  |  |  |  |  |  |
| samsung-s6-sboot-part-i.html | . | credentials level 2. | W3C Recommendation, 2021. | URL: |  |  |  |  |
| [49] Quarkslab. | A | deep | dive | into | Samsung’s | trust- | https://www.w3.org/TR/webauthn-2/ | . |
| zone | (part | 1), 2019. | Accessed: | 2019-12-11. | URL: | [66] Wikipedia. | List of best-selling mobile phones. | URL: |
| https://blog.quarkslab.com/a-deep-dive-into- | https://en.wikipedia.org/wiki/List_of_best- |  |  |  |  |  |  |  |
| [50] E. Rescorla. | The Transport Layer Security (TLS) Protocol | [67] Shawn Willden. | Keystore key attestation. | Google blog, |  |  |  |  |
| Version 1.3. | RFC 8446, IETF, August 2018. | URL: | http: | 2017. URL: | https://android-developers.googleblog. |  |  |  |
| //tools.ietf.org/rfc/rfc8446.txt | . | com/2017/09/keystore-key-attestation.html | . |  |  |  |  |  |
| [51] Keegan Ryan. | Hardware-backed heist: extracting ECDSA | [68] John Wu. Magisk: The magic mask for Android. URL: | https: |  |  |  |  |  |
| keys from Qualcomm’s TrustZone. In | Proceedings of the 2019 | //github.com/topjohnwu/Magisk | . |  |  |  |  |  |
| [52] Mohamed Sabt and Jacques Traoré. Breaking into the keystore: | a | little | safer. | Google | security | blog, 2018. | URL: |  |
| A practical forgery attack against Android keystore. In | Eu- | https://security.googleblog.com/2018/12/new- |  |  |  |  |  |  |
| ropean Symposium on Research in Computer Security | , pages | keystore-features-keep-your-slice.html | . |  |  |  |  |  |
| [55] Samsung. | Samsung | open | source. | URL: | https:// | Secure World is usually implemented by a specific vendor |  |  |
| [56] Samsung. Samsung SCrypto cryptographic module, version | responsible for performing Secure Boot, loading the differ- |  |  |  |  |  |  |  |
| 2.0. FIPS 140-2 Non-Proprietary Security Policy v1.3, 2017. | ent bootloaders and launching the REE and TEE [2]. It also |  |  |  |  |  |  |  |
| URL: | https://csrc.nist.gov/CSRC/media/projects/ | contains a reference implementation for a Secure Monitor. |  |  |  |  |  |  |
| [57] Samsung Mobile Security. Personal communications, 2021. | is in Secure state and set to 1 if the processor is in Non-Secure |  |  |  |  |  |  |  |
| [58] Alon Shakevsky, Eyal Ronen, and Avishai Wool. Keybuster: | state. The secure state can be switched by executing the SMC |  |  |  |  |  |  |  |
| a keymaster client for samsung devices. | URL: | https:// | opcode (in exception level higher than EL0, e.g., EL1). |  |  |  |  |  |
| github.com/shakevsky/keybuster | . | The Secure state applies to hardware peripherals and mem- |  |  |  |  |  |  |
| [59] Alon Shakevsky, Eyal Ronen, and Avishai Wool. Trust Dies in | ory, by using the TZASC register (allows to restrict memory |  |  |  |  |  |  |  |
| Darkness: Shedding Light on Samsung’s TrustZone Keymaster | to Secure World only) and the TrustZone Protection Con- |  |  |  |  |  |  |  |
| Design. | IACR Cryptol. ePrint Arch. | , 2022. | URL: | https: | troller (TZPC). Menarini et al. [43] shows an example of how |  |  |  |
| //eprint.iacr.org/2022/208 | . | the Trusted User Interface (TUI) uses the TZPC to modify |  |  |  |  |  |  |
| 266 | 31st USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |

---

## Page 18

| the display and touch controllers as secure and the TZASC | There are more than 21 command handlers in the Keymas- |
| --- | --- |
| configures secure memory for the display. Thus, a user can | ter TA, including the following, that implement the similarly |
| enter a pin for a payment which will be safe from any Nor- | named API calls as in Section 3.2: |

mal World attacker (even if the attacker executes code in the

Android OS kernel) and will not be leaked.

The Normal World can only access Non-secure memory,

but the Secure World can access Non-Secure memory. The

ARM documentation [7] states that Secure and Non-secure

cache entries can coexist, and that the Normal World can only

get a cache hit on Non-secure cache lines.

The ARMv8-A processor supports 4 exception levels [4]:

4. EL3 - Secure Monitor

Fig. 1 shows the components in each exception level in the

TrustZone architecture.

When the processor is in Secure mode, we can denote S-

ELx, e.g., S-EL0 is the secure EL0. Most of our research

focuses on S-EL0 (where the Keymaster TA executes), S-EL1

code running in EL3. The arguments are passed in registers

and then used to select which Secure function to execute.

These calls may then be passed on to a Trusted OS in S-EL1.”.

Note that the Secure World also uses SMC for some oper-

ations, such as power management or privileged operations

that can only be done in the Secure Monitor (EL3).

B The Control Flow in the Keymaster TA

Upon receiving control from an API call (from our client or

from the Keymaster HAL), the Keymaster TA has the follow-

ing flow in TA_InvokeCommandEntryPoint :

1. Validates the parameter types for the input and output

buffers and makes sure that the memory references that

4. Fills the output buffer with ASN.1 structure outdata .

• swd_generate_key

• swd_import_key

• swd_import_wrapped_key

• swd_get_key_characteristics

• swd_export_key

• swd_attest_key

• swd_begin / swd_update / swd_finish

Blob-creating commands accept key parameters that are

– Algorithm (RSA/EC/AES/DES/HMAC)

– Key size (e.g., 768/1024/2048/3072/4096 for RSA

or 128/192/256 for AES)

– Mode of operation (e.g., ECB/CBC/CTR/GCM)

– Padding (e.g., none/RSA-OAEP/RSA-PSS)

– Digest (e.g., none/md5/sha1/sha256)

The main focus of our research is how key blobs are de-

crypted/encrypted. The blob structure is as follows: The

key material is serialized into an ASN.1 structure called

km_key_blob that contains a version number, key mate-

rial and key parameters. The ASN.1 structure is then en-

crypted using AES-256-GCM with an Hardware Derived Key-

encryption-key (HDK). This encryption is called “wrapping”

and is the topic of much of our work. The “wrapped” key

blob is serialized again into another ASN.1 structure called

km_ekey_blob that contains information that is required for

decryption, such as the IV and AAD that was used to encrypt.

Fig. 8 shows the process of key wrapping/unwrapping in the

Keymaster TA which we describe in this section.

To ensure that key blobs are hardware-protected, the device

uses the following keys:

Section 3.4.

| 1. EL0 - usermode (application in Android, TA in TZOS) | delivered in the | indata | structure. The parameters control how |  |
| --- | --- | --- | --- | --- |
| 2. EL1 - kernelmode (Android kernel, TZOS kernel) | the key is generated and are also placed inside the blob. They |  |  |  |
| 3. EL2 - hypervisor (used by Samsung to implement | are subsequently used during the cryptographic operations |  |  |  |
| RKP [54], which protects the integrity of the Android | that take the blob as input. Key parameters include: |  |  |  |
| kernel) | • Cipher information including: |  |  |  |
| (where the TZOS kernel handles ioctls that the Keymaster TA | • The parameters can also include optional access control |  |  |  |
| calls) and EL3 (where the Secure Monitor executes a function | restrictions on the created blob, including: |  |  |  |
| handler for a given SMC). | – | Purpose (e.g., limit to encryption/signing only, or |  |  |
| The Secure Monitor provides the interface between the | only encryption and decryption). |  |  |  |
| two worlds and performs switching when the SMC (Secure | – | Maximum number of uses per boot / minimum |  |  |
| Monitor Call) opcode is executed. Per the ARM SMC Calling | seconds between operations / expiration date. |  |  |  |
| Convention [5], “The SMC instruction is used to generate | – | Require authentication (e.g., by password or bio- |  |  |
| a synchronous exception that is handled by Secure Monitor | metric prompt) or confirmation by the user. |  |  |  |
| are sent from the Normal World belong to the REE. | • Root Encryption Key (REK): a 256-bit AES key that is |  |  |  |
| 2. Parses the input buffer as an ASN.1 structure | indata | available only in secure hardware and is device-unique. |  |  |
| and validates it. | • Hardware Derived Key (HDK): a 256-bit AES key that |  |  |  |
| 3. Calls | the | appropriate | command handler based on | is derived from the REK per blob encryption using the |
| indata->cmd | . | Key Derivation Function (KDF) which we discussed in |  |  |
| USENIX Association | 31st USENIX Security Symposium | 267 |  |  |

---

## Page 19

| Normal World | Secure Monitor EL3 | Secure World EL1 | Secure World EL0 |
| --- | --- | --- | --- |
| TEEGRIS kernel | Keymaster TA |  |  |
| Keymaster HAL | SMC | SMC | Schedule TA |

Handle ioctl

AES-GCM-256 then SMC

in SoC

Wrapped key

Handle ioctl

then SMC

KDF with REK HDK

in SoC

Figure 8: Key wrapping in Keymaster TA in TEEGRIS

• The IV, that is either generated or is located in

the parameters that are required for decryption

( KM_TAG_EKEY_BLOB_IV )

• The AAD that is computed in swd_get_aad

• The data to encrypt/decrypt

• The authentication tag for decryption

( KM_TAG_EKEY_BLOB_AUTH_TAG )

• A salt value that is computed in swd_get_salt and is

used by KDF to derive the HDK from the REK.

“v20-s10” based on the constant strings that are used by the

Option 1: "Short" key wrap

ioctl

WRAPPED_WITH_REK tz_wrap/tz_unwrap

key_blob_asn1_size <= 4096

Wrapped key fill struct with salt, iv, aad,

plaintext/encrypted, auth_tag,

request (encyption/decryption)

| ioctl | Option 2: "Long" key wrap |
| --- | --- |
| KDF_WITH_REK | tz_wrap/tz_unwrap |

key_blob_asn1_size > 4096

HDK

fill struct with kdf_key, salt, hdk

Keymaster TA calls

aes256_gcm_{en,de}crypt with HDK as the

encryption key to get the wrapped key

2

HDK from the salt and then perform AES-GCM in the crypto

engine. Conversely, if the length is greater than 4096 bytes,

the Keymaster TA uses the TEES_DeriveKeyKDF library func-

tion to derive the HDK by calling the crypto driver, and then

uses a software implementation of AES-GCM-256 (using

the SCrypto library [56] that is based on BoringSSL [26]) to

perform the encryption.

In order to understand how the key blobs are encrypted,

we reversed engineered TEEGRIS, found the dev://crypto

driver and analysed its ioctl method. We focus on two

master TA (resp.).

Keymaster TA.

with a different arguments (0 as the first argument instead

| At a high level, the AES operation uses the following fields: | the | TEES_WrappedWithREK | library function to derive the |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| The salt value is computed in the | swd_get_salt | function | specific ioctl commands: | CRYPT_FUNC_WRAPPED_WITH_REK |  |  |
| as the SHA256 digest of a concatenation of values based on | (that encrypts or decrypts key blobs) and | CRYPT_FUNC_KDF |  |  |  |  |
| the encryption version | ekey_blob->enc_ver | . We refer to | (that derives a HDK from the REK), that are called from |  |  |  |
| values of | enc_ver | symbolically as either “v15”, “v20-s9” or | TEES_WrappedWithREK | / | TEES_DeriveKeyKDF | in the Key- |
| KDF and the device model we observed them on (technically | CRYPT_FUNC_WRAPPED_WITH_REK | checks that the calling |  |  |  |  |
| enc_ver | is a byte value). | task in TEEGRIS is the Keymaster TA by comparing the |  |  |  |  |
| The | decryption/encryption | of | ASN.1-serialized | key | current UID to the UID of the Keymaster (10 bytes of null, |  |
| material occurs in the | tz_unwrap | / | tz_wrap | functions (resp.), | then “KEYMST”) and rejects any other task. It then copies the |  |
| which | call | TEES_WrappedWithREK | / | TEES_DeriveKeyKDF | struct that the Keymaster TA sent to DMA memory, edits the |  |
| from | libteesl.so | , which in turn does a ioctl to the crypto | salt by appending the Keymaster TA’s own UID (16 bytes) and |  |  |  |
| driver ( | dev://crypto | ). See Appendix C for details on how | executes an SMC instruction (passing the physical address of |  |  |  |
| TEEGRIS uses the hardware crypto engine to compute the | the memory where the struct resides as the third argument). If |  |  |  |  |  |
| KDF with REK and AES-GCM operations. | the SMC returns 0, the modified struct is copied back to the |  |  |  |  |  |
| C | KDF and Key Wrapping in TEEGRIS | CRYPT_FUNC_KDF | also calls the same SMC function but |  |  |  |
| Figure 8 illustrates the two flows that use the salt, IV, AAD, | of 1). It computes the SHA-256 digest of the KDF key, the |  |  |  |  |  |
| and authentication tag to perform the cryptographic wrap- | task UID and group and the salt, then passes the address of |  |  |  |  |  |
| ping/unwrapping in TEEGRIS. If the length of the ASN.1- | the struct that contains both the hash and the HDK (with its |  |  |  |  |  |
| serialized key is at most 4096 bytes, the Keymaster TA calls | length). The SMC fills the bytes of the HDK. |  |  |  |  |  |
| 268 | 31st USENIX Security Symposium | USENIX Association |  |  |  |  |

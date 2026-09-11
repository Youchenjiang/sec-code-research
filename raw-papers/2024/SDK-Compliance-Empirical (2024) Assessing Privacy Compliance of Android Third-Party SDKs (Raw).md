---
title: "Assessing Privacy Compliance of Android Third-Party SDKs"
author: "Mark Huasong Meng; Chuan Yan; Qing Zhang; Zeyu Wang; Kailong Wang; Sin Gee Teo; Guangdong Bai; Jin Song Dong"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 14
---

# Assessing Privacy Compliance of Android Third-Party SDKs

> **作者**：Mark Huasong Meng; Chuan Yan; Qing Zhang; Zeyu Wang; Kailong Wang; Sin Gee Teo; Guangdong Bai; Jin Song Dong
> **總頁數**：14 頁

---

## Page 1

1

Assessing Privacy Compliance of Android

Third-Party SDKs

Mark Huasong Meng, Chuan Yan, Qing Zhang, Zeyu Wang, Kailong Wang,

Sin G. Teo, Guangdong Bai, and Jin Song Dong

Abstract —Third-party Software Development Kits (SDKs) are with an average app integrating approximately 8.6 SDKs [6],

widely adopted in Android app development, to accelerate devel- [7]. However, this widespread dependency also introduces

opment pipelines and enhance app functionality effortlessly. How- significant security and privacy concerns. The complexity

ever, this convenience raises substantial concerns about unautho-

rized access to users’ privacy-sensitive information, which could of the software supply chain and the opaque data handling

be further abused for illegitimate purposes like user tracking or practices of some SDKs can lead to privacy risks and security

monetization. Our study offers a targeted analysis of user privacy vulnerabilities, either due to malicious intent or unintentional

protection among Android third-party SDKs, filling a critical gap oversights. These can be exploited by malevolent actors or

in the Android software supply chain. It focuses on two aspects of lead to inadvertent privacy violations, as evidenced by recent

their privacy practices, including data exfiltration and behavior-

policy compliance (or privacy compliance ), utilizing techniques of high-profile incidents related to third-party SDKs [8], [9].

taint analysis and large language models. It covers 158 widely- The privacy issues caused by SDKs could be further magni-

used SDKs from two key SDK release platforms, the official fied in the pre-installed apps on Android devices. These apps

one and a large alternative one. From them, we identified 338 are bundled by device manufacturers or network carriers, and

instances of privacy data exfiltration. On privacy compliance, our therefore, often have an extremely great user population. They

study reveals that more than 30% of the examined SDKs fail to

provide a privacy policy to disclose their data handling practices. come with high privileges and are typically non-removable,

Among those that provide privacy policies, 37% of them over- such that an SDK embedded by them can stealthily perform

collect user data, and 88% falsely claim access to sensitive data. higher-privileged operations that normal apps are unable to.

We revisit the latest versions of the SDKs after 12 months. An illustrative example is an app named “ Mobile Services

Our analysis demonstrates a persistent lack of improvement in Manager ” pre-installed on certain Android devices, which

these concerning trends. Based on our findings, we propose three

actionable recommendations to mitigate the privacy leakage risks was found to download apps without user consent due to a

and enhance privacy protection for Android users. Our research malicious third-party SDK embedded [10], [11].

| not only serves as an urgent call for industry attention but also | Assessing privacy practices of SDKs includes two key as- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| provides crucial insights for future regulatory interventions. | pects, i.e., | data exfiltration | and | behavior-policy compliance | (or |
| Index Terms | —mobile, privacy assessment, taint analysis. | privacy compliance | ). The data exfiltration involves the behav- |  |  |

iors of locating sensitive data in publicly accessible places,

I. I NTRODUCTION such as the publicly accessible directories in file systems and

The advent and ubiquity of third-party Software Devel- the Internet. The opacity of SDKs’ operations and their “black-

opment Kits (SDKs) in Android app development herald a box” nature hinders meaningful assessments, leaving both end-

profound shift in the mobile software development paradigm, users and app developers in the dark and elevating risks.

transforming efficiency and accelerating innovation. These Dishonest or malicious SDKs may disguise as their embedding

SDKs provide pre-built reusable code that offers a broad apps to extensively collect privacy-sensitive data, while the

spectrum of functionalities, from fundamental features like end-users are unable to distinguish which party requests their

arXiv:2409.10411v2 [cs.CR] 18 Jun 2025 user authentication [1] and data encryption [2] to specialized privacy data. Incidents like the X-Mode controversy [12],

components like analytics [3], advertisement delivery [4], where user locations were tracked by over 100 apps through

and user interface enhancements [5]. The open-source nature embedded SDKs, underscore this point and serve as a stark

and global reach of the Android ecosystem further fuel the reminder of the challenges associated with preserving user’s

| proliferation of these SDKs. | privacy in third-party SDKs. |
| --- | --- |
| Integrating an SDK into an app is often as simple as | On the regulatory front, data protection regulations have |

declaring dependencies in the build configuration file, thus been put in place globally, such as the General Data Protection

drastically reducing development time, and allowing devel- Regulation (GDPR) [13] and the California Consumer Privacy

opers to focus on app-specific features. Nowadays, the ma- Act (CCPA) [14], which impose a stringent requirement on

jority of Android apps incorporate multiple third-party SDKs, data processors. In response to this, software developers are

required to provide a privacy policy to explicitly disclose what

M. H. Meng is with Technical University of Munich, Germany. C. Yan is

with the University of Queensland, Australia. G. Bai is with the University personal information is collected and how these data are han-

of Queensland, Australia, and National University of Singapore, Singapore. dled by their software. Dissecting whether the data handling

Q. Zhang and Z. Wang are with ByteDance Group, China, K. Wang is with behaviors of SDKs comply with the claims in their privacy

Huazhong University of Science and Technology, China, S. G. Teo is with

Agency for Science, Technology and Research, Singapore, and J. S. Dong is policies, which we define as behavior-policy compliance (or

with National University of Singapore, Singapore. privacy compliance), becomes an urgent task.

---

## Page 2

policies. Specifically, we conduct a static taint analysis for

in public spaces, and accordingly investigate whether these

traces can lead to potential privacy-sensitive data exfiltration.

For the privacy compliance assessment, we employ a large

language model (LLM) to analyze the SDKs’ privacy policies

and thereby identify what data is requested, cross-check the

data claimed in privacy policies with the data access behaviors

caught during the taint analysis, and determine if an excessive

collection or over-claiming issue exists.

Our study reveals critical privacy shortcomings in Android

third-party SDKs. Astonishingly, 346 traces are found to read

privacy data and share them in publicly accessible places.

Among these traces, 338 are confirmed to be subject to

data leakage. Only 109 out of the 158 examined SDKs

provide privacy policies, among which approximately 37%

over-collect private data and over 88% falsely claim their data

collection scopes, seriously violating global data protection

norms. Our re-inspection after 12 months shows no meaningful

improvement in these practices over time. We also uncover a

novel system settings injection issue: some malicious SDKs

exploit pre-installed apps to share privacy-sensitive data into

Android OS’s public system settings, effectively creating a

unique user-unresettable identifier (UUI) accessible to any

app. This unprecedented finding highlights an urgent need

for improvement in SDK development practices, permission

management, and privacy violation detection. To this end,

we further propose three key strategic recommendations as

mitigation.

Contributions . Our work makes the following key contribu-

tions:

2

The General Data Protection Regulation (GDPR) [13], a

landmark legislation enacted by the European Union (EU)

in 2018, has profoundly transformed the landscape of data

privacy laws within the region. Under GDPR, entities process-

ing personal data, defined broadly as any data enabling the

direct or indirect identification of individuals, are subjected

to stringent regulations that underscore the importance of

“ lawfulness, fairness, and transparency ”. Furthermore, GDPR

provides explicit requirements for obtaining valid consent,

necessitating that it is freely given, specific, informed, and

unambiguous.

Privacy compliance, in the context of GDPR, necessitates a

thorough examination of privacy policies to ensure adherence

to the GDPR’s comprehensive principles and stipulations. It

entails a meticulous inspection of data processing activities,

thereby ensuring data is acquired and utilized only for explicit,

legitimate purposes. Furthermore, the principle of “ data min-

imization ” obliges organizations to limit their data processing

activities to the minimum necessary, thereby reinforcing the

importance of data accuracy and relevance. This process also

extends to an examination of storage practices, necessitating

the validation that data is retained only for as long as necessary

and is safeguarded against unlawful processing, inadvertent

loss, or damage. Privacy compliance, therefore, functions as

a crucial mechanism to enforce accountability, reinforcing the

necessity for organizations to demonstrate, unequivocally, their

adherence to GDPR principles.

| Our Work | . In this work, we conduct a large-scale study on | • | Revelation of Privacy Compliance Landscape at the |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the privacy practices of existing third-party SDKs. Our study | SDK level. | Our study uncovers a startling level of data |  |  |  |  |  |  |
| covers 158 prevalently-installed SDKs from two mainstream | over-collection among third-party SDKs, with an estimated |  |  |  |  |  |  |  |
| release platforms, including Google Play SDK Index [15] and | 37% of SDKs engaging in this practice. Through our re- |  |  |  |  |  |  |  |
| CAICT SDK Index [16]. The former is the official source | inspection, we depict the trends of SDKs’ practices in |  |  |  |  |  |  |  |
| of Android SDKs as a part of Google Play infrastructure, | collecting and sharing privacy data, and underscore the |  |  |  |  |  |  |  |
| which lists the most widely used commercial SDKs in the | urgency of tackling privacy risks in the Android ecosystem |  |  |  |  |  |  |  |
| Android app ecosystem [17]. The latter is claimed to be the | at a fine-grained SDK level. |  |  |  |  |  |  |  |
| largest release platform of mobile SDKs in China, serving as a | • | Discovery | of | Privacy | Risk | caused | by | Pre-installed |
| complementary source of SDKs due to the absence of Google’s | Privileges. | We find a system settings injection issue in |  |  |  |  |  |  |
| service in the Chinese market. Based on the statistical data | the pre-installed apps, in which a malicious SDK can |  |  |  |  |  |  |  |
| provided by the two platforms, over 100 collected SDKs have | excessively read and share privacy data into the system |  |  |  |  |  |  |  |
| been embedded by at least 100 apps with over 10 million | settings. This enables an arbitrary pre-installed app with the |  |  |  |  |  |  |  |
| installations, demonstrating the broad impact of this study. | malicious SDK to create uniquely unresettable identifiers |  |  |  |  |  |  |  |
| Our study comprises two main strategies, i.e., conducting | and share them, violating the relevant regulations about |  |  |  |  |  |  |  |
| a data exfiltration assessment through static program analysis, | privacy protection. It is the first time such issues have been |  |  |  |  |  |  |  |
| and assessing privacy compliance through interpreting privacy | revealed and systematically investigated. |  |  |  |  |  |  |  |
| tracking the flow of privacy-sensitive data within the SDK. We | II. B | ACKGROUNDS AND | P | ROBLEM | D | EFINITIONS |  |  |

explore the traces that read and share privacy-sensitive data A. GDPR and Privacy Compliance

• Detecting Potential Privacy Data Exfiltration on a Large B. Android SDKs and Data Collection Practices

Scale. We collect 158 SDKs from two mainstream reposito- Android third-party SDKs represent a crucial component

ries and leverage taint analysis to track sensitive data flow, within the broader ecosystem of Android app development.

thereby exploring their potential data exfiltration. We find These software SDKs offer pre-written code to app developers,

338 data exfiltration evidenced by sharing obtained privacy enabling the efficient integration of different features and func-

data into public spaces. Our work highlights the substantial tions within their apps, ranging from user interface elements to

privacy risks stemming from the widespread use of third- complex data analytics capabilities. Data collection practices

party SDKs in the Android ecosystem, unveiling complex associated with Android third-party SDKs have been a subject

and often opaque data-handling practices. of scrutiny within academic and industry communities. It

---

## Page 3

increasing need of a large-scale privacy assessment of SDKs.

C. Objectives and Problem Definitions

This work aims to (1) detect potential exfiltration of users’

privacy data existing in the third-party SDKs, (2) explore

the privacy compliance of developers in the SDK release,

and thereby, (3) unveil the landscape of privacy protection

in the Android ecosystem at the SDK level. To this end,

we propose a compliance model to systematically assess

the privacy practices of Android SDKs regarding personal

information collection. We let D represent a set of diverse

data considered as user privacy, and let S be the set of publicly

released third-party SDKs. Then we define what privacy data

an SDK claims to collect and actually collects as follows.

Compliance Disclosure ( C ) . We let C denote the compliance

disclosure of an SDK s ∈ S . Specifically, it defines the set

of privacy data claimed to access in the privacy policy of the

to the public.

Implementation-level Practice ( P ) . The compliance practice

of an SDK concerns two types of operations in its implemen-

implementation, in which R s ⊆ D . We also let U s denote

consent. Moreover, some regulations like the GDPR have

which we formalize as the compliance not being true (i.e.,

strikethrough in a unary turnstile, ⊬ ) due to implementation-

level practice P . We detail this as follows:

∃ s ∈ S , ∃ d ∈ D , d ∈ U s ⇒ ⊬ P C s . (1)

3

∃ s ∈ S , ∃ d ∈ D , ( d ∈ R s ) ∧ ( d / ∈ C s ) ⇒ R s ⊬ P C s . (2)

We remark that Google has not set a formal definition of

“data collection” at the SDK level as what it does for third-

party apps [18]. Thus, we refer to the guideline of GDPR

Article 13 [13], [19] and take a conservative strategy by con-

sidering data accessed by SDKs as collected when evaluating

the excessive collection, given that the data accessed by an

SDK can flow into the host apps, which can then consume or

send the data out.

Type III: Over-claiming . We assert that an SDK has an

over-claiming issue if it is found to claim access to more

types of privacy data than it actually reads. Over-claiming

issues, although they may not substantially lead to privacy data

exfiltration, seriously violate the data minimization principle

stipulated in Article 5(1)(c) of GDPR. It is defined as follows.

D. Threat Model

gains capabilities as follows:

app.

storage.

III. M ETHODOLOGY

A. Approach Overview

has been observed that some SDKs, while providing utility Type II: Excessive Collection . Excessive collection concerns

functions, also engage in extensive data collection activities the privacy practice of an SDK that attempts to read more

without explicit acknowledgment or consent received from types of privacy data than what it requests/claims in its privacy

the end-users. Furthermore, there are instances where data policy. Excessive collection infringes on users’ right to be

is transmitted to remote servers, raising concerns about data informed as the SDK collects privacy data without users’

security and potential misuse. In light of this, there is an awareness and consent. We define this type of risk as follows.

SDK s . It shall also be assumed not to leak any privacy data ∃ s ∈ S , ∃ d ∈ D , ( d / ∈ R s ) ∧ ( d ∈ C s ) ⇒ R s ⊭ P C s . (3)

tation, i.e., collecting privacy data, and sharing the collected We consider that the exfiltration of users’ privacy data

privacy data. We let R s denote the scope of privacy data caused by malicious SDKs should follow a unified routine.

that would be read/collected by an SDK s based on its To achieve such exfiltration, the malicious SDK (the attacker)

| the collected privacy data involved in any uploading/sharing | • | The malicious SDK is released in a public platform/market |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| operations, given that | U | s | ⊆ R | s | . Thus, we have the compliance | and thus, can be embedded in an arbitrary app and installed |  |  |  |  |  |
| practice of an SDK | s | as a tuple of its collecting and sharing | on an Android device. Without causing an advantage to |  |  |  |  |  |  |  |  |
| behaviors, written as | P | s | = ( | R | s | , | U | s | ) | . | the attacker, that device is not rooted and is properly |
| Next, we formalize three types of compliance issues con- | maintained with the latest security update installed. |  |  |  |  |  |  |  |  |  |  |
| cerned in our investigation. | • | The malicious SDK accesses users’ privacy data through |  |  |  |  |  |  |  |  |  |
| Type I: Privacy Leakage | . Sharing users’ privacy in public | the interfaces of the Android OS with permissions granted |  |  |  |  |  |  |  |  |  |
| spaces poses compliance risks, especially when the collec- | to the embedding app, i.e., all its collection of users’ |  |  |  |  |  |  |  |  |  |  |
| tion or the sharing operations are not performed with users’ | privacy data must be realized on behalf of the embedded |  |  |  |  |  |  |  |  |  |  |
| explicitly prohibited any collection of UUIs, amplifying the | • | The malicious SDK saves or shares the collected privacy |  |  |  |  |  |  |  |  |  |
| risks of privacy sharing on the SDK side. Here we define that | data in a public space, i.e., there exists no party (including |  |  |  |  |  |  |  |  |  |  |
| any pre-recognized privacy data | d | being observed in sharing | the embedding app) colluding with the malicious SDK in |  |  |  |  |  |  |  |  |
| operations of an SDK | s | would constitute privacy sharing risk, | sharing the collected privacy data, or saving it in private |  |  |  |  |  |  |  |  |
| Besides improper sharing, recent developments in privacy | We propose a four-phase approach and briefly illustrate it in |  |  |  |  |  |  |  |  |  |  |

protection regulations also pose stricter requirements in even Figure 1. In Phase 1 , we collect 158 Android SDKs, including

reading privacy data on personal devices. Developers are their binary files, privacy policies, and metadata from two

required to not only declare a list of privacy data to be release platforms. After that, Phase 2 involves analyzing the

collected but also to ensure the actual collection operations privacy policies using state-of-the-art LLMs to identify the

are always consistent with what has been declared. Next, we types of privacy data requested by the SDKs. In Phase 3 , we

formalize two types of inconsistency issues that could happen perform static taint analysis on the SDKs to examine their data

in privacy data collection. collection behaviors at the implementation level, aiming to

---

## Page 4

41 types of privacy

data in 5 categories

| Meta-information | Privacy Policy |
| --- | --- |
| & Privacy Policies | Analysis |

Phase 2. Identifying Data Requested

• 2 release platforms.

Platforms

• 741 source methods.

AAR

JAR • 46 sink methods.

SDK Libraries Static Taint Analysis

Phase 3. Exploring Privacy

Phase 1. Collecting Third-Party SDKs Collection & Exfiltration

security change section of each Android OS release report,

the research community. As a result, we recognize 41 types of

privacy data and categorize them into five groups. These 41

may tend to only declare the data to be collected roughly by

4

| • | 216 | requests | Compliance |
| --- | --- | --- | --- |
| L L M | identified | . | Assessment |

• 87.4% overall

precision.

• Excessive collection in 36.7%

SDKs (type II issues).

• 346 tainted traces found. permission (type III issue).

• 338 potential leakage

detected (type I issues). Insights &

Recommendations

Phase 4. Compliance Assessment

| (C1) Chip, Cellular & Peripheral | Wifi | 38 |  |
| --- | --- | --- | --- |
| External storage | 18 | Camera | 54 |
| IMEI | 5 | Misc. sensors | 140 |
| IMSI | 3 | Subtotal | (281) |
| Network info | 6 | Android ID | 2 |
| SIM info | 7 | Media location | 1 |
| Subtotal | (148) | Subtotal | (45) |
| (C2) Wireless Communication | (C5) Personal Data |  |  |
| Bluetooth ID | 2 | Calendar | 2 |
| SSID/BSSID | 17 | Subtotal | (22) |

data into one category.

SDK Release • 158 SDKs collected. • 88.1% SDKs are over-claiming

Fig. 1: The workflow of potential data exfiltration exploration and compliance assessment at the SDK level

identify traces that constitute a complete privacy data reading TABLE I: List of 41 pre-identified privacy data types and the

and sharing process. SDKs caught to read and share user distribution of the 741 source methods

| privacy would be prone to privacy leakage (i.e., type I issues). | Data type & class | Count Data type & class | Count |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Finally, in | Phase 4 | , we assess privacy compliance by cross- | Call phone | 41 | Wifi MACs | 5 |
| checking the data requested in the privacy policies with the | Carrier info | 5 | Subtotal | (245) |  |  |
| actual data collection behaviors, aiming to detect excessive | Cellbroadcast | 2 | (C3) Location & Sensors |  |  |  |
| collection (Type II) and over-claiming (Type III) issues. | ICCID | 15 | Location | † | 87 |  |
| B. Scope of Privacy Data | MEID | 2 | (C4) Media & Software Specific |  |  |  |
| Considering most privacy data stipulates an explicit per- | Phone status | 1 | App list | 7 |  |  |
| mission for apps to access, we mainly resort to the list of | SD card serial | 4 | Audio record | 22 |  |  |
| permissions [20] from Android developer documentation to | Serial | 4 | Google Ad ID | 3 |  |  |
| define the list of privacy data. The list is further complemented | SMS | 23 | OAID | 9 |  |  |
| with privacy-sensitive items recognized from the | privacy or | Telephone number | 12 | Screen record | 1 |  |
| for example, the clipboard and a group of user-unresettable | Bluetooth | 117 | Account info | 6 |  |  |
| identifiers (UUIs) are recognized in the release document of | Bluetooth call | 6 | Browser bookmarks | 1 |  |  |
| Android 10 [21] and added to the scope of this study. In | Bluetooth MAC | 36 | Clipboard data | 2 |  |  |
| addition, we also take existing literature in personal infor- | IP address | 2 | Contact list | 9 |  |  |
| mation collection [22]–[27] and app analysis [28]–[31] into | SIP service (VOIP) | 21 | Contact log | 2 |  |  |
| consideration to complement the list of privacy data. We thus | Ultra-wideband | 1 | Total | 741 |  |  |

include the usage of diverse sensors (e.g., motion and light † Includes coarse location that is determined by network, and fine location

sensors) into the list because they have been widely studied in that is jointly determined by network and GPS.

| data types constitute | D | defined in Section II-C and formulate | changes in Android privacy mechanism are mainly reflected |
| --- | --- | --- | --- |
| the scope of our compliance assessment. The list of recognized | in permission rules of calling sensitive APIs, grouping per- |  |  |
| privacy data is shown in Table I. | sonal data that involve APIs mentioned in the same privacy |  |  |
| Categorization | . We then categorize the identified 41 types of | change can facilitate our discussion and gain insights if |  |
| privacy data by three criteria: | any non-compliance is observed. A typical example is that |  |  |
| • | We primarily group those privacy data that share a similar | the invocation permission of most APIs to read device |  |
| functionality or purpose. This is to ease our privacy policy | identifiers including serial, IMEI, and ICCID, are escalated |  |  |
| based compliance assessment, because many developers | in Android 10. We accordingly group these aforementioned |  |  |
| functionality (e.g., device identifiers, location, etc.) rather | Based on the criterion listed above, we further categorize |  |  |
| than accessing specific data or certain APIs. | them into five classes, namely | chip, cellular & peripheral |  |

• We then refine our categorization by grouping those data ( C1 ), wireless communication ( C2 ), camera, location, and

that can be programmatically accessed through APIs in the other sensors , ( C3 ), media and software specific ( C4 ), and

same or similar classes based on the Android developer’s miscellaneous personal data ( C5 ).

documentation. This is to facilitate our next step’s taint Ontology for Semantic Relationships . Considering the re-

analysis as we need to collect as many involved APIs as quest of personal data in privacy policies may not always

possible to be the source methods, which we will detail in written in a precise manner as defined in the developer’s

Section III-E. documentation, and sometimes certain privacy data items have

• We also consider the API permissions of collecting those multiple names or colloquial phrases, we refer to relevant

privacy data into our categorization. Due to the historic research [32], [33] and propose an ontology to capture the

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

5

semantic relationship among the 41 types of privacy data, and source. As a result, we download the latest version of 158

consequently to guide our assessment. distinct SDKs as of October 2022, among which 139 are

First, we manually collect alternative names or colloquial from the Google Play SDK Index and 19 are released on the

phrases for each type of identified privacy data and treat them CAICT website. These 158 constitute our previously defined

as synonyms ( ≡ ). For example, we find that the advertising S (Section II-C) for the later assessment. We also revisit the

ID and GAID are interchangeably used in privacy policy latest versions of the same group of SDKs in October 2023

documents to refer to the Google Ad ID. Thus, all the and conduct an additional assessment, which we will detail in

synonymous terms of a privacy data type will be considered Section IV-D.

in our assessment. We remark that, at the time of this study, both the Google

Besides that, we define a hypernymy relationship ( ⊏ ) be- Play SDK Index and CAICT have not enforced strict regula-

tween privacy data types in generic and specific terms. For tion or code auditing mechanisms like the Google Play App

example, we learn that both the user name and email are com- Store. As a result, there is no guarantee that the SDKs from

positions of the account information of an Android device, and these sources include comprehensive documentation or privacy

accordingly treat both user name and email hyponyms of the policies required by regulations such as GDPR.

term account information (denoted as name ⊏ account_info Crawling Meta Information and Privacy Policies . Next,

and email ⊏ account_info ). In case an SDK developer claims we implement a crawler with Selenium [34] to retrieve meta

to request the email address of the device owner, we assume information and privacy policy links from the two sources.

the API for reading account information will be invoked, and The meta information includes the SDK name, provider (de-

therefore, both the email and name of the user will be accessed. veloper’s identity), Maven IDs, and functional categories. Such

We also learned that some SDK developers use the rough information will be jointly used to uniquely identify SDKs

term “device identifiers” in disclaiming privacy data to collect. during our subsequent analysis. We then collect the privacy

Unlike the definition of “ DeviceID ” in Android documen- policies from the retrieved links. We will use them to extract

tation, device identifiers are often referred to as a broad the list of personal data that the SDK requests.

sense of hardware identifiers in privacy policies, such as the The retrieval of privacy policies is found more complex than

serial number of the smartphone. Thus, we consider device collecting meta information due to the lack of a compulsory

identifiers as a hypernym of diverse hardware identifiers (e.g., standard for drafting them. For SDKs from the Google Play

serial ⊏ device_identifiers ). We hold a conservative SDK Index, we rely on the links provided in the “data safety

stance in this study and, thus, assume the involved SDKs section” section if available, and download the corresponding

claim to request all types of privacy data that fall into the webpages. Similarly, for SDKs from the CAICT website, we

scope of device identifiers, including IMEI, MEID, ICCID, download the webpages from the “SDK privacy policy” link

and serial. We also remark that although a user’s location on the SDK details page. We use Google Translate to process

can also be inferred through his/her devices’ IP addresses, all non-English text on these webpages.

we assume the term “location” and its synonyms indicate Due to the limited availability of privacy policies, we only

the data is derived from SDK’s access to location services collected policies for 52 SDKs directly from the two platforms.

of Android OS (e.g., LocationManager ). The main reason For those do not provide privacy policy URLs, we manually

is that we believe the SDK developers are supposed to use searched the Internet using keywords like “disclaimer”, “pol-

precise and unambiguous language in writing their privacy icy”, “disclosure”, and “guidance” to look for any available

policies. Besides that, inferring users’ location through differ- privacy policies drafted by the SDKs’ developers. As a result,

ent OS components involves different privacy mechanisms and we identify privacy policy webpages for another 57 SDKs. In

requests for different permissions. Thus, an SDK’s claiming total, we obtained valid privacy policies for 109 SDKs (69.0%

to access users’ locations through any manners other than of all SDKs). The text from these webpages will be extracted

location services without an explicit explanation would be for further analysis.

treated as non-compliance in this study.

D. Phase 2: Identifying Data Requested in Privacy Policies

After collecting the 109 privacy policies, our next step aims

C. Phase 1: Collecting Android SDKs

to identify the data requested by each SDK from them. In

Our study starts by collecting as many Android SDKs contrast to traditional app privacy policies that are written in

as possible from mainstream sources. Since our approach the user-oriented language, SDK privacy policies are more

involves cross-checking SDK privacy disclosures with actual developer-oriented and may contain many domain-specific

data collection behaviors at the implementation level, we terminology (e.g., ICCID, BSSID) and technical synonyms

gather not only SDK binaries (typically in AAR and JAR (e.g., Google Ad ID, which also appears as Advertising ID,

formats) but also the privacy policies and relevant metadata or GAID). This uniqueness makes it challenging for existing

provided by the developers, when available. methods [32], [33], [35]–[38] to extract domain-specific en-

Sourcing SDKs from Multiple Repositories . We identify the tities accurately. To tackle these challenges, we leverage an

Google Play SDK Index as the primary source for collecting LLM-based Natural Language Inference (NLI) model to infer

Android SDKs. Additionally, considering the uniqueness of the data collection practice from the privacy policies.

mainland China’s Android ecosystem where Google Play Adoption of NLI Model . NLI has proven effective in un-

infrastructure is absent, we use CAICT as a supplementary derstanding natural language across different domains [39]. In

---

## Page 6

| (GMA) SDK | Premises | Hypotheses |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Google Play's data disclosure | • | IH | It does not mention whether to (Verbal |  |  |  |  |  |
| In May 2021, Google Play announced the | new Data safety section, which is a | Inference by a RoBERTa-based | • | NH | It does not (Verbal Phrase) (Object) . |  |  |  |
| data collection, sharing, and security | practices. | access | read | collect | share | request | upload |  |
| requirements for this data disclosure in | Carrier Info | IMEI | MEID | IMSI | ICCID | Serial | Set of | Objects |
| regards to your usage of the Google | Network Info | SIM Card Info | Telephone No |  |  |  |  |  |
| information on whether and how our SDK | … |  |  |  |  |  |  |  |
| handles end-user data, including any | Serial | Network Info | SIM Card Info | Telephone No. |  |  |  |  |
| applicable settings or configurations you | Inference Outcomes | Carrier Info | Bluetooth | Bluetooth MAC | IP Address |  |  |  |
| developer, you are solely responsible … | List of privacy data an |  |  |  |  |  |  |  |

SDK claims to collect

Validation

Ad ID) to ensure hypothesis completeness. Besides that, we

also tailored hypotheses by matching different verb phases

1 The full name of the model is roberta-large-snli_mnli_fever_anli

6

behavior is “performed” by the SDK itself.

Finding the Optimal Threshold . Intuitively, to infer a specific

always higher than the prediction of the neutral and con-

tradiction hypotheses. However, our preliminary experiments

and AOSP source code to collect as many APIs that are

collect 741 source methods. 2 The distribution of 741 methods

| Google Mobile Ads | • | PH | It will (Verbal Phrase) (Object) . | where Score | p | indicates the entailment confidence score |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| requirements | Phrase) (Object) . | for the | positive hypothesis | . An entailment inference requires |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| developer-provided disclosure for an app's | Large Language Model | Set of | Verbal Phrases | Score | p | to be greater than a threshold value, written as | T | . |  |  |  |  |  |  |  |  |  |  |
| This page can help you complete the | … | Simultaneously, Score | p | must be greater than the scores for |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Mobile Ads SDK. On this page, you can find | Carrier Info | Bluetooth | Bluetooth MAC | Location | Carrier Info | IMEI | MEID | IMSI | ICCID | SMS | negative | and | irrelevant hypotheses | (i.e., Score | n | and Score | i | ), |
| can control as the app developer. | … | indicating | that | the | premise | does | not | only | “mention” | the |  |  |  |  |  |  |  |  |
| We aim to be as transparent as possible in | supporting you; however, as the app | collection of that data type but also confirm that collection |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Fig. 2: The workflow of our privacy policy analysis to find type of data being collected, the entailment prediction score

out what an SDK claims to collect (Score p ) is supposed to be greater than 0.5 to ensure it is

this work, we use the state-of-the-art LLM-based NLI model observe a large number of false positives by setting the

named roberta-NLI 1 to identify requested data in privacy threshold to 0.5. For that reason, we perform a small-scale

policies. By parsing sentences from these policies as premises , analysis to tune the threshold value from 0.5 and above

we input them into the model alongside hypotheses based on until we find an optimal value that minimizes the number of

41 pre-identified data types (refer to Section III-B), allowing false positive predictions. Specifically, we assume that Google

the model to assess the entailment relationship between them. should provide high-quality privacy policies for their own

We briefly illustrate our approach in Figure 2. SDKs, and therefore we collected five distinct privacy policy

There are two key challenges arose during the hypothesis shared by 13 Google in-house SDKs. We manually analyzed

formulation. The first challenge is the missing of a canonical declared privacy data types from the five privacy policies to

writing standard of SDK privacy policies. Privacy policies of- set a ground truth. We then fine-tuned the threshold value and

ten use developer-oriented language with technical synonyms, discovered that the NLI model could achieve perfect prediction

requiring us to manually gather synonyms (e.g., the advertising with a threshold of 0.73. For that reason, we adopt 0.73 as the

ID and GAID are interchangeably used to refer to the Google optimal threshold in our large-scale privacy policy analysis.

(e.g., “collect”, “read”) to each data type and its synonyms E. Phase 3: Exploring Privacy Collection and Leakages

| to maximize the entailment score when the collection of the | We leverage the static taint analysis techniques to explore |
| --- | --- |
| inferred data type is mentioned in the privacy policy. | privacy collection behaviors and potential exfiltration in SDKs. |

The second challenge is handling the complex context of We define a valid privacy data exfiltration is constituted of a

SDK privacy policies, as the NLI model is not domain- collection action that queries one or more privacy data from

specifically trained. For example, we found common sentence the OS, and a sharing action that shares the obtained privacy

formats in privacy policies, such as “According to GDPR, all data, directly or indirectly, to the public spaces including

collection of device identifiers must be declared in advance.” the Internet, system settings, and the public storage. Thus,

Conventional inference models might incorrectly conclude we consider that an SDK engages in privacy collection if

with high confidence that this implies the collection of device its implementation contains a data flow originating from a

identifiers , but it is irrelevant to the actual behaviors of the privacy data collection action. This privacy collection leads to

SDK being analyzed. To address this issue, we created three exfiltration if the data flow ends at a sensitive sharing action.

tailored hypotheses for each combination of verbal phrase Configuring Taint Analysis . We aim to collect all relevant

and object, namely the positive hypothesis (shown as PH in APIs that contribute to a collection action and include them

Figure 2, e.g., “It will collect ...”), negative hypothesis ( NH , into the source methods for taint analysis. To this end, We refer

e.g., “It does not collect ...”), and irrelevant hypothesis ( IR , to an existing research [40] which proposes a technique named

e.g., “It does not mention whether to collect ...”). As a result, SuSi , which classifies over 900 API methods that can poten-

we have composed a list of 507 hypotheses covering the 41 tially leak users’ privacy in Android 4.3 and earlier versions.

pre-identified data types. Considering there have been multiple version’s evolutions

Inference of Data Requested . Given three hypotheses have since Android 4.3 that the API rules may have experienced

been defined for each combination of verbal phrase and significant change, we first map the APIs identified in [40]

object, we only consider a data type claimed to be collected with the 41 types of privacy data. We iterate the developers’

by an SDK if there exists at least one combination of the documents of those APIs and filter out those APIs that are no

associated object (e.g., location) and applicable verbal phrase longer valid in Android Open Source Project (AOSP) imple-

| (e.g., request) satisfying the logical condition as follows: | mentation. We then manually visit the developer’s document |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ( | Score | p | > T | ) | ∧ | ( | Score | p | > | Score | n | ) | ∧ | ( | Score | p | > | Score | i | ) | associated with the new data types as possible. As a result, we |
| _R1_R2_R3-nli | . We shortly write as | roberta-NLI | to save space. | 2 | We count the number of methods by unique method signatures in this paper. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

*[Image: Page 6 Image]*

---

## Page 7

| Network Transfer | java.net.HttpURLConnection | 1 |
| --- | --- | --- |
| org.android.spdy.SpdySession | 3 |  |
| org.apache.http.client.methods.HttpPost | 8 |  |
| File Saving | java.io.Writer | 5 |
| java.io.FileOutputStream | 1 |  |
| Total | 46 |  |

corresponding to the 41 types of privacy data can be found in

Table I.

Next, we retrieve all methods that perform a sharing action

from Android SDKs. Although there are not many new APIs

introduced after Android 4.2 that can be treated as sink meth-

ods, we find most sink methods studied in earlier literature

including SuSi [40], such as logging and SQLite databases,

are no longer valid in the latest Android versions and therefore

be excluded in this study [41], [42]. In the end, we identify

as an undocumented channel to share data among different

Our evaluation aims to assess the performance of our

proposed NLI model-based privacy policy analysis and explore

the privacy data collection and potential leakages in the SDKs.

After that, we analyze the privacy preservation landscape at the

SDK level by cross-checking the data requested in the privacy

policies and the data collected in SDKs’ implementation (refer

to Phase 4 of Figure 1).

package named Transformers . 3

on our experimental PC, feed four best-selling non-game apps

from the Google Play App Store, namely Facebook, Instagram,

Snapchat, and TikTok, into these tools, and explore data flows

simultaneously containing a privacy collection action and a

7

the automatic taint analysis program.

ing three research questions (RQs):

vacy data claimed to be collected by SDKs on a large

scale? What is the performance of our NLI model-based

approach?

• RQ2 . Can our taint analysis find privacy data collection

and sharing behaviors from the SDKs? How many tainted

traces are detected? Can those tainted traces (really) leak

users’ privacy?

• RQ3 . By cross-checking their privacy policies, what is the

status quo of privacy data protection at the SDK level? Do

the collected SDKs comply with their privacy policies?

number 1.9.

these requests as the ground truth in evaluating our analysis

effectively analyze privacy policies on a large scale, achieving

a promising precision of 87.4% and an F1 score of 89.5%.

(see Table III).

We find our NLI model-based analysis achieves perfect pre-

cision in detecting data collection for 10 data types despite 27

false positive cases being observed, i.e., wrongly recognized

by the NLI model. Our evaluation outcomes show that account

information (6), network information (5), and SMS (4) are

These errors likely stem from the model’s misinterpretation of

B. RQ2: Privacy Collection and Potential Leakages at the

SDK Level

Our static taint analysis identified 2318 instances of privacy

| TABLE II: | A brief statistics of recognized sink methods | sharing action. Our observation shows that AppShark performs |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Purpose | Class name | Count | the best in terms of time efficiency, success rate of analysis, |  |  |
| java.net.URL | 2 | and capability of handling inter-process communication (IPC). |  |  |  |
| java.net.URLConnection | 2 | For those reasons, we adopt AppShark for the taint analysis |  |  |  |
| org.android.spdy.SpdyRequest | 12 | of SDKs on a large scale. For each SDK, we implement a |  |  |  |
| org.apache.http.client.methods.HttpGet | 8 | blank Android app to embed it and pass the app package to |  |  |  |
| org.apache.http.params.HttpParams | 1 | Evaluation Goals | . Our evaluation aims to answer the follow- |  |  |
| System Settings | android.provider.Settings | 3 | • | RQ1 | . Can our privacy policy analysis identify the pri- |

46 methods from 11 classes and then configure them as sink A. RQ1: Privacy Policy Analysis Performance

methods . We present a brief statistics of the sink methods by We perform NLI model-based analysis on the 109 SDK

their containing classes in Table II. privacy policies and present the analysis outcomes in Table III.

The majority of sink methods are relevant to data transfer Our analysis identifies 214 data requests from privacy policies.

via network interfaces, reserving 37 out of 46 identified Among the 214 data requests, IP address reserves the largest

method signatures. Besides that, six method are recognized share, contributing to 47 (21.9%) occurrences. network infor-

because they can share sensitive data via public storage. The mation and location are the remaining data types among the

remaining three sink methods are counted because they can top three. From the perspective of SDKs, the number of data

be used for modifying the system settings, which is known types claimed by an SDK ranges from 0 to 6, with the average

parties on the device [43]. We note that writing contents into We then conduct a manual inspection of our findings in

the system settings requires privileged permission and we will the 109 privacy policies. As a result, we find 187 verified

discuss it in Section V. data requests covering 19 data types, and accordingly treat

IV. E VALUATION approach. The results demonstrate that our approach can

Implementation . We implement our privacy policy analysis in the top three data types involved in false positives, indicating

Python with PyTorch. The NLI model is provided by a Python the model struggled to infer data collection for certain types.

Adoption of Automatic Taint Analysis . We learned that there terms and data type scopes. For example, although our NLI

are some off-the-shelf automatic static taint analysis tools model correctly recognizes SMS, it fails to differentiate SMS

for Android apps. Our preliminary investigation considers and other messaging methods like emails, leading to high-

three open-sourced tools, namely FlowDroid [44], Mariana confidence false positives while dealing with sentences like

Trench [45], and AppShark [46]. We set up these three tools “we may send email to the users...” as SMS collection.

3 Available at https://huggingface . co/docs/transformers/index data access across 27 of the 41 pre-identified data types. Out

---

## Page 8

#SDKs

detected

TABLE IV: A brief statistics of the taint analysis results (only

| C1 | Carrier info | 106 | 0 | 106 | C2 | WiFi MAC | 62 | 64 | 126 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IMEI | 92 | 26 | 118 | Subtotal | (356) | (172) | (528) |  |  |
| ICCID | 20 | 4 | 24 | Misc sensors | 383 | 0 | 383 |  |  |
| Network info | 2 | 0 | 2 | Subtotal | (872) | (130) | (1002) |  |  |
| SIM card info | 14 | 0 | 14 | App list | 128 | 0 | 128 |  |  |
| SMS | 6 | 0 | 6 | Audio record | 11 | 0 | 11 |  |  |
| Subtotal | (370) | (44) | (414) | OAID | 68 | 0 | 68 |  |  |
| C2 | Bluetooth | 20 | 0 | 20 | Subtotal | (310) | (0) | (310) |  |
| Bluetooth MAC | 10 | 0 | 10 | C5 | Account info | 2 | 0 | 2 |  |
| IP Address | 23 | 1 | 24 | Contact list | 5 | 0 | 5 |  |  |
| Total | 1972 | 346 | 2318 |  |  |  |  |  |  |

of 158 SDKs, 95 (60.1%) were found to read privacy data,

with 34 (21.5%) having at least one tainted trace. The analysis

revealed that 346 (14.9%) of these accesses were tainted,

suggesting potential privacy leakage into public spaces. We

present the taint analysis outcomes by data types in Table IV.

Distribution of Data Collected & Shared . As shown in

Table IV, location and sensors’ data (category C3) reserves

the greatest portion of collection actions, contributing 1002

out of 2318 (43.2%) caught collection actions. The remaining

privacy data categories ordered by their number of caught

collection actions are data for wireless communication (C2,

22.8%), data for chip, cellular and peripheral (C1, 17.9%),

media and software-specific data (C4, 13.4%), and personal

data (C5, 2.8%), respectively.

From the privacy data sharing perspective, the access of

wireless communication data (C2) constitutes the largest part

of the tainted flow, as 172 out of 346 (49.7%) traces are tainted.

The numbers of sharing actions involving data in categories

C3 and C1 are following up, reserving 37.6% and 12.7% of

all sharing actions, respectively. No sharing actions about data

in categories C4 and C5 are observed. From the identifiability

perspective, we find that most privacy data involved in sharing

actions are referred to as personally identifiable information

(PII) in relevant literature [25], [26], [47], [48].

8

#SDKs

detected

1 public static String a(Context context) {

5 ...

6 try {

();

8 }

10 }

Potential Privacy Data Leakage (Type I Issues) . During

our analysis, we noticed that static taint analysis cannot well

determine the execution paths in conditional and branched

code. If any tainted trace is found spanning over an unreach-

able, dead, or logically infeasible code, we exclude the tainted

trace from the statistics of potential leakages. In Figure 3, we

provide an example code reverse-engineered from one of our

examined SDKs named “ mipush ”. We find it attempts to read

the SSID of the connected WiFi but is later assessed by us

as a false alarm. The SSID reading action (can be realized by

the method getExtraInfo (line 7) until Android 10) would

only take place if the device is not connecting to WiFi (after

line 4), therefore we determine this is a logically infeasible

code regarding privacy data access. In this study, we manually

exclude the false alarms from the 346 traces and accordingly

identify 338 (97.7%) logically valid traces, among which each

trace indicates an occurrence of privacy leakage issue.

For the sharing operations, we observe that 332 out of 338

(98.2%) valid traces are tainted at network interfaces. The six

remaining traces are tainted at system setting APIs. Compared

with sharing privacy data through the Internet, we remark that

writing privacy data in system settings is a more worrying

issue because it exploits the privilege of pre-installed apps

and is capable of sharing user privacy even without reading

any privacy data from the Android OS. We will detail this in

Section V.

TABLE III: Evaluation outcomes of privacy policy analysis (only data types requested are displayed)

Data type & class to collect TP FP FN Precision Recall F1-score Data type & class to collect TP FP FN Precision Recall F1-score

| C1 | Carrier info | 12 | 10 | 2 | 3 | 83.3% | 76.9% | 80.0% | C3 | Location | 28 | 25 | 3 | 4 | 89.3% | 86.2% | 87.7% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Device identifiers* | 21 | 21 | 0 | 3 | 100.0% | 87.5% | 93.3% | Misc sensors | 1 | 1 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| Network info | 30 | 25 | 5 | 0 | 83.3% | 100.0% | 90.9% | Android ID | 8 | 8 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| SIM card info | 7 | 7 | 0 | 0 | 100.0% | 100.0% | 100.0% | App list | 4 | 4 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| SMS | 7 | 3 | 4 | 0 | 42.9% | 100.0% | 60.0% | Audio record | 10 | 10 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| Telephone No | 5 | 3 | 2 | 2 | 60.0% | 60.0% | 60.0% | Google Ad ID | 6 | 6 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| C2 | BSSID/SSID | 4 | 4 | 0 | 0 | 100.0% | 100.0% | 100.0% | OAID | 2 | 2 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |
| IP address | 47 | 45 | 2 | 1 | 95.7% | 97.8% | 96.8% | C4 | Account info | 10 | 4 | 6 | 4 | 40.0% | 50.0% | 44.4% |  |
| WiFi | 4 | 3 | 1 | 0 | 75.0% | 100.0% | 85.7% | Clipboard | 1 | 1 | 0 | 0 | 100.0% | 100.0% | 100.0% |  |  |
| C3 | Camera | 7 | 5 | 2 | 0 | 71.4% | 100.0% | 83.3% | Total | 214 | 187 | 27 | 17 | 87.4% | 91.7% | 89.5% |  |

* We use a broad sense of device identifiers to represent all hardware UUIs, including IMEI, MEID, IMSI, ICCID, and serial.

| data types called and/or tainted are displayed) | 2 | ConnectivityManager cm = (ConnectivityManager) context. |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Caught access traces | Sum is 109 | Caught access traces | getSystemService(Context.CONNECTIVITY_SERVICE); |  |  |  |  |  |  |  |  |  |  |
| Data type | Not | Tainted | Data type | Recall = TP/(TP+FN) | Not | Tainted | 3 | NetworkInfo info = cm.getActiveNetworkInfo(); |  |  |  |  |  |
| & class | tainted | (Type I) | Total | & class | F1 = 2 Pr*Re / (Pr+Re) | tainted | (Type I) | Total | 4 | if | (info.isConnected()) { | return | "wifi"; } |
| MEID | 0 | 4 | 4 | C3 | Camera | 3 | 0 | 3 | 7 | return | info == | null | ? "" : info.getTypeName()+"-"+info. |
| IMSI | 15 | 5 | 20 | Location | 486 | 130 | 616 | getSubtypeName()+"-"+info.getExtraInfo().toLowerCase |  |  |  |  |  |
| Serial | 82 | 5 | 87 | C4 | Android ID | 83 | 0 | 83 | 9 | catch | (Exception e) { | return | ""; } |
| Telephone no | 33 | 0 | 33 | Google Ad ID | 20 | 0 | 20 | Fig. 3: A false positive example of SSID reading (line 7) |  |  |  |  |  |
| BSSID/SSID | 220 | 107 | 327 | Clipboard data | 57 | 0 | 57 | to exclude false positive tainted traces. We will elaborate more |  |  |  |  |  |
| WiFi | 21 | 0 | 21 | Subtotal | (64) | (0) | (64) | on them in the remainder of this section. |  |  |  |  |  |

We remark that whether SDKs can collect privacy data C. RQ3: SDK-Level Privacy Compliance

eventually depends on the permission and privilege of their We resort to cross-checking the privacy policies with the

embedding apps, and tainted traces do not automatically imply actual data collection behaviors of the collected SDKs to

the exfiltration in runtime. A manual validation is performed understand the status quo of privacy compliance at the SDK

---

## Page 9

| and class | (EC) | (OC) | and class | (EC) | (OC) | and class | (EC) | (OC) |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICCID | 4 | 16 | WiFi | 3 | 0 | OAID | 0 | 3 |  |  |  |
| Telephone no | Telephone no | 1 | 3 | Misc. sensors | Misc. sensors | 7 | 0 | Contact list | Contact list | 1 | 10 |
| Total | 108 | 200 |  |  |  |  |  |  |  |  |  |

of 158 (69.0%) SDKs that provide privacy policies, and the 27

Excessive Collection (Type II Issues) . Our evaluation finds

that 40 out of 109 (36.7%) SDKs collected excessive privacy

from 1 to 9. Each SDK has an average of three undeclared

data types. As shown in Table V, 22 out of the 41 pre-

identified data types (81.5%) have been excessively collected

SDKs. By jointly considering data collection behaviors (refer

of the 11 caught SDKs have declared to read the clipboard

privacy policies over-claim their access to IP addresses. Such

9

| SMS | +4 (new) | Audio record | +5 (new) |  |
| --- | --- | --- | --- | --- |
| Telephone no | +2 (new) | Google Ad ID | +9 (new) |  |
| Subtotal | +20 (45%) | OAID | +3 (new) |  |
| C2 | Bluetooth | +5 (new) | Screen record | +1 (new) |
| BSSID/SSID | -73 (68%) | C5 | Clipboard data | +17 (new) |
| IP Address | +9 (900%) | Contact list | +1 (new) |  |

†

time.

D. Privacy Compliance Re-inspection

results.

spaces.

of sharing such data.

| TABLE V: | Assessment of privacy compliance by data types | TABLE VI: | Changes in the tainted traces after 12 months |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data type | Type II | Type III | Data type | Type II | Type III | Data type | Type II | Type III | (only tainted data types are displayed) |  |  |  |  |  |  |  |  |
| C1 | Carrier info | Carrier info | 10 | 7 | C2 | Bluetooth | 4 | 0 | C4 | Android ID | Android ID | 10 | 0 | Data type & | Changes in | Data type & | Changes in |
| IMEI | 1 | 6 | Bluetooth MAC | Bluetooth MAC | 2 | 0 | App list | 22 | 1 | class | tainted traces | class | tainted traces |  |  |  |  |
| MEID | 0 | 21 | BSSID/SSID | BSSID/SSID | 8 | 2 | Audio record | Audio record | 0 | 9 | C1 | Carrier info | +31 (new) | † | C2 | Subtotal | -106 (-61%) |
| IMSI | 1 | 18 | IP Address | 2 | 44 | Google Ad ID | Google Ad ID | 2 | 3 | IMEI | -17 (65%) | C3 | Camera | +2 (new) |  |  |  |
| Network info | Network info | 0 | 24 | WiFi MAC | WiFi MAC | 2 | 2 | Screen record | Screen record | 0 | 1 | MEID | -2 (50%) | Location | -94 (72%) |  |  |
| Serial | 1 | 6 | Subtotal | (21) | (48) | Subtotal | (34) | (17) | IMSI | -2 (40%) | Misc sensors | +20 (new) |  |  |  |  |  |
| SIM card info | SIM card info | 1 | 0 | C3 | Camera | 0 | 4 | C5 | Account info | Account info | 1 | 4 | ICCID | +0 (0%) | Subtotal | -72 (55%) |  |
| SMS | 3 | 2 | Location | 11 | 14 | Clipboard data | Clipboard data | 11 | 0 | Serial | +3 (60%) | C4 | Android ID | +34 (new) |  |  |  |
| Subtotal | (22) | (103) | Subtotal | (18) | (18) | Subtotal | (13) | (14) | SIM card info | +1 (new) | App list | +53 (new) |  |  |  |  |  |
| level. We remark our assessment only focuses on the 109 out | Bluetooth MAC | +3 (new) | Subtotal | +105 (new) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| data types that appear in the data collection behaviors observed | WiFi | +9 (new) | Subtotal | +18 (new) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from the taint analysis. We present our assessment results in | WiFi MAC | -59 (92%) | Total | -35 (10%) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Table V. | We use “new” to indicate data types observed re-inspection for the first |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

data compared with their privacy policies (e.g., an SDK our taint analysis shows that most SDKs only use location

collects personal identifiers but does not declare them in its APIs, leading to over-claiming cases of IP addresses. This

privacy policy). Among the 40 SDKs that excessively collect lack of clarity can confuse users about what data is actually

users’ privacy, the number of undeclared data types ranges collected, reducing transparency in privacy policies.

by the examined SDKs. The app list, clipboard data, and On the basis of our large-scale analysis performed on 158

location are the top three most excessively collected data types. SDKs collected in October 2022, we re-visited the two sources

Specifically, 22 SDKs (20.2%) collect the app list without any and collected the same group of SDKs in their latest release

declaration in their privacy policies, followed by clipboard version as of October 2023 and conducted a cross-version

data and location that are excessively collected by 11 (10.0%) analysis. Table VI depicts a summary of our re-inspection

to Table IV), our findings show that the app list and clipboard Trends of Privacy Collection Behaviors . We find 311 traces

data are the two most stealthily collected data types. Only 4 tainted from the latest version of 158 SDKs. Compared with

SDKs collecting the app list have mentioned it in their privacy our initial assessment, we observed 35 (10.1%) fewer traces

policies (leading to 22 excessive collection behaviors). None that attempt to collect and share user privacy data in public

data. The change between the outcomes of the two assessments

Over-claiming (Type III Issues) . Apart from the excessive mainly falls in the sources of tainted traces. As shown in

collection, we find that the over-claiming issue in privacy Table VI, we find obvious growth from the sharing of data

policies is far more pervasive in the tested SDKs. In our study, relevant to media and installed software (C4), reserving over

96 out of 109 (88.1%) SDKs are found to claim more data 1/3 of the total caught traces. Among the 105 tainted traces,

types in privacy policies than what they (really) need. The IP reading and sharing the list of installed apps ranks the top

address, network information, and MEID are the top three data among all sources, with 53 traces caught. Although the access

types that have been over-claimed in the tested SDK privacy to data in that category has been pervasively observed in our

policies. Especially, 44 out of 109 (40.4%) SDKs that provide initial assessment, our re-inspection did not catch any traces

| pervasive claims, again, reflect the worrisome landscape of | Additionally, we find that the collection behaviors for loca- |
| --- | --- |
| privacy compliance at the SDK level. | tion and SSID/BSSID have significantly declined, marking the |

Lessons Learned . Our study reveals two key findings. First, two greatest decreases. There is also an overall reduction in

some SDK developers use vague or broad terms like “identi- the collection of UUIs, including data types in categories C1

fiers” or “device information” instead of specifying the exact and C2. Upon reviewing the historical changes in permission

data being collected, leading to differing interpretations. For requirements, we note that most data types showing decreased

instance, while most developers use “identifiers” to indicate collection behaviors had their access rules significantly up-

device identifiers, some refer to advertisement identifiers, dated in Android 10 [21], which imposed strict restrictions on

causing over-claims for device identifiers and under-claims for third-party apps’ access to personally identifiable information.

Android ID or Google Ad ID. Second, although many SDKs In contrast, we find the growth of tainted traces for the app

declare access to both GPS and IP addresses for location data, list. Although the access to app list has also been restricted in

---

## Page 10

| Class com.ta.utdid2.a.a.d | Class com.ta.utdid2.device.c |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | public | static | String | getImei | ( | Context context | ) | { | 1 | public | synchronized | String |  |  |  |  |  |  |  |
| 2 | String s | = | null | ; | 2 | byte | [] | arr_b | = | this | . | b |  |  |  |  |  |  |  |
| 3 | TelephonyManager | tm0 | = | ( | TelephonyManager | ) | context | 3 | this | . | g | = | com | . | ta | . | utdid2 |  |  |
| 4 | . | getSystemService | ( | "phone" | ); | 4 | String s1 | = | com | . | ta | . |  |  |  |  |  |  |  |
| 5 | s | = | tm0 | . | getDeviceId | (); | // source #1 | 5 | if | ( | s1 | != | null | ) | { |  |  |  |  |
| 6 | if | ( | f | . | isEmpty | ( | str | )) | { | str | = | a | (); | } | 6 | h | ( | s1 | ); |
| 7 | if | ( | f | . | isEmpty | ( | str | )) | { | str | = | a | ( | context | ); | } | 7 | } |  |
| 8 | return | s | ; | 8 | return | this | . | g |  |  |  |  |  |  |  |  |  |  |  |
| 9 | } | 9 | } |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | private | static | String | a | () | { | 10 | private | byte | [] | b | () | throws |  |  |  |  |  |  |

11 String str = g . getProp ( " ro.aliyun.clouduuid " , "" ); 11 String s ;

12 if ( TextUtils . isEmpty ( str )) { 12 ByteArrayOutputStream

13 str = g . getProp ( " ro.sys.aliyun.clouduuid " , "" ); 13 new ByteArrayOutputStream

14 } return str ; 14 try {

15 } 15 s = com . ta . utdid2 . a .

16 private static String a ( Context context ) {

17 String str ;

18 try {

19 str = Settings . Secure . getString (

20 context . getContentResolver (),

21 " android_id " ); // source #2

22 } catch ( Throwable e ) { str = "" ; }

23 return str ;

24 }

| Push | AES encrypted, base64 encoded |  |
| --- | --- | --- |
| LBS | hashed | ‡ |
| com.baidu.uuid | Package name and serial or a random |  |

† depending on the permissions granted to the embedded app.

inferred description based on the reading logic in the implementation.

V. S YSTEM S ETTINGS I NJECTION I SSUES

system settings. Specifically, two entries of system settings

are involved, as shown in Table VII. Writing into the system

and abuses the “ preinstalled ” privilege by counting on itself

to be embedded in pre-installed apps or even privileged system

10

d () { 16 } catch ( Exception e0 ) {

(); 17 s = "" + new Random (). nextInt ();

. a . a . b . encodeToString ( b , 2); 18 }

utdid2 . a . a . b . encodeToString ( b , 2); 19 stream0 . write ( com . ta . utdid2 . a . a . c . getBytes (

20 f . hashCode ( s )), 0, 4);

21 return stream0 . toByteArray ()

22 }

23 private void h ( String s ) {

24 try {

| Exception | { | 25 | Settings.System.putString | ( |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26 | this | .mContext.getContentResolver | (), |  |  |  |  |  |
| stream0 | = | 27 | " | dxRMxhQkdGePGnp | ", s); |  |  |  |
| (); | 28 | } | catch | ( | Exception e1 | ) | { | } |

29 return ;

a . d . getImei ( this . mContext ); 30 }

Legend

______ The source method ______ The sink method

______ Key points of the trace Trace flow

permission, and the second approach is only viable when there

system properties in advance, we consider both them infeasible

approach, i.e., reading Android ID through a system setting

table named SECURE , does not request special permission. As a

hash value into the system settings with a customized key

(lines 25-27, right). This process, although it complies with

the Android permission mechanism, transforms the value of

settings.

unknown to us.

Fig. 4: Information flow demonstrates how the device ID is accessed and saved to the system settings by one of our analyzed

SDKs (the obfuscated code is obtained from reverse engineering and has been simplified to save space)

TABLE VII: System setting entries found that contains a UUI engineering. In order to obtain a UUI, it attempts to invoke

| SDK | Entry name | Description of the value | a privileged API (line 5, left), query the existence of pre- |  |  |
| --- | --- | --- | --- | --- | --- |
| Alicloud | dxCRMxhQkdGePGnp | IMEI/MEID, serial, or Android ID | † | , | written system properties (lines 6 and 10-15, left), and read |
| mqBRboGZkQPcAkyk | IMEI/MEID, serial, or Android ID | † | , | the Android ID (lines 7 and 16-24, left) sequentially, as shown |  |
| AES encrypted, base64 encoded | in the figure. Due to the first approach requests the embedded |  |  |  |  |
| Baidu | com.baidu.deviceid.v2 | Package name and Android ID, MD5 | app to be a system app with “ | READ_PRIVILEGED_PHONE_STATE | ” |
| UUID | † | , MD5 hashed | ‡ | exists a system app on the same device to write the two |  |
| ‡ | by default on nowadays Android devices. However, the third |  |  |  |  |

a future release, these results still seriously concern us since result, the SDK can at least obtain the Android ID to uniquely

the latest version of SDKs implies their persistent attempt to identify the device. It then performs a hash function over

excessively and stealthily collect user privacy data. the obtained Android ID (lines 19-20, right) and writes the

During our analysis, we find some traces from an SDK resettable Android ID into a de facto UUI that can be accessed

named “Alicloud push” are sunk at writing a value into the by any app that knows the customized key in the system

settings requires privileged permission so that ordinary third- Considering the exploitability of the pre-installed privileges,

party apps are unable to do so. However, we find that SDKs we carry out another round of investigation of all 158 SDKs

being embedded by pre-installed apps can write arbitrary val- to find if there exists any other potential privacy infringement

ues into the system settings even without the user’s awareness. by taking advantage of the system settings mechanism. As

We name this finding a system settings injection issue , because a result, we managed to find another two entries that have

it can be manipulated by an SDK to create and share user- been read in an SDK named “Baidu LBS” (see Table VII). As

unresettable identifiers (UUIs). their names imply, these two entries are obviously written by

Although leaking privacy data through covert channels has third-party privileged apps. We suspect the formation of the

been studied in existing literature [49], the system settings two entries should follow a similar routine, and accordingly

injection issues still seriously concern us as the caught SDK reverse engineer the involved SDK and present our inferred

subtly evades accessing highly sensitive UUIs (e.g., IMEI, as descriptions of the two entries in Table VII. Unfortunately,

discussed in [49]) but attempts to generate UUIs on their we did not find any app to write these entries into the system

own. The caught SDK then takes advantage of its popularity settings. Who exploited this system settings issue remains

apps. By exploiting this issue, the system settings become a Impact . We notice that the two studied SDKs are widely

covert channel to enable privacy-sensitive data sharing to apps adopted in third-party apps, especially in the Chinese market.

without privileged permission. Therefore, we conduct a small-scale study to explore the

Figure 4 illustrates an example of system setting injection impact of the system settings injection issues. We collect

from our findings. The source code is obtained through reverse devices from 9 OEM manufacturers (8 OEM devices pur-

---

## Page 11

Privilege Free-riding . An SDK’s access to privacy data de-

pends on the permissions granted to the apps it’s embedded in.

However, third-party apps pre-installed by OEMs can obtain

Precautions of Privilege Abuse . We regard that the pre-

installed privileges open an attack surface for a malicious

SDK, specifically when the SDK uses app-differential Android

ID to identify a device user, transforms it into a de facto UUI,

and provides free access with all apps installed on the victim

device. Based on this finding, we advocate Google restricting

Samsung, Vivo, and Xiaomi.

11

limitations at the moment of this work being performed.

and maintained in non-Google platforms.

C. Limitations

Elusive and Ambiguous Disclosure . Although developers

elusive or ambiguous phrasing widely exists in many SDK’s

privacy policies, leading to potential false negatives in our

NLI model-based analysis. We aim to explore the latest

advancements in LLMs and improve our approach to minimize

such impacts.

receive positive responses regarding non-compliance concerns

chased in the Chinese market 4 and 1 Google Pixel device platforms. For that reason, we call for strengthened regulation

purchased in the US market), download the packages of pre- over the usage of Android SDKs. We also advocate platforms

install apps, and investigate whether the two aforementioned performing static analysis over the SDK binaries to exhaus-

SDKs have been once embedded in the pre-installed apps. tively list requested permissions, especially for those at the

We observe a worrisome fact that except for the Google dangerous level and above. This measure could address the

Pixel devices, all the tested devices have at least one pre- black-box concern for app developers.

installed app using the investigated SDKs. According to the Transparent App Development . We advocate transparent

latest market report [50], these 8 OEM manufacturers reserve management over the permission requested by the embedding

over 66% global Android smartphone market share. They also SDKs. Thus, app developers can have their own discretion in

shipped over 94% new Android devices in China in 2023 [51]. granting permissions without compromising functionality. We

This implies that almost all Android smartphones sold in are delighted to see Google’s efforts in improving the SDK’s

the Chinese market may already pose a privacy leakage risk governance. A new mechanism called SDK Runtime has been

based on an assumption that the choice of pre-installed apps introduced in Android 13 that provides a dedicated execution

should remain the same across different models produced by environment for SDKs [52]. However, this mechanism is not

| a manufacturer. | compulsory and still faces many usability and functionality |  |
| --- | --- | --- |
| VI. D | ISCUSSION | Besides that, how to ensure the cooperation of SDK developers |
| A. Causes of Privacy Mishandling | remains a challenging issue, given many SDKs are released |  |

privileged permissions. A malicious SDK in such an app can Absence of Dynamic Testing . While our static taint analy-

exploit system settings to deploy privilege free-riding attacks, sis approach is effective, dynamic testing can improve effi-

creating and sharing UUIs without users’ awareness. As read- ciency by automatically identifying and excluding logically

ing system settings require no permissions, privilege free- invalid tainted traces, reducing manual validation efforts.

riding significantly undermines Google’s efforts in restricting However, dynamic SDK testing is challenging due to inade-

third-party app access to UUIs since Android 10. quate documentation, undisclosed interfaces, and highly event-

Insufficient Regulations . It is well known that the release driven/credential-required logic. For example, some finance

of Android apps is subject to strict regulations, with non- and customer service SDKs require a valid license or token to

compliance in privacy preservation potentially leading to re- function. Satisfying all functional prerequisites of the collected

moval from app stores or fines. However, SDK releases lack SDKs can be another challenging task and therefore is out of

similar fine-grained regulations and sufficient legislation to the scope of this study. We plan to explore potential dynamic

ensure compliance with personal data protection laws. Iron- testing solutions in the future.

ically, even some Google in-house SDKs do not have privacy Coverage of Targeted Methods . Our analysis covered 741

policies listed on the SDK Index 5 . Currently, both repositories API source methods and 46 sinks. Although we frequently

function merely as search engines for available SDKs, without update the configuration during this study, we may still miss

a platform-level compliance checking mechanism to ensure some data exfiltration channels as new APIs can be introduced

| complete permission disclosure. | along with OS evolution and emerging hardware. |  |  |  |
| --- | --- | --- | --- | --- |
| B. Our Recommendations | should clearly disclose personal data collection, we find that |  |  |  |
| pre-installed apps from writing data into the system settings | VII. E | THICS | C | ONSIDERATIONS |
| in the future. We also advise OEM manufacturers to minimize | We have reported all our findings to the relevant parties |  |  |  |
| the number of pre-installed apps on their devices. | and we also have kept them confidential for at least 90 days. |  |  |  |

Strengthened Platform Regulation . Currently, both release For each SDK that found a compliance issue, we manually

platforms selected in this study are merely index websites, searched the contact left by its developers and e-mailed our

which do not host the SDK binaries and lack substantial findings since our first round of SDK investigation. Although

enforcement. Developers voluntarily register SDKs on these we observed slight mitigation from re-inspection, we did not

4 These devices are manufactured by Honor, Huawei, Lenovo, OnePlus, Oppo, from the developers that we have attempted to contact. We also

5 An example can be found at https://play . google . com/sdks/details/com- expressed our concern to Google about the system settings

google-android-gms-play-services-auth injection issues (to be detailed in Section V) and suggested

---

## Page 12

12

removing the pre-installed privileges in writing system settings IX. C ONCLUSION

in the future release. Google replied and suggested that it is at In this study, we investigate the intricate privacy challenges

the device manufacturer’s discretion to select and grant pre- associated with the widespread use of third-party SDKs in An-

installed privileges to third-party apps. droid apps. Our large-scale analysis involved an evaluation of

158 third-party SDKs, prevalent across Android applications,

VIII. R ELATED W ORKS

with an approach intertwining rigorous taint analysis for data

Privacy Compliance Evaluation . Numerous works focus collection practices and LLM-aided interpretation of privacy

on detecting inconsistencies between the privacy practices policies. The findings were startling, with 338 potential privacy

of an application and its descriptions or its privacy poli- leakages detected from 158 SDKs. Besides that, our study

cies [53]–[60]. This line of research begins with automatic reveals that less than 70% of examined SDKs provide privacy

risk assessment of Android apps, such as WHYPER [56] and policies, among which approximately 37% SDKs are found

AutoCog [57] that leverage NLP techniques to evaluate the indulging in the over-collection of privacy data, signaling a

necessity of required permissions based on apps’ descriptions. clear violation of privacy norms. Our findings suggest the need

Gorla et al. [54] study mismatches between app descriptions for stricter regulations, improved development guidelines, and

and app behaviors by clustering Android apps based on their more transparent permission management to reduce privacy

description topics and identifying outliers in each cluster with risks in Android apps.

respect to their API usage. Recent work extends the scope

| of privacy compliance evaluation to examining third-party | R | EFERENCES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| data harvesting, user consent, service misconfigurations, and | [1] | P. | Ruiz, | “Authenticating | on | Android | with | the | AppAuth |
| quality of privacy policies at the app level. XFinder [27] | Library,” | 2022, | (accessed | 9 | July | 2024). | [Online]. | Avail- |  |

able: https://medium . com/androiddevelopers/authenticating-on-android-

| uses dynamic analysis and NLP techniques to parse terms-of- | with-the-appauth-library-7bea226555d5 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| service and extract data-sharing policies. Nguyen et al. [61] | [2] | Android | Documentation, | “Work | with | data | more | securely,” |
| study user consent verification through traffic analysis and | 2023, | (accessed | 9 | July | 2024). | [Online]. | Available: | https: |

//developer . android . com/topic/security/data

| ablation experiments. Zhang et al. [62] highlight the issue | [3] | Segment, | “Analytics | for | Android,” | 2023, | (accessed | 9 | July |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| of analytical service misconfigurations, while Yu et al. [63] | 2024). | [Online]. | Available: | https://segment | . | com/docs/connections/ |  |  |  |
| scrutinize the apps’ privacy policies with regard to the in- | sources/catalog/libraries/mobile/android |  |  |  |  |  |  |  |  |

[4] Android Documentation, “Add Ads to Your Instant App,”

| clusion of third-party libraries. Andow et al. [32] propose | 2023, | (accessed | 9 | July | 2024). | [Online]. | Available: | https: |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| POLICHECK that identifies ambiguous or omitted disclosures | //developer | . | android | . | com/topic/google-play-instant/guides/advertising |  |  |  |  |  |  |
| of third parties. Pan et al. [64] study the automated generation | [5] | ——, | “Develop | UI | for | Android,” | 2023, | (accessed | 9 | July | 2024). |

[Online]. Available: https://developer . android . com/develop/ui

| of privacy policies for mobile apps and unveil that defective | [6] | P. Salza, F. Palomba, D. Di Nucci, C. D’Uva, A. De Lucia, and |  |
| --- | --- | --- | --- |
| compliance widely exists in the automatically generated pri- | F. Ferrucci, “Do Developers Update Third-Party Libraries in Mobile |  |  |
| vacy policies. Zhao et al. [65] study privacy compliance of | Apps?” in | ICPC | , 2018, p. 255–265. |

[7] Y. Zhang, J. Dai, X. Zhang, S. Huang, Z. Yang, M. Yang, and

| third-party libraries in Android through the lens of pattern | H. Chen, “Detecting third-party libraries in android applications with |  |
| --- | --- | --- |
| matching in privacy disclosure. Compared with it, our work | high precision and recall,” in | 2018 IEEE 25th International Conference |
| investigates SDKs, which are more complex in implementation | on Software Analysis, Evolution and Reengineering (SANER) | , 2018, pp. |

141–152.

| and business logic. Our study also resorts to a language | [8] | blackkite, “Data Breaches Caused By Third-Parties,” 2022, (accessed |  |
| --- | --- | --- | --- |
| model in privacy disclosure analysis that does not request | 9 July 2024). [Online]. Available: https://blackkite | . | com/data-breaches- |
| manual data annotation and model training. Parallel research | caused-by-third-parties |  |  |

[9] P. Mahajan, “3rd Party Libraries: Your Next Data Breach

by Xiao et al. [66] investigate compliance of third-party Nightmare,” 2022, (accessed 9 July 2024). [Online]. Available:

libraries by assessing the consistency between API documents https://www . privado . ai/post/3rd-party-libraries-data-breach

and dynamic analysis results. In comparison, our work fo- [10] Droid, “How to fix my Android - What Is Mobile Services

Manager?” 2023, (accessed 9 July 2024). [Online]. Available: https:

cuses on compliance of SDKs that contains more complicated //www . howtofixmyandroid . com/what-is-mobile-services-manager/

implementation that hinders from effective dynamic analysis, [11] M. Mollah, “What Is Mobile Services Manager? Is It A Threat?

and meanwhile our study examine the privacy disclosure by How To Fix It?” 2022, (accessed 9 July 2024). [Online]. Available:

https://www . socialmediamagazine . org/mobile-services-manager/

directly interpreting the privacy policies, which are written in [12] J. Keegan and A. Ng, “Over 100 apps that sold location data to

natural language without a standard format. sketchy data broker revealed,” 2022, (accessed 9 July 2024). [Online].

Privacy Leakage Assessment . There is a substantial body Available: https://mashable . com/article/app-location-data-sold

[13] The European Parliament, “Regulation (eu) 2016/679 of the european

| of literature addressing various aspects of privacy concerns | parliament and of the council of 27 april 2016 on the protection of |
| --- | --- |
| in the Android ecosystem [28], [67], [68]. Meng et al. [43] | natural persons with regard to the processing of personal data and on |
| study user-unresettable identifier safeguards on a wide range | the free movement of such data, and repealing directive 95/46/ec (general |

data protection regulation) (text with eea relevance),” Official Journal

of Android devices. He et al. [69] utilize dynamic analysis of the European Union , 2016.

to explore the leakage of permission-related data from third- [14] State of California Department of Justice, “California consumer

party libraries in Android apps Ekambaranathan et al. [70] privacy act (ccpa),” 2023, (accessed 9 July 2024). [Online]. Available:

https://oag . ca . gov/privacy/ccpa

investigate data usage and disclosure in children’s app. Liu [15] Google, “Google play sdk index,” 2024, (accessed 9 July 2024).

et al. [71] examine data leakage from nine analytic libraries [Online]. Available: https://play . google . com/sdks

across 300 apps, using both static and dynamic analyses. [16] China Academy of Information and Communication Technology,

“Nationwide sdk management and service platform (translated

Razaghpanah et al. [72] detect third-party advertising and from chinese),” 2024, (accessed 9 July 2024). [Online]. Available:

tracking services via dynamic analysis of network traffic data. https://sdk . caict . ac . cn/official

---

## Page 13

compliance in android apps,” IEEE Access , 2024.

(accessed 9 July 2024). [Online]. Available: https://gdpr . eu/data-privacy/

Rodriguez, “A longitudinal study of pii leaks across android app

MobiSys , 2016, pp. 361–374.

library data harvesting on android,” in USENIX Security , 2021.

system for realtime privacy monitoring on smartphones,” TOCS , vol. 32,

no. 2, pp. 1–29, 2014.

[29] C. Gibler, J. Crussell, J. Erickson, and H. Chen, “Androidleaks: auto-

matically detecting potential privacy leaks in android applications on a

large scale,” in TrustCom . Springer, 2012, pp. 291–307.

[30] L. Qiu, Z. Zhang, Z. Shen, and G. Sun, “Apptrace: Dynamic trace on

android devices,” in ICC , 2015, pp. 7145–7150.

[31] M. Sun, T. Wei, and J. C. Lui, “Taintart: A practical multi-level

privacy policy and data flow analysis with PoliCheck,” in 29th USENIX

analysis of data-usage purposes in mobile apps,” in Proceedings of

[34] B. Muthukadan, “Selenium with Python,” 2018, (accessed 9 July 2024).

requirements for mobile apps,” in 2016 AAAI Fall Symposium Series ,

vol. 14, 2014, p. 1125.

13

log-info-disclosure

2023.

314–328.

2019.

market-share/mobile

share/mobile/china

[52] Google, “SDK Runtime,” 2024, (accessed 9 July 2024).

[Online]. Available: https://developer . android . com/design-for-safety/

privacy-sandbox/sdk-runtime

[53] D. Bui, B. Tang, and K. G. Shin, “Detection of inconsistencies in privacy

practices of browser extensions,” in 2023 IEEE Symposium on Security

and Privacy (SP) . IEEE, 2023, pp. 2780–2798.

VL/HCC , 2018.

2013, pp. 527–542.

applications,” in CCS , 2014.

21) , 2021, pp. 3667–3684.

vol. 47, no. 2, pp. 221–242, 2018.

[17] D. Rodriguez, J. M. Del Alamo, C. Fernández-Aller, and N. Sadeh, [41] Google, “Log Info Disclosure,” 2023, (accessed 9 July 2024).

“Sharing is not always caring: Delving into personal data transfer [Online]. Available: https://developer . android . com/topic/security/risks/

[18] Google, “Understand app privacy & security practices with [42] ——, “Application Sandbox,” 2022, (accessed 9 July 2024). [Online].

google play’s data safety section,” 2024, (accessed 9 July Available: https://source . android . com/docs/security/app-sandbox

2024). [Online]. Available: https://support . google . com/googleplay/ [43] M. H. Meng, Q. Zhang, G. Xia, Y. Zheng, Y. Zhang, G. Bai, Z. Liu,

answer/11416267?sjid=6208336964583751082-AP S. G. Teo, and J. S. Dong, “Post-gdpr threat hunting on android phones:

[19] B. Wolford, “A guide to gdpr data privacy requirements,” 2024, dissecting os-level safeguards of user-unresettable identifiers,” in NDSS ,

[20] Google, “Manifest.permission,” 2024, (accessed 28 June 2024). [44] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein,

| [Online]. | Available: | https://developer | . | android | . | com/reference/android/ | Y. Le Traon, D. Octeau, and P. McDaniel, “Flowdroid: Precise context, |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Manifest | . | permission | flow, field, object-sensitive and lifecycle-aware taint analysis for android |  |  |  |  |
| [21] | ——, “Privacy changes in Android 10,” 2023, (accessed 9 July 2024). | apps,” | Acm Sigplan Notices | , vol. 49, no. 6, pp. 259–269, 2014. |  |  |  |

[Online]. Available: https://developer . android . com/about/versions/10/ [45] Facebook Open Source, “Mariana Trench: Security-Focused Static

| privacy/changes | Analysis for Android and Java Applications,” 2024, (accessed 9 July |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [22] | T. Chen, I. Ullah, M. A. Kaafar, and R. Boreli, “Information leakage | 2024). [Online]. Available: https://mariana-tren | . | ch/ |  |  |  |  |  |  |  |
| through mobile analytics services,” in | HotMobile | , 2014, pp. 1–6. | [46] | Bytedance, | “Appshark,” | 2022, | (accessed | 9 | July | 2024). | [Online]. |
| [23] | C. Leung, J. Ren, D. Choffnes, and C. Wilson, “Should you use the | Available: https://github | . | com/bytedance/appshark |  |  |  |  |  |  |  |

app for that? comparing the privacy implications of app-and web-based [47] Y. Shen, P.-A. Vervier, and G. Stringhini, “Understanding worldwide

online services,” in IMC , 2016, pp. 365–372. private information collection on android,” in NDSS , 2021.

[24] E. P. Papadopoulos, M. Diamantaris, P. Papadopoulos, T. Petsas, S. Ioan- [48] Z. Wang, Z. Li, M. Xue, and G. Tyson, “Exploring the eastern frontier:

| nidis, and E. P. Markatos, “The long-standing privacy debate: Mobile | A first look at mobile app tracking in china,” in | Passive and Active |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| websites vs mobile apps,” in | WWW | , 2017, pp. 153–162. | Measurement: 21st International Conference, PAM 2020, Eugene, Ore- |  |  |  |  |  |  |  |  |  |
| [25] | J. Ren, M. Lindorfer, D. J. Dubois, A. Rao, D. Choffnes, and N. Vallina- | gon, USA, March 30–31, 2020, Proceedings 21 | . | Springer, 2020, pp. |  |  |  |  |  |  |  |  |
| versions,” in | NDSS | , 2018. | [49] | J. Reardon, Á. Feal, P. Wijesekera, A. E. B. On, N. Vallina-Rodriguez, |  |  |  |  |  |  |  |  |
| [26] | J. Ren, A. Rao, M. Lindorfer, A. Legout, and D. Choffnes, “Recon: | and S. Egelman, “50 ways to leak your data: An exploration of apps’ |  |  |  |  |  |  |  |  |  |  |
| Revealing | and | controlling | pii | leaks | in | mobile | network | traffic,” | in | circumvention of the android permissions system,” in | USENIX Security | , |

[27] J. Wang, Y. Xiao, X. Wang, Y. Nan, L. Xing, X. Liao, J. Dong, [50] Statcounter, “Mobile Vendor Market Share Worldwide,” 2024, (accessed

N. Serrano, H. Lu, X. Wang et al. , “Understanding malicious cross- 9 July 2024). [Online]. Available: https://gs . statcounter . com/vendor-

[28] W. Enck, P. Gilbert, S. Han, V. Tendulkar, B.-G. Chun, L. P. Cox, J. Jung, [51] ——, “Mobile Vendor Market Share China,” 2024, (accessed 9 July

P. McDaniel, and A. N. Sheth, “Taintdroid: an information-flow tracking 2024). [Online]. Available: https://gs . statcounter . com/vendor-market-

information-flow tracking system for android runtime,” in CCS , 2016, [54] A. Gorla, I. Tavecchia, F. Gross, and A. Zeller, “Checking app behavior

pp. 331–342. against app descriptions,” in ICSE , 2014.

[32] B. Andow, S. Y. Mahmud, J. Whitaker, W. Enck, B. Reaves, K. Singh, [55] X. Liu, Y. Leng, W. Yang, W. Wang, C. Zhai, and T. Xie, “A large-scale

| and S. Egelman, “Actions speak louder than words: Entity-Sensitive | empirical study on android runtime-permission rationale messages,” in |  |  |  |
| --- | --- | --- | --- | --- |
| Security Symposium (USENIX Security 20) | , 2020, pp. 985–1002. | [56] | R. Pandita, X. Xiao, W. Yang, W. Enck, and T. Xie, “Whyper: Towards |  |
| [33] | D. Bui, Y. Yao, K. G. Shin, J.-M. Choi, and J. Shin, “Consistency | automating risk assessment of mobile applications,” in | USENIX Security | , |

the 2021 ACM SIGSAC Conference on Computer and Communications [57] Z. Qu, V. Rastogi, X. Zhang, Y. C. Chen, T. Z. Zhu, and Z. Chen,

| Security | , 2021, pp. 2824–2843. | “Autocog: Measuring the description-to-permission fidelity in android |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [Online]. Available: https://selenium-python | . | readthedocs | . | io/ | [58] | R. Slavin, X. Wang, M. B. Hosseini, J. Hester, R. Krishnan, J. Bhatia, |
| [35] | B. Andow, S. Y. Mahmud, W. Wang, J. Whitaker, W. Enck, B. Reaves, | T. D. Breaux, and J. Niu, “Toward a framework for detecting privacy |  |  |  |  |
| K. Singh, and T. Xie, “PolicyLint: investigating internal privacy policy | policy violations in android application code,” in | Proceedings of the 38th |  |  |  |  |
| contradictions on google play,” in | 28th USENIX security symposium | International Conference on Software Engineering | , 2016, pp. 25–36. |  |  |  |
| (USENIX security 19) | , 2019, pp. 585–602. | [59] | X. Wang, X. Qin, M. B. Hosseini, R. Slavin, T. D. Breaux, and J. Niu, |  |  |  |
| [36] | F. Xie, Y. Zhang, C. Yan, S. Li, L. Bu, K. Chen, Z. Huang, and G. Bai, | “Guileak: Tracing privacy policy claims on user input data for android |  |  |  |  |
| “Scrutinizing privacy policy compliance of virtual personal assistant | applications,” in | Proceedings of the 40th International Conference on |  |  |  |  |
| apps,” in | ASE | , 2022. | Software Engineering | , 2018, pp. 37–47. |  |  |

[37] L. Yu, X. Luo, X. Liu, and T. Zhang, “Can we trust the privacy [60] L. Zhou, C. Wei, T. Zhu, G. Chen, X. Zhang, S. Du, H. Cap, and H. Zhu,

| policies of android apps?” in | 2016 46th Annual IEEE/IFIP International | “POLICYCOMP: Counterpart comparison of privacy policies uncovers |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Conference on Dependable Systems and Networks (DSN) | . | IEEE, 2016, | overbroad personal data collection practices,” in | USENIX Security | , 2022. |  |  |  |
| pp. 538–549. | [61] | T. T. Nguyen, M. Backes, N. Marnau, and B. Stock, “Share first, ask |  |  |  |  |  |  |
| [38] | S. Zimmeck, Z. Wang, L. Zou, R. Iyengar, B. Liu, F. Schaub, S. Wilson, | later (or never?) studying violations of | { | GDPR’s | } | explicit consent in |  |  |
| N. Sadeh, S. Bellovin, and J. Reidenberg, “Automated analysis of privacy | android apps,” in | 30th USENIX Security Symposium (USENIX Security |  |  |  |  |  |  |
| 2016. | [62] | X. Zhang, X. Wang, R. Slavin, T. Breaux, and J. Niu, “How does |  |  |  |  |  |  |
| [39] | H. Harkous, S. T. Peddinti, R. Khandelwal, A. Srivastava, and N. Taft, | misconfiguration | of | analytic | services | compromise | mobile | privacy?” |
| “Hark: A deep learning system for navigating privacy feedback at scale,” | in | Proceedings of the ACM/IEEE 42nd International Conference on |  |  |  |  |  |  |
| in | 2022 IEEE Symposium on Security and Privacy (SP) | . | IEEE, 2022, | Software Engineering | , 2020, pp. 1572–1583. |  |  |  |
| pp. 2469–2486. | [63] | L. Yu, X. Luo, J. Chen, H. Zhou, T. Zhang, H. Chang, and H. K. |  |  |  |  |  |  |
| [40] | S. Rasthofer, S. Arzt, and E. Bodden, “A machine-learning approach | Leung, “Ppchecker: Towards accessing the trustworthiness of android |  |  |  |  |  |  |
| for classifying and categorizing android sources and sinks.” in | NDSS | , | apps’ privacy policies,” | IEEE Transactions on Software Engineering | , |  |  |  |

---

## Page 14

14

[64] S. Pan, D. Zhang, M. Staples, Z. Xing, J. Chen, X. Xu, and T. Hoang, “Is

it a trap? a large-scale empirical study and comprehensive assessment

of online automated privacy policy generators for mobile apps,” in 33rd

USENIX Security Symposium (USENIX Security 24) , 2024, pp. 5681–

5698.

[65] K. Zhao, X. Zhan, L. Yu, S. Zhou, H. Zhou, X. Luo, H. Wang, and

Y. Liu, “Demystifying privacy policy of third-party libraries in mobile

apps,” in 2023 IEEE/ACM 45th International Conference on Software

Engineering (ICSE) . IEEE, 2023, pp. 1583–1595.

[66] Y. Xiao, C. Zhang, Y. Qin, F. F. S. Alharbi, L. Xing, and X. Liao,

“Measuring compliance implications of third-party libraries’ privacy

label disclosure guidelines,” in Proceedings of the 2024 on ACM SIGSAC

Conference on Computer and Communications Security , 2024, pp.

1641–1655.

[67] K. Zhang and X. Wang, “Peeping tom in the neighborhood: Keystroke

eavesdropping on multi-user systems,” in USENIX Security , 2009.

[68] X. Zhou, S. Demetriou, D. He, M. Naveed, X. Pan, X. Wang, C. A.

Gunter, and K. Nahrstedt, “Identity, location, disease and more: Inferring

your secrets from android public resources,” in Proceedings of the 2013

ACM SIGSAC conference on Computer & communications security ,

2013, pp. 1017–1028.

[69] Y. He, B. Hu, and Z. Han, “Dynamic privacy leakage analysis of android

third-party libraries,” in 2018 1st International Conference on Data

Intelligence and Security (ICDIS) , 2018, pp. 275–280.

[70] A. Ekambaranathan, J. Zhao, and M. Van Kleek, ““money makes the

world go around”: Identifying barriers to better privacy in children’s

apps from developers’ perspectives,” in Proceedings of the 2021 CHI

Conference on Human Factors in Computing Systems , 2021, pp. 1–15.

[71] X. Liu, J. Liu, S. Zhu, W. Wang, and X. Zhang, “Privacy risk analysis

and mitigation of analytics libraries in the android ecosystem,” IEEE

Transactions on Mobile Computing , vol. 19, no. 5, pp. 1184–1199, 2019.

[72] A. Razaghpanah, R. Nithyanand, N. Vallina-Rodriguez, S. Sundaresan,

M. Allman, C. Kreibich, P. Gill et al. , “Apps, trackers, privacy, and

regulators: A global study of the mobile tracking ecosystem,” in The 25th

Annual Network and Distributed System Security Symposium (NDSS

2018) , 2018.

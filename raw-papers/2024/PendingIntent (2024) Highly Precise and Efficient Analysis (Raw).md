---
title: "Highly Precise and Efficient Analysis of PendingIntent Vulnerabilities for Android Apps"
creator: "Aspose Pty Ltd."
pages: 12
---

# Highly Precise and Efficient Analysis of PendingIntent Vulnerabilities for Android Apps

> **總頁數**：12 頁

---

## Page 1

Wiley

Security and Communication Networks

Volume 2024, Article ID 8663701, 12 pages

https://doi.org/10.1155/2024/8663701

Research Article

Highly Precise and Efficient Analysis of PendingIntent

Vulnerabilities for Android Apps

Azadeh Sarvazimi , Mehdi Sakhaei-nia , and NargesSadat Bathaeian

Department of Computer Engineering, Faculty of Engineering, Bu-Ali Sina University, Hamedan, Iran

Correspondence should be addressed to Mehdi Sakhaei-nia; sakhaei@basu.ac.ir

Received 24 December 2023; Revised 12 May 2024; Accepted 14 September 2024

Academic Editor: Ghanshyam Singh

Copyright © 2024 Azadeh Sarvazimi et al. Tis is an open access article distributed under the Creative Commons Attribution

License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly

cited.

Te expanding development of android applications is partially due to the communication model, named inter-component

communication (ICC) model. PendingIntent (PI) is a powerful feature that is used for ICC. Many android developers use PI in

their apps, but if it is used insecurely, it can pose risks and result in diferent types of attacks like denial of service, privilege

escalation, and data leakage. Hence, it is crucial to detect vulnerabilities related to PI before android apps are released on Android

app stores. In this paper, a new PI-related vulnerability is introduced, which is detected by the proposed method in addition to the

vulnerabilities pointed out in other methods. In addition, the proposed method that is based on static analysis takes less time than

other methods to detect the vulnerabilities. For evaluation, we compare the proposed method with PIAnalyzer tool. Results on 51

application benchmarks show that the proposed method detects the new PI-related vulnerability that is not detected by

PIAnalyzer. Also, the proposed method detects vulnerabilities 27% faster than PIAnalyzer.

Keywords: android; intent analysis; PendingIntent; PIAnalyzer; vulnerability

1. Introduction necessary to detect these vulnerabilities before publishing

Android applications in diferent markets [3]. However,

| Alongside the increase in popularity and number of users of | testing the applications published in diferent markets poses |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| the Android operating system (OS), thousands of applica- | challenges for provider stores, including the fact that such |  |  |  |  |
| tions appear every day in the ofcial Android Market | test and analysis are time-consuming. |  |  |  |  |
| (Google Play Store) and alternative markets [1]. Tis pop- | PI is a powerful feature for ICC in Android. Te PI stores |  |  |  |  |
| ularity and expansion can be attributed to the capabilities | a base Intent that will be executed later by another appli- |  |  |  |  |
| provided by the development of Android applications [2]. | cation or component but with the same identity and per- |  |  |  |  |
| However, sometimes these capabilities are prone to some | missions as the sender application [5]. In fact, PI is a token |  |  |  |  |
| vulnerabilities leading to their misusage [3]. One of such | that one application, such as Application A, sends to another |  |  |  |  |
| capabilities | is | inter-component | communication | (ICC), | application, such as Application B, thus allowing Applica- |
| specifcally PendingIntent (PI) [4]. Tough this feature is | tion B to inherit Application A’s permissions to execute |  |  |  |  |
| very useful in Android applications, as in notifcations and | a predefned piece of code. Terefore, insecure use of PIs can |  |  |  |  |
| alerts, its insecure use can pose various risks for the user and | lead to severe security consequences in the form of denial of |  |  |  |  |
| it may lead to attacks such as denial of service, privilege | service attacks, identity theft, and privilege escalation [6, 7]. |  |  |  |  |
| escalation, and data leakage [4, 5]. Failure to detect these | Several methods have been proposed to detect PI vul- |  |  |  |  |
| vulnerabilities in Android applications can lead to a decrease | nerabilities that vary in their precision, execution time, and |  |  |  |  |
| in the use of such applications by the victim of attacks, | analysis type. XManDroid is a security framework that has |  |  |  |  |
| imposing losses on the industry in general. It is, therefore, | limited precision and produces a large number of false |  |  |  |  |

*[Image: Page 1 Image]*

---

## Page 2

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| 2 | Security and Communication Networks |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| positives [7]. In [8] is presented a static-based approach that | forms | a | signifcant | part | of | Android | applications; | (2) |
| is capable of detecting only one type of PI vulnerability with | Broadcast Receiver that waits to receive messages from the |  |  |  |  |  |  |  |
| low precision and many false positives. IntentDroid [9] is | Android system or other Android applications, such as |  |  |  |  |  |  |  |
| a dynamic analysis approach that has inherited the limita- | incoming calls or text messages from other components or |  |  |  |  |  |  |  |
| tions of dynamic analysis such as runtime overhead. PIA- | other systems; (3) Content Provider, which acts as a standard |  |  |  |  |  |  |  |
| nalyzer [10] is a method based on static analysis that is | interface for sharing data between applications; and (4) |  |  |  |  |  |  |  |
| capable of detecting a higher number of PI-related vul- | Service that runs applications in the background. Service |  |  |  |  |  |  |  |
| nerabilities | with | higher | precision | compared | to | other | components are unique because their processing is hidden in |  |
| methods but has the challenge of execution time. Table 1 | the | user | device | and | creates | various | opportunities | for |
| showcases examples of tools, with comprehensive details | malicious actions [13]. |  |  |  |  |  |  |  |
| elaborated upon in the “Related Work” section. | An Intent specifes the target component of a message, |  |  |  |  |  |  |  |
| In this paper, a new PI-related vulnerability is in- | facilitating communication among Android components. |  |  |  |  |  |  |  |
| troduced. Te PI can be vulnerable if an explicit base Intent | Tere are two types of Intent: explicit Intent and implicit |  |  |  |  |  |  |  |
| is wrapped in the implicit Intent with nonstandard action. | Intent. An Intent is explicit if it specifes the target com- |  |  |  |  |  |  |  |
| However, as far as we know, other methods have been | ponent and thus must be passed to the same component. |  |  |  |  |  |  |  |
| proposed to detect PI vulnerabilities, if the base Intent is | However, if an action instead of a component is specifed in |  |  |  |  |  |  |  |
| explicit, it is considered as a secure PI. Te proposed method | an Intent, the Intent is implicit. Tis Intent can pass the |  |  |  |  |  |  |  |
| is a fast and precise method based on static analysis to detect | request to any application that can perform the specifed |  |  |  |  |  |  |  |
| PI-related vulnerabilities. Te proposed method is imple- | action and has declared that action in its Intent flter. To |  |  |  |  |  |  |  |

1

| mented as a tool called PIVAT | (see Nomenclature for | receive an Intent, a service or activity must be declared in the |
| --- | --- | --- |
| a complete list of abbreviations). For evaluation, PIVAT is | manifest (broadcast receivers can be declared in the manifest |  |
| compared with PIAnalyzer. To this end, both methods are | or at runtime). If the Exported attribute is true for a com- |  |
| implemented and experimentally evaluated for 51 bench- | ponent in the manifest, or the component contains at least |  |
| mark applications. PIVAT detects the new PI-related vul- | one Intent flter, then that component is public. Tis means |  |
| nerability that is not detected by PIAnalyzer. In addition, | that it can receive Intents from other applications. Intent |  |
| PIVAT takes less time to detect the vulnerabilities than | flters specify the types of Intent to be delivered to public |  |
| PIAnalyzer. | components [14]. |  |
| Te main contributions of this research are as follows: | A PI is a special kind of Intent that stores a base Intent to |  |

be executed later by another application or component,

• Introducing a new PI-related vulnerability.

while having the identity and permissions of the sender

| • | Providing a new method based on static analysis for | application. An application can send a PI to a third-party |
| --- | --- | --- |
| detecting PI-related vulnerabilities that is faster than | application or system component to perform predefned |  |
| other methods reviewed above [11]. | tasks at another time on behalf of the sender application. Te |  |
| • | Evaluating two methods, i.e., proposed method and | point is that the main application does not need to be ac- |
| PIAnalyzer, on 51 benchmark applications. | tively running or in memory at that moment, as the receiver |  |

will run it just it were being run by the main application. For

Tis paper is organized as follows. In Section 2, the basic

this purpose, Android transfers the permissions and identity

concepts related to the components of Android applications,

of the sender application to the target application receiving

Intent and PI objects used for ICC, and PI-related vulner-

the PI. In fact, PI is an Intent that will perform the action

abilities are described. Section 3 reviews the related litera-

specifed by the source application, on its behalf, i.e., with its

ture. In Section 4, a new PI-related vulnerability is

identity and permissions, irrespective of whether the source

introduced. Section 5 describes in detail the proposed

application is running or not [5, 15, 16]. PI is most used for

method for analyzing and detecting PI vulnerabilities. In

notifcation and alarm services [4].

Section 6, the evaluation of the proposed method and

Whenever the PI receiver calls its Send method, the

comparison with PIAnalyzer is presented, and fnally, the

associated Intent is executed with the identity and per-

paper is ended with a conclusion.

missions of the source application [8]. However, the PI

receiver can modify three main parts of the basic Intent data,

2. Background which may in turn modify the meaning of the basic Intent

that runs with the permissions and identity of the main

| Tis section reviews the basic concepts underlying this | application. If the sender already defnes the target com- |
| --- | --- |
| study. An Android application contains several fles and | ponent or Intent action, the PI receiver can no longer |
| folders. A key fle in the structure of Android applications is | override it. However, if not already defned by the sender, an |
| AndroidManifest.xml, which contains a list of components | unwanted target component or Intent action can be defned |
| hosted by an application. Some information in the fle is used | after delivering it to the recipient. Finally, the PI receiver can |
| for communication among components during runtime, | always add extra data after receipt. Tat is, an implicit Intent |
| while others are related to the permissions applied and | (whose target component has not been defned) can be |
| requested by the application [12]. | modifed by the receiver application to target any compo- |
| Every Android application is made up of four compo- | nent (with the main application’s permission), including |
| nents: (1) Activity that represents the user interface and | system features such as clearing the phone [10]. Such |

---

## Page 3

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Security and Communication Networks 3

Table 1: Tools and methods for PI analysis.

Tool name Details Method

A security framework with limited precision but produces a large number of false

XManDroid Dynamic analysis

positives

A dynamic analysis approach inheriting the limitations of dynamic analysis such as

IntentDroid Dynamic analysis

runtime overhead

A method based on static analysis capable of detecting a higher number of PI-related

PIAnalyzer vulnerabilities with higher precision compared to other methods but with the Static analysis

challenge of execution time

Open-source tool for ICC-based taint analysis, capable of detecting PI-related

IccTA Static analysis

vulnerabilities

| PITracker | Automated analysis tool based on Intent fow analysis, capable of detecting PI | Static analysis |
| --- | --- | --- |
| vulnerabilities can result in attacks leading to privilege es- | Exploit: A malware can show interest in PI via Intent |  |
| calation, denial of service, and data leakage. Terefore, | flter. As soon as the empty PI is received, the malware sets |  |
| detecting these vulnerabilities is essential. | a malicious action in the PI, so that the malicious action is |  |
| Te PI can be transferred either to a trusted system | performed by Application X when the PI is processed [17]. |  |
| component (such as an alarm manager) or to another Intent | Tis can result in privilege escalation and denial of service |  |
| that wraps it. PI-related vulnerabilities depend on the types | attacks. Figure 3 shows an example of such vulnerability. |  |

of their transmission, which are briefy described below.

2.4. An Example of a Vulnerable PI. An example of a code

| 2.1. | Type | I: | Implicit | PI | Sent | to | a | System | Component. | representing the insecure use of PI is shown in Figure 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vulnerability: Te application X can create a PI containing | (quoted from [10]). Te code provided in Figure 4(a) is an |  |  |  |  |  |  |  |  |  |
| an implicit Intent and pass it to a system component such as | example of a vulnerable program. Tis program has per- |  |  |  |  |  |  |  |  |  |
| a notifcation manager [10]. | mission to make phone calls. In line four, an empty base |  |  |  |  |  |  |  |  |  |
| Exploit: When the user clicks on the notifcation, the | Intent has been created. In line fve, the base Intent is |  |  |  |  |  |  |  |  |  |
| target component of the X is expected to take delivery of the | wrapped inside a PI and sent through another implicit Intent |  |  |  |  |  |  |  |  |  |
| Intent. However, any application that can perform the action | called implicitWrappingIntent (lines six to eight). As the |  |  |  |  |  |  |  |  |  |
| specifed in the base Intent and has declared this action in its | Intent including PI is sent implicitly in the application, it can |  |  |  |  |  |  |  |  |  |
| Intent flter may receive the Intent, potentially leading to | be received by any application that has declared a corre- |  |  |  |  |  |  |  |  |  |
| a denial of service attack. Figure 1 shows an example of such | sponding | flter | in | its | manifest. | Te | code | provided | in |  |
| vulnerability. | Figure 4(b) represents a malicious program that can use its |  |  |  |  |  |  |  |  |  |

Intent flter to receive the implicit Intent sent by the vul-

nerable application and receive the PI wrapped therein. Te

| 2.2. Type II: Implicit PI Wrapped in an Implicit Intent. | program does not have permission to make phone calls. In |
| --- | --- |
| Vulnerability: Application X can create a PI containing an | line three of the code, PI is extracted and given that the base |
| implicit Intent and send it through an implicit Intent. When | Intent in the vulnerable code is empty with no defned |
| the PI is processed, the associated base Intent is detected and | action, the base Intent has been manipulated in line four and |
| processed by a component based on the Intent flter. When | the action has been defned to make a phone call to a specifc |
| several components have the same Intent flter, the com- | phone number. Calling the Send method of the PI object in |
| ponent with the highest priority is selected for processing the | line six, the malicious application has been able to make |
| corresponding Intent [17]. | a phone call using the identity and permission of the vul- |
| Exploit: Each application can receive an implicit PI [17] | nerable application. Terefore, the malicious application |
| and use the Send method of that PI to send intents with the | could execute its malicious request by exploiting a vulner- |
| desired data on behalf of the original sender. A malware can | able application that used PI insecurely. |

manipulate Intent data and thus use leakage or modifcation

of sensitive data and distribute PI for Intent spoofng 3. Related Work

purposes, which can lead to denial of service and data

| leakage attacks [8]. Figure 2 shows an example of such | Tere are several methods for analysis and detection of PI |
| --- | --- |
| vulnerability. | vulnerabilities that vary in their type of analysis, accuracy, |

execution time, and efciency. Existing security methods are

implemented in diferent manners and architectures and use

| 2.3. Type III: Empty PI Wrapped in an Implicit Intent. | various techniques and mechanisms that are generally divided |
| --- | --- |
| Vulnerability: Application X can create a PI containing an | into three main groups, i.e., prevention-based, analysis-based |
| empty Intent and send it through an implicit Intent. When | (static or dynamic), and runtime monitoring [12]. |
| no action is specifed in the PI, the PI receiver can confgure | XManDroid enables runtime monitoring of ICC and |
| any action and perform it on behalf of the application that | develops communication policies based on a combination of |
| has sent the PI [17]. | specifc permissions [7]. Since XManDroid monitors all |

---

## Page 4

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

4 Security and Communication Networks

Figure 1: An example of the vulnerability (Type I) discussed in Section 2.1.

Figure 2: An example of the vulnerability (Type II) discussed in Section 2.2 [10].

Figure 3: An example of the vulnerability (Type III) discussed in Section 2.3 [10].

(a)

(b)

Figure 4: An example of the program code with PI vulnerability [10]. (a) Vulnerable program. (b) Malicious program.

| communications among components, it is capable of pre- | from colluding cases and generates a large number of false |
| --- | --- |
| venting vulnerabilities. However, XManDroid has limita- | alarms. Tis method is more suited for monitoring a small |
| tions in distinguishing benign fow of ICC communication | number of applications installed on a device. |

---

## Page 5

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| Security and Communication Networks | 5 |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Te method presented in [8] is based on static analysis | application, a vulnerability is reported, and an alarm is |  |  |  |  |  |  |  |  |  |
| and | is | able | to | identify | only | one | type | of | PI-related | made if it is sent to a system component. PIAnalyzer is able |
| vulnerabilities. | to detect PI-related vulnerabilities with about 90% precision, |  |  |  |  |  |  |  |  |  |
| IntentDroid is another approach that can dynamically | but it has limitations in terms of application analysis speed. |  |  |  |  |  |  |  |  |  |
| analyze Android applications and detect PI-related vul- | We introduce a new PI-related vulnerability which is |  |  |  |  |  |  |  |  |  |
| nerabilities [9]. IntentDroid is only capable of detecting | detected by PIVAT in addition to the vulnerabilities pointed |  |  |  |  |  |  |  |  |  |
| vulnerabilities arising out of communications among Ac- | out in other methods. Furthermore, PIVAT is capable of |  |  |  |  |  |  |  |  |  |
| tivity components of the application and does not examine | detecting PI-related vulnerabilities with greater speed in |  |  |  |  |  |  |  |  |  |
| vulnerabilities related to communications among Service, | comparison of PIAnalyzer. |  |  |  |  |  |  |  |  |  |

Broadcast Receiver, and Content Provider components.

IccTA is an open-source tool for performing ICC-based 4. Type IV: A New PI-Related Vulnerability

taint analysis that can identify privacy data leakages by

| providing a control fow diagram through the application | A new vulnerability characterized as explicit PI wrapped in |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| code instrumentation technique [18]. IccTA is able to detect | the implicit Intent is introduced in this paper. |  |  |  |  |  |  |  |  |  |  |
| PI-related vulnerabilities [19]. | Vulnerability: Program X has permission to access the |  |  |  |  |  |  |  |  |  |  |
| PITracker is an automated analysis tool based on Intent | Internet and upload data. It creates a PI containing an |  |  |  |  |  |  |  |  |  |  |
| fow analysis [20]. Tis means that each PI object will analyze | explicit Intent to upload data to the Internet and sends it |  |  |  |  |  |  |  |  |  |  |
| an application to determine how it was created (origin) and | through an implicit Intent. When an implicit Intent con- |  |  |  |  |  |  |  |  |  |  |
| where | it | ultimately | goes | (target). | For | this | purpose, | it | taining a PI is processed, it is detected and received by |  |  |
| decompiles the APK fle and converts the DEX fle into an | a component based on the Intent flter. |  |  |  |  |  |  |  |  |  |  |
| intermediate SMALI code. By identifying PI methods in | Exploit: Abuse of this vulnerability can occur in two |  |  |  |  |  |  |  |  |  |  |
| SMALI code and backward slicing of previous statements on | scenarios. Te frst is similar to the vulnerability described in |  |  |  |  |  |  |  |  |  |  |
| method’s control fow graph (CFG), the information of base | Section 2.2, where the implicit Intent containing PI has |  |  |  |  |  |  |  |  |  |  |
| Intent is obtained. In the next step, the fourth parameter of | a standard action. In this case, the malicious Application Y, |  |  |  |  |  |  |  |  |  |  |
| the | creator | method | of | PI | is | checked. | If | it | is | FLA- | which has permission to access the contact information and |
| G_IMMUTABLE, it means that the malware cannot change | has declared in its Intent flter the action used in the implicit |  |  |  |  |  |  |  |  |  |  |
| the semantic of PI and this PI is secure. If the fourth pa- | Intent of Application X can receive an implicit Intent |  |  |  |  |  |  |  |  |  |  |
| rameter is not set, the permissions requested by that appli- | containing PI and extract the PI therein. Ten, it can add the |  |  |  |  |  |  |  |  |  |  |
| cation will be extracted. And in the next step, with forward | contact information in the extended data of base Intent, call |  |  |  |  |  |  |  |  |  |  |
| analysis, it fnds all statements that are the destination of PI. If | the Send PI method, and upload the data that it has added to |  |  |  |  |  |  |  |  |  |  |
| the destination of PI is an implicit Intent or a notifcation, and | the base Intent. As a result, Application Y, which does not |  |  |  |  |  |  |  |  |  |  |
| based on the delegated permissions, the tool gives that ap- | originally have permission to access the Internet and upload |  |  |  |  |  |  |  |  |  |  |
| plication a component hijacking or permission re-delegation | data, can receive the PI and thus inject the user’s private |  |  |  |  |  |  |  |  |  |  |
| label. Te authors reported that based on manual inspection | information into the creator application of PI and send it out |  |  |  |  |  |  |  |  |  |  |
| of the SMALI code of 50 randomly selected apps, PITracker | of the device. As a result, data injection and data leakage |  |  |  |  |  |  |  |  |  |  |
| detects PI vulnerability with a high precision [20]. | attacks occur. Te second scenario is when the implicit |  |  |  |  |  |  |  |  |  |  |
| In [21], a Soot-based tool is developed for detecting the | Intent containing the PI has a nonstandard action. In this |  |  |  |  |  |  |  |  |  |  |
| PI vulnerabilities. Like PITracker, they check the fourth | case, Application Y, which does not have permission to |  |  |  |  |  |  |  |  |  |  |
| parameter of creator of PI to detect potential vulnerabilities. | access contact information and whose developer is the |  |  |  |  |  |  |  |  |  |  |
| In this paper, the security implications of empty PI and | developer of Application X and which is the only application |  |  |  |  |  |  |  |  |  |  |
| Pending Intents with implicit base Intents are examined. Te | that recognizes the nonstandard action used in Application |  |  |  |  |  |  |  |  |  |  |
| detection process begins by converting the APK fles of the | X, can declare the same nonstandard action in its Intent flter |  |  |  |  |  |  |  |  |  |  |
| programs | into | Jimple | intermediate | code | and | detecting | and receive the PI. Next, it can add the contact information |  |  |  |  |
| methods that create PI without the FLAG_IMMUTABLE | in the extended data of the base Intent and call the Send PI |  |  |  |  |  |  |  |  |  |  |
| parameter. Tese methods are then analyzed to determine if | method. In this way, it can upload to the Internet the data |  |  |  |  |  |  |  |  |  |  |
| the base Intent is implicit or empty. If either condition is | that it has added to the base Intent. As a result, Application |  |  |  |  |  |  |  |  |  |  |
| met, it is reported as insecure. However, the analysis does | X, which does not originally have permission to access |  |  |  |  |  |  |  |  |  |  |
| not extend to examining the destination of the Intent, | contact information, can collude with Application Y to |  |  |  |  |  |  |  |  |  |  |
| resulting in an incomplete Intent fow analysis. | access this information and send it out of the device. As |  |  |  |  |  |  |  |  |  |  |
| PIAnalyzer is a static analysis tool designed to detect PI- | a result, a collusion attack occurs. Figure 5 is an example of |  |  |  |  |  |  |  |  |  |  |
| related vulnerabilities [10]. PIAnalyzer converts the byte- | this vulnerability and shows collusion between applications. |  |  |  |  |  |  |  |  |  |  |

code extracted from the APK fle into an intermediate

SMALI code using the ApkTool, which is a reverse engi- 5. The Proposed Method

neering tool. Te developers of PIAnalyzer have designed

| SMALI Slicer, which performs the main part of PIAnalyzer | Figure 6 shows an overview of the proposed method, which |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| analysis, in order to analyze the intermediate SMALI code. | is performed in three main analysis stages. In the frst stage, |  |  |  |  |  |  |  |  |  |
| PIAnalyzer returns a set of infuencing statements using | the PI in the application is identifed. To this end, the ap- |  |  |  |  |  |  |  |  |  |
| SMALI Slicer. After analysis of the statements, if the PI has | plication | manifest | fle | is | extracted | using | the | ApkTool. |  |  |
| an | implicit | base | Intent | and | is | sent | to | a | third-party | Component extraction in the method identifes components |

---

## Page 6

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

6 Security and Communication Networks

Figure 5: An example of the vulnerability (Type IV) discussed in Section 4 [10].

Android APP

6pkßool –oot

The proposed method

| Manifest | Jimple code |
| --- | --- |
| Component | Intra-proc. CFG |

PI extraction

| extraction | construction |
| --- | --- |
| Exported component | Units calling PI |

Target comp.

| Target | detection |
| --- | --- |
| component | CFG |
| Vulnerability | Potential vulnerable |
| analysis | target component |

Basic Intent

Basic Intent detection

Vulnerable PI

list

Figure 6: Overview of the proposed method.

| of the application that need to be analyzed based on the | In the last stage of analyzing and reporting vulnerabilities, |
| --- | --- |
| manifest. On the other hand, using the Soot tool, the Dalvik | if there is a possibility of PI vulnerability, the base Intent is |
| bytecodes are converted into the three-address Jimple code, | analyzed and the vulnerabilities, if there are any, are reported. |
| which is an intermediate code. In the PI extraction step, the | Te details of each stage are described below. |

PIs called in each component are extracted upon receiving

the Jimple code of the components extracted in the

| previous step. | 5.1. PI Detection. | Te Android application fle, APK, is |
| --- | --- | --- |
| In the second stage, PI analysis is performed to identify | reverse engineered using the ApkTool so that its manifest fle |  |
| the base Intent and the target component of the PI and to | is extracted. Te components of the application can be |  |
| determine its status. To this end, an intra-procedural CFG is | identifed and extracted using its manifest fle. To identify PI, |  |
| constructed to detect the basic blocks containing PI and its | the components of Activity, Broadcast Receiver, and Service |  |
| previous and next blocks that are in turn used to identify the | need to be analyzed. Terefore, PIVAT analyzes parts of |  |
| PI target components and the base Intent related with PI. | Jimple code that are related to the intended components. On |  |
| Te base Intent is detected only if the target components are | the Android platform, Java source codes are compiled into |  |
| likely to have vulnerabilities. | .class fles and then converted to .dex fles using “dx” tool. |  |

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

---

## Page 7

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| Security and Communication Networks | 7 |
| --- | --- |
| Tis .dex fle contains the Dalvik bytecode that is run on the | an implicit Intent as extra data, a vulnerability is probable. |
| Dalvik virtual machine. PIVAT converts the Dalvik bytec- | Terefore, the base Intent should be analyzed for detecting |
| odes into intermediate Jimple code using Soot tool. Te | and reporting vulnerabilities. |
| intermediate Jimple code is a three-address code of bytecode | For base Intent analysis, the variables that contain the |
| that improves the static analysis capability of Android ap- | base Intent are frst identifed. Ten, the instructions of the |
| plications. An example of Java code and its translation into | basic block containing the PI caller that are placed before the |
| the intermediate Jimple code using Soot is shown in Figure 7. | PI-calling instructions are analyzed to identify the base |
| Chain is a collection data structure that provides fxed-time | Intent type. If the instructions under analysis call the base |
| access to its elements. Tere are three types of chains in the | Intent constructor method and explicitly state the target |
| body of Jimple code: Chain of Locals, Chain of Units, and | component in the constructor method parameter, the base |
| Chain of Traps. In Chain of Locals, there are variables in the | Intent constructor is explicit. If the analyzed instructions call |
| application that either accept a value in an instruction | one of the fve methods, i.e., setClassName (), setClass (), |
| (Defnition) or their values are used in an instruction (Use). | setComponent (), setPackage (), and setSelector (), the base |
| As shown in Figure 7, Chain of Locals is defned at the top of | Intent is considered as explicit; otherwise, it is implicit. If the |
| the method along with the types of value they accept. Te | base Intent type is not specifed in the basic block containing |
| Chain of Units contains the main instructions of the ap- | the PI-calling instruction, the instructions in the predecessor |
| plication and the Chain of Traps includes the exceptions of | basic blocks are also analyzed. |

the program.

To identify the variables of type PI in the Jimple code, the

| local chain section is examined and the variables of type PI | 5.3. Analysis and Report of Vulnerabilities. | According to the |
| --- | --- | --- |
| are identifed. Ten, using the Chain of Units, the instruction | classifcation presented in Figure 8 and PI-related vulner- |  |
| where the PI variables specifed in the previous step are | abilities in Sections 2 and 4 of this paper, when the PI is sent |  |
| defned (i.e., assign values) is found. If these instructions call | to a system component (target component) and its base |  |
| one of the four methods of getActivity (), getActivities (), | intent is implicit, Type I vulnerability discussed in Section |  |
| getBroadcast (), and getService (), these instructions are | 2.1 is reported. On the other hand, when the PI has been |  |
| designated as PI callers and the analysis will continue based | placed inside another implicit Intent as extra data and the |  |
| on such instructions. Terefore, the output of this stage is | base Intent is implicit, Type II vulnerability described in |  |
| a list of instructions that defne the variables of type PI and | Section 2.2 is reported. However, if the base Intent is implicit |  |
| call one of the four methods mentioned above. | with no action, Type III vulnerability described in Section 2.3 |  |

is reported. When the PI is placed as extra data inside

another implicit Intent that has no standard action and the

5.2. PI Analysis. As stated in Section 2, PI may have vul- base Intent is explicit, Type IV vulnerability discussed in

nerabilities depending on the type of base Intent and the Section 4 is reported.

target component of PI. Terefore, the base Intent as well as

the target component must be identifed and analyzed. To this 6. Evaluation and Results

end, it is necessary to specify the data and control de-

| pendencies of the instructions that defne the values of the PI | In this section, PIVAT is compared to PIAnalyzer, an open- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| variables and the instruction that use them. To fnd these | source tool for PI-related vulnerability analysis. To better |  |  |  |  |  |  |  |
| control dependencies, an intra-procedural CFG is used and | compare and evaluate the results, both methods are frst |  |  |  |  |  |  |  |
| then the data dependencies are analyzed by traversing the | converted to intermediate Jimple code using Soot tool and |  |  |  |  |  |  |  |
| graph. Terefore, it is necessary to construct a CFG for the | then | the | algorithm | associated | with | each | approach | is |

2

| methods containing the instructions of the previous stage. For | implemented [11] | . Ten, the execution time and efcacy of |
| --- | --- | --- |
| this purpose, the method code containing the instructions is | both tools are evaluated by running them on 51 benchmark |  |
| analyzed and its CFG is constructed via identifying its basic | applications; 50 benchmark applications are randomly se- |  |
| blocks. Terefore, the basic block containing the PI-calling | lected from Google Play and one benchmark application |  |
| instructions and the predecessor and successor blocks of this | containing four types of vulnerabilities is developed by the |  |
| block will be available based on the CFG. | authors of the paper. All evaluations in this section are |  |
| Traversing predecessor and successor basic blocks of the | performed on a system with an Intel Core i3-3120M pro- |  |
| PI-calling instructions can help fnd the block containing the | cessor with 4 GB of RAM and Windows 10 OS. |  |
| base Intent and the target component of the PI, which can be | Te authors employed manual inspection to evaluate the |  |
| analyzed to determine whether the PI has been used securely | precision of PI vulnerability detection tools [10, 20]. Tis |  |
| or not. First, the target component is analyzed, and if it is | method requires a signifcant amount of time and efort, as it |  |
| likely to be vulnerable, the base Intent is analyzed. Te target | necessitates the analysis of many source or intermediate |  |
| component is the component to which the PI-containing | code fles. In a manual inspection of ten applications, |  |
| variable is sent. To this end, the blocks succeeding the block | PIAnalyzer accurately identifed vulnerabilities in nine in- |  |
| that contains PI-calling instructions are analyzed. If the | stances [10]. To evaluate precision, PIVAT is compared with |  |
| variables used in these instructions contain PI variables, they | PIAnalyzer. For the vulnerabilities of Types I, II, and III, |  |
| are considered as the target component. If the instructions | PIVAT successfully detected all vulnerabilities identifed by |  |
| send the PI variable to a system component or place it inside | PIAnalyzer, indicating that its precision is comparable to |  |

---

## Page 8

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

8 Security and Communication Networks

focal1

8hain

´nit1

8hain

Nimpliocation

ßraps1

8hain

Figure 7: An example of the intermediate Jimple code.

Xase1Vntent1is ßype1V

–ystem1component

| implicit | vulnerability |
| --- | --- |
| Xase1Vntent1is | ßype1VV |
| implicit | vulnerability |
| ßarget1component | Vmplicit1Vntent |
| Xase1Vntent1is | ßype1VVV |
| implicit1without | vulnerability |

action

Vmplicit1Vntent1with

Xase1Vntent1is ßype1VZ

nonstandard

explict vulnerability

action

Figure 8: Classifcation of PI vulnerability analysis based on target component and base Intent.

| that of PIAnalyzer at approximately 90%. But PIAnalyzer | All 51 benchmark applications are listed in Table 2 with |
| --- | --- |
| cannot detect Type IV vulnerability that is detected by | application size and execution time of analysis for each tool |
| PIVAT. Also, PITracker and others tools and approaches | and its category. Each application analyzed can be in one of |
| cannot detect Type IV vulnerability. | the following categories: |

Table 2 shows the results of comparing the execution

1. (A) Te application does not contain any PI.

time of the above tools in detection of PI-related vulnera-

bility, and Figure 9 shows the graphs related to evaluation 2. (B) Te application contains one or more

results. vulnerable PIs.

*[Image: Page 8 Image]*

*[Image: Page 8 Image]*

*[Image: Page 8 Image]*

*[Image: Page 8 Image]*

*[Image: Page 8 Image]*

---

## Page 9

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Security and Communication Networks 9

Table 2: Execution time results for running tools on benchmark applications.

| Execution time of | Execution time of |  |  |  |
| --- | --- | --- | --- | --- |
| Program | Size (MB) | Category |  |  |
| PIAnalyzer (s) | PIVAT (s) |  |  |  |
| P1 | 1.25 | 2.08 | 1.86 | (A) |
| P2 | 0.181 | 2.59 | 1.89 | (A) |
| P3 | 2.09 | 3.79 | 2.74 | (A) |
| P4 | 0.182 | 2.60 | 2.01 | (A) |
| P5 | 2.72 | 2.87 | 2.96 | (A) |
| P6 | 2.33 | 5.63 | 5.08 | (B) |
| P7 | 1.3 | 3.30 | 2.92 | (A) |
| P8 | 9.46 | 14.0 | 12.72 | (B) |
| P9 | 0.05 | 3.16 | 2.73 | (B) |
| P10 | 15.7 | 7.70 | 5.0 | (A) |
| P11 | 4.72 | 7.57 | 4.14 | (A) |
| P12 | 24 | 4.40 | 2.12 | (A) |
| P13 | 13 | 1.96 | 1.66 | (A) |
| P14 | 7.08 | 14.30 | 6.03 | (A) |
| P15 | 15.2 | 6.25 | 3.98 | (A) |
| P16 | 2.48 | 2.51 | 1.64 | (A) |
| P17 | 5.42 | 6.39 | 5.62 | (A) |
| P18 | 5.58 | 5.64 | 5.25 | (A) |
| P19 | 16.9 | 6.23 | 3.24 | (A) |
| P20 | 1.25 | 5.01 | 4.26 | (A) |
| P21 | 6.57 | 14.56 | 11.15 | (B) |
| P22 | 5.73 | 10.23 | 11.18 | (C) |
| P23 | 11.6 | 3.13 | 2.68 | (B) |
| P24 | 14.3 | 10.68 | 8.79 | (A) |
| P25 | 10.6 | 4.472 | 2.32 | (A) |
| P26 | 23.6 | 4.92 | 2.37 | (A) |
| P27 | 7.11 | 5.33 | 2.43 | (A) |
| P28 | 16 | 15.74 | 8.60 | (A) |
| P29 | 6.8 | 8.34 | 4.96 | (A) |
| P30 | 9.11 | 4.25 | 3.28 | (A) |
| P31 | 61.5 | 5.28 | 4.64 | (A) |
| P32 | 20.4 | 10.11 | 3.05 | (A) |
| P33 | 27.2 | 9.20 | 2.47 | (A) |
| P34 | 3.17 | 3.57 | 3.14 | (A) |
| P35 | 12.4 | 3.87 | 2.41 | (A) |
| P36 | 14.3 | 6.33 | 3.67 | (A) |
| P37 | 3.18 | 5.94 | 2.69 | (A) |
| P38 | 16.2 | 12.86 | 9.92 | (A) |
| P39 | 14.5 | 8.78 | 4.30 | (A) |
| P40 | 15.6 | 3.50 | 4.25 | (C) |
| P41 | 25.3 | 7.75 | 3.24 | (A) |
| P42 | 11.8 | 3.12 | 2.92 | (A) |
| P43 | 18.9 | 6.62 | 2.79 | (A) |
| P44 | 9.50 | 4.12 | 4.02 | (A) |
| P45 | 9.72 | 9.23 | 9.13 | (A) |
| P46 | 15.2 | 3.77 | 3.29 | (A) |
| P47 | 3.5 | 5.39 | 2.91 | (A) |
| P48 | 6.07 | 8.18 | 8.39 | (C) |
| P49 | 4.55 | 6.59 | 3.02 | (A) |
| P50 | 2.94 | 3.91 | 3.32 | (A) |
| P51 | 6.08 | 8.56 | 6.89 | (A) |

Abbreviations: MB, megabyte; s, second.

---

## Page 10

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

10 Security and Communication Networks

)%

)5

)H

)P

)I

%

5

Txecution1time1zsecondsT

H

P

I

J) JP Jf JH JF J5 J7 J% JO J)I J)) J)P J)f J)H J)F J)5 J)7 J)% J)O JPI JP) JPP JPf JPH JPF JP5 JP7 JP% JPO JfI Jf) JfP Jff JfH JfF Jf5 Jf7 Jf% JfO JHI JH) JHP JHf JHH JHF JH5 JH7 JH% JHO JFI JF)

Xenchmark1application

JV6nalyzer

JVZ6ß

Figure 9: Comparison of execution time for the two methods.

)

3. (C) Te application contains PIs which are IfO

nonvulnerable. If%

If7

In (A), PIVATdetects the absence of PI faster because it only

If5

| searches for local variables in each method. However, it takes | IfF |
| --- | --- |
| longer for PIAnalyzer to detect the lack of PI in the application | 89“ |

IfH

| because it searches all the instructions in the application code. | Iff |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Terefore, in (1), PIVAT performs a faster analysis. | IfP |  |  |  |  |  |  |  |  |
| In (B), PIVAT detects PI-related vulnerabilities faster | If) |  |  |  |  |  |  |  |  |
| because it only analyzes basic blocks that may contain the PI | I |  |  |  |  |  |  |  |  |
| I | P | H | 5 | % | )I | )P | )H | )5 | )% |

target component and its base Intent and does not analyze all

Txecution1time1zsecondT

instructions of the application.

| In (C), the application contains an explicit PI and sends | JVZ6ß |  |
| --- | --- | --- |
| it to a system component. In this case, the PIAnalyzer detects | JV6nalyzer |  |
| the absence of PI-related vulnerabilities earlier because it | Figure | 10: CDF plot of execution time for the two methods. |

frst analyzes the base Intent type and does not continue the

analysis if it detects that the base Intent is explicit. However,

PIVAT frst analyzes the PI target component and then 7. Conclusion

analyzes the base Intent type in the next step, and therefore it

| takes longer for it to realize that the PI is not vulnerable. | Secure use of PIs in Android application development can |
| --- | --- |
| Te results in Table 2 and Figure 9 show that PIVAT | reduce vulnerabilities in Android applications and prevent |
| performed better than PIAnalyzer in 95% of cases, and just | various attacks such as denial of service, data leakage, and |
| in 5% of cases, PIAnalyzer performed faster than PIVAT | privilege escalation. In this paper, a new PI-related vul- |
| with a time diference which is not signifcant. | nerability is introduced. Te PI can be vulnerable if an |
| Te results of the evaluations show that PIVAT is highly | explicit base Intent is wrapped in the implicit Intent with |
| precise and about 27% faster than PIAnalyzer in terms of | nonstandard action. Te proposed method is presented for |
| application analysis speed. | detecting PI-related vulnerabilities in a shorter time. For this |
| In Figure 10, we present cumulative distribution func- | purpose, the Android application code is converted to the |
| tion (CDF) plot of the execution time for our tool, PIVAT, | intermediate Jimple code and PIs are extracted from its |
| and PIAnalyzer to analyze each application. We can see that | components. Ten, vulnerabilities are analyzed and reported |
| more than 50% applications can be analyzed by PIVAT in | in the proposed method using the status of the base Intent |
| less than 4.5 s each, while PIAnalyzer can analyze less than | and the target component. To identify the base Intent and |
| 30% of the applications in this time. | the target component, data fow analysis is performed on an |

---

## Page 11

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| Security and Communication Networks | 11 |  |
| --- | --- | --- |
| intra-procedural CFG for methods containing PI caller. To | Software Engineering and Systems | (Florence, Italy, February |
| evaluate the proposed method, it is implemented besides | 2015), 113–116. |  |
| PIAnalyzer and the analysis is performed on 51 benchmark | [5] A. Sadeghi, R. Jabbarvand, N. Ghorbani, H. Bagheri, and |  |
| applications. Te results show that the proposed method | S. Malek, “A Temporal Permission Analysis and Enforcement |  |
| detects Type IV vulnerability that is not detected by PIA- | Framework for Android,” in | Proceedings of the 40th In- |

ternational Conference on Software Engineering (Gothenburg,

nalyzer. In addition, the proposed method is 27% faster than

Sweden, March 2018), 846–857.

PIAnalyzer in terms of application analysis speed. Further

[6] S. Dhavale and B. Lokhande, “Comnoid: Information Leakage

research can focus on increasing the precision of the pro-

Detection Using Data Flow Analysis on Android Devices,”

posed method and evaluating the proposed method with International Journal of Computer Application 134, no. 7

more benchmark applications. (2016): 15–20, https://doi.org/10.5120/ijca2016907855.

[7] S. Bugiel, L. Davi, A. Dmitrienko, T. Fischer, and

Nomenclature A.-R. Sadeghi, “Xmandroid: A New Android Evolution to

Mitigate Privilege Escalation Attacks,” Technische Universit¨ at

| APK: | Android application package | Darmstadt, Technical Report TR-2011-04 | (2011). |
| --- | --- | --- | --- |
| CDF: | Cumulative distribution function | [8] P. Gadient, M. Ghafari, P. Frischknecht, and O. Nierstrasz, |  |
| CFG: | Control fow graph | “Security Code Smells in Android ICC,” | Empirical Software |
| ICC: | Inter-component communication | Engineering | 24, no. 5 (2019): 3046–3076, https://doi.org/ |
| PI: | PendingIntent | 10.1007/s10664-018-9673-y. |  |

[9] R. Hay, O. Tripp, and M. Pistoia, “Dynamic Detection of

PIVAT: PendingIntent Vulnerability Analysis Tool.

Inter-Application Communication Vulnerabilities in An-

droid,” in Proceedings of the 2015 International Symposium on

Data Availability Statement Software Testing and Analysis (Baltimore, MD, July 2015),

118–128.

| Te data consist of benchmark programs available as APK | [10] S. Groß, A. Tiwari, and C. P. Hammer, “Pianalyzer: A Precise |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| fles through public app marketplaces. While we cannot | Approach | for | Pendingintent | Vulnerability | Analysis,” | in |
| distribute the data separately due to legal restrictions, a list of | Computer Security: 23rd European Symposium on Research in |  |  |  |  |  |
| the programs can be provided upon request. | Computer Security, ESORICS2018 | (Barcelona, Spain, Sep- |  |  |  |  |

tember 3-7, 2018), 41–59.

[11] A. Sarvazimi and M. Sakhaei-Nia, “PIVATool- a Fast and

Conflicts of Interest

Precise Tool for Analysis and Detection of PendingIntent

Te authors declare no conficts of interest. Vulnerabilities,” Electronic and Cyber Defense 9 (2021): 75–83.

[12] B. Rashidi and C. J. Fung, “A Survey of Android Security

Treats and Defenses,” Journal of Wireless Mobile Networks

Funding Ubiquitous Computing Dependable Application 6 (2015):

3–35.

Tis research did not receive any specifc grant from funding

[13] J. A. Shaheen, M. A. Asghar, and A. Hussain, “Android OS

agencies in the public, commercial, or not-for-proft sectors. with its Architecture and Android Application With Dalvik

Virtual Machine Review,” International Journal of Multime-

Endnotes dia and Ubiquitous Engineering 12, no. 7 (2017): 19–30,

https://doi.org/10.14257/ijmue.2017.12.7.03.

1

PIVAT: PendingIntent Vulnerability Analysis Tool. [14] E. Chin, A. P. Felt, K. Greenwood, and D. Wagner, “Analyzing

2

https://github.com/msniea/PIVATool. Inter-Application Communication in Android,” in Pro-

ceedings of the 9th International Conference on Mobile Sys-

tems, Applications, and Services (Bethesda, MD, June 2011),

References

239–252.

| [1] Statcounter, | in | Mobile | Operating | System | Market | Share | [15] P. Bhiwani and C. Parekh, “Diferent Android Vulnerabil- |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Worldwide | (2021), | https://gs.statcounter.com/os-market- | ities,” | Advances in Computational Sciences and Technology | 10 |  |  |
| share/mobile/worldwide/2021. | (2017): 1449–1455. |  |  |  |  |  |  |
| [2] S. Rani and K. S. Dhindsa, “Android Malware Detection in | [16] Pendingintent, | Te code samples, guides, and API reference |  |  |  |  |  |
| Ofcial and Tird Party Application Stores,” | International | (2013): | https://developer.android.com/reference/android/ |  |  |  |  |
| Journal of Advanced Networking and Applications | 9 (2018): | app/PendingIntent. |  |  |  |  |  |
| 3506–3509. | [17] J. Mitra and V. P. G. Ranganath, “A Repository of Android |  |  |  |  |  |  |
| [3] J. Senanayake, H. Kalutarage, M. O. AL-Kadri, A. Petrovski, | App Vulnerability Benchmarks,” in | Proceedings of the 13th |  |  |  |  |  |
| and L. Piras, “Android Source Code Vulnerability Detection: | International | Conference | on | Predictive | Models | and | Data |
| A Systematic Literature Review,” | ACM Computing Surveys | 55, | Analytics in Software Engineering | (January 2017), 43–52. |  |  |  |
| no. 9 (2023): 1–37, https://doi.org/10.1145/3556974. | [18] L. Li, A. Bartel, T. F. Bissyand´ | e, et al., “IccTA: Detecting Inter- |  |  |  |  |  |
| [4] A. K. Jha, S. Lee, and W. J. Lee, “Modeling and Test Case | Component Privacy Leaks in Android Apps,” in | 2015 IEEE/ |  |  |  |  |  |
| Generation | of | Inter-Component | Communication | in | An- | ACM 37th IEEE International Conference on Software Engi- |  |
| droid,” in | 2015 2nd ACM International Conference on Mobile | neering | (Florence, Italy, March 2015), 280–291. |  |  |  |  |

---

## Page 12

2037, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2024/8663701 by National Central University, Wiley Online Library on [26/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

12 Security and Communication Networks

[19] S. Bhandari, W. B. Jaballah, V. Jain, et al., “Android App

Collusion Treat and Mitigation Techniques,” (2016), https://

arxiv.org/abs/1611.10076.

[20] C. Zhang, S. Li, W. Diao, and S. Guo, “PITracker: Detecting

Android Pendingintent Vulnerabilities Trough Intent Flow

Analysis,” in Proceedings of the 15th ACM Conference on

Security and Privacy in Wireless and Mobile Networks (April

2022), 20–25.

[21] H. En, C. Wenbo, and D. Wu, “Re-Route Your Intent for

Privilege Escalation: A Universal Way to Exploit Android

PendingIntents in High-Profle and System Apps,” in Black

Hat Conference, Europe (London, UK, 2021).

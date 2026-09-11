---
title: "From code to security: machine learning approaches in android vulnerability detection"
author: "Kaya Emre Arikan "
creator: "Springer"
pages: 30
---

# From code to security: machine learning approaches in android vulnerability detection

> **作者**：Kaya Emre Arikan 
> **總頁數**：30 頁

---

## Page 1

International Journal of Information Security (2026) 25:17

https://doi.org/10.1007/s10207-025-01190-1

R E G U L A R C O N T R I B U T I O N

vulnerability detection

Kaya Emre Arikan 1 · Sait Melih Do ˘ gan 1 · Ercan Nurcan Yilmaz

Received: 2 April 2025 / Accepted: 8 December 2025 / Published online: 27 December 2025

© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2025

Abstract

vulnerability detection.

kayaemrearikan@gmail.com

06560, Turkey

of Technology, Gazi University, Ankara 06560, Turkey

and Architecture, Istanbul Gelisim University, Istanbul,

Turkey

2 · Serkan Gönen 3

photography and videography. Biometrics, such as facial

systems and a thriving app ecosystem have revolutionized

Software systems in domains face numerous vulnerabili-

itory [3]. In each of the 5 years, an average of over 17,000

represents a doubling of the vulnerability count compared to

123

From code to security: machine learning approaches in android

In today’s technology-driven society, an increasing number of individuals rely on mobile devices, leading to a surge in

the availability of applications. Smartphone users constantly search for apps that meet their needs, resulting in a flood of

options in the marketplace. However, there is a growing concern regarding the security of Android applications, as many

have shortcomings in addressing critical security aspects. One reason behind this issue often lies in the lack of automated

mechanisms during the design and development stages to identify, test, and rectify vulnerabilities in the source code. It

is crucial to address these issues proactively rather than relying solely on updates and patches for already published apps.

In response to this challenge, researchers have proposed machine learning techniques to enhance application security by

detecting vulnerabilities and malicious code within source code. This systematic literature review delves into this domain by

examining 85 carefully selected technical studies published between 2017 and 2024. It aims to shed light on the strengths,

weaknesses, and practical applicability of these techniques, while also identifying areas for further improvement. Moreover,

the growing focus on advanced approaches—such as Large Language Models (LLMs) and Explainable AI (XAI)—indicates

a trend toward more transparent and context-aware vulnerability detection. By synthesizing key insights from the current

literature, this review enhances our understanding of Android security approaches, identifies promising directions for future

research, and ultimately contributes to the advancement of more secure mobile applications through machine learning-based

Keywords Vulnerability analysis · Machine learning · Mobile security · Intrusion detection · Vulnerability detection

| 1 Introduction | image processing capabilities have significantly enhanced |  |
| --- | --- | --- |
| Technological advancements in mobile devices have been | recognition and fingerprint sensors, offer secure and conve- |  |
| remarkable, with the introduction of foldable displays offer- | nient device unlocking. Powerful processors, AI integration, |  |
| ing more screen space in a portable form factor. 5G connec- | and longer-lasting batteries have enhanced overall perfor- |  |
| tivity has brought faster speeds and low latency, enhancing | mance and user experience. Augmented and virtual reality |  |
| internet experiences and enabling real-time applications [1]. | technologies [2] have bridged the gap between the physi- |  |
| Advanced camera systems equipped with multiple lenses and | cal and virtual worlds. At the same time, mobile payment |  |
| B | Kaya Emre Arikan | transactions and user functionalities. |
| 1 | Department of Information Security Engineering, Graduate | ties due to their accompanying source code. As of July 2023, |
| School of Natural and Applied Sciences, Gazi University, | there are over 192,000 recorded instances of vulnerabilities |  |
| Tunahan, Dumlupinar 30 Agustos Street, No:2 D8, Ankara | in the Common Vulnerabilities and Exposures (CVE) repos- |  |
| 2 | Department of Electrical and Electronics Engineering, Faculty | manifestations of vulnerabilities have been identified, which |
| 3 | Department of Software Engineering, Faculty of Engineering | a decade ago. These vulnerabilities are caused by factors |

---

## Page 2

| 17 | Page 2 of 30 | K. E. Arikan et al. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| related to the source code itself, including reuses, imple- | engagement. Moreover, the integration of 5G networks has |  |  |  |  |  |  |  |
| mentation, dependencies, changes, and mistakes made by | further accelerated this transition by offering connectivity. |  |  |  |  |  |  |  |
| developers [4–6]. Additionally, online question-and-answer | It has also opened up experiences such as augmented real- |  |  |  |  |  |  |  |
| forums like Stack Overflow can unintentionally introduce | ity, smart devices powered by the Internet of Things (IoT), |  |  |  |  |  |  |  |
| software vulnerabilities when users unknowingly replicate | and hassle-free mobile payments [15]. As this shift towards |  |  |  |  |  |  |  |
| responses as code snippets [7–9]. | mobility continues, it shapes our future by driving innovation |  |  |  |  |  |  |  |
| Mitigation of software vulnerabilities typically entails | and paving the way for a world centered around movement. |  |  |  |  |  |  |  |
| either preemptive or retrospective scrutiny through code | Cybersecurity encompasses a combination of technolo- |  |  |  |  |  |  |  |
| reviews | conducted | by | the | original | developers | or | other | gies and methods carefully designed to protect information, |
| members within a collaborative development environment, | software applications, computer systems, and interconnected |  |  |  |  |  |  |  |
| whether it is a team or a broader community context [10]. | networks from infiltrations, adversities, or unauthorized |  |  |  |  |  |  |  |
| Nevertheless, it is plausible that vulnerabilities could per- | access [16]. Machine Learning (ML) paradigms have proven |  |  |  |  |  |  |  |
| sist across temporal intervals, whether acknowledged or not | highly effective in cybersecurity. In this context, ML appli- |  |  |  |  |  |  |  |
| [11]. While code reviews serve as a valuable mechanism, | cations become crucial because they can analyze datasets |  |  |  |  |  |  |  |
| their undertaking can entail substantial temporal and finan- | with the help of advanced hardware resources and improved |  |  |  |  |  |  |  |
| cial investments for developers, necessitating the exploration | algorithms [17]. In particular, ML has three dimensions: the |  |  |  |  |  |  |  |
| of potential avenues of exploitation and the identification of | reasons behind its deployment (the “why” aspect), the objec- |  |  |  |  |  |  |  |
| commensurate remedial measures. In extensive code bases, | tives it serves (the “what” aspect), and the methods it employs |  |  |  |  |  |  |  |
| the exhaustive examination and rectification of every source | to conduct security assessments (the “how” aspect). |  |  |  |  |  |  |  |
| code file associated with a vulnerability may prove imprac- | The initial dimension, addressing the “why,” pertains to |  |  |  |  |  |  |  |
| ticable [12]. | elucidating the motives behind the execution of cybersecurity |  |  |  |  |  |  |  |
| Researchers | have | enhanced | conventional | analytical | undertakings. Adhering to the taxonomy posited by the Gart- |  |  |  |
| approaches by incorporating machine learning methodolo- | ner model, these rationales are categorized into five classes: |  |  |  |  |  |  |  |
| gies, thereby augmenting the efficacy of software vulnera- | Prediction, Prevention, Detection, Response, and Monitoring |  |  |  |  |  |  |  |
| bility identification. Nonetheless, a recent investigation of | [18]. |  |  |  |  |  |  |  |
| the pervasiveness of security vulnerabilities inherent in code | The second dimension, encapsulating the “what,” delves |  |  |  |  |  |  |  |
| snippets, as manifested within the collaborative question- | into the technical strata subject to vigilant scrutiny. Hierarchi- |  |  |  |  |  |  |  |
| and-answer platform Stack Overflow, has ascertained that | cally organized layers within this dimension encompass the |  |  |  |  |  |  |  |
| a substantial 36% of the entirety of Common Weakness Enu- | network, endpoint, application, user, and process domains. |  |  |  |  |  |  |  |
| meration (CWE) vulnerability classifications were discerned | The third dimension, encompassing the “how,” delineates |  |  |  |  |  |  |  |
| among an aggregate of over 600,000 instances of C/C++ code | the modalities by which security mechanisms are scrutinized. |  |  |  |  |  |  |  |
| snippets. Remedial amendments aimed at alleviating these | This examination may be rendered historically, during the |  |  |  |  |  |  |  |
| vulnerabilities were proffered for the code snippet responses, | quiescent state, or in real-time transit. A comprehensive con- |  |  |  |  |  |  |  |
| yet only half of these recommendations were integrated into | solidation of these facets is succinctly presented in Table 1, |  |  |  |  |  |  |  |
| practice [9]. | summarizing the information. |  |  |  |  |  |  |  |
| Android is a target for security breaches because it is | Furthermore, integrating technology with the IoT has led |  |  |  |  |  |  |  |
| incredibly popular and widely used on devices such as desk- | to advancements like smart homes and cities that optimize |  |  |  |  |  |  |  |
| tops and laptops. Cybercriminals are particularly interested in | resource management efforts while promoting sustainabil- |  |  |  |  |  |  |  |
| exploiting apps and devices to access sensitive information, | ity. Beyond this scope, mobility has revolutionized health- |  |  |  |  |  |  |  |
| use the device’s processing power, collect data through sen- | care, education, and agriculture industries by facilitating |  |  |  |  |  |  |  |
| sors, and exploit network connections. Over the past decade, | telemedicine services, remote learning opportunities, and |  |  |  |  |  |  |  |
| the number of vulnerabilities discovered in the Android oper- | precision farming techniques [20]. Lastly, mobile commu- |  |  |  |  |  |  |  |
| ating system has significantly increased, with 6251 reported | nication platforms and social media have effectively bridged |  |  |  |  |  |  |  |
| incidents as shown in Fig. 1 [13]. | geographical distances, fostering interconnectedness among |  |  |  |  |  |  |  |
| A shift towards mobility has brought significant changes | communities worldwide. Overall, it is undeniable that the |  |  |  |  |  |  |  |
| to various industries and our everyday lives. Thanks to | shift toward mobility has fueled innovation, driven growth, |  |  |  |  |  |  |  |
| advancements, we are experiencing a connected, flexible, | and advanced societal progress, thereby establishing itself as |  |  |  |  |  |  |  |
| and efficient world. The widespread use of smartphones | an integral part of modern life. |  |  |  |  |  |  |  |
| and tablets has empowered individuals to stay connected | While organizations often prioritize securing their net- |  |  |  |  |  |  |  |
| while accessing information, communication channels, and | works, endpoints, and critical data, they may unintentionally |  |  |  |  |  |  |  |
| services from anywhere [14]. This growing trend towards | overlook aspects that can leave vulnerabilities. These over- |  |  |  |  |  |  |  |
| mobility has led businesses to prioritize interfaces and | looked components could include systems, outdated devices, |  |  |  |  |  |  |  |
| applications as part of their strategies for increasing user | or frequently used applications that might not receive regular |  |  |  |  |  |  |  |

123

---

## Page 3

From code to security: machine learning approaches in android … Page 3 of 30 17

Fig. 1 Android vulnerability trends between the years 2014 and 2023

Protection layer Task (Why?) Role of ML

Detection of

varied network

attacks

Categorizing

programs into

malware,

spyware, adware,

etc

requests,

Detection of

known attacks

User behavior Detection, Anomaly detection

Prevention, and in User actions,

analysis based

on different users

Process behavior Prediction and Prediction of the

Detection of

known fraud

grations and supply chain security might be disregarded,

tify and address these overlooked components to ensure

In this paper, we focus on studies using ML and DL tech-

niques in the vulnerability analysis of applications on the

detection [21]. Consequently, a comprehensive understand-

ing of the ML processes becomes imperative for thoroughly

comprehending ML-based studies focusing on source code

vulnerability detection. The ML lifecycle includes several

This review contributes to the field in the following ways:

endeavors in the vulnerability analysis of Android Appli-

cations, focusing on the application of machine learning

techniques.

ability researchers, focusing solely on vulnerability detection

methods that utilize machine learning. Unlike previous

123

| Table 1 | ML dimensions in cyber security areas [19] | security updates or patches. Moreover, third-party inte- |  |
| --- | --- | --- | --- |
| (What?) | (How?) | creating entry points for attackers. Organizations must iden- |  |
| Network (SCADA | Prediction and | Prediction of | cybersecurity by implementing security measures, regular |
| systems, Ethernet, | Detection | network packet | updates, and ongoing monitoring to mitigate potential risks |
| Virtual networks) | parameters, | and establish a robust and comprehensive security strategy. |  |
| Endpoint (IoT device, | Prediction and | Prediction of the | Android operating system. In recent years, there has been a |
| Mobile, Server) | Detection | next system call, | notable increase in the use of ML methods for vulnerability |
| Application security | Detection and | Anomaly detection | essential steps: data extraction, preprocessing, feature selec- |
| Prevention | in HTTP | tion, model training, evaluation, and deployment [22]. |  |
| Monitoring | Peer-group | It provides a comprehensive overview of prior research |  |
| Detection | next user action, | This study presents a systematic literature review for vulner- |  |

*[Image: Page 3 Image]*

---

## Page 4

| 17 | Page 4 of 30 | K. E. Arikan et al. |
| --- | --- | --- |
| studies, which mainly emphasized malware detection, this | validity of our findings and facilitates critical peer assess- |  |
| research stands out as unique. | ment. Below, we outline our systematic review protocol, |  |
| From 2017 to 2024, we examined research on the topic, high- | which includes the search strategy, selection criteria, and |  |
| lighting challenges and open issues to provide insights into | analysis methods employed. |  |

addressing problems within the Android application vulner-

It offers insights into their detection accuracy and effective-

that require the attention and investigation of researchers.

Additionally, it discusses future research directions based on

recent innovative techniques such as Explainable AI (XAI),

Large Language Models, and context-aware models.

Recognizing and identifying open issues and challenges in

the design of ML/DL-based vulnerability detection mech-

anisms around Android applications, aiming to provide

direction for future research efforts.

Unless explicitly specified otherwise, the term “ML tech-

term encompassing both ML and DL techniques and mod-

The subsequent sections of this paper are organized as

the background, terms and definitions, and relevant liter-

tered in the current state of research in the field. Section 7

addresses the threats to the validity of the review. Finally,

and final remarks from the study, and the last section out-

and reproducibility of our literature review, we adopted the

PRISMA (Preferred Reporting Items for Systematic Reviews

and Meta-Analyses) framework [23]. This framework is

123

databases included:

IEEE Xplore: A premier repository for computer science and

engineering literature

ACM Digital Library: Essential for accessing high-impact

computing research

ScienceDirect: Offering extensive interdisciplinary scientific

publications

SpringerLink: Provides access to journals with robust peer-

review processes

and citation metrics

database

sensitivity and specificity.

ity of our corpus, we developed comprehensive selection

criteria through collaborative deliberation among research

ria throughout our screening procedure to mitigate selection

2.3 Inclusion criteria

| ability detection around ML techniques. | 2.1 Databases and search terms |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ness in identifying vulnerabilities. | Our | review | systematically | explored | several | reputable |
| It gathers and presents valuable resources, including avail- | databases to ensure comprehensive coverage and address the |  |  |  |  |  |
| able datasets, relevant to conducting future studies in this | epistemological gaps in the research domain. The rigorous |  |  |  |  |  |
| area. | selection of multiple databases allowed for the triangula- |  |  |  |  |  |
| It synthesizes and summarizes the existing open challenges | tion of findings and minimized potential selection bias. The |  |  |  |  |  |
| niques” is employed throughout this paper as an umbrella | Web of Science: Selected for its rigorous indexing criteria |  |  |  |  |  |
| els. | Scopus: Valued for its comprehensive abstract and citation |  |  |  |  |  |
| follows. Section 2 describes the methodology used for this | Google Scholar: Utilized as a supplementary source to cap- |  |  |  |  |  |
| systematic literature review. Section 3 thoroughly examines | ture grey literature and emerging scholarship |  |  |  |  |  |
| ature. The experimental studies analyzed in this research | We formulated specific search queries using Boolean |  |  |  |  |  |
| are divided into three main sections: vulnerability analy- | operators and controlled vocabulary to optimize recall and |  |  |  |  |  |
| sis, available datasets, and challenges. Section 4 offers a | precision. The temporal parameters were deliberately set |  |  |  |  |  |
| comprehensive review of studies focused on vulnerability | from 2017 to 2024 to capture contemporary developments in |  |  |  |  |  |
| analysis using machine learning for Android applications, | the field while ensuring sufficient longitudinal perspective. |  |  |  |  |  |
| while Sect. 5 is dedicated to the review of available datasets. | The search terms used are meticulously detailed in Table 2, |  |  |  |  |  |
| Section 6 assesses the challenges and limitations encoun- | refined through iterative pilot searches to achieve optimal |  |  |  |  |  |
| Sect. 8 concludes the article by summarizing the findings | 2.2 Inclusion and exclusion criteria |  |  |  |  |  |
| lines future directions based on our findings. | To ensure methodological integrity, relevance, and qual- |  |  |  |  |  |
| 2 Methodology | team members. We then systematically applied these crite- |  |  |  |  |  |
| To address methodological rigor and ensure the transparency | bias and strengthen the validity of our synthesized findings. |  |  |  |  |  |
| widely acknowledged within the scholarly community as | Published between 2017 and 2024, capturing recent advance- |  |  |  |  |  |
| the gold standard for ensuring methodological precision in | ments while providing sufficient temporal scope to observe |  |  |  |  |  |
| systematic reviews. Implementing PRISMA enhances the | evolutionary trends in the field. |  |  |  |  |  |

---

## Page 5

| From code to security: machine learning approaches in android … | Page 5 of 30 | 17 |
| --- | --- | --- |
| Table 2 | Search terms used in the literature review | Publications with inadequate evaluation metrics or validation |

| Search term | Keywords |
| --- | --- |
| Android Vulnerability Detection | “Android vulnerability |

detection”, “Android

security flaws”, “Android

exploit detection.”

vulnerability”, “AI in

Android security”

Deep Learning for Android “Deep learning Android

Android vulnerability

analysis”, “Neural networks

Android security”

security”, “Mobile app

vulnerability detection”,

“Smartphone security

threats”

Security in Mobile Operating “Security in mobile operating

vulnerability assessment”,

“Smartphone OS security”

English language publications to ensure accessibility and

accurate interpretation by the research team

Studies specifically focused on ML or DL applications in

Android vulnerability detection represent the core intersec-

tion of our research domains.

Peer-reviewed journal articles or conference proceedings to

ensure scientific quality and scholarly validation

Studies presenting empirical evidence, methodological inno-

vations, or substantial theoretical contributions to the field.

procedures

Studies that focus on malware detection mainly

These criteria were applied in a two-phase screening

process—first to titles and abstracts, followed by full-text

subjectivity.

A detailed PRISMA Flow Diagram (Fig. 2) visually repre-

sented the study selection process. Initially, 300 studies were

cates, 222 studies remained. These were screened based on

titles and abstracts, resulting in 127 studies for full-text eval-

uation. Ultimately, 85 studies met our inclusion criteria and

were included in this review.

covered that some of the records returned by the string

“vulnerability detection” concentrated on malware detection

fundamentally in scope, threat model, and analytical method-

ology: vulnerability detection seeks to uncover latent flaws in

seemingly benign code, whereas malware detection aims to

distinguish malicious artifacts from benign ones [24–28]. As

a result, studies primarily focused on malware classification,

analysis, or signature generation were considered beyond the

scope of our review and were manually excluded at this point.

3 Background and related literature reviews

3.1 Background

Android applications have become ubiquitous in modern

nerabilities that can compromise user privacy and data

123

| Machine Learning in Android | “Machine learning Android | assessment—with disagreements resolved through consen- |
| --- | --- | --- |
| Security | security”, “ML Android | sus discussions among multiple researchers to minimize |
| Vulnerabilities | vulnerabilities”, “DL | 2.5 Study selection process |
| Mobile Application Security | “Mobile application | identified through database searches. After removing dupli- |
| Systems | systems”, “Mobile OS | During the title-and-abstract screening stage, we dis- |
| Note: Each search term was combined with relevant keywords to ensure | rather than on identifying software vulnerabilities. Although |  |
| a comprehensive literature search | the two research areas occasionally overlap, they differ |  |
| 2.4 Exclusion criteria | society, yet they often present significant security vul- |  |
| Non-English publications, due to translation resource con- | integrity. A primary concern is insecure data storage prac- |  |
| straints and potential interpretation inaccuracies | tices, where applications store sensitive information without |  |
| Studies not directly related to Android or security vulnera- | proper encryption, rendering it susceptible to unauthorized |  |
| bilities, ensuring domain specificity | access if the device’s security is compromised. Equally con- |  |
| Publications that did not employ ML or DL methodologies | cerning is inadequate user input validation, which creates |  |
| as their primary analytical framework | opportunities for malicious actors to execute code injec- |  |
| Duplicated or incomplete records are prevented from redun- | tion attacks, including SQL injection and cross-site scripting |  |
| dancy and ensure data integrity. | (XSS). These attacks potentially grant attackers control |  |
| Review papers without original contributions (though these | over application functionality or unauthorized access to sen- |  |
| were cataloged separately for background context) | sitive data [22]. Communication vulnerabilities represent |  |
| Studies lacking methodological transparency or sufficient | another critical security concern, as unencrypted or improp- |  |
| technical details for reproducibility | erly secured transmission channels can expose user data |  |

---

## Page 6

17 Page 6 of 30 K. E. Arikan et al.

Fig. 2 Study selection process using PRISMA

123

*[Image: Page 6 Image]*

---

## Page 7

| From code to security: machine learning approaches in android … | Page 7 of 30 | 17 |
| --- | --- | --- |
| to man-in-the-middle attacks. In these scenarios, attack- | libraries [34] that enable the implementation of strong secu- |  |
| ers intercept data transmitted between the application and | rity features and reduce common vulnerabilities in Android |  |
| server, compromising confidentiality and potentially modi- | application development. |  |
| fying information in transit. | Recent advancements in ML have introduced innovative |  |
| Using outdated libraries and components introduces addi- | approaches to vulnerability detection in Android applica- |  |
| tional security risks, as these elements frequently contain | tions. ML-based solutions analyze application source code |  |
| known vulnerabilities that attackers can exploit to gain con- | and binaries to identify security weaknesses using algorithms |  |
| trol of applications or devices. Furthermore, privilege escala- | trained on datasets containing known vulnerabilities. These |  |
| tion vulnerabilities arise when applications request excessive | models can recognize patterns and characteristics of inse- |  |
| permissions beyond their functional requirements, creating | cure code, effectively identifying vulnerabilities, including |  |
| potential vectors for attackers to access sensitive information | input validation issues, insecure data storage practices, and |  |
| or misuse device features and capabilities [29]. Applica- | authentication weaknesses. |  |
| tion repackaging and code manipulation techniques have | The primary advantages of ML-based approaches lie |  |
| emerged as sophisticated attack vectors, where malicious | in their scalability and adaptability to emerging threats. |  |
| actors modify legitimate applications and distribute them to | These systems continuously refine their detection capabili- |  |
| unsuspecting users through unofficial channels. Additionally, | ties through ongoing learning, improving accuracy. However, |  |
| insufficient authentication mechanisms frequently lead to | significant challenges exist in implementing ML-based secu- |  |
| account compromise or identity impersonation attacks, fun- | rity solutions, including the requirement for comprehensive |  |
| damentally undermining the security architecture of Android | labeled datasets for model training—a process that can be |  |
| applications. | resource-intensive and costly. Additionally, the effective- |  |
| To address these vulnerabilities effectively [30], devel- | ness of these approaches is highly dependent on the quality |  |
| opers must implement comprehensive security measures, | and comprehensiveness of training data, feature selection |  |
| including secure coding practices, regular and rigorous | methodologies, and the appropriateness of the selected ML |  |
| security assessments, and timely updates to application | algorithms for security analysis applications. |  |

components and libraries. Concurrently, end users must exer-

cise vigilance when granting application permissions and 3.2 Terms and definitions

refrain from installing applications from unverified sources

to minimize exposure to potentially malicious software. The 3.2.1 Artificial Intelligence (AI)

literature [31] outlines several approaches to mitigating vul-

| nerabilities in Android applications. Secure coding practices | AI is a field within computer science that enables computers |
| --- | --- |
| are a foundational strategy during application develop- | to simulate intelligent behaviors typically associated with |
| ment, including proper input validation through established | human intelligence, including reasoning, problem-solving, |
| APIs and adherence to coding standards to minimize secu- | and decision-making [35]. |

rity weaknesses. Implementing these practices significantly

lowers the likelihood of introducing vulnerabilities during 3.2.2 Machine Learning (ML)

development.

| Automated security testing tools provide another effective | ML is a subfield of AI that equips systems with the capability |
| --- | --- |
| approach to securing Android applications. These sophisti- | to autonomously learn and enhance their performance based |
| cated tools analyze application code to identify vulnerabil- | on experience without requiring explicit programming. This |
| ities related to data storage, communication protocols, and | learning process begins by examining data (such as examples, |
| authentication mechanisms [32]. Integrating these tools into | instructions, or experiences) to identify patterns, thereby |
| the development lifecycle enables early identification and | facilitating improved decision-making in future tasks. The |
| remediation of security flaws, resulting in more robust and | ultimate objective is to enable automated learning with min- |
| secure applications. | imal human intervention [36]. |

Research emphasizes the critical importance of contin-

uous monitoring and timely updates [33]. Post-deployment 3.2.3 Supervised machine learning algorithms

surveillance of Android applications is essential for identi-

| fying emerging threats and vulnerabilities. Regular updates | Supervised algorithms utilize a known training dataset to |
| --- | --- |
| tackle known vulnerabilities and fortify applications against | develop a predictive model. By analyzing the provided |
| evolving attack methods. Moreover, academic studies sup- | inputs and comparing the model’s predictions to known |
| port the adoption of specialized security frameworks and | outputs, these algorithms iteratively refine themselves, reduc- |

ing errors and improving their predictive accuracy on new,

unseen data [36].

123

---

## Page 8

17 Page 8 of 30 K. E. Arikan et al.

3.2.4 Unsupervised machine learning algorithms Thus, this subsection provides a summary of relevant review

3.2.6 Reinforcement Learning (RL)

RL algorithms enable systems to interact dynamically with

their environments, learning from actions through trial and

error. Unlike other machine learning methods that depend on

explicit instructions, RL algorithms independently discover

optimal behaviors by aiming to maximize rewards or mini-

mize penalties within specific contexts, an approach inspired

by behaviorist psychology [36].

3.2.7 Deep learning

Deep learning is an advanced subset of machine learn-

ing, inspired by the neural networks of the human brain,

that focuses on processing and extracting complex pat-

terns from large, unstructured, or unlabeled datasets. This

approach facilitates decision-making and predictive mod-

eling by autonomously identifying deep structural insights

from data [37].

123

works that establish the foundational context for our study.

around 200 studies, highlighted privacy breaches, crypto-

priation, code validation, malware identification, test case

revealed an amount of research dedicated to uncovering vul-

nerabilities and leaks in Android systems. Furthermore, this

comprehensive inquiry examined numerous Android assess-

ment methodologies, with a focus on call graphs and control

flow graphs as the primary data structures used. However,

it is important to note that studies related to vulnerability

mitigation were not addressed in this discussion.

The analysis presented in Ref. [40] encompassed an

assessment of 124 distinct research studies spanning the

years 2011–2015, with the overarching goal of delineating

static analysis mechanisms deployed within the domain of

Android applications. The investigation effectively identi-

fied the prevalent use of static analysis techniques in many

research endeavors, predominantly those concerned with pri-

vacy and security matters. Among these techniques, taint

analysis emerged as the most widely employed approach.

In this context, it was established that prominent tools and

formats for conducting such analyses included Soot, a com-

prehensive framework facilitating the analysis, instrumenta-

tion, optimization, transformation, and visualization of Java

and Android applications [41], alongside Jimple, an interme-

diate representation conducive to the streamlined analysis

studies also showed a tendency toward path-sensitivity con-

In their studies, Senanayake et al. [43] reviewed 118 stud-

vulnerability detection using either conventional or ML/DL-

| Unlike supervised learning, unsupervised algorithms seek to | Garg et al. [39] researched Android security evaluations, |
| --- | --- |
| uncover hidden structures or relationships within unlabeled | examining the evolving trends and patterns in different |
| datasets. Instead of relying on predefined outputs, these algo- | analysis approaches, techniques, code representation tools, |
| rithms explore and interpret the data, identifying inherent | and frameworks. This comprehensive research, covering |
| patterns without explicit guidance or labeled examples [36]. | the period from 2013 to 2020 and drawing insights from |
| 3.2.5 Semi-supervised machine learning algorithms | graphic concerns, app duplication, permission misappro- |
| Positioned between supervised and unsupervised methods, | formulation, and energy consumption. The study explored |
| semi-supervised algorithms leverage both labeled and unla- | static analysis techniques, focusing on sensitivity analysis, |
| beled data during training. Typically, a relatively small set of | data structures, and code representations, based on a litera- |
| labeled data is combined with a larger amount of unlabeled | ture review. Additionally, dynamic analysis techniques were |
| data, significantly enhancing the accuracy and efficiency of | examined at kernel, application, and emulator levels using |
| the learning process [36]. | taint analysis and anomaly-based approaches. The review |
| 3.2.8 Explainable Artificial Intelligence (XAI) | and transformation of Java bytecode [42]. Notably, certain |
| XAI is a concept emphasizing transparency and compre- | siderations. After a careful examination, the review identified |
| hensibility in AI systems. It involves creating AI models | leaks and vulnerabilities as the primary concerns addressed |
| with clear and understandable decision-making logic and | by the combined research efforts. Additionally, the investiga- |
| processes. XAI aims to mitigate the opacity of traditional | tion revealed a range of further focal points, including issues |
| “black-box” models, thereby promoting the ethical use of AI | such as permission misuse, energy consumption, detection |
| by enhancing trust, reducing bias, and ensuring accountabil- | of app clones, generation of test cases, code verification, and |
| ity in automated decisions [38]. | implementation of cryptographic techniques. |
| 3.3 Related literature reviews | ies between the years 2016 and 2022 related to Android |
| Before presenting the detailed analysis of current studies, it | based models. They discussed various methods for detecting |
| is essential to acknowledge previous literature reviews that | vulnerabilities, including static, dynamic, and hybrid anal- |
| have informed the understanding of this research domain. | yses. The authors also discussed the use of ML and DL |

---

## Page 9

From code to security: machine learning approaches in android … Page 9 of 30 17

methods for detecting vulnerabilities. The advantages of 4 Vulnerability analysis

using ML-based methods include automatic early detection

| of security issues and vulnerabilities. However, the perfor- | Vulnerability analysis encompasses a broad spectrum of |
| --- | --- |
| mance of ML-based methods can be affected by the quality | techniques for identifying, understanding, and mitigating |
| and quantity of the training data, the choice of features, and | security weaknesses in software systems. Traditional static |
| the selection of the ML algorithm. The authors also dis- | and dynamic analysis methods have been widely used for |
| cuss the importance of analyzing the source code of Android | this purpose; however, the increasing complexity of software |
| applications to detect vulnerabilities. Study selection, data | architectures and the growing sophistication of cyber threats |
| extraction, and synthesis were conducted to identify stud- | necessitate more advanced and scalable solutions. |
| ies aiming to answer the formulated research questions. | Recent advancements in artificial intelligence, particularly |
| The results were cross-validated by performing a peer- | in ML and DL, have significantly contributed to the automa- |
| verification process with all the authors. | tion and efficiency of vulnerability detection. Additionally, |
| Sharma et al. [44] provide a comprehensive and metic- | integrating Large Language Models (LLMs) and Explainable |
| ulous exposition of the confluence between source code | AI (XAI) has opened new possibilities for improving detec- |
| analysis and machine learning. A meticulously curated | tion accuracy, interpretability, and developer adoption. This |
| assemblage of 479 principal research studies, spanning the | section explores various approaches to vulnerability analy- |
| period from 2011 to 2021 (with partial extension into 2022), | sis, including ML-based detection methods, taint analysis, |
| has been scrutinized, encompassing a diverse spectrum of | the role of LLMs, cross-language detection techniques, and |
| 12 distinct software engineering domains. The culmina- | the application of XAI to enhance transparency in security |
| tion of this endeavor is the presentation of a synthesized | assessments. |

compendium of the chosen investigations, methodically cat-

egorized and subcategorized, further elucidated through the

detailed description of the intricate steps involved.

| In addition to this review, the survey aims to provide vari- | 4.1 Vulnerability detection with machine learning |
| --- | --- |
| ous valuable resources, including datasets and tools, thereby | methods |

creating a helpful platform for future research efforts. The

| survey concludes by highlighting the challenges and opportu- | In vulnerability analysis, machine learning techniques play |
| --- | --- |
| nities in this field. It encourages practitioners and researchers | a role by helping us identify patterns that indicate vulner- |
| to contribute methods, tools, and techniques. The ultimate | abilities. A crucial aspect is carefully constructing datasets |
| goal is to create an environment that seamlessly integrates | [21] that encompass a range of vulnerabilities. We also need |
| machine learning techniques into software engineering appli- | to extract and select features from the underlying code or |
| cations in a flexible manner. | binaries to improve the accuracy and relevance of vulnera- |
| Though the existing reviews provide in-depth details of | bility detection. Choosing the anomaly detection or pattern |
| the related studies, the review in Ref. [40] did not cover | recognition algorithms is equally important in ensuring the |
| the recent works conducted in this area. The review in Ref. | model’s effectiveness. Additionally, domain expertise is vital |
| [43] thoroughly reviewed the studies on Android-specific | to understanding vulnerabilities in their context and defining |
| vulnerability detection/prevention using conventional and | learning objectives. Combining all these elements enables us |
| ML methods performed in source code analysis. However, | to develop machine learning techniques [80] that effectively |
| it seems they missed some notable research in this field, | identify vulnerabilities, thereby strengthening cybersecurity |
| as well as the new techniques and approaches developed | efforts. |
| through the analysis period using ML techniques. Sharma | The above figure (Fig. 3) presents an overview of a typical |
| et al. [44] provide a detailed survey of source code anal- | pipeline involved in code representation. Many repositories |
| ysis with machine learning mechanisms without focusing | undergo processing to train a model during the training phase, |
| on particular programming languages in the time range | which is subsequently employed in the inference phase. |
| between 2011 and 2021. Therefore, a comprehensive review | The source code is prepared and transformed into a model, |
| of recent studies on Android vulnerability detection using | such as an Abstract Syntax Tree (AST) or a sequence of |
| ML methods and prevention is necessary. In this work, | tokens. This model is then passed to a feature extractor, which |
| we summarize the currently available datasets along with | extracts important features such as AST paths and tree-based |
| their strengths and weaknesses, illustrating the existing sta- | embeddings. Subsequently, a ML model is trained using the |
| tus from an Android-specific perspective. Additionally, this | extracted features. The model generates a numerical rep- |
| study presents a comprehensive overview of the latest trends | resentation, i.e., a vector, which can be further utilized for |
| and challenges related to the topic. Table 3 summarizes and | specific software engineering applications, including defect |
| compares the related reviews with this work’s contribution. | prediction, vulnerability detection, and code smell detection. |

123

---

## Page 10

17 Page 10 of 30 K. E. Arikan et al.

0.84

=

malicious access patterns & generates 331 policy rules

Android dataset availability[39] × Accuracy 99.11% 96.60% 88.70% 96.76% Learns 2518 benign & 91.79% 98.37% 99.75% 93.78% 97.50% F1-score 91.70%

functions, code features Network Addresses API, Dynamic Behaviors Libraries, Broadcast receivers Storage, Contacts, Location, Camera, etc Epoll_pwait, Receive from, Send to, Ioctl, Write, Getuid Intrinsic- Size Antivirus

New research areas × Features Permissions, API calls, Permissions, API calls, N/A Permissions, Sensitive N/A API call sequences Permissions, API Calls, API calls Permissions, API calls Static-SMS, Phone, Clock get time, Mprotect, API calls

= =

5560

| = | 10,867 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 510 Malicious | 1,23,453 | 1000, Malware | = | 20,000 Malicious | 10,000 Malicious | 60,000 Malicious | 28,489 Malicious | 300 Malicious | 1901 Malicious |  |  |  |  |  |
| = | = | = | = | = | = | = | = | = |  |  |  |  |  |  |
| 1760 | 10,000 | 24,000 | 30,113 | 1600 |  |  |  |  |  |  |  |  |  |  |
| 910 | Malicious | samples | = | = | = | = | 300 | 259,608 malware | = |  |  |  |  |  |
| Challenges/Limitations | × | Dataset/Apps/Tools | Benign | Benign | Benign | Benign | 1.3 million audit logs | Benign | Benign | Benign | 3,00,000 apks | Benign | 82,866 suspicious apps, | Benign |

+ +

CNN, RNN RIDOR, Ensemble

ML-based vulnerability detection ✓ Classifier Adaboost with DT k-means Rd, SVM, CNNs DBN K-NN RF-DT, XGBoost, NN, MLP, SVM, PART, SVM LLGC k-NN, LR LR, RF DNN

used

Period 2013–2020 ML/DL Technique SL UL DL DL SSL DL SL SL SSL SL SL DL

assessments and Application analysis methods

The focus of the review Android security Paper AdDroid [45] Appice et al.[46] ATMPA [47] DroidDetector [48] EASEAndroid [49] Fadadu et al.[50] Garg et al.[27] Han et al. [51] Chandra et al. [52] Mantoo et al.[53] Martín et al.[54] Nguyen-Vu et al. [55]

Summary of Related reviews (including this SLR) and key research papers

Table 3 Literature review Garg et al. [39] Garg et al. [30]

123

---

## Page 11

From code to security: machine learning approaches in android … Page 11 of 30 17

*

| Android dataset | availability[39] | 99.02% | ✓ | Accuracy | 92.87 | 83.6 | 77 | 98.27 | 70,1 | 96 | 98,77 | × | Accuracy | 97.30% | 94% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| * | source code | calls |  |  |  |  |  |  |  |  |  |  |  |  |  |
| New research areas | Permissions, API calls | ✓ | Features | Source Code | Function call collection | Permissions, Intents | System calls | Source Code | functions | PE | ✓ | Features | Tokenized part of the | Image texture and API |  |

10,000 Malicious

=

8560

= source code using N-gram, APKs from F-Droid (9,872), VDiscover tool [33] differentiate vulnerable and non-vulnerable source code vulnerability detection rules, tenfold cross-validation generation, ML algorithms judging maliciousness benign) benign apps

Challenges/Limitations Benign × Dataset/Tools/apps Features based on mining Function call sequences From major sources From major sources ML-based analysis to Efficient human-readable PE data extraction, image ✓ Dataset/Tools/apps 60,561 apps (malicious and 5560 malicious, 123,453

CNN-LSTM RIDOR model

| ML-based vulnerability | detection | DNN | ✓ | Classifier | DNN algorithm | CNN, LSTM, | AB and DT | MLP, SVM, PART, | MLP and a customized | J48 and JRip | CNN | ✓ | Classifier | MKL-SVM | Deep Belief Networks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| used | used |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Period | DL, SSL | 2016–2022 | ML/DL Technique | DL | DL | SL | SL | SL | ML | DL | 2011–2021 | ML/DL Technique | SL | DL |  |
| vulnerability detection | and prevention | methods for source | code analysis |  |  |  |  |  |  |  |  |  |  |  |  |

The focus of the review Sharmeen et al.[56] Android source code Paper Pang et al. [57] Wu et al. [58] Zhuo et al. [59] Garg et al. [27] Bilgin et al. [60] Gupta et al. [61] Kim et al., [62] Machine learning Paper Narayanan et al.[17] Shiqi et al., [63]

(continued)

Table 3 Literature review Senanayake et al. [43] Sharma et al. [44]

123

---

## Page 12

| 17 | Page 12 of 30 | K. E. Arikan et al. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Android dataset | availability[39] | 89.47% | 91.38% | 98.98% | 96% | 92% | ✓ | Accuracy | 91.38% | 83% | 82.60% | 84% | 92.87% | 96% | 85% | 94% | 96% | 91.67% | 95% | 98% | 96% |
| behavior | analysis | code with code metrics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

New research areas Static and dynamic 20 static code metrics API calls, APIs freqs Static code metrics System functions ✓ Features Static code metrics Static code metrics Functions Dynamic and static Static analysis/source Functions System calls Code chunks Code chunks Functions Code chunks Code changes Code chunks

benign rest are malware different versions apps popular Java frameworks sources issues samples Project [78]

Challenges/Limitations 5063 Android apps, 1000 1406 apps with 4416 10 k benign and vulnerable 2 Android projects 219 malicious apps ✓ Dataset/Tools/apps Fdroid [68] Fdroid [68] 235 methods from 10 300 APKs from major Fdroid [68] 2 Android projects Four apps with known 46,333 vulnerable code Lvdandro [72] Ghera benchmark [75] Lvdandro [72] Android Open Source Lvdandro [72]

| ML-based vulnerability | detection | SVM | DT RF | DNN LSTM | J48 JRip | DT and Naïve Bayesian | ✓ | Classifier | RF | r-SVM | SVM | AB and DT | DNN | J48 JRip | KNN | XGBoost | Vanilla | LLM (GPT-4) | XGBoost | RF | RF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| used | Networks |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Period | SL | SL | DL | ML | SL | 2017–2024 | ML/DL Technique | SL | SL | SL | SL | DL | ML | ML | AutoML | Neural Networks | DL | ML | ML | Federated Neural |  |

detection using ML/DL techniques

The focus of the review Alatwi et al., [64] Zang et al., [65] Ma et al., [66] Gupta et al.. [61] Wei et al., [67] Android vulnerability Paper Zhang et al. [65] Rahman et al. [69] Piskachev et al., [70] Zhuo et al. [59] Pang et al. [57] Gupta et al. [61] Malik et al. [71] Senanayake et al. [72] Defendroid [73] Llbezpeky [74] Acved [76] Yim et al. [77] Fedrevan [79]

(continued)

*, Partially

Table 3 Literature review This work ✓

123

---

## Page 13

From code to security: machine learning approaches in android … Page 13 of 30 17

Fig. 3 Vulnerability detection pipeline [44]

| Building | upon | these | fundamental | machine | learning | Android applications. They only protect code during devel- |
| --- | --- | --- | --- | --- | --- | --- |
| approaches for code analysis, recent advancements in vulner- | opment as plugins, which still leaves millions of currently |  |  |  |  |  |
| ability detection for Android applications have demonstrated | developed and used applications in the app stores needing |  |  |  |  |  |
| significant promise across multiple methodologies. Stud- | additional approaches. |  |  |  |  |  |
| ies employing traditional machine learning algorithms have | Studies such as [86–89], and [90] explore techniques for |  |  |  |  |  |
| shown considerable efficacy. For instance, Zhang et al. [65] | detecting security vulnerabilities in Android applications. |  |  |  |  |  |
| highlighted the superior performance of Random Forest | As evaluated in [86], traditional static and dynamic anal- |  |  |  |  |  |
| across various risk levels in IoT applications, while Rahman | ysis methods exhibit significant limitations, as they fail to |  |  |  |  |  |
| et al. [69] achieved a precision of 0.83 using radial-based sup- | detect many known vulnerabilities. Large Language Models |  |  |  |  |  |
| port vector machines (r-SVM) for security risk prediction. | (LLMs) like GPT-4, assessed in [87], outperform conven- |  |  |  |  |  |
| Several specialized tools and frameworks have emerged to | tional analyzers by identifying four times more vulnerabil- |  |  |  |  |  |
| address specific vulnerability detection challenges, including | ities with lower false positives. Similarly, [88] compares |  |  |  |  |  |
| SWAN [70], which generalizes detection to Java applications | multiple LLMs in detecting Android vulnerabilities, reveal- |  |  |  |  |  |
| with 0.826 precision; VuRLE [81], which focuses on auto- | ing considerable discrepancies in performance. The work |  |  |  |  |  |
| mated vulnerability repair through template learning; and | in [89] highlights the effectiveness of a hybrid approach |  |  |  |  |  |
| Vulvet [82], which achieved an impressive 95.23% preci- | that combines static and dynamic analysis, demonstrating |  |  |  |  |  |
| sion across 3700 applications using multi-tier static analysis. | superior detection capabilities compared to traditional tools. |  |  |  |  |  |
| Research on neural network applications has also progressed, | Finally, [90] presents VulsTotal, a unified platform for bench- |  |  |  |  |  |
| as evidenced by studies that utilize deep neural networks for | marking static application security testing (SAST) tools, |  |  |  |  |  |
| predicting vulnerable components [53] and specialized algo- | addressing the inconsistency and incompleteness in prior |  |  |  |  |  |
| rithms for detecting vulnerability in the Intent mechanism | vulnerability detection frameworks. Predicting future secu- |  |  |  |  |  |
| [59]. However, the latter achieved a moderate accuracy of | rity vulnerabilities is critical for proactive defense strategies. |  |  |  |  |  |
| 77%. Dataset innovations represent another crucial advance- | Study [91] employs time-series and deep learning techniques |  |  |  |  |  |
| ment, the studies [73, 76, 79, 83] with the LVDAndro dataset | to predict vulnerabilities in Android OS versions, utilizing |  |  |  |  |  |
| [72] providing over 20 million annotated code samples and | data from the National Vulnerability Database (NVD). The |  |  |  |  |  |
| enabling 94% accuracy in vulnerability classification despite | results demonstrate that LSTM models can achieve com- |  |  |  |  |  |
| limitations inherited from its underlying scanning tools, | petitive accuracy, though classical models like ARIMA still |  |  |  |  |  |
| MobSF [84] and Qark [85]. Despite these advances, recur- | outperform in some cases. The findings suggest that hybrid |  |  |  |  |  |
| ring limitations persist across studies, including insufficient | approaches yield better long-term predictions. |  |  |  |  |  |
| dataset size and diversity, challenges in accurately label- | Study in this reference [77] explores a preventive approach |  |  |  |  |  |
| ing data for supervised learning approaches, and difficulties | to vulnerability detection. In this approach, a security review |  |  |  |  |  |
| in detecting Android-specific vulnerabilities within varied | bot automatically flags potentially insecure code changes |  |  |  |  |  |
| application contexts, highlighting areas that require further | before they are submitted. This classifier-based framework |  |  |  |  |  |
| investigation to develop comprehensive security solutions for | achieves a high detection rate, offering a promising method |  |  |  |  |  |

123

---

## Page 14

| 17 | Page 14 of 30 | K. E. Arikan et al. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| for integrating security checks into the software develop- | analysis has been proposed to mitigate this—static features |  |  |  |  |  |
| ment lifecycle. The study suggests that integrating machine | are prone to obfuscation. In contrast, dynamic features are |  |  |  |  |  |
| learning-based analysis into code review pipelines can sig- | more challenging to collect despite being more resistant to |  |  |  |  |  |
| nificantly enhance secure coding practices. | such techniques. Another key challenge is the variability of |  |  |  |  |  |
| While many efforts focus on detection, the study [92] | in-app behavior across different devices, which complicates |  |  |  |  |  |
| investigates the automated repair of vulnerabilities using pre- | detection accuracy, particularly in large-scale frameworks |  |  |  |  |  |
| trained models. It highlights that transfer learning from bug | such as federated learning. These obstacles underscore the |  |  |  |  |  |
| fixing can significantly improve prediction accuracy, empha- | necessity of employing up-to-date datasets, leveraging adap- |  |  |  |  |  |
| sizing the potential for AI-driven vulnerability patching in | tive modeling techniques, and addressing the complexities of |  |  |  |  |  |
| reducing manual debugging efforts. However, challenges | evolving security threats. Insights gained from these studies |  |  |  |  |  |
| remain in systematically evaluating the effectiveness and lim- | could also inform future advancements, making vulnerability |  |  |  |  |  |
| itations of these models in real-world applications. | detection methods more robust and applicable in real-world |  |  |  |  |  |
| Recent studies in ML-based vulnerability detection have | scenarios. In a related study [99], researchers introduced a |  |  |  |  |  |
| explicitly | addressed | hyperparameter | tuning | to | optimize | supervised learning approach for detecting Android malware, |
| model performance. For example, researchers varied neural | utilizing a labeled dataset comprising over 18,000 samples |  |  |  |  |  |
| network depth and perceptron counts, applying systematic | across five categories. Their methodology, validated against |  |  |  |  |  |
| grid search procedures to identify optimal configurations and | multiple benchmark datasets, yielded competitive results |  |  |  |  |  |
| validate parameter suitability [73, 79]. These efforts were | compared to state-of-the-art techniques, offering valuable |  |  |  |  |  |
| often complemented by magnitude-based pruning, where | insights into malware classification and detection enhance- |  |  |  |  |  |
| insignificant weights were gradually removed to increase | ments. In addition, Wajahat et al. [100] directly addressed |  |  |  |  |  |
| throughput while preserving accuracy; pruning levels were | the challenge of dataset imbalance by proposing a prepro- |  |  |  |  |  |
| carefully tuned using the TensorFlow optimization tool- | cessing framework that removes duplicates, balances class |  |  |  |  |  |
| box to balance sparsity against predictive precision [73, | distributions, and applies feature selection techniques such |  |  |  |  |  |
| 79]. Beyond deep learning models, parameter tuning has | as Gain Ratio and Chi-square tests. Their evaluation on the |  |  |  |  |  |
| also been explored in selective security testing frameworks, | Drebin and Tuandromd datasets demonstrated that classi- |  |  |  |  |  |
| where configuration parameters—such as maximum test | fiers like Random Forest and SVM can achieve accuracy |  |  |  |  |  |
| duration and function-level targeting—were dynamically | rates approaching 99% when supported by these data-centric |  |  |  |  |  |
| adjusted based on source code changes and project-specific | strategies. While this study focuses on Android malware |  |  |  |  |  |
| vulnerability statistics [77]. Collectively, these approaches | detection, its emphasis on class rebalancing and feature opti- |  |  |  |  |  |
| highlight the diversity of hyperparameter optimization strate- | mization provides a transferable perspective for enhancing |  |  |  |  |  |
| gies across the literature, ranging from grid search and | the robustness of vulnerability detection models, which are |  |  |  |  |  |
| pruning in neural networks to adaptive configuration in secu- | often limited by imbalanced datasets. |  |  |  |  |  |

rity testing pipelines, underscoring the importance of tuning

for both performance and efficiency. 4.2 Taint analysis with machine learning

While vulnerability detection and malware detection are

| frequently confused as being synonymous, they serve distinct | In analyzing taint, source and sink functions are vital in |
| --- | --- |
| purposes and operate under different principles. Vulnerabil- | monitoring how information moves within a program. Taint |
| ity detection identifies weaknesses within systems that could | analysis is a security technique to detect how data, known |
| be exploited, whereas malware detection identifies harm- | as “taint,” spreads throughout the code. Interacting with dif- |
| ful software or behaviors. Recognizing these differences is | ferent functions and recognizing the significance of sources |
| essential to understanding the contribution of this study, | and sinks is crucial for identifying security weaknesses and |
| which seeks to enhance the field of vulnerability detection | safeguarding sensitive data [101]. |
| by addressing critical gaps in real-world dataset accessibility | Sources refer to functions or methods in the code where |
| and reproducibility. | sensitive data originates. These can include user inputs such |
| Several significant studies [93–96] have examined chal- | as passwords, credit card numbers, or personally identifiable |
| lenges associated with Android malware detection, offering | information (PII). A source labels data as “tainted,” indi- |
| valuable insights that could contribute to improving vulnera- | cating that it should be tracked throughout the program’s |
| bility detection techniques. A persistent issue in this domain | execution. Identifying sources is crucial, as they establish |
| is the dependence on outdated or small-scale datasets, such as | entry points for potential data breaches or security vulnera- |
| MalGenome [97] and Drebin [98], which do not adequately | bilities. By tracing data to its sources, security analysts can |
| reflect contemporary threat landscapes. This shortcoming | comprehend how confidential information enters the appli- |
| limits the ability to train effective machine learning models, | cation and monitor its movement. Sinks are functions or |
| often leading to overfitting. Integrating static and dynamic | methods that interact with the outside world, such as network |

123

---

## Page 15

| From code to security: machine learning approaches in android … | Page 15 of 30 | 17 |
| --- | --- | --- |
| communication, file I/O, or database queries. These functions | an average recall of 85%, the model exhibited a high false |  |
| are potential destinations for tainted data to leak outside the | positive rate for source and sink classifications, suggesting |  |
| application’s intended scope. Security analysts can identify | the need for improved semantic analysis. |  |
| potential data leaks or vulnerabilities that expose sensitive | FlowDroid [108], on the other hand, employs a static taint |  |
| information to unauthorized users or attackers by monitor- | analysis approach that precisely tracks data flows within |  |
| ing tainted data as it reaches these sinks. Properly identifying | applications. It detects a high fraction of data leaks while |  |
| and securing sinks prevents data exfiltration and protects user | maintaining a low false positive rate, outperforming com- |  |
| privacy. | mercial tools such as IBM AppScan Source and Fortify |  |
| Source and sink functions are crucial for data propaga- | SCA. FlowDroid successfully identifies leaks in large-scale |  |
| tion, as they help taint analysis algorithms track how tainted | datasets, including those from Google Play apps and malware |  |
| information moves through code. Developers can implement | samples on VirusShare. However, like other static analysis |  |
| effective security measures by understanding how sensitive | tools, FlowDroid may struggle with scalability when han- |  |
| data enters an application and where it might be leaked [102]. | dling complex, obfuscated applications and dynamic code |  |
| Taint analysis also ensures that sensitive information is han- | execution. |  |
| dled securely during application execution, minimizing the | When compared, SuSi provides an automated method for |  |
| risks of data breaches and privacy violations. Additionally, | classifying sources and sinks, making it highly efficient for |  |
| integrating taint analysis with machine learning techniques | identifying taint entry and exit points. In contrast, FlowDroid |  |
| shows promise for detecting vulnerabilities in source code | excels in precise taint propagation analysis. However, Sas |  |
| [103]. | et al. [110] highlighted that SuSi’s classification accuracy |  |
| Over the years, various tools have been developed to | can be compromised by misidentifications. In contrast, Flow- |  |
| conduct taint analysis of Android applications. However, | Droid’s reliance on static analysis may limit its performance |  |
| comparing these tools is challenging due to different eval- | in real-world scenarios where dynamic execution plays a cru- |  |
| uation targets and methodologies. Some studies fail to | cial role. Combining these approaches—leveraging SuSi’s |  |
| describe the datasets used for evaluation, while others rely | classification for source-sink identification and FlowDroid’s |  |
| on benchmarks but only partially cover them. Furthermore, | propagation analysis—could lead to a more comprehensive |  |
| discrepancies exist in the types of data leaks considered, and | taint analysis framework. Future research could integrate |  |
| many tools lack a ground truth for accurate validation. These | machine learning-based classification with advanced static |  |
| inconsistencies make it difficult to compare the effectiveness | and dynamic analysis techniques to enhance accuracy and |  |
| of different tools. | scalability. |  |
| To address these challenges, ReproDroid [104] was intro- | Furthermore, Ausera [111] introduced a comprehensive |  |
| duced as a framework for benchmarking Android taint | vulnerability taxonomy to address the shortcomings of func- |  |
| analysis tools in a reproducible manner. It enables researchers | tionality, limited vulnerability coverage, and the restricted |  |
| to infer the ground truth for data leaks, apply tools auto- | availability of benchmark datasets. This taxonomy encom- |  |
| matically to benchmarks, and systematically evaluate their | passes 50 different vulnerability types to enhance coverage |  |
| results. Using ReproDroid, six major taint analysis tool- | and reduce false negatives and false positives. Additionally, |  |
| s—Amandroid [105], DIALDroid [106], DidFail [107], and | it provides a robust benchmark dataset that may be utilized in |  |
| FlowDroid [108]—were evaluated under uniform conditions. | future machine learning methods for further improvement. |  |

While the overall results were positive, the study revealed that

four of these tools did not fully meet their claimed capabili- 4.3 Leveraging Large Language Models (LLMs)

ties in terms of features and accuracy. Additionally, the study

| contributed an improved version of the DroidBench test suite | The emergence of LLMs with billions of parameters has sig- |
| --- | --- |
| to enhance unbiased benchmarking in future research. | nificantly expanded the capabilities of artificial intelligence |
| Among the most prominent taint analysis tools, SuSi | in various domains, including software security. These mod- |
| and FlowDroid adopt distinct approaches. SuSi [109] lever- | els are believed to capture intricate patterns related to syntax, |
| ages machine learning techniques to automatically classify | semantics, and the structural properties of human language |
| Android source and sink functions. It extracts semantic | [112]. Interestingly, their proficiency extends to program- |
| and syntactic features from Android source code, training | ming languages, as these often exhibit well-defined grammar |
| a model that can categorize unknown methods as sources, | and semantic structures [113]. Recent research has explored |
| sinks, or neither. While SuSi achieves high precision and | the potential of LLMs in identifying security vulnerabili- |
| recall, discrepancies exist between testing and validation | ties in code, yielding promising but varied results [87]. For |
| precision scores, leading to misclassifications, particularly | instance, studies evaluating GPT-based models for vulnera- |
| in differentiating source and sink classes. Sas et al. [110] | bility detection have shown mixed effectiveness—Cheskov |
| reported that although SuSi achieved 86.2% accuracy with | et al. [114] reported that their approach did not perform well. |

123

---

## Page 16

| 17 | Page 16 of 30 | K. E. Arikan et al. |
| --- | --- | --- |
| However, their methodology was relatively simplistic. On | focus on collecting vulnerable components at the binary level |  |
| the other hand, more advanced techniques, such as extended | and that it is essential to verify vulnerabilities after develop- |  |
| prompting strategies and hybrid approaches that integrate | ers claim to patch them and assess the effectiveness of their |  |
| LLM-driven analysis with complementary security mecha- | approach in this manner. |  |
| nisms, have demonstrated improved accuracy in detecting | Most ML approaches aim to identify parts in source code, |  |
| CWEs within code [115, 116]. | whether a line or a function. We believe that a code seg- |  |
| Additionally, some studies have taken a more comprehen- | ment vulnerability depends on its context, specifically in |  |
| sive approach, investigating multiple facets of LLM-based | terms of control flow and data flow considerations. Therefore, |  |
| security analysis. These in-depth evaluations suggest that | we argue that context awareness is crucial for vulnerabil- |  |
| LLMs can offer valuable insights into software vulnerabili- | ity detection. In a study [118], the authors introduced a |  |
| ties when appropriately fine-tuned and guided, making them | framework designed to generate code embeddings specifi- |  |
| a promising avenue for future security research and practical | cally for detecting vulnerabilities at the function level. The |  |
| applications [117]. | proposed framework focuses on capturing source-sink data |  |

flows without getting caught up in validation complexities,

| 4.4 Cross-language vulnerability detection | which relies on a model that helps uncover meaning hidden |
| --- | --- |
| approaches | within the source code. By transforming code sequences into |

rich semantic association vectors, it feeds these vectors into

| This review has explored methodologies and patterns rele- | Bi LSTM layer to better understand long-term dependencies. |
| --- | --- |
| vant to identifying vulnerabilities in Android applications. | As a result, their presented network has become skilled at |
| However, considering the need for up-to-date insights, it is | identifying code segments. To ensure the compatibility of the |
| wise to examine the need for up-to-date insight fields. This | extracted code embeddings with machine learning classifiers, |
| investigation can be useful for evaluating Android applica- | a max pooling layer transforms the acquired embeddings into |
| tions and providing insights for research directions. To the | vector representations. This approach avoids code analysis |
| best of our knowledge, we would like to share a study con- | by taking the source code as input. Empirical validation con- |
| ducted on various languages, though they may not directly | firms that the code embeddings generated by their method |
| align with our specific interests. | serve as feature sets for detecting vulnerabilities. Interest- |
| In a study, a DL-based framework was presented that | ingly, when applied to our real-world software projects, using |
| offers user-friendly Python scripts for developing and eval- | these embeddings in conjunction with the forest classifier |
| uating vulnerability detection mechanisms. This framework | yields better performance than four other baseline systems. |
| undertakes a dual-pronged evaluation using distinct datasets | When locating vulnerable codes, the role of Natural Lan- |
| to assess its efficacy and the proficiency of the embedded neu- | guage Processing (NLP) is crucial in enhancing the detection |
| ral networks [67]. The initial dataset, SARD, encompasses | of sections in source code repositories. By utilizing NLP tech- |
| synthetic vulnerabilities, while the second dataset is meticu- | niques, we can bridge the gap between human explanations |
| lously curated, comprising over 1300 instances of vulnerable | of vulnerabilities and the complex syntax of source code. |
| files and functions extracted from real-world sources. Lever- | This enables the development of models that can comprehend |
| aging the framework, it conducts three empirical case studies | and analyze code snippets, much like humans understand |
| utilizing the Deep Neural Network (DNN), Bidirectional | language. NLP helps create algorithms that not only iden- |
| Long Short-Term Memory (Bi-LSTM) network, and Text | tify vulnerabilities but also understand nuances, leading to |
| Convolutional Neural Network (text-CNN). The outcomes | a more comprehensive understanding of potential security |
| of these experiments indicate a uniform performance trend | threats. Consequently, integrating NLP into vulnerability |
| across the synthetic SARD dataset, implying that the struc- | detection processes significantly enhances the accuracy and |
| tural configurations of the networks play a subordinate role in | efficiency of identifying and mitigating security risks within |
| influencing performance within the context of synthetic vul- | software systems. The researchers [119] propose using a |
| nerability samples. However, the performance diverges when | learning approach to identify vulnerabilities by analyzing |
| confronted with an authentic, real-world dataset. Notably, | their LLVM IR representations. They draw inspiration from |
| the contextually aware network models, namely the text- | techniques commonly used in natural language processing. |
| CNN and Bi-LSTM networks, exhibit enhanced capabili- | First, they identify source codes that contain vulnerabilities. |
| ties in detecting real-world vulnerabilities. This highlights | Then, they pinpoint the lines of code responsible for those |
| the effectiveness of context-aware network architectures in | vulnerabilities. This two-step approach effectively reduces |
| identifying genuine vulnerabilities in real-world scenarios. | the number of alarms when detecting lines. Through exper- |
| However, the proposed real-world vulnerability dataset in | imentation with world and synthetic code datasets obtained |

this study is still in its early stages and could be improved;

further effort is required. They acknowledge that they will

123

---

## Page 17

| From code to security: machine learning approaches in android … | Page 17 of 30 | 17 |
| --- | --- | --- |
| from NVD and SARD, they achieved an impressive accu- | demonstrate improvements compared to established base- |  |
| racy rate of approximately 98% in detecting vulnerabilities | line methodologies—achieving a precision increase of up |  |
| in source code. | to 33.57% and a recall boost of 128.38% compared to the |  |
| This research [120] aims to address the issue of the | successful model documented in the existing literature. In |  |
| “start” problem in machine learning. The main concern is | conclusion, the study examines the underlying issues in vul- |  |
| acquiring features that can be generalized across projects. | nerability prediction systems, with a focus on learning. It |  |
| To strike a balance between having features and being able | provides a roadmap for research efforts to fully utilize the |  |
| to generalize, we have developed a data-centric approach | capabilities of learning methods in predicting vulnerabilities. |  |
| incorporating several innovative ideas. Primarily, the seman- | While our focus remains primarily on Android applica- |  |
| tic intricacies of code are unveiled through serialized abstract | tions, it is important to note that the underlying method- |  |
| syntax trees (ASTs), with tokens encoded via Continuous | ologies, particularly those based on semantic embeddings, |  |
| Bag-of-Words neural embeddings. Subsequently, these seri- | control/data flow analysis, and transfer learning strategies, |  |
| alized ASTs undergo analysis via a sequential deep learning | are not restricted to a single programming language or plat- |  |
| classifier, specifically a bidirectional LSTM network. This | form. In principle, these approaches can be adapted to other |  |
| cognitive process culminates in generating a distinctive rep- | ecosystems, enabling broader applicability across diverse |  |
| resentation indicative of software vulnerability. Importantly, | codebases. Future research should therefore place greater |  |
| the neural representation acquired from pre-existing soft- | emphasis on cross-project and cross-language validation to |  |
| ware projects is transposed onto new projects, facilitating | ensure that models trained in one environment can generalize |  |
| early-stage vulnerability detection even without an exten- | effectively to others. |  |

sive corpus of training labels. To assess the effectiveness of

| this vulnerability detection approach, they conducted a label- | 4.5 Behavioral pattern analysis and compact model |
| --- | --- |
| ing process involving 457 instances of vulnerabilities. They | design |

curated a dataset containing over 30,000 vulnerable functions

| from six open-source projects. The empirical findings con- | Behavioral pattern analysis refers to approaches that cap- |
| --- | --- |
| firm that the model can accurately generate representations | ture how software components or code segments behave over |
| indicating vulnerabilities. It demonstrates adaptability across | time—whether through runtime traces, control-flow patterns, |
| project scenarios. Compared to code metrics, the transfer | or function-level interactions—rather than relying solely on |
| learning-based representations effectively predict vulnera- | static code tokens. Compact model design, on the other |
| ble functions within individual projects and across multiple | hand, focuses on reducing the size, complexity, and resource |
| diverse projects. Advancements in DL have sparked interest | demands of ML models so that they remain deployable in |
| in applying DL methodologies to automated vulnerability | practical environments such as CI/CD pipelines or mobile |
| detection. Several recent studies have shown results achiev- | devices. |
| ing up to 95% accuracy in vulnerability detection. In this | Recent contributions have emphasized that improving |
| research contribution, we investigate the performance of | vulnerability detection requires moving beyond static token- |
| state-of-the-art DL-driven techniques in real-world vulner- | level features toward behavioral pattern analysis. Inter- |
| ability prediction. | pretable dynamic-analysis pipelines for Android demon- |
| Unexpectedly, this analysis [121] reveals a performance | strate how fine-grained runtime traces (e.g. system-call |
| drop of over 50% when transitioning from controlled envi- | sequences) can be linked to human-readable rationales, |
| ronments to real-world scenarios. A thorough investigation | thereby improving trust in model outputs [122]. Similarly, |
| into the reasons behind this decline in performance highlights | temporal behavior modeling approaches explicitly capture |
| the challenges present in vulnerability prediction methods | how execution patterns evolve, which enhances the robust- |
| based on machine learning. These challenges arise from | ness of classification in security-sensitive contexts [123]. At |
| both the makeup of the training data, which suffers from | the source-code level, researchers have introduced frame- |
| issues such as data quality and imbalanced class distribu- | works that model abstract behavioral semantics and function |
| tions, and the selection of model architectures, which often | interactions, allowing detectors to generalize across projects |
| prioritize token-based approaches. These methods often fail | instead of memorizing surface-level features [124]. These |
| to identify the underlying causes of vulnerabilities, instead | studies collectively highlight that context-aware and behav- |
| relying on superficial knowledge extracted from the dataset, | ioral perspectives substantially improve both accuracy and |
| such as specific variables or function names. Building on | interpretability in ML-based vulnerability analysis. |
| these insights, a more methodologically sound approach is | Meanwhile, another key area of research focuses on |
| advocated for acquiring data and designing model architec- | making models more efficient for real-world applications. |
| tures that accurately capture the contexts of vulnerability | Surveys on model compression techniques—including quan- |
| prediction. By adopting this approach, the resulting tools | tization, pruning, and knowledge distillation—show that |

123

---

## Page 18

| 17 | Page 18 of 30 | K. E. Arikan et al. |
| --- | --- | --- |
| compact neural networks can significantly cut down mem- | should be considered an essential requirement for future |  |
| ory use and inference time while still delivering competitive | research. |  |

accuracy [125]. Such techniques are particularly relevant for

continuous integration pipelines and resource-constrained

environments, where vulnerability detection models must

| operate under strict efficiency requirements. Finally, to inte- | 4.7 Practical application: real-time deployment |
| --- | --- |
| grate code-based vulnerability detectors into operational | feasibility and tooling |

security practices, researchers have proposed threat modeling

| frameworks specifically tailored to ML-intensive systems. | Bridging research and real-world utility, one promising direc- |
| --- | --- |
| These frameworks emphasize the systematic identification of | tion involves designing prototype web-based vulnerability |
| assets, attack surfaces, and controls during deployment [126]. | analysis systems. Such systems could automatically decom- |
| Incorporating such perspectives bridges the gap between | pile uploaded Android APKs, extract static code metrics |
| academic prototypes and real-world secure development | and semantic code embeddings, and apply pre-trained ML |
| workflows, strengthening both the reliability and the deploy- | models to provide both file-level binary vulnerability classi- |
| ability of ML-based detection systems. | fication and an overall normalized “Application Risk Score.” |

This type of architecture demonstrates how advanced ML

4.6 Explainable AI (XAI) methods can be transformed into lightweight, user-friendly

interfaces suitable for integration into web services or con-

| At the start of 2017, the Defense Advanced Research Projects | tinuous integration pipelines. |
| --- | --- |
| Agency (DARPA) funded the “Explainable AI Program” | In parallel, real-time feasibility on mobile or edge devices |
| [127]. The primary goal of this initiative is to create AI | requires attention to model compression [132] and inference |
| models that are both highly interpretable and capable of | optimization [133]. Recent studies on quantization-aware |
| maintaining robust predictive performance. Furthermore, the | training and pruning have demonstrated that lightweight |
| program seeks to ensure that human users can easily under- | neural networks can achieve substantial reductions in mem- |
| stand, trust, and effectively manage upcoming generations of | ory footprint and latency while maintaining high accuracy, |
| AI technologies. In 2020, the National Institute of Standards | thereby enabling deployment on constrained Android envi- |
| and Technology (NIST) complemented this effort by outlin- | ronments [134]. In Android-specific security tasks, design- |
| ing four core principles for XAI—Explanation, Meaningful, | ing robust feature representations is equally important, as |
| Explanation Accuracy, and Knowledge Limits, as shown in | demonstrated in obfuscation-resilient approaches for mal- |
| Fig. 4. Together, these initiatives highlight the dual need | ware detection [135] and recent transformer-based detection |
| for accuracy and transparency in AI-driven decision-making | models [136]. Together, these findings suggest that quanti- |
| [128]. | zation (e.g., 8-bit integer inference) and feature robustness |
| In the field of vulnerability detection, however, inter- | strategies can make ML-driven vulnerability analysis both |
| pretability remains a crucial challenge. While ML-based | lightweight and resilient to adversarial conditions. |
| methods have achieved significant accuracy, many models | Beyond resource efficiency, practical deployment also |
| still fail to understand the semantic meaning of code. They | depends on integration into modern development practices. |
| cannot clearly explain why a segment is flagged as vulnera- | DevSecOps pipelines are increasingly incorporating secu- |
| ble. This undermines trust and hinders adoption in real-world | rity checks directly into the build and release stages, where |
| settings. Recent efforts [73, 129–131] have explored model- | ML-based vulnerability detection can serve as an additional |
| agnostic methods such as feature attribution and visualization | safeguard. Recent reviews highlight effective strategies for |
| to improve interpretability, yet balancing accuracy with trans- | embedding static analysis security testing (SAST), depen- |
| parency continues to be an open problem. Future research | dency scanning analysis (SCA), and anomaly detection into |
| must focus on context-aware explainability—embedding | CI/CD workflows [137]. Complementary work on ML in |
| functional and structural code semantics into explanation- | pipelines demonstrates how automated models can operate |
| s—to make automated vulnerability detection both reliable | as pre-merge gates or nightly batch scanners, offering scal- |
| and developer-friendly. Techniques such as LIME and SHAP | ability without burdening developers [138]. Earlier studies |
| exemplify how interpretability can be enhanced by reveal- | on lightweight AI deployment also confirm that resource- |
| ing which features or code segments contribute most to | constrained integration is feasible, even in edge environments |
| predictions. Although they introduce computational over- | [139]. Collectively, these insights suggest that ML-based |
| head, these mechanisms provide actionable insights that | vulnerability detection can be effectively integrated into |
| build developer trust and support more effective mitigation. | both web-accessible testing services and automated CI/CD |
| Given the high-stakes nature of Android vulnerability detec- | pipelines, thereby ensuring relevance in real-world secure |
| tion, combining predictive performance with explainability | software development lifecycles. |

123

---

## Page 19

From code to security: machine learning approaches in android … Page 19 of 30 17

Fig. 4 Illustration of four principles of XAI by NIST [128]

5 Datasets decided to investigate available datasets tailored to Android

for vulnerability analysis and presented the current status

| Data is essential in machine learning as the foundation for | of available datasets for Android applications in terms of |
| --- | --- |
| model development and training. They offer the raw mate- | usability for further research studies. Table 4 summarizes |
| rial from which models extract patterns and relationships, | the datasets and their useful features. Note that referenced |
| allowing them to make informed predictions. The quality | datasets contain source codes and/or commit history of the |
| and diversity of a dataset significantly impact a model’s abil- | applications generated in vulnerability analysis, meaning this |
| ity to generalize its learning beyond the training data, thereby | does not include malware repositories or similar entities. |
| enhancing its overall performance and reliability. | Geiger et al. [141] created a dataset of 8431 real Android |
| Moreover, datasets are essential for evaluating model per- | apps whose source code is available in 8216 GitHub reposi- |
| formance as benchmarks against which models are tested | tories. The data was gathered through app identification and |
| and compared. They facilitate the identification of biases and | metadata collection and stored in a graph-based database |
| fairness issues inherent in the data, which is crucial for devel- | using Neo4j. This research also highlights the potential uses |
| oping equitable and just algorithms. Additionally, datasets | of the data, including investigations using algorithms from |
| drive innovation by inspiring new solutions to complex prob- | graph theory, and identifies the limitations of the dataset. |
| lems and opening avenues for creative research. | However, upon examining this dataset, we noticed that it |
| Dataset selection and curation impact feature extraction | included codes in languages other than Java, which could |
| and engineering, affecting a model’s predictive accuracy. | potentially confuse future authors interested in studying |
| Specialized datasets tailored to specific domains imbue | Android vulnerability detection using this dataset. This also |
| models with domain-specific knowledge, enhancing their | generates irrelevant data when referencing it in machine |
| contextual relevance and practical application. | learning processes. |
| The most recent review [145] regarding available datasets | F-droid [68], the dataset consists of 1179 applications |
| in the literature was conducted in 2018 and undertakes the | with 4416 different versions and 435,680 total commits. The |
| identification and comprehensive assessment of 31 extant | analysis includes static analysis results obtained from vari- |
| datasets on Android applications. Each dataset is categorized | ous tools. The dataset also includes detailed information on |
| based on specific attributes, including the aggregate count of | each app’s AndroidManifest.xml file, permissions, intents, |
| encompassed applications, the availability of commit his- | and minimum SDK version. This dataset was found to be |
| tory for the applications, the predominant focus on either the | useful for research that requires different versions of the same |
| source code or the executable binaries of the applications, | application to compare the apps and determine vulnerability |
| and the sources harnessed for the assembly of the respec- | across the versions after adding new features to the applica- |
| tive dataset, among other pertinent criteria. Therefore, we | tions. However, after a detailed investigation of this dataset, |

123

*[Image: Page 19 Image]*

---

## Page 20

17 Page 20 of 30 K. E. Arikan et al.

Table 4 Available android

| Krutz et al. [140] | 2017 |
| --- | --- |
| Geiger et al. [141] | 2018 |
| Androvul [142] | 2019 |
| JEMMA[144] | 2023 |
| LVDAndro[72] | 2023 |

(e.g., metrics, static analysis results) for 50,000 Java projects

from the 50 K-C dataset, with over 1.2 million classes and

to entry in ML4Code research by providing the building

summarization, defect prediction, classification, and transla-

and HTTP(s) implementations specific to Android-based

scanned source code from open-source and closed-source

123

code history

1402 Yes Yes F-Droid [68],

GitHub

8431 Yes Yes GitHub, Google

Play

| 16,000 | Yes | No | AndroZoo[143] |
| --- | --- | --- | --- |
| 50,000 (from Java | Yes | No | Major sources |

projects)

15,021 Yes No MobSF [84],

Qark [85]

detection.

datasets.

analysis techniques.

| datasets for vulnerability analysis | Paper | Year | Number of apps | Source | Commit | Sourced from |
| --- | --- | --- | --- | --- | --- | --- |
| it becomes apparent that many are small applications with | applications containing 23 different CWE ID labels. It also |  |  |  |  |  |
| limited real-world usage. | has a 9:11 Vulnerable: non-vulnerable code sample ratio. |  |  |  |  |  |
| JEMMA [144] is an extensible Java dataset designed | Although collecting vulnerable Android code from real- |  |  |  |  |  |
| for ML4Code applications. It is a large-scale, diverse, and | world environments is a good approach, it relies heavily on |  |  |  |  |  |
| high-quality dataset that comes with a considerable amount | certain open-source tools for creating these vulnerable code |  |  |  |  |  |
| of pre-processed information such as metadata, represen- | snippets. As a result, it may be subject to storing false posi- |  |  |  |  |  |
| tations (e.g., code tokens, graphs), and several properties | tives from the tools they have used. |  |  |  |  |  |
| over 8 million methods [85]. JEMMA lowers the barrier | 6 Challenges and limitations |  |  |  |  |  |
| blocks to experiment with source code models and tasks. | Despite significant advancements in Android security anal- |  |  |  |  |  |
| With JEMMA, users can easily train and evaluate several | ysis, several challenges persist, hindering the effectiveness |  |  |  |  |  |
| models, conduct inference, and establish task benchmarks. | and real-world applicability of existing approaches. These |  |  |  |  |  |
| The diversity of representations facilitates training on sev- | challenges primarily stem from the complexity of obfuscated |  |  |  |  |  |
| eral types of model architectures, from graph-based models | applications, the lack of comprehensive real-world datasets, |  |  |  |  |  |
| to models that take ASTs as input and other architectures | and the substantial computational resources required for |  |  |  |  |  |
| such as code2seq, which reason over a bag of ASTs. This | machine-learning-based security analysis. Moreover, inter- |  |  |  |  |  |
| enables users to model source code in various formats and | preting the decisions of machine learning models remains |  |  |  |  |  |
| combinations, extracting valuable insights. ML4Code stands | a crucial issue, as their black-box nature limits their trans- |  |  |  |  |  |
| for Machine Learning for Source Code, a research area focus- | parency | and | usability | in | security-critical | environments. |
| ing on developing machine learning models to handle various | Additionally, risks such as bias in training data and overfit- |  |  |  |  |  |
| tasks related to source code, such as code completion, code | ting pose a threat to the reliability of automated vulnerability |  |  |  |  |  |
| tion. ML4Code is important in software engineering because | To address these challenges, upcoming research should |  |  |  |  |  |
| it enables developers to become faster and more productive | focus on developing comprehensive labeled datasets and |  |  |  |  |  |
| by providing appropriate tool support for source code. With | evaluation metrics, enhancing the interpretability of machine |  |  |  |  |  |
| this dataset, developers can automate repetitive tasks, reduce | learning models, and minimizing biases that affect the gener- |  |  |  |  |  |
| errors, and improve the quality of their code. However, this | alization of detection methods. Transfer learning and domain |  |  |  |  |  |
| proposed dataset does not include the specific routines of | adaptation may offer viable solutions to enhance model |  |  |  |  |  |
| Android applications, such as intent security, privacy issues, | robustness while reducing dependence on extensive labeled |  |  |  |  |  |
| mobile applications. Additionally, it involves some codes that | The following subsections provide an in-depth discus- |  |  |  |  |  |
| Android applications do not have, such as authentication and | sion of the major obstacles faced in this domain, specifically |  |  |  |  |  |
| authorization processes. | examining the impact of obfuscation on Android security |  |  |  |  |  |
| LVDAndro [72] has three different datasets but uses the | testing, the necessity of real-world datasets, and the hard- |  |  |  |  |  |
| one formed by scanning 15,021 APKs. This dataset includes | ware constraints that limit the scalability of ML-driven code |  |  |  |  |  |

---

## Page 21

| From code to security: machine learning approaches in android … | Page 21 of 30 | 17 |
| --- | --- | --- |
| 6.1 Challenges of an obfuscated android APK | Recent research has aimed to develop more resilient tools |  |
| for conducting a security test and its impact | and methods less affected by obfuscation. For example, [151] |  |
| on the analysis | introduced a tool to resist specific obfuscation strategies, such |  |

as structural transformations (e.g., modifications in the con-

| Providing a percentage of Android applications that use | trol flow graph) and dummy code insertion. However, while |
| --- | --- |
| obfuscation tools is challenging, as this information is not | obfuscation-resistant techniques enhance malware detection |
| easily accessible to the public. However, it is quite com- | capabilities, they do not necessarily improve reverse engi- |
| mon for developers to employ code obfuscation to protect | neering and code comprehension. Instead of completely |
| their assets and prevent others from reverse-engineering | pulling the program’s source code, these techniques depend |
| their applications [146]. Among the options available to | on extracting non-code attributes to identify malware. Of |
| Android app developers, ProGuard [147] stands out due | special concern in this era is the emergent trend of multi- |
| to its integration into the Android SDK and user-friendly | layered obfuscation, in which multiple uses of different types |
| design. Conducting a security assessment on an Android | of obfuscation are applied iteratively to produce very intri- |
| APK presents challenges for security testers and researchers. | cate defense systems. Recent studies, including Mirzaei et al. |
| One significant obstacle arises from the increased code | [149, 152], reinforce this observation, demonstrating that lay- |
| complexity caused by obfuscation techniques, which makes | ered obfuscation remains one of the most challenging barriers |
| analyzing and understanding the app’s functionality more | in Android security analysis. |
| difficult [146, 147]. When classes, methods, and variables are | However, conducting a security test on an Android APK is |
| renamed, static code analysis tools can become bewildered, | not impossible. Skilled security testers can effectively iden- |
| leading to difficulties in identifying security vulnerabilities. | tify vulnerabilities by employing analysis, customized tools, |
| Security analysis in Android applications faces two sig- | and dynamic testing techniques. Nevertheless, it requires |
| nificant challenges due to obfuscation techniques: | expertise and persistence compared to testing obfuscated |

APKs. Collaborating with app developers or gaining access

| Misleading automation—Obfuscation methods are delib- | to the APK version can significantly assist security testing |
| --- | --- |
| erately employed to bypass automated detection mecha- | endeavors. If researchers could discover ways to effectively |
| nisms and obstruct forensic analysis. For instance, adver- | test these applications without relying on source code, it |
| sarial attacks can deceive machine-learning-based obfus- | would pave the way for future directions in app testing in |
| cation detection techniques. Furthermore, straightforward | real-world scenarios. |

approaches like repacking and manifest modifications can

| render traditional application fingerprinting techniques, such | 6.2 The importance of a dataset with real-world |
| --- | --- |
| as hash-based identification, ineffective. | information |

Complexity in manual analysis—Some obfuscation tech-

| niques hinder automated methods and significantly compli- | Real-world vulnerabilities exhibit a higher degree of com- |
| --- | --- |
| cate manual analysis. When code is heavily encrypted or | plexity, necessitating the consideration and analysis of con- |
| cluttered with excessive junk code, traditional static analysis | trol flow, data flow, dominance relationships, and various |
| methods become impractical. | other interdependencies among code elements. This paper |

[121] presents a systematic study focusing on various aspects

| These issues indicate an increasing complexity in Android | of Deep Learning-based Vulnerability detection to iden- |
| --- | --- |
| security analysis, especially in automated methods that | tify real-world vulnerabilities efficiently. Through empirical |
| depend on highly skilled analysts and extensive forensic | analysis, the authors highlighted the deficiencies in current |
| procedures. Various tools have been created to detect and | datasets and models that may hinder the practical applicabil- |
| even deobfuscate applications, with some methods yielding | ity of these techniques. They also proposed a framework for |
| encouraging outcomes, particularly in managing obfuscation | collecting a real-world dataset for C/C++ languages. Despite |
| layers within Dalvik bytecode. However, our review noticed | these efforts, a significant challenge remains: the availability |
| that most of these automated solutions are not publicly avail- | of high-quality, real-world datasets for effective ML-based |
| able—a finding that aligns with [148], who observed that | vulnerability detection. |
| many developed tools remain undisclosed. | One of the primary challenges in leveraging machine |
| Another limitation of existing literature is the insufficient | learning for Android vulnerability detection is the need for |
| focus on obfuscation techniques applied to native libraries. | large-scale, real-world datasets. The applicability of exist- |
| Multiple studies [149, 150] have emphasized that obfus- | ing approaches remains limited in practical settings due |
| cated native libraries can conceal malicious activities and | to the extensive training data required to achieve reliable |
| evade certain detection techniques, but existing solutions still | results. Many models rely heavily on carefully curated fea- |
| largely overlook this aspect. | ture engineering techniques to approximate the complexity |

123

---

## Page 22

| 17 | Page 22 of 30 | K. E. Arikan et al. |
| --- | --- | --- |
| of real-world applications. However, these models struggle | reproducibility. AndroidTimeMachine [141] differs concep- |  |
| to generalize effectively without diverse and representative | tually, offering a large graph-based dataset of 8431 real apps |  |
| datasets that capture various vulnerabilities across develop- | with commit histories and Google Play metadata. At the |  |
| ment practices. Furthermore, most publicly available datasets | same time, repository and package deduplication are applied; |  |
| are either synthetic, outdated, or lack the contextual rich- | the dataset does not provide any predefined ML benchmark |  |
| ness necessary to reflect real-world software vulnerabilities. | splits, leaving researchers to design their own. Finally, Krutz |  |
| This limitation is further evident when comparing real-world | et al. [140] focus on analyzing 1402 F-Droid repositories at |  |
| datasets with commonly used synthetic datasets. | the commit level, including all historical versions of Android- |  |
| Based on their experimental results, synthetic and semi- | Manifest.xml; here, duplication is not treated as bias but as |  |
| synthetic datasets like SARD [153] and Juliet [154] (com- | an inherent feature, although this would make the dataset |  |
| posed of much simpler code snippets) result in a large number | unsuitable for direct ML benchmarking. |  |
| of duplicates. In contrast, real-world vulnerabilities are much | Overall, none of the datasets explicitly examine the nega- |  |
| more complex and have far fewer duplicates [121]. Indeed, | tive effect of code duplication on ML performance, as shown |  |
| duplicate instances within the training set can induce a DL | in Table 5, which is a limitation noted in the literature. |  |
| model to acquire irrelevant features. Furthermore, common | Consequently, future work should not only provide standard- |  |
| examples between the training and test sets pose challenges | ized and well-documented train/test partitions but also apply |  |
| in fairly comparing distinct DL models designed for the | project-level and semantic deduplication strategies, ensuring |  |
| vulnerability prediction task. In an ideal scenario, a DL- | that benchmark results genuinely reflect model generaliza- |  |
| based model should undergo training and testing on a dataset | tion rather than memorization of recurring code fragments. |  |

where all examples are unique. The existence of duplications

tends to inflate the overall performance of a method, as evi-

dent from the observed discrepancy in the baseline results

[155]. This discrepancy suggests that evaluations based on

such datasets may not accurately reflect a model’s actual

performance in real-world settings, leading to unreliable vul-

nerability detection in practical applications.

6.3 Limitations of existing benchmarks and splitting

strategies

Addressing dataset coverage, train/test splitting strategies,

and the implications of code duplication is crucial, as

these factors directly affect the validity, generalizability,

and empirical reliability of ML-based vulnerability predic-

tion studies. In particular, the study [155] demonstrates how

duplicated or recurring code fragments can artificially inflate

model performance, since models may simply recognize

code previously seen in the training set rather than truly gen-

eralize to unseen cases.

Existing datasets used for Android security and ML4Code

[144] studies reveal significant limitations in terms of train-

ing/testing splits and duplication control. LVDAndro [72]

adopts a fixed 80:20 random split and applies a basic dedupli-

cation step at the line level; however, it does not ensure that

near-duplicate code fragments across training and test sets

are eliminated, thus risking inflated performance. AndroVul

[142] relies on tenfold cross-validation and removes dupli-

as the reuse of third-party libraries. JEMMA [144] pro-

123

6.4 Hardware resources

Considering the necessity for a substantial training dataset

and multiple hidden layers, machine learning model train-

ing frequently demands high-performance processing units,

such as Graphics Processing Units (GPUs), and significant

memory capacity [156, 157]. A user survey investigation

[157] underscores the importance of specialized hardware for

machine learning training. However, these hardware require-

ments present challenges to researchers operating within

limited hardware resources.

Researchers have been actively exploring ways to opti-

mize resource utilization in response to the challenges

posed by the demanding hardware requirements for train-

ing machine learning models. Several studies have proposed

techniques to improve the efficiency of training processes in

hardware environments. For example, methods such as model

compression and algorithmic optimizations have shown

promise in reducing the burden on processing units and mem-

ory [4]-5]. Moreover, advancements in hardware technology,

such as the development of energy-efficient processors, offer

potential solutions for overcoming these challenges [6]. As

this field progresses, it becomes crucial to find a balance

between the increasing demands of machine-learning models

and the practical limitations imposed by hardware resources.

| cate APKs, but fails to address code-level duplication, such | 7 Threats to the validity of the review |
| --- | --- |
| vides more systematic filtering through clone detection and | While this literature review was conducted to cover key stud- |
| redundant code removal, yet it delegates train/test split | ies on vulnerability analysis for Android applications, it is |
| decisions entirely to the user, which hinders experimental | important to acknowledge that the results obtained may not |

---

## Page 23

From code to security: machine learning approaches in android … Page 23 of 30 17

Table 5 Analysis of available datasets in terms of limitations

level)

APKs removed)

removal)

7.1 Construct validity

Potential threats to construct validity arise from the use

of search term-based queries in repositories. It is crucial

to recognize the possible existence of high-quality papers

excluded from this study’s scope due to their absence from

key research repositories like the ACM Digital Library, IEE-

EXplore Digital Library, Web of Science, and Springer Link.

To address this limitation, Google Scholar was utilized as an

additional resource to identify studies that may have been

overlooked. However, it is acknowledged that some rele-

vant publications may still be missing from the compiled

dataset. Another aspect concerns construct validity, where the

possibility of minor errors during the filtration process—en-

compassing inclusion and exclusion criteria—can introduce

bias. In response to this challenge, a comprehensive analysis

of the publication list was conducted, including a detailed

cross-referencing of primary studies to identify and correct

potential errors and discrepancies.

analysis

duplication causes

train/test overlap

(e.g., SDKs/libraries) is

not addressed

standardization

user for ML tasks

duplication is an integral

part of the methodology

issue, a key strategy involves engaging the original authors

for verification purposes, thereby enhancing the accuracy and

integrity of the extracted and analyzed information.

7.3 External validity

External validity pertains to the generalizability of the

outcomes derived from the primary investigations. The ana-

lytical scrutiny, constituting an integral facet of this review,

was executed on a corpus of research publications from

2017 to 2024, encompassing a comprehensive appraisal of

contemporary Android applications regarding vulnerabil-

ity detection and prediction methodologies. This temporal

boundary was strategically selected, considering the pro-

nounced upsurge in ML techniques harnessed for vulnera-

bility detection during this interval, attributable to notable

advancements in software security and artificial intelligence.

diverge when assessed across disparate temporal epochs is

123

| Dataset | Train/Test Split | Duplication handling | Duplication impact | Notes |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| LVDAndro [72] | Fixed 80:20 random split | Basic (same line | + | same label | None | Unclear whether code |
| AndroVul [142] | Tenfold cross-validation | APK hash-level (duplicate | None | Code-level duplication |  |  |
| JEMMA [144] | User-defined, no predefined | More comprehensive (clone | None | Benchmarking is left to |  |  |
| split | detection, redundant | the user; lack of |  |  |  |  |
| Geiger et al. | None (commit | + | Google Play | Repository/Package-level | None | Graph-based commit |
| [141] | metadata) | deduplication | dataset; split left to the |  |  |  |
| Krutz et al. [140] | None (statistical analysis of | None (all app commits | None | The goal is permission |  |  |
| commits) | intentionally included) | evolution analysis; |  |  |  |  |
| include all relevant studies due to certain limitations encoun- | covering data extraction and subsequent analytical processes. |  |  |  |  |  |
| tered during the review process. Consequently, this section | Given this, careful cross-validation strengthened data collec- |  |  |  |  |  |
| outlines potential sources of vulnerability to the study’s | tion, consolidating results after agreement among all authors |  |  |  |  |  |
| validity, categorized into construct, internal, external, and | regarding the comparative findings. Despite these careful |  |  |  |  |  |
| conclusion validity, while also detailing the measures taken | measures, the possibility of errors in the data extraction and |  |  |  |  |  |
| to address these concerns. | analytical phases remains a consideration. To address this |  |  |  |  |  |
| 7.2 Internal validity | Acknowledging that the prevailing trends and dynamics may |  |  |  |  |  |
| Internal validity refers to the strength of the data extraction | vital. Consequently, it is plausible that certain seminal and |  |  |  |  |  |
| and analysis procedures, which is a crucial aspect of the over- | exhaustive studies predating the stipulated period may not be |  |  |  |  |  |
| all review methodology. This effort involved significant work | encompassed within the present analysis. |  |  |  |  |  |

---

## Page 24

17 Page 24 of 30 K. E. Arikan et al.

8 Conclusion throughout the development process rather than waiting until

the integration of ML techniques into software engineering

Furthermore, bridging the gap between technical insight

and developer-friendly tools remains paramount for sustain-

parency and trust in automated analysis. Equally important is

underexplored yet critical for real-world adoption. Address-

ing these challenges will contribute to a more effective and

vulnerability detection scenarios.

9 Future directions

While detection mechanisms are crucial in identifying secu-

rity vulnerabilities, they are insufficient for the app devel-

opment community. Future research should investigate how

these detection techniques can be seamlessly incorporated

123

the entire application is finished.

findings.

Author contribution K.E.A . and E.N.Y. conceptualized and structured

the research framework, conducted the systematic literature review fol-

the design and creation of all visual representations included in the

manuscript. S.G. provided expertise during the manuscript preparation,

E.N.Y. , S.M.D. , and S.G.

Funding This research did not receive any specific grant from funding

Data availability No datasets were generated or analysed during the

current study.

Declarations

Conflict of interests The authors declare no competing interests.

References

| In response to the increasing demand for Android applica- | Another major challenge is the lack of automated methods |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tion development, developers are constantly trying to meet | for determining the root causes of vulnerabilities. Research |  |  |  |  |  |  |
| the demand with new software. It is important to con- | should focus on integrating XAI methodologies into vulnera- |  |  |  |  |  |  |
| sider security concepts while developing new software. This | bility detection frameworks to address this issue. Combining |  |  |  |  |  |  |
| comprehensive review examines the latest techniques for | LLMs and XAI techniques can enhance vulnerability iden- |  |  |  |  |  |  |
| detecting vulnerabilities in Android applications, encom- | tification and the interpretability of results. By providing |  |  |  |  |  |  |
| passing research from 2017 to 2024. The review examines | detailed insights into why certain code segments are clas- |  |  |  |  |  |  |
| application and code analysis methods, exploring how ML | sified as vulnerable, these approaches could bridge the gap |  |  |  |  |  |  |
| and DL techniques can be applied for vulnerability detec- | between complex AI-driven security analysis and developer- |  |  |  |  |  |  |
| tion. Additionally, recent advances in LLMs have introduced | friendly tools, improving transparency and usability. |  |  |  |  |  |  |
| new possibilities in this field, as they exhibit a strong ability | Additionally, preserving the semantic integrity of code |  |  |  |  |  |  |
| to analyze code structures and identify potential vulner- | while applying ML-based detection techniques remains a |  |  |  |  |  |  |
| abilities. However, while some studies report promising | significant challenge. Current studies often overlook the |  |  |  |  |  |  |
| results, LLM-based vulnerability detection still faces chal- | importance of interpreting code within its broader functional |  |  |  |  |  |  |
| lenges, particularly in handling obfuscated and complex code | and structural context, which is crucial for accurate and |  |  |  |  |  |  |
| structures, as well as in ensuring balanced, duplication-free | reliable vulnerability detection. Future work should explore |  |  |  |  |  |  |
| datasets for reliable evaluation. | context-aware analysis techniques that ensure vulnerabilities |  |  |  |  |  |  |
| The findings presented in this review serve as an invita- | are detected without introducing excessive false positives. |  |  |  |  |  |  |
| tion to practitioners and researchers, encouraging them to | Future research should also prioritize dataset quality, |  |  |  |  |  |  |
| propose methods, tools, and techniques for further explo- | addressing duplication, imbalance, and outdated bench- |  |  |  |  |  |  |
| ration and development. The ultimate objective is to facilitate | marks, to ensure empirical validity and reproducibility of |  |  |  |  |  |  |
| applications while ensuring ease of use, flexibility, and main- | Finally, strategically integrating LLMs within phased |  |  |  |  |  |  |
| tainability. While traditional ML and DL techniques remain | AI-driven security frameworks could unlock new capa- |  |  |  |  |  |  |
| pivotal, incorporating LLMs offers a new avenue for secu- | bilities. By combining ML, DL, XAI, and LLMs, future |  |  |  |  |  |  |
| rity analysis. However, more research is needed to optimize | systems can deliver contextualized, explainable, and action- |  |  |  |  |  |  |
| these models for practical use and ensure their effectiveness | able insights—paving the way for secure, intelligent, and |  |  |  |  |  |  |
| in real-world Android development environments. | developer-oriented Android applications. |  |  |  |  |  |  |
| ing robust security practices. Future research should focus on | lowing the PRISMA guidelines, and authored the primary manuscript |  |  |  |  |  |  |
| developing models that identify vulnerabilities and provide | content. | K.E.A. | , | E.N.Y. | , and | S.M.D. | collectively participated in the |
| meaningful explanations for their decisions, ensuring trans- | selection, critical analysis, and synthesis of relevant publications and |  |  |  |  |  |  |
| the evaluation of model scalability, inference speed, and inte- | contributed to the interpretation of results, and supported manuscript |  |  |  |  |  |  |
| gration feasibility into DevSecOps pipelines, which remain | revisions. All authors reviewed the manuscript, including | K.E.A. | , |  |  |  |  |
| interpretable application of machine learning in real-world | agencies in the public, commercial, or not-for-profit sectors. |  |  |  |  |  |  |
| into Android development environments as tools or plug- | 1. Kazmi, S.H.A., Qamar, F., Hassan, R., Nisar, K., Chowdhry, |  |  |  |  |  |  |
| ins. Such integration would enable developers to test security | B.S.: Survey on joint paradigm of 5G and SDN emerging mobile |  |  |  |  |  |  |

---

## Page 25

| From code to security: machine learning approaches in android … | Page 25 of 30 | 17 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| technologies: architecture, security, challenges and research direc- | and | malicious | code | localization. | Empirical | Software | Engi- |  |  |
| tions. Wirel. Pers. Commun. | 130 | (4), 2753–2800 (2023). https:// | neering. https://link.springer.com/article/https://doi.org/10.1007/ |  |  |  |  |  |  |
| doi.org/10.1007/s11277-023-10402-7 | s10664-017-9539-8. Accessed 12 Mar 2025. [Online]. |  |  |  |  |  |  |  |  |
| 2. Al-Ansi, A.M., Jaboob, M., Garad, A., Al-Ansi, A.: Analyzing | 18. Carpenter, P.: Using the Predict, Prevent, Detect, Respond Frame- |  |  |  |  |  |  |  |  |
| augmented reality (AR) and virtual reality (VR) recent develop- | work to Communicate Your Security Program Strategy. https:// |  |  |  |  |  |  |  |  |
| ment in education. Soc Sci & Humanit Open | 8 | (1), 100532 (2023). | www.gartner.com/en/documents/3286317. Accessed 12 March |  |  |  |  |  |  |
| https://doi.org/10.1016/j.ssaho.2023.100532 | 2025. [Online]. |  |  |  |  |  |  |  |  |
| 3. CVE: Common Vulnerabilities and Exposures: https://www.cve. | 19. Garg, S., Baliyan, N.: Machine learning based android vulnera- |  |  |  |  |  |  |  |  |
| org/about/overview. Accessed 12 March 2025 | bility detection: a roadmap. In: Kanhere, S., Patil, V.T., Sural, S., |  |  |  |  |  |  |  |  |
| 4. Dowd, M., McDonald, J., Schuh, J.: The art of software security | Gaur, M.S. (eds.) Information Systems Security, Springer Inter- |  |  |  |  |  |  |  |  |
| assessment: identifying and preventing software vulnerabilities. | national Publishing, Cham (2020), pp. 87–93. https://doi.org/10. |  |  |  |  |  |  |  |  |
| Pearson Education (2006). | 1007/978-3-030-65610-2_6. |  |  |  |  |  |  |  |  |
| 5. Pam, | N.H.: | Detection | of | recurring | software | vulnerabilities. | 20. Lee, J., Babcock, J., Pham, T.S., Bui, T.H.: Myounggu Kang |  |  |
| In: Proceedings of the 25th IEEE/ACM International Confer- | Smart city as a social transition towards inclusive development |  |  |  |  |  |  |  |  |
| ence on Automated Software Engineering. https://dl.acm.org/doi/ | through technology: a tale of four smart cities. https://www.tand |  |  |  |  |  |  |  |  |
| abs/https://doi.org/10.1145/1858996.1859089. Accessed 12 Mar | fonline.com/doi/full/https://doi.org/10.1080/12265934.2022.20 |  |  |  |  |  |  |  |  |
| 2025. [Online]. | 74076. Accessed 12 March 2025. [Online]. |  |  |  |  |  |  |  |  |
| 6. Piessens, F.: A taxonomy of causes of software vulnerabilities | 21. Ghaffarian, S.M., Shahriari, H.R.: Software vulnerability analysis |  |  |  |  |  |  |  |  |
| in internet software. In: Vouk, M. (ed.), The 13th International | and discovery using machine-learning and data-mining tech- |  |  |  |  |  |  |  |  |
| Symposium on Software Reliability Engineering, Supplementary | niques: a survey. ACM Comput Survey: | 50 | (4). https://dl.acm. |  |  |  |  |  |  |
| Proceedings of the 13th International Symposium on Software | org/doi/abs/https://doi.org/10.1145/3092566. Accessed 12 March |  |  |  |  |  |  |  |  |
| Reliability Engineering, pp. 47–52. Annapolis, Maryland, USA, | 2025. [Online]. |  |  |  |  |  |  |  |  |
| November 12–15 (2002) | 22. Aslan, Ö., Aktu˘ | g, S.S., Ozkan-Okay, M., Yilmaz, A.A., Akin, E.: |  |  |  |  |  |  |  |
| 7. Abdalkareem, R., Shihab, E., Rilling, J.: On code reuse from | A comprehensive review of cyber security vulnerabilities, threats, |  |  |  |  |  |  |  |  |
| StackOverflow: an exploratory study on Android apps. Inf. Softw. | attacks, and solutions. Electronics | 12 | (6), 6 (2023). https://doi.org/ |  |  |  |  |  |  |
| Technol. | 88 | , 148–158 (2017). https://doi.org/10.1016/j.infsof. | 10.3390/electronics12061333 |  |  |  |  |  |  |
| 2017.04.005 | 23. Tugwell, P., Tovey, D.: PRISMA 2020. J. Clin. Epidemiol. | 134 | , |  |  |  |  |  |  |
| 8. Fischer, F., et al.: Stack overflow considered harmful? The | A5–A6 (2021). https://doi.org/10.1016/j.jclinepi.2021.04.008 |  |  |  |  |  |  |  |  |
| Impact of Copy&Paste on Android Application Security. In: | 24. Garg, S., Baliyan, N.: Data on vulnerability detection in Android. |  |  |  |  |  |  |  |  |
| 2017 IEEE Symposium on Security and Privacy (SP), May 2017, | Data Brief | 22 | , 1081–1087 (2018). https://doi.org/10.1016/j.dib. |  |  |  |  |  |  |
| pp. 121–136. https://doi.org/10.1109/SP.2017.31. | 2018.12.038 |  |  |  |  |  |  |  |  |
| 9. Zhang, H., Wang, S., Li, H., Chen, T.-H., Hassan, A.E.: A study | 25. Kapitsaki, G.M.: Examining the Privacy Vulnerability Level of |  |  |  |  |  |  |  |  |
| of C/C++ code weaknesses on Stack Overflow. IEEE Trans. | Android Applications. In: 15th International conference on web |  |  |  |  |  |  |  |  |
| Softw. Eng. | 48 | (7), 2359–2375 (2022). https://doi.org/10.1109/ | information systems and technologies. https://doi.org/10.5220/00 |  |  |  |  |  |  |
| TSE.2021.3058985 | 07955100002366 (2019) |  |  |  |  |  |  |  |  |
| 10. Mäntylä, M.V., Lassenius, C.: What types of defects are really dis- | 26. Rathod, J., Bhatti, D.: Building comprehensive dataset: android |  |  |  |  |  |  |  |  |
| covered in code reviews? IEEE Trans. Softw. Eng. | 35 | (3), 430–448 | file and unstructured data collection from APKs for enhanced vul- |  |  |  |  |  |  |
| (2009). https://doi.org/10.1109/TSE.2008.71 | nerability detection. Int. J. Comput. Appl. Technol. Res. (2023). |  |  |  |  |  |  |  |  |
| 11. McQueen, M.A., McQueen, T.A., Boyer, W.F., Chaffin, M.R.: | https://doi.org/10.7753/IJCATR1212.1004. |  |  |  |  |  |  |  |  |
| Empirical Estimates and Observations of 0Day Vulnerabilities. | 27. Garg, S., Baliyan, N.: A novel parallel classifier scheme for vul- |  |  |  |  |  |  |  |  |
| In: 2009 42nd Hawaii International Conference on System Sci- | nerability detection in Android. Comput. Electr. Eng. | 77 | , 12–26 |  |  |  |  |  |  |
| ences, January 2009, pp. 1–12. https://doi.org/10.1109/HICSS.20 | (2019). https://doi.org/10.1016/j.compeleceng.2019.04.019 |  |  |  |  |  |  |  |  |
| 09.186. | 28. Lochanan, | A., | Jaysankar, | M.R., | Subramanian, | N.: | Permis- |  |  |
| 12. Czerwonka, J., Greiler, M., Tilford, J.: Code reviews do not find | sions based android vulnerability detection and classification |  |  |  |  |  |  |  |  |
| bugs. How the Current Code Review Best Practice Slows Us | based on severity using machine learning. In: Recent Develop- |  |  |  |  |  |  |  |  |
| Down. In: 2015 IEEE/ACM 37th IEEE International Conference | ments in Electronics and Communication Systems, IOS Press, |  |  |  |  |  |  |  |  |
| on Software Engineering, May 2015, pp. 27–28. https://doi.org/ | pp. 200–207. https://doi.org/10.3233/ATDE221258 (2023) |  |  |  |  |  |  |  |  |
| 10.1109/ICSE.2015.131. | 29. Zhan, X., et al.: Research on third-party libraries in Android |  |  |  |  |  |  |  |  |
| 13. Google: | List | of | all | products | and | related | security | vulner- | apps: a taxonomy and systematic literature review. IEEE Trans. |
| abilities. https://www.cvedetails.com/product-list/product_type-/ | Softw. Eng. | 48 | (10), 4181–4213 (2022). https://doi.org/10.1109/ |  |  |  |  |  |  |
| vendor_id-1224/firstchar-/page-1/Google.html. Accessed 12 Mar | TSE.2021.3114381 |  |  |  |  |  |  |  |  |
| 2025. [Online]. | 30. Wei, X., Wolf, M.: A survey on HTTPS implementation by |  |  |  |  |  |  |  |  |
| 14. Nikolaeva, A., Lin, Y.-T., Nello-Deakin, S., Rubin, O., von Schön- | Android apps: issues and countermeasures. Appl. Comput. Infor- |  |  |  |  |  |  |  |  |
| feld, K.C.: Living without commuting: experiences of a less | matics | 13 | (2), 101–117 (2017). https://doi.org/10.1016/j.aci.2016. |  |  |  |  |  |  |
| mobile life under COVID-19. Mobilities | 18 | (1), 1–20 (2023). | 10.001 |  |  |  |  |  |  |
| https://doi.org/10.1080/17450101.2022.2072231 | 31. Abdullah, H., Zeebaree, S.R.M.: Android mobile applications |  |  |  |  |  |  |  |  |
| 15. Wei, Z., et al.: Integrated sensing and communication sig- | vulnerabilities and prevention methods: a review. In: 2021 2nd |  |  |  |  |  |  |  |  |
| nals toward 5G-A and 6G: a survey. IEEE Internet Things J. | Information Technology to Enhance e-learning and Other Appli- |  |  |  |  |  |  |  |  |
| 10 | (13), 11068–11092 (2023). https://doi.org/10.1109/JIOT.2023. | cation (IT-ELA), December 2021, pp. 148–153. https://doi.org/ |  |  |  |  |  |  |  |
| 3235618 | 10.1109/IT-ELA52201.2021.9773615. |  |  |  |  |  |  |  |  |
| 16. von Solms, B., von Solms, R.: Cybersecurity and information | 32. Automated security testing of Android applications for secure |  |  |  |  |  |  |  |  |
| security – what goes where? Info & Comput Security | 26 | (1), 2–9 | mobile development. In: IEEE Conference Publication, IEEE |  |  |  |  |  |  |
| (2018). https://doi.org/10.1108/ICS-04-2017-0025 | Xplore. | https://ieeexplore.ieee.org/abstract/document/9155681. |  |  |  |  |  |  |  |
| 17. Narayanan, A., Chandramohan, M., Chen, L., Liu, Y.: A multi- | Accessed 12 March 2025. [Online]. |  |  |  |  |  |  |  |  |

view context-aware approach to Android malware detection

123

---

## Page 26

| 17 | Page 26 of 30 | K. E. Arikan et al. |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33. Casilari, E., Luque, R., Morón, M.-J.: Analysis of Android device- | Springer International Publishing, Cham, pp. 18–33. https://doi. |  |  |  |  |  |  |  |  |  |
| based solutions for fall detection. Sensors | 15 | (8), 8 (2015). https:// | org/10.1007/978-3-030-41579-2_2 (2020) |  |  |  |  |  |  |  |
| doi.org/10.3390/s150817827 | 51. Han, H., Lim, S., Suh, K., Park, S., Cho, S., Park, M.: Enhanced |  |  |  |  |  |  |  |  |  |
| 34. Secure coding practices in Java. In: Proceedings of the 40th Inter- | android malware detection: an svm-based machine learning |  |  |  |  |  |  |  |  |  |
| national Conference on Software Engineering. https://dl.acm.org/ | approach. In: 2020 IEEE International Conference on Big Data |  |  |  |  |  |  |  |  |  |
| doi/abs/https://doi.org/10.1145/3180155.3180201. Accessed: 12 | and Smart Computing (BigComp), February 2020, pp. 75–81. |  |  |  |  |  |  |  |  |  |
| March 2025. [Online]. | https://doi.org/10.1109/BigComp48618.2020.00-96 (2020) |  |  |  |  |  |  |  |  |  |
| 35. Definition of ARTIFICIAL INTELLIGENCE. https://www.merr | 52. Mahindru, A., Sangal, A.L.: Feature-based semi-supervised learn- |  |  |  |  |  |  |  |  |  |
| iam-webster.com/dictionary/artificial+intelligence. Accessed 25 | ing to detect malware from android. In: Satapathy, S.C., Jena, |  |  |  |  |  |  |  |  |  |
| March 2025. [Online]. | A.K., Singh, J., Bilgaiyan, S. (eds.) Automated Software Engi- |  |  |  |  |  |  |  |  |  |
| 36. Mitchell, T.M.: Machine Learning. McGraw-Hill (1997). | neering: A Deep Learning-Based Approach, Springer Interna- |  |  |  |  |  |  |  |  |  |
| 37. Kelleher, J.D.: Deep Learning. MIT Press (2019). | tional Publishing, Cham, pp. 93–118. https://doi.org/10.1007/ |  |  |  |  |  |  |  |  |  |
| 38. Explainable | Artificial | Intelligence. | DARPA. | https://www.da | 978-3-030-38006-9_6 (2020) |  |  |  |  |  |
| rpa.mil/research/programs/explainable-artificial-intelligence. | 53. Mantoo, B.A., Khurana, S.S.: Static, dynamic and intrinsic fea- |  |  |  |  |  |  |  |  |  |
| Accessed 25 March 2025. [Online]. | tures based android malware detection using machine learning. |  |  |  |  |  |  |  |  |  |
| 39. Garg, S., Baliyan, N.: Android security assessment: a review, | In: Singh, P.K., Kar, A.K., Singh, Y., Kolekar, M.H., Tanwar, S. |  |  |  |  |  |  |  |  |  |
| taxonomy and research gap study. Comput. Secur. | 100 | , 102087 | (eds.) Proceedings of ICRIC 2019, Springer International Pub- |  |  |  |  |  |  |  |
| (2021). https://doi.org/10.1016/j.cose.2020.102087 | lishing, Cham, pp. 31–45. https://doi.org/10.1007/978-3-030-29 |  |  |  |  |  |  |  |  |  |
| 40. Li, L., et al.: Static analysis of android apps: a systematic literature | 407-6_4 (2020) |  |  |  |  |  |  |  |  |  |
| review. Inf. Softw. Technol. | 88 | , 67–95 (2017). https://doi.org/10. | 54. Martín, I., Hernández, J.A., de los Santos, S.: Machine-learning |  |  |  |  |  |  |  |
| 1016/j.infsof.2017.04.001 | based analysis and classification of Android malware signatures. |  |  |  |  |  |  |  |  |  |
| 41. Vallée-Rai, R., Co, P., Gagnon, E., Hendren, L., Lam, P., Sun- | Future Gener. Comput. Syst. | 97 | , 295–305 (2019). https://doi.org/ |  |  |  |  |  |  |  |
| daresan, V.: Soot: a Java bytecode optimization framework. In: | 10.1016/j.future.2019.03.006 |  |  |  |  |  |  |  |  |  |
| CASCON First Decade High Impact Papers, in CASCON ’10. | 55. Nguyen-Vu, L., Ahn, J., Jung, S.: Android fragmentation in mal- |  |  |  |  |  |  |  |  |  |
| USA, IBM Corp., November 2010, pp. 214–224. https://doi.org/ | ware detection. Comput. Secur. | 87 | , 101573 (2019). https://doi. |  |  |  |  |  |  |  |
| 10.1145/1925805.1925818. | org/10.1016/j.cose.2019.101573 |  |  |  |  |  |  |  |  |  |
| 42. Vallée-Rai, R., Hendren, L.J.: Jimple: Simplifying Java Bytecode | 56. Sharmeen, S., Huda, S., Abawajy, J., Hassan, M.M.: An adaptive |  |  |  |  |  |  |  |  |  |
| for Analyses and Transformations, Request PDF. https://www. | framework against android privilege escalation threats using deep |  |  |  |  |  |  |  |  |  |
| researchgate.net/publication/243776080_Jimple_Simplifying_ | learning and semi-supervised approaches. Appl. Soft Comput. | 89 | , |  |  |  |  |  |  |  |
| Java_Bytecode_for_Analyses_and_Transformations. | Accessed | 106089 (2020). https://doi.org/10.1016/j.asoc.2020.106089 |  |  |  |  |  |  |  |  |
| 12 March 2025. [Online]. | 57. Pang, Y., Xue, X., Wang, H.: Predicting vulnerable software com- |  |  |  |  |  |  |  |  |  |
| 43. Senanayake, J., Kalutarage, H., Al-Kadri, M.O., Petrovski, A., | ponents through deep neural network. In: Proceedings of the |  |  |  |  |  |  |  |  |  |
| Piras, L.: Android source code vulnerability detection: a system- | 2017 International Conference on Deep Learning Technologies, |  |  |  |  |  |  |  |  |  |
| atic literature review. ACM Comput. Surv. | 55 | (9), 1–37 (2023). | in ICDLT ’17. New York, NY, USA, June 2017. Association |  |  |  |  |  |  |  |
| https://doi.org/10.1145/3556974 | for Computing Machinery, pp. 6–10. https://doi.org/10.1145/30 |  |  |  |  |  |  |  |  |  |
| 44. Sharma, T. et al.: A Survey on Machine Learning Techniques for | 94243.3094245 (2017) |  |  |  |  |  |  |  |  |  |
| Source Code Analysis, 13 September, arXiv: arXiv:2110.09610. | 58. Wu, F., Wang, J., Liu, J., Wang, W.: Vulnerability detection |  |  |  |  |  |  |  |  |  |
| https://doi.org/10.48550/arXiv.2110.09610 (2022) | with deep learning. In: 2017 3rd IEEE International Confer- |  |  |  |  |  |  |  |  |  |
| 45. Mehtab, A., et al.: AdDroid: rule-based machine learning frame- | ence on Computer and Communications (ICCC), December |  |  |  |  |  |  |  |  |  |
| work for Android malware analysis. Mob. Networks Appl. | 25 | (1), | 2017, pp. 1298–1302. https://doi.org/10.1109/CompComm.2017. |  |  |  |  |  |  |  |
| 180–192 (2020). https://doi.org/10.1007/s11036-019-01248-0 | 8322752 (2017) |  |  |  |  |  |  |  |  |  |
| 46. Appice, A., Andresini, G., Malerba, D.: Clustering-aided multi- | 59. Zhuo, L., Zhimin, G., Cen, C.: Research on android intent security |  |  |  |  |  |  |  |  |  |
| view classification: a case study on Android malware detection. | detection based on machine learning. In: 2017 4th International |  |  |  |  |  |  |  |  |  |
| J. Intell. Inf. Syst. | 55 | (1), 1–26 (2020). https://doi.org/10.1007/s1 | Conference on Information Science and Control Engineering |  |  |  |  |  |  |  |
| 0844-020-00598-6 | (ICISCE), July 2017, pp. 569–574. https://doi.org/10.1109/IC |  |  |  |  |  |  |  |  |  |
| 47. Liu, X., Zhang, J., Lin, Y., Li, H.: ATMPA: attacking machine | ISCE.2017.124 (2017) |  |  |  |  |  |  |  |  |  |
| learning-based | malware | visualization | detection | methods | via | 60. Bilgin, Z., Ersoy, M.A., Soykan, E.U., Tomur, E., Çomak, P., |  |  |  |  |
| adversarial examples. In: Proceedings of the International Sympo- | Karaçay, L.: Vulnerability prediction from source code using |  |  |  |  |  |  |  |  |  |
| sium on Quality of Service, in IWQoS ’19. New York, NY, USA, | machine | learning. | IEEE | Access | 8 | , | 150672–150684 | (2020). |  |  |
| June 2019. Association for Computing Machinery, pp. 1–10. | https://doi.org/10.1109/ACCESS.2020.3016774 |  |  |  |  |  |  |  |  |  |
| https://doi.org/10.1145/3326285.3329073. | 61. Gupta, A., Suri, B., Kumar, V., Jain, P.: Extracting rules for vul- |  |  |  |  |  |  |  |  |  |
| 48. Yuan, Z., Lu, Y., Xue, Y.: Droiddetector: android malware char- | nerabilities detection with static metrics using machine learning. |  |  |  |  |  |  |  |  |  |
| acterization and detection using deep learning. Tsinghua Sci. | Int. J. Syst. Assur. Eng. Manag. | 12 | (1), 65–76 (2021). https://doi. |  |  |  |  |  |  |  |
| Technol. | 21 | (1), 114–123 (2016). https://doi.org/10.1109/TST. | org/10.1007/s13198-020-01036-0 |  |  |  |  |  |  |  |
| 2016.7399288 | 62. Kim, S., Yeom, S., Oh, H., Shin, D., Shin, D.: Automatic malicious |  |  |  |  |  |  |  |  |  |
| 49. Wang, R., et al.: {EASEAndroid}: Automatic Policy Anal- | code classification system through static analysis using machine |  |  |  |  |  |  |  |  |  |
| ysis | and | Refinement | for | Security | Enhanced | Android | via | learning. Symmetry | 13 | (1), 1 (2021). https://doi.org/10.3390/sy |
| {Large-Scale} {Semi-Supervised} Learning. In: Presented at | m13010035 |  |  |  |  |  |  |  |  |  |
| the | 24th | USENIX | Security | Symposium | (USENIX | Secu- | 63. Shiqi, L., Shengwei, T., Long, Y., Jiong, Y., Hua, S.: Android mali- |  |  |  |
| rity 15), pp. 351–366. https://www.usenix.org/conference/usenix | cious code classification using deep belief network. KSII Trans. |  |  |  |  |  |  |  |  |  |
| security15/technical-sessions/presentation/wang-ruowen (2015). | Internet Inf. Syst. | 12 | (1), 454–475 (2018). https://doi.org/10.3837/ |  |  |  |  |  |  |  |
| Accessed 13 March 2025. [Online]. | tiis.2018.01.022 |  |  |  |  |  |  |  |  |  |
| 50. Fadadu, F., Handa, A., Kumar, N., Shukla, S.K.: Evading API | 64. Ali Alatwi, H., Oh, T., Fokoue, E., Stackpole, B.: Android mal- |  |  |  |  |  |  |  |  |  |
| call sequence based malware classifiers. In: Zhou, J., Luo, X., | ware detection using category-based machine learning classifiers. |  |  |  |  |  |  |  |  |  |
| Shen, Q., Xu, Z. (eds.) Information and Communications Security, | In: Proceedings of the 17th Annual Conference on Informa- |  |  |  |  |  |  |  |  |  |

tion Technology Education, in SIGITE ’16. New York, NY,

123

---

## Page 27

| From code to security: machine learning approaches in android … | Page 27 of 30 | 17 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| USA, September 2016. Association for Computing Machinery, | project. 26 May 2024, arXiv: arXiv:2405.16655. https://doi.org/ |  |  |  |  |  |  |  |  |
| pp. 54–59. https://doi.org/10.1145/2978192.2978218 (2016) | 10.48550/arXiv.2405.16655. |  |  |  |  |  |  |  |  |
| 65. Cui, J., Wang, L., Zhao, X., Zhang, H.: Towards predictive anal- | 78. Android Open Source Project. Android Open Source Project. |  |  |  |  |  |  |  |  |
| ysis of android vulnerability using statistical codes and machine | https://source.android.com/(2025) | Accessed | 14 | March | 2025. |  |  |  |  |
| learning for IoT applications. Comput. Commun. | 155 | , 125–131 | [Online]. |  |  |  |  |  |  |
| (2020). https://doi.org/10.1016/j.comcom.2020.02.078 | 79. Senanayake, J., Kalutarage, H., Petrovski, A., Al-Kadri, M.O., |  |  |  |  |  |  |  |  |
| 66. Li, Y., Ma, R., Jiao, R.: A hybrid malicious code detection method | Piras, | L.: | FedREVAN: | Real-time | DEtection | of | Vulnerable |  |  |
| based on deep learning. Int. J. Secur. Appl. | 9 | (5), 205–216 (2015). | Android | Source | Code | Through | Federated | Neural | Network |
| https://doi.org/10.14257/ijsia.2015.9.5.21 | with XAI. In: Katsikas, S., Abie, H., Ranise, S., Verderame, L., |  |  |  |  |  |  |  |  |
| 67. Lin, G., Xiao, W., Zhang, J., Xiang, Y.: Deep learning-based vul- | Cambiaso, E., Ugarelli, R., Praça, I., Li, W., Meng, W., Furnell, |  |  |  |  |  |  |  |  |
| nerable function detection: a benchmark. In: Zhou, J., Luo, X., | S., Katt, B., Pirbhulal, S., Shukla, A., Ianni, M., Dalla Preda, |  |  |  |  |  |  |  |  |
| Shen, Q., Xu, Z. (eds.) Information and Communications Security, | M., Choo, K.-K. R., Pupo Correia, M., Abhishta, A., Sileno, G., |  |  |  |  |  |  |  |  |
| pp. 219–232. Springer International Publishing, Cham (2020), | Alishahi, M., Kalutarage, H., Yanai, N. (eds.) Computer Security. |  |  |  |  |  |  |  |  |
| https://doi.org/10.1007/978-3-030-41579-2_13. | ESORICS 2023 International Workshops, pp. 426–441. Springer |  |  |  |  |  |  |  |  |
| 68. Krutz, D.E., et al.: A dataset of open-source android applications. | Nature Switzerland, Cham (2024). https://doi.org/10.1007/978-3- |  |  |  |  |  |  |  |  |
| In: 2015 IEEE/ACM 12th Working Conference on Mining Soft- | 031-54129-2_25. |  |  |  |  |  |  |  |  |
| ware Repositories, May 2015, pp. 522–525. https://doi.org/10. | 80. Nasteski, V.: An overview of the supervised machine learning |  |  |  |  |  |  |  |  |
| 1109/MSR.2015.79. | methods. In: ResearchGate, December 2024, https://doi.org/10. |  |  |  |  |  |  |  |  |
| 69. Rahman, A., Pradhan, P., Partho, A., Williams, L.: Predicting | 20544/HORIZONS.B.04.1.17.P05. |  |  |  |  |  |  |  |  |
| android application security and privacy risk with static code met- | 81. Ma, S., Thung, F., Lo, D., Sun, C., Deng, R.H.: VuRLE: automatic |  |  |  |  |  |  |  |  |
| rics. In: 2017 IEEE/ACM 4th International Conference on Mobile | vulnerability detection and repair by learning from examples. |  |  |  |  |  |  |  |  |
| Software Engineering and Systems (MOBILESoft), May 2017, | In: Foley, S.N., Gollmann, D., Snekkenes, E. (eds.) Computer |  |  |  |  |  |  |  |  |
| pp. 149–153. https://doi.org/10.1109/MOBILESoft.2017.14. | security—ESORICS 2017, pp. 229–246. Springer International |  |  |  |  |  |  |  |  |
| 70. Piskachev, G., Do, L.N.Q., Bodden, E.: Codebase-adaptive detec- | Publishing, Cham (2017), https://doi.org/10.1007/978-3-319-66 |  |  |  |  |  |  |  |  |
| tion of security-relevant methods. In: Proceedings of the 28th | 399-9_13. |  |  |  |  |  |  |  |  |
| ACM SIGSOFT International Symposium on Software Testing | 82. Gajrani, J., Tripathi, M., Laxmi, V., Somani, G., Zemmari, A., |  |  |  |  |  |  |  |  |
| and Analysis, in ISSTA 2019. New York, NY, USA: Association | Gaur, M.S.: Vulvet: vetting of vulnerabilities in Android apps to |  |  |  |  |  |  |  |  |
| for Computing Machinery, July 2019, pp. 181–191. https://doi. | thwart exploitation. Digit. Threats | 1 | (2), 1–25 (2020). https://doi. |  |  |  |  |  |  |
| org/10.1145/3293882.3330556. | org/10.1145/3376121 |  |  |  |  |  |  |  |  |
| 71. Malik, Y., Campos, C.R.S., Jaafar, F.: Detecting android security | 83. Senanayake, J., Kalutarage, H., Al-Kadri, M.O., Petrovski, A., |  |  |  |  |  |  |  |  |
| vulnerabilities using machine learning and system calls analy- | Piras, L.: Developing secured android applications by mitigating |  |  |  |  |  |  |  |  |
| sis. In: 2019 IEEE 19th International Conference on Software | code vulnerabilities with machine learning. In: Proceedings of the |  |  |  |  |  |  |  |  |
| Quality, Reliability and Security Companion (QRS-C), July 2019, | 2022 ACM on Asia Conference on Computer and Communica- |  |  |  |  |  |  |  |  |
| pp. 109–113. https://doi.org/10.1109/QRS-C.2019.00033. | tions Security, in ASIA CCS ’22. New York, NY, USA: Associa- |  |  |  |  |  |  |  |  |
| 72. Senanayake, J., Kalutarage, H., Al-Kadri, M.O., Piras, L., Petro- | tion for Computing Machinery, May 2022, pp. 1255–1257. https:// |  |  |  |  |  |  |  |  |
| vski, A.: Labelled Vulnerability Dataset on Android Source | doi.org/10.1145/3488932.3527290 (2022) |  |  |  |  |  |  |  |  |
| Code | (LVDAndro) | to | develop | AI-Based | code | vulnerability | 84. LaMalva, G., Schmeelk, S.: MobSF: Mobile Health Care Android |  |  |
| detection | models. | In: | Presented | at | the | 20th | International | Applications Through The Lens of Open Source Static Analysis. |  |
| Conference on Security and Cryptography, September 2024, | In: 2020 IEEE MIT Undergraduate Research Technology Con- |  |  |  |  |  |  |  |  |
| pp. 659–666. https://www.scitepress.org/Link.aspx?doi=https:// | ference (URTC), October 2020, pp. 1–4. https://doi.org/10.1109/ |  |  |  |  |  |  |  |  |
| doi.org/10.5220/0012060400003555. | Accessed | 19 | September | URTC51696.2020.9668870. |  |  |  |  |  |
| 2024. [Online]. | 85. Kulkarni, K., Javaid, A.Y.: Open source android vulnerability |  |  |  |  |  |  |  |  |
| 73. Senanayake, J., Kalutarage, H., Petrovski, A., Piras, L., Al-Kadri, | detection tools: a survey, 31 July 2018, arXiv: arXiv:1807.11840. |  |  |  |  |  |  |  |  |
| M.O.: Defendroid: real-time Android code vulnerability detection | https://doi.org/10.48550/arXiv.1807.11840 (2018) |  |  |  |  |  |  |  |  |
| via blockchain federated neural network with XAI. J. Inf. Secur. | 86. Ranganath, V.-P., Mitra, J.: Are free Android app security analysis |  |  |  |  |  |  |  |  |
| Appl. | 82 | , 103741 (2024). https://doi.org/10.1016/j.jisa.2024.10 | tools effective in detecting known vulnerabilities? Empir. Softw. |  |  |  |  |  |  |
| 3741 | Eng. | 25 | (1), 178–219 (2020). https://doi.org/10.1007/s10664-019- |  |  |  |  |  |  |
| 74. Mathews, N.S., Brus, Y., Aafer, Y., Nagappan, M., McIntosh, S.: | 09749-y |  |  |  |  |  |  |  |  |
| LLbezpeky: leveraging large language models for vulnerability | 87. Noever, D.: Can large language models find and fix vulnerable |  |  |  |  |  |  |  |  |
| detection, 13 February 2024. arXiv: arXiv:2401.01269. https:// | software?. 20 August 2023, arXiv: arXiv:2308.10345. https://doi. |  |  |  |  |  |  |  |  |
| doi.org/10.48550/arXiv.2401.01269. | org/10.48550/arXiv.2308.10345 (2023) |  |  |  |  |  |  |  |  |
| 75. Mitra, J., Ranganath, V.-P.: Ghera: a repository of android app vul- | 88. Kouliaridis, V., Karopoulos, G., Kambourakis, G.: Assessing the |  |  |  |  |  |  |  |  |
| nerability benchmarks. In: Proceedings of the 13th International | effectiveness of LLMs in android application vulnerability anal- |  |  |  |  |  |  |  |  |
| Conference on Predictive Models and Data Analytics in Software | ysis, 27 June 2024, arXiv: arXiv:2406.18894. https://doi.org/10. |  |  |  |  |  |  |  |  |
| Engineering, in PROMISE. New York, NY, USA: Association for | 48550/arXiv.2406.18894 (2024) |  |  |  |  |  |  |  |  |
| Computing Machinery, November 2017, pp. 43–52. https://doi. | 89. Amin, A., Eldessouki, A., Magdy, M.T., Abdeen, N., Hindy, H., |  |  |  |  |  |  |  |  |
| org/10.1145/3127005.3127010. | Hegazy, I.: AndroShield: automated Android applications vulner- |  |  |  |  |  |  |  |  |
| 76. Senanayake, J., Kalutarage, H., Al-Kadri, M.O., Petrovski, A., | ability detection, a hybrid static and dynamic analysis approach. |  |  |  |  |  |  |  |  |
| Piras, L.: Android code vulnerabilities early detection using AI- | Information | 10 | (10), 10 (2019). https://doi.org/10.3390/info1010 |  |  |  |  |  |  |
| Powered ACVED plugin. In: Atluri, V., Ferrara, A.L. (eds.) Data | 0326 |  |  |  |  |  |  |  |  |
| and applications security and privacy XXXVII, pp. 339–357. | 90. Zhu, J., Li, K., Chen, S., Fan, L., Wang, J., Xie, X.: A compre- |  |  |  |  |  |  |  |  |
| Springer Nature Switzerland, Cham (2023) https://doi.org/10. | hensive study on static application security testing (SAST) tools |  |  |  |  |  |  |  |  |
| 1007/978-3-031-37586-6_20. | for Android. IEEE Trans. Softw. Eng. | 50 | (12), 3385–3402 (2024). |  |  |  |  |  |  |
| 77. Yim, K.S.: Predicting likely-vulnerable code changes: machine | https://doi.org/10.1109/TSE.2024.3488041 |  |  |  |  |  |  |  |  |
| learning-based vulnerability protections for android open source | 91. Gencer, K., Ba¸ | sçiftçi, F.: Time series forecast modeling of vulner- |  |  |  |  |  |  |  |

abilities in the android operating system using ARIMA and deep

123

---

## Page 28

| 17 | Page 28 of 30 | K. E. Arikan et al. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| learning methods. Sustain. Comput. Inform. Syst. | 30 | , 100515 | 107. Klieber, W., Flynn, L., Bhosale, A., Jia, L., Bauer, L.: Android |  |  |  |  |  |
| (2021). https://doi.org/10.1016/j.suscom.2021.100515 | taint flow analysis for app sets. In: Proceedings of the 3rd ACM |  |  |  |  |  |  |  |
| 92. Zhang, Q., Fang, C., Yu, B., Sun, W., Zhang, T., Chen, Z.: | SIGPLAN International Workshop on the State of the Art in Java |  |  |  |  |  |  |  |
| Pre-trained model-based automated software vulnerability repair: | Program Analysis, Edinburgh United Kingdom: ACM, June 2014, |  |  |  |  |  |  |  |
| how far are we? IEEE Trans. Dependable Secur. Comput. | 21 | (4), | pp. 1–6. https://doi.org/10.1145/2614628.2614633. |  |  |  |  |  |
| 2507–2525 (2024). https://doi.org/10.1109/TDSC.2023.3308897 | 108. Arzt, S., et al.: FlowDroid: precise context, flow, field, object- |  |  |  |  |  |  |  |
| 93. Wang, C., Zhang, L., Zhao, K., Ding, X., Wang, X.: AdvAndMal: | sensitive and lifecycle-aware taint analysis for Android apps. |  |  |  |  |  |  |  |
| adversarial training for Android malware detection and family | SIGPLAN Not. | 49 | (6), 259–269 (2014). https://doi.org/10.1145/ |  |  |  |  |  |
| classification. Symmetry | 13 | (6), 6 (2021). https://doi.org/10.3390/ | 2666356.2594299 |  |  |  |  |  |
| sym13061081 | 109. Rasthofer, S., Arzt, S., Bodden, E.: A machine-learning approach |  |  |  |  |  |  |  |
| 94. Bala, N., Ahmar, A., Li, W., Tovar, F., Battu, A., Bambarkar, P.: | for classifying and categorizing android sources and sinks. In: |  |  |  |  |  |  |  |
| DroidEnemy: battling adversarial example attacks for Android | Proceedings 2014 Network and Distributed System Security Sym- |  |  |  |  |  |  |  |
| malware detection. Digit. Commun. Networks | 8 | (6), 1040–1047 | posium, Internet Society, San Diego, CA. https://doi.org/10.14 |  |  |  |  |  |
| (2022). https://doi.org/10.1016/j.dcan.2021.11.001 | 722/ndss.2014.23039 (2014) |  |  |  |  |  |  |  |
| 95. Renjith, G., Laudanna, S., Aji, S., Visaggio, C.A., Vinod, P.: | 110. Sas, D., Bessi, M., Arcelli Fontana, F.: Automatic Detection of |  |  |  |  |  |  |  |
| GANG-MAM: GAN based engine for modifying Android mal- | Sources and Sinks in Arbitrary Java Libraries. In: 2018 IEEE 18th |  |  |  |  |  |  |  |
| ware. SoftwareX | 18 | , 100977 (2022). https://doi.org/10.1016/j.so | International Working Conference on Source Code Analysis and |  |  |  |  |  |
| ftx.2022.100977 | Manipulation (SCAM), September 2018, pp. 103–112. https:// |  |  |  |  |  |  |  |
| 96. Rathore, H., Nikam, P., Sahay, S.K., Sewak, M.: Identification of | doi.org/10.1109/SCAM.2018.00019 (2018) |  |  |  |  |  |  |  |
| adversarial android intents using reinforcement learning. In: 2021 | 111. Chen, S., Zhang, Y., Fan, L., Li, J., Liu, Y.: AUSERA: Auto- |  |  |  |  |  |  |  |
| International Joint Conference on Neural Networks (IJCNN), | mated Security Vulnerability Detection for Android Apps. In: |  |  |  |  |  |  |  |
| July 2021, pp. 1–8. https://doi.org/10.1109/IJCNN52387.2021.95 | Proceedings of the 37th IEEE/ACM International Conference |  |  |  |  |  |  |  |
| 34142. | on Automated Software Engineering, in ASE ’22. New York, |  |  |  |  |  |  |  |
| 97. Zhou, Y., Jiang, X.: Dissecting android malware: characterization | NY, USA: Association for Computing Machinery, January 2023, |  |  |  |  |  |  |  |
| and evolution. In: 2012 IEEE Symposium on Security and Privacy, | pp. 1–5. https://doi.org/10.1145/3551349.3559524 (2023) |  |  |  |  |  |  |  |
| May 2012, pp. 95–109. https://doi.org/10.1109/SP.2012.16. | 112. Manning, C.D.: Human language understanding & reasoning. |  |  |  |  |  |  |  |
| 98. Arp, D., Spreitzenbarth, M., Hubner, M., Gascon, H., Rieck, K.: | Daedalus | 151 | (2), 127–138 (2022). https://doi.org/10.1162/daed_ |  |  |  |  |  |
| (PDF) DREBIN: effective and explainable detection of android | a_01905 |  |  |  |  |  |  |  |
| malware in your pocket, In: ResearchGate, https://doi.org/10.14 | 113. Hou, X., et al.: Large language models for software engineering: |  |  |  |  |  |  |  |
| 722/ndss.2014.23247. | a systematic literature review, ACM Trans Softw Eng Methodol, |  |  |  |  |  |  |  |
| 99. Gómez, A., Muñoz, A.: Deep learning-based attack detection and | December 2024, vol. 33, no. 8, pp. 1–79. https://doi.org/10.1145/ |  |  |  |  |  |  |  |
| classification in Android devices. Electronics | 12 | (15), 15 (2023). | 3695988 (2024) |  |  |  |  |  |
| https://doi.org/10.3390/electronics12153253 | 114. Cheshkov, | A., | Zadorozhny, | P., | Levichev, | R.: | Evaluation | of |
| 100. Wajahat, A., et al.: Outsmarting Android malware with cutting- | ChatGPT Model for Vulnerability Detection, 12 April 2023, |  |  |  |  |  |  |  |
| edge feature engineering and machine learning techniques. Com- | arXiv: arXiv:2304.07232. https://doi.org/10.48550/arXiv.2304. |  |  |  |  |  |  |  |
| put. Mater. Contin. | 79 | (1), 651–673 (2024). https://doi.org/10.32 | 07232 (2023) |  |  |  |  |  |
| 604/cmc.2024.047530 | 115. Asare, O.: Security Evaluations of GitHub’s Copilot, August |  |  |  |  |  |  |  |
| 101. Faruki, P., et al.: Android security: a survey of issues, mal- | 2023. http://hdl.handle.net/10012/19675. Accessed 18 March |  |  |  |  |  |  |  |
| ware penetration, and defenses. IEEE Commun. Surv. Tutor. | 2025. [Online]. |  |  |  |  |  |  |  |
| 17 | (2), 998–1022 (2015). https://doi.org/10.1109/COMST.2014. | 116. Wang, J., Huang, Z., Liu, H., Yang, N., Xiao, Y.: DefectHunter: |  |  |  |  |  |  |
| 2386139 | a Novel LLM-Driven Boosted-Conformer-based Code Vulnera- |  |  |  |  |  |  |  |
| 102. Tam, K., Feizollah, A., Anuar, N.B., Salleh, R., Cavallaro, L.: The | bility Detection Mechanism, 27 September 2023, arXiv: arXiv: |  |  |  |  |  |  |  |
| evolution of Android malware and Android analysis techniques. | 2309.15324. https://doi.org/10.48550/arXiv.2309.15324 (2023) |  |  |  |  |  |  |  |
| ACM Comput. Surv. | 49 | (4), 1–41 (2017). https://doi.org/10.1145/ | 117. Zhang, C., Liu, H., Zeng, J., Yang, K., Li, Y., Li, H.: Prompt- |  |  |  |  |  |
| 3017427 | enhanced software vulnerability detection using ChatGPT. In: |  |  |  |  |  |  |  |
| 103. Gyamfi, N.K., Goranin, N., Ceponis, D., ˇ | Cenys, H.A.: Automated | Proceedings of the 2024 IEEE/ACM 46th International Con- |  |  |  |  |  |  |
| system-level malware detection using machine learning: a com- | ference on Software Engineering: Companion Proceedings, in |  |  |  |  |  |  |  |
| prehensive review. Appl. Sci. | 13 | (21), 21 (2023). https://doi.org/ | ICSE-Companion ’24. New York, NY, USA (2024). Association |  |  |  |  |  |
| 10.3390/app132111908 | for Computing Machinery, May 2024, pp. 276–277. https://doi. |  |  |  |  |  |  |  |
| 104. Pauck, F., Bodden, E., Wehrheim, H.: Do Android taint analysis | org/10.1145/3639478.3643065. |  |  |  |  |  |  |  |
| tools keep their promises? In: Proceedings of the 2018 26th ACM | 118. Wei, H., Lin, G., Li, L., Jia, H.: A context-aware neural embedding |  |  |  |  |  |  |  |
| Joint Meeting on European Software Engineering Conference | for function-level vulnerability detection. Algorithms | 14 | (11), 11 |  |  |  |  |  |
| and Symposium on the Foundations of Software Engineering, | (2021). https://doi.org/10.3390/a14110335 |  |  |  |  |  |  |  |
| in ESEC/FSE 2018. Association for Computing Machinery, Oct. | 119. Mahyari, A.: A hierarchical deep neural network for detecting |  |  |  |  |  |  |  |
| 2018, pp. 331–341. New York, NY, USA. https://doi.org/10.1145/ | lines of codes with vulnerabilities. In: 2022 IEEE 22nd Interna- |  |  |  |  |  |  |  |
| 3236024.3236029. | tional Conference on Software Quality, Reliability, and Security |  |  |  |  |  |  |  |
| 105. Wei, F., Roy, S., Ou, X., Robby.: Amandroid: a precise and general | Companion (QRS-C), Dec. 2022, pp. 1–7. https://doi.org/10. |  |  |  |  |  |  |  |
| inter-component data flow analysis framework for security vetting | 1109/QRS-C57518.2022.00011 (2022) |  |  |  |  |  |  |  |
| of android apps. ACM Trans. Priv. Secur. | 21 | (3), 1–32 (2018). | 120. Lin, G., et al.: Cross-project transfer representation learning for |  |  |  |  |  |
| https://doi.org/10.1145/3183575. | vulnerable function discovery. IEEE Trans. Ind. Inform. | 14 | (7), |  |  |  |  |  |
| 106. Bosu, A., Liu, F., Wang, G.: Android Collusive Data Leaks with | 3289–3297 (2018). https://doi.org/10.1109/TII.2018.2821768 |  |  |  |  |  |  |  |
| Flow-sensitive DIALDroid Dataset. In: Proceedings of the 2017 | 121. Chakraborty, S., Krishna, R., Ding, Y., Ray, B.: Deep learning |  |  |  |  |  |  |  |
| ACM on Asia Conference on Computer and Communications | based vulnerability detection: are we there yet? IEEE Trans. |  |  |  |  |  |  |  |
| Security, pp. 71–85. ACM, Abu Dhabi United Arab Emirates | Softw. Eng. | 48 | (9), 3280–3296 (2022). https://doi.org/10.1109/ |  |  |  |  |  |
| (2017). https://doi.org/10.1145/3052973.3053004 | TSE.2021.3087402 |  |  |  |  |  |  |  |

123

---

## Page 29

| From code to security: machine learning approaches in android … | Page 29 of 30 | 17 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 122. Malware detection in android based on dynamic analysis. In: | 137. Prates, L., Pereira, R.: DevSecOps practices and tools. Int. J. Inf. |  |  |  |  |  |  |  |  |
| 2017 International Conference on Cyber Security And Protec- | Secur. | 24 | (1), 11 (2024). https://doi.org/10.1007/s10207-024-00 |  |  |  |  |  |  |
| tion Of Digital Services (Cyber Security), IEEE, London, UK | 914-z |  |  |  |  |  |  |  |  |
| ResearchGate | (2017). | https://doi.org/10.1109/CyberSecPODS. | 138. Alugunuri, N.: AI for continuous security in DevOps (DevSec- |  |  |  |  |  |  |
| 2017.8074847. | Ops): integrating machine learning into CI/CD pipelines. Int. J. |  |  |  |  |  |  |  |  |
| 123. Misalkar, H.D., Harshavardhanan, P.: TDBAMLA: temporal and | Intell. Syst. Appl. Eng. | 12 | (23s), 3048–3062 (2024) |  |  |  |  |  |  |
| dynamic behavior analysis in Android malware using LSTM | 139. Nazir, A., et al.: Evaluating energy efficiency of buildings using |  |  |  |  |  |  |  |  |
| and attention mechanisms. Comput. Stand. Interfaces | 92 | , 103920 | artificial neural networks and k-means clustering techniques. In: |  |  |  |  |  |  |
| (2025). https://doi.org/10.1016/j.csi.2024.103920 | 2020 3rd International Conference on Computing, Mathematics |  |  |  |  |  |  |  |  |
| 124. Yuan, B., et al.: Enhancing deep learning-based vulnerability | and Engineering Technologies (iCoMET), Jan. 2020, pp. 1–7. |  |  |  |  |  |  |  |  |
| detection by building behavior graph model. In: Proceedings of the | https://doi.org/10.1109/iCoMET48670.2020.9073816 (2020) |  |  |  |  |  |  |  |  |
| 45th International Conference on Software Engineering, in ICSE | 140. Krutz, D.E., Munaiah, N., Peruma, A., Wiem Mkaouer, M.: |  |  |  |  |  |  |  |  |
| ’23, pp. 2262–2274. IEEE Press, Melbourne, Victoria, Australia | Who | Added | That | Permission | to | My | App? | An | Analysis |
| (2023) https://doi.org/10.1109/ICSE48619.2023.00190. | of Developer Permission Changes in Open Source Android |  |  |  |  |  |  |  |  |
| 125. Li, Z., Li, H., Meng, L.: Model compression for deep neural net- | Apps. In: 2017 IEEE/ACM 4th International Conference on |  |  |  |  |  |  |  |  |
| works: a survey. Computers | 12 | (3), 60 (2023). https://doi.org/10. | Mobile | Software | Engineering | and | Systems | (MOBILESoft), |  |
| 3390/computers12030060 | May 2017, pp. 165–169. https://doi.org/10.1109/MOBILESoft. |  |  |  |  |  |  |  |  |
| 126. Jedrzejewski, F.V.: Threat Modeling of ML-intensive Systems: | 2017.5. (2017) |  |  |  |  |  |  |  |  |
| Research Proposal. In: Proceedings of the IEEE/ACM 3rd Interna- | 141. Geiger, F.-X., Malavolta, I., Pascarella, L., Palomba, F., Di Nucci, |  |  |  |  |  |  |  |  |
| tional Conference on AI Engineering—Software Engineering for | D., Bacchelli, A.: A graph-based dataset of commit history of |  |  |  |  |  |  |  |  |
| AI, in CAIN ’24. New York, NY, USA: Association for Comput- | real-world Android apps. In: Proceedings of the 15th Interna- |  |  |  |  |  |  |  |  |
| ing Machinery, June 2024, pp. 264–266. https://doi.org/10.1145/ | tional Conference on Mining Software Repositories, in MSR ’18. |  |  |  |  |  |  |  |  |
| 3644815.3644975 (2024) | Association for Computing Machinery, May 2018, pp. 30–33. |  |  |  |  |  |  |  |  |
| 127. DARPA’s Explainable Artificial Intelligence (XAI) Program. | New York, NY, USA (2018) https://doi.org/10.1145/3196398.31 |  |  |  |  |  |  |  |  |
| ResearchGate. https://doi.org/10.1609/aimag.v40i2.2850 (2024) | 96460. |  |  |  |  |  |  |  |  |
| 128. Phillips, P.J., et al.: Four principles of explainable artificial intelli- | 142. Namrud, Z., Kpodjedo, S., Talhi, C.: AndroVul: a repository |  |  |  |  |  |  |  |  |
| gence. NIST. https://www.nist.gov/publications/four-principles- | for Android security vulnerabilities, In: Proceedings of the 29th |  |  |  |  |  |  |  |  |
| explainable-artificial-intelligence (Sep. 2021). Accessed 25 Mar | Annual International Conference on Computer Science and Soft- |  |  |  |  |  |  |  |  |
| 2025 [Online]. | ware Engineering, in CASCON ’19, November 2019, pp. 64–71. |  |  |  |  |  |  |  |  |
| 129. Srivastava, G., et al.: XAI for Cybersecurity: State of the Art, Chal- | USA, IBM Corp (2019) |  |  |  |  |  |  |  |  |
| lenges, Open Issues and Future Directions, arXiv: arXiv:2206. | 143. Allix, K., Bissyandé, T. F., Klein, J., Le Traon, Y.: AndroZoo: |  |  |  |  |  |  |  |  |
| 03585. https://doi.org/10.48550/arXiv.2206.03585 (2022) | collecting millions of Android apps for the research community, |  |  |  |  |  |  |  |  |
| 130. Nguyen, T.N., Choo, R.: Human-in-the-Loop XAI-enabled Vul- | In: Proceedings of the 13th International Conference on Mining |  |  |  |  |  |  |  |  |
| nerability Detection, Investigation, and Mitigation. In: 2021 36th | Software Repositories, in MSR ’16, New York, NY, USA (2016). |  |  |  |  |  |  |  |  |
| IEEE/ACM International Conference on Automated Software | Association for Computing Machinery, May 2016, pp. 468–471. |  |  |  |  |  |  |  |  |
| Engineering (ASE), Nov. 2021, pp. 1210–1212. https://doi.org/ | https://doi.org/10.1145/2901739.2903508. |  |  |  |  |  |  |  |  |
| 10.1109/ASE51524.2021.9678840 (2021) | 144. JEMMA: An extensible Java dataset for ML4Code applications. |  |  |  |  |  |  |  |  |
| 131. Wijekoon, A., Wiratunga, N.: A user-centred evaluation of Dis- | \|Empirical | Software | Engineering. | https://link.springer.com/ar |  |  |  |  |  |
| CERN: discovering counterfactuals for code vulnerability detec- | ticle/https://doi.org/10.1007/s10664-022-10275-7. Accessed 18 |  |  |  |  |  |  |  |  |
| tion and correction. Knowl.-Based Syst. | 278 | , 110830 (2023). | Mar 2025 [Online] |  |  |  |  |  |  |
| https://doi.org/10.1016/j.knosys.2023.110830 | 145. Geiger, F.-X., Malavolta, I.: Datasets of android applications: a |  |  |  |  |  |  |  |  |
| 132. Francy, S., Singh, R.: Edge AI: Evaluation of Model Compres- | literature review. (2018). arXiv:1809.10069. https://doi.org/10.48 |  |  |  |  |  |  |  |  |
| sion Techniques for Convolutional Neural Networks. 02 Sep | 550/arXiv.1809.10069. |  |  |  |  |  |  |  |  |
| 2024, arXiv: arXiv:2409.02134. https://doi.org/10.48550/arXiv. | 146. Qiu, J., Zhang, J., Luo, W., Pan, L., Nepal, S., Xiang, Y.: A |  |  |  |  |  |  |  |  |
| 2409.02134. | survey of Android malware detection with deep neural models. |  |  |  |  |  |  |  |  |
| 133. Ngo, D., Park, H.-C., Kang, B.: Edge intelligence: a review of | ACM Comput. Surv. | 53 | (6), 1–36 (2020). https://doi.org/10.1145/ |  |  |  |  |  |  |
| deep neural network inference in resource-limited environments. | 3417978 |  |  |  |  |  |  |  |  |
| Electronics | 14 | (12), 2495 (2025). https://doi.org/10.3390/electron | 147. Zhang, X., Breitinger, F., Luechinger, E., O’Shaughnessy, S.: |  |  |  |  |  |  |
| ics14122495 | Android application forensics: a survey of obfuscation, obfus- |  |  |  |  |  |  |  |  |
| 134. Tan, F., et al.: MobileQuant: Mobile-friendly Quantization for On- | cation detection and deobfuscation techniques and their impact |  |  |  |  |  |  |  |  |
| device Language Models. In: Al-Onaizan, Y., Bansal, M., Chen, | on investigations. Forensic Sci. Int. Digit. Investig. | 39 | , 301285 |  |  |  |  |  |  |
| Y.-N. (eds.) Findings of the Association for Computational Lin- | (2021). https://doi.org/10.1016/j.fsidi.2021.301285 |  |  |  |  |  |  |  |  |
| guistics: EMNLP 2024, pp. 9761–9771. Miami, Florida, USA | 148. Wu, T., Breitinger, F., O’Shaughnessy, S.: Digital forensic tools: |  |  |  |  |  |  |  |  |
| (2024) Association for Computational Linguistics, Nov. 2024. | recent advances and enhancing the status quo. Forensic Sci. Int. |  |  |  |  |  |  |  |  |
| https://doi.org/10.18653/v1/2024.findings-emnlp.570. | Digit. Investig. | 34 | , 300999 (2020). https://doi.org/10.1016/j.fsidi. |  |  |  |  |  |  |
| 135. Molina-Coronado, | B., | Ruggia, | A., | Mori, | U., | Merlo, | A., | 2020.300999 |  |
| Mendiburu, A., Miguel-Alonso, J.: Light up that Droid! On the | 149. Mirzaei, O., de Fuentes, J.M., Tapiador, J., Gonzalez-Manzano, |  |  |  |  |  |  |  |  |
| effectiveness of static analysis features against app obfuscation for | L.: AndrODet: an adaptive Android obfuscation detector. Future |  |  |  |  |  |  |  |  |
| Android malware detection. J. Netw. Comput. Appl. | 235 | , 104094 | Gener. Comput. Syst. | 90 | , 240–261 (2019). https://doi.org/10. |  |  |  |  |
| (2025). https://doi.org/10.1016/j.jnca.2024.104094 | 1016/j.future.2018.07.066 |  |  |  |  |  |  |  |  |
| 136. Sun, Y., et al.: A transformer based malicious traffic detection | 150. Li, Z., Sun, J., Yan, Q., Srisa-an, W., Tsutano, Y.: Obfusifier: |  |  |  |  |  |  |  |  |
| method in android mobile networks. In: Sheng, Q.Z., Dobbie, G., | Obfuscation-Resistant Android Malware Detection System. In: |  |  |  |  |  |  |  |  |
| Jiang, J., Zhang, X., Zhang, W. E., Manolopoulos, Y., Wu, J., Man- | Chen, S., Choo, K.-K. R., Fu, X., Lou, W., Mohaisen, A. (eds.) |  |  |  |  |  |  |  |  |
| soor, W., Ma, C. (eds.) Advanced Data Mining and Applications, | Security and Privacy in Communication Networks, pp. 214–234. |  |  |  |  |  |  |  |  |
| pp. 370–385. Springer Nature, Singapore (2025) https://doi.org/ | Springer International Publishing, Cham (2019). https://doi.org/ |  |  |  |  |  |  |  |  |
| 10.1007/978-981-96-0821-8_25. | 10.1007/978-3-030-37228-6_11. |  |  |  |  |  |  |  |  |

123

---

## Page 30

| 17 | Page 30 of 30 | K. E. Arikan et al. |  |
| --- | --- | --- | --- |
| 151. Pasetto, M., Marastoni, N., Preda, M. D.: Revealing similari- | 157. Wan, Z., Xia, X., Lo, D., Murphy, G.C.: How does machine |  |  |
| ties in android malware by dissecting their methods. In: 2020 | learning change software development practices? IEEE Trans. |  |  |
| IEEE European Symposium on Security and Privacy Workshops | Softw. Eng. | 47 | (9), 1857–1871 (2021). https://doi.org/10.1109/ |
| (EuroS&PW), pp. 625–634. https://doi.org/10.1109/EuroSPW5 | TSE.2019.2937083 |  |  |

1379.2020.00090(2020).

152. The rise of obfuscated Android malware and impacts on detec-

tion methods [PeerJ]. https://peerj.com/articles/cs-907/ (2022).

Accessed 18 Mar 2025. [Online].

153. Software Assurance Reference Dataset (SARD) Manual. NIST.

https://www.nist.gov/itl/ssd/software-quality-group/software-

assurance-reference-dataset-sard-manual (2021). Accessed 18

March 2025. [Online].

154. Juliet C/C++ 1.3. NIST Software Assurance Reference Dataset.

https://samate.nist.gov/SARD (2011). Accessed 18 Mar 2025.

[Online].

155. Allamanis, M.: The adverse effects of code duplication in

machine learning models of code In: Proceedings of the

2019 ACM SIGPLAN International Symposium on New

Ideas, New Paradigms, and Reflections on Programming

and Software. https://dl.acm.org/doi/abs/https://doi.org/10.1145/

3359591.3359735 (2019). Accessed 18 Mar 2025 [Online].

156. Giray, G.: A software engineering perspective on engineering

machine learning systems: state of the art and challenges. J. Syst.

Softw. 180 , 111031 (2021). https://doi.org/10.1016/j.jss.2021.11

1031

123

Publisher’s Note Springer Nature remains neutral with regard to juris-

dictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds

exclusive rights to this article under a publishing agreement with the

author(s) or other rightsholder(s); author self-archiving of the accepted

manuscript version of this article is solely governed by the terms of such

publishing agreement and applicable law.

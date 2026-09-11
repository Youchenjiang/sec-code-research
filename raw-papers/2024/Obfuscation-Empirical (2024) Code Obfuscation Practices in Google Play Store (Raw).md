---
title: "35_Niroshan_et_al.,_Empirical_Study_of_Obfuscation_in_Google_Play"
creator: "LaTeX with hyperref"
pages: 13
---

# 35_Niroshan_et_al.,_Empirical_Study_of_Obfuscation_in_Google_Play

> **總頁數**：13 頁

---

## Page 1

employ code obfuscation techniques. However, while effective

year period, to investigate the evolution and prevalence of code

obfuscation is more prevalent in top-ranked apps and gaming

Store, providing insights for developers and security analysts.

NDROID plays a vital role in the smartphone market,

A holding more than 70% market share [2]. Within that,

the Google Play Store serves as the primary app repository,

offering over 1.7 million apps as of August 2024 [3]. The

Google Play Store is highly accessible, allowing developers to

publish and monetize their apps with fewer barriers to entry.

Due to the relative ease of publishing apps, various mal-

practices are common in the Google Play Store [4]. For

example, some malicious authors may repackage or counterfeit

legitimate apps for nefarious purposes [5], [6]. Similarly, some

† This is an extension of our previous work [1] published in the

a.seneviratne@unsw.edu.au).

1

†

in the Google Play Store

Akila Niroshan, Suranga Seneviratne, Aruna Seneviratne

obfuscation adoption over time.

To this end, in this paper, we investigate code obfuscation

ecosystem. For developers, our work highlights the importance

and IP. For researchers, we provide insights into industry

trends. For malware analysts and app store administrators, our

work underscores the necessity of robust security measures

and regulations. Our research involves developing a set of

classifiers to detect obfuscated code using various tools and

techniques and analyzing trends over time by conducting

a longitudinal study using data from two snapshots of the

Google Play Store, taken five years apart. More specifically,

we make the following contributions.

is the first large-scale study of its kind to analyse over

be accessible.

An Empirical Study of Code Obfuscation Practices

Abstract —The Android ecosystem is vulnerable to issues such analysis by app investigators [11]–[13]. This poses chal-

as app repackaging, counterfeiting, and piracy, threatening both lenges for malware analysts and app store administrators in

developers and users. To mitigate these risks, developers often enforcing security policies, as obfuscation can bypass anti-

in protecting legitimate applications, obfuscation also hinders malware mechanisms and app store regulations [9], [10].

security investigations as it is often exploited for malicious Additionally, obfuscation introduces performance degradations

purposes. As such, it is important to understand code obfuscation and limitations in Android research [13]–[15]. While some

practices in Android apps. In this paper, we analyze over studies propose obfuscation-resilient research methods [16]–

500,000 Android APKs from Google Play, spanning an eight- [18], others either overlook obfuscation or consider only basic

obfuscation techniques. First, we propose a set of classifiers to techniques and tools [19]–[21], possibly due to limited aware-

detect obfuscated code, tools, and techniques and then conduct a ness of its prevalence. Given these challenges, it is important

longitudinal analysis to identify trends. Our results show a 13% to examine the prevalence and trends of obfuscation in the

increase in obfuscation from 2016 to 2023, with ProGuard and Google Play Store. While some prior work has introduced

Allatori as the most commonly used tools. We also show that methods for obfuscation detection [22]–[26], no studies have

genres such as Casino apps. To our knowledge, this is the first fully examined the use of code obfuscation by app developers,

large-scale study of obfuscation adoption in the Google Play the tools and techniques they employ, or the evolution of

Index Terms —Android, Code Obfuscation, Mobile Apps, App adoption and practices in the Google Play Store from different

Store Mining. aspects to benefit various stakeholders of the app market

I. I NTRODUCTION of obfuscation tools and industry standards to protect apps

arXiv:2502.04636v1 [cs.CR] 7 Feb 2025 • We propose a bank of classifiers to detect whether an

| malicious parties may steal intellectual property (IP) by reverse | app is obfuscated and, if so, identify the obfuscation |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| engineering apps [7]. These malpractices pose a significant | tools and techniques used. On our test set, we achieved |  |  |  |  |  |  |  |  |  |  |  |  |  |
| threat to legitimate app developers and end users. As a coun- | 97% accuracy in detecting obfuscation, 99% accuracy |  |  |  |  |  |  |  |  |  |  |  |  |  |
| termeasure, app developers use code obfuscation to protect | in identifying the tool used for obfuscation, and 88% |  |  |  |  |  |  |  |  |  |  |  |  |  |
| their apps and intellectual property (IP) [8]. Equally, malware | accuracy in identifying the obfuscation technique. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| authors can also use obfuscation to evade anti-malware tools | • | Using these classifiers, we conduct a longitudinal study |  |  |  |  |  |  |  |  |  |  |  |  |
| and to conceal functionality [9], [10]. | spanning eight years, from 2016 to 2023, to understand |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Although | obfuscation | provides | security | benefits, | it | also | how | code | obfuscation | practices | have | evolved | in | the |
| hinders | reverse | engineering, | which | is | essential | for | static | Google Play Store. To the best of our knowledge, this |  |  |  |  |  |  |
| ACM/SIGAPP Symposium on Applied Computing (SAC), 2025. | half a million Android applications. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Akila Niroshan and Aruna Seneviratne are with the University of New South | • | We show that overall code obfuscation in the Google Play |  |  |  |  |  |  |  |  |  |  |  |  |
| Wales (UNSW), Sydney, Australia (e-mail: a.pothpitiyage don@unsw.edu.au, | Store increased by nearly 13% from 2016 to 2023. We |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Suranga Seneviratne is with the University of Sydney, Sydney, Australia | also find that ProGuard [27] and Allatori [28] are the two |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (e-mail: suranga.seneviratne@sydney.edu.au). | most commonly used tools by developers. Gaming apps |  |  |  |  |  |  |  |  |  |  |  |  |  |

This work has been submitted to the IEEE for possible publication. Copyright © may be transferred without notice, after which this version may no longer

---

## Page 2

2

| tend to use obfuscation more than non-gaming apps, with | component | of | the | native | Java | library, | to | access | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Casino games showing the highest prevalence, at 80% of | manipulate methods during program execution. |  |  |  |  |  |  |  |  |
| apps obfuscated, and over 85% using multiple techniques. | • | Other | obfuscation methods involve techniques that some- |  |  |  |  |  |  |
| • | We report a 28% increase in obfuscation among top | times overlap with the earlier methods, and as such, |  |  |  |  |  |  |  |
| developers from 2018 to 2023 and an 11.7% increase | delineating boundaries between these techniques is chal- |  |  |  |  |  |  |  |  |
| among developers with only one app. Over 90% of the | lenging. For example, [33] introduces adding | ‘nop’ | in- |  |  |  |  |  |  |
| top 1,000 apps are obfuscated, with higher-ranked apps | structions and unconditional jumps. This is known as | junk |  |  |  |  |  |  |  |
| using multiple obfuscation techniques more frequently | code insertion | . Moreover, developers can employ | opaque |  |  |  |  |  |  |
| than lower-ranked ones. We further report that ProGuard | predicates | , such as conditional statements or branches, |  |  |  |  |  |  |  |
| is the most commonly used tool among lower-ranked | to create a simulated branch [31], which constitutes a |  |  |  |  |  |  |  |  |
| apps. | bogus control flow | . This practice generates two branches |  |  |  |  |  |  |  |
| The rest of the paper is organized as follows. In Section II, | yielding the same outcome, with one branch containing |  |  |  |  |  |  |  |  |
| we present background information such as common obfusca- | the original code and the other comprising unreachable |  |  |  |  |  |  |  |  |
| tion tools and techniques. Section III details our obfuscation | junk instructions. |  |  |  |  |  |  |  |  |
| detection framework, and Section IV describes our large-scale | 3) String Encryption (SE): | Storing sensitive information or |  |  |  |  |  |  |  |

dataset. We present our findings on obfuscation trends in the identifiable prompts in plain text strings within the source

Google Play Store in Section V. Section VI reviews related code may render the application vulnerable to third-party

work, while Section VII discusses the implications and the examination and reverse engineering. To avoid that, String

limitations of our work and concludes the paper. Encryption transforms human-readable strings within the code

into human-unreadable character sequences.

II. B ACKGROUND

A. Common Obfuscation Techniques

B. Commonly used Obfuscation Tools

Obfuscation systematically converts the source code of

the program into a form that is beyond human readability. Developers usually resort to tools to obfuscate code. Previ-

This transformation maintains the application’s functionality ous works [22], [24], [25], [34] have reported multiple code

unchanged while altering the program’s code. Several previous obfuscation tools of various kinds, as we describe below.

| works studied and categorized obfuscation techniques [22], | • | ProGuard | [27] is an inbuilt and free obfuscator for |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [26], [29]–[31]. In the following, we describe some of the | Android Studio by GuardSquare. It can be easily activated |  |  |  |  |  |  |  |  |  |
| well-known obfuscation techniques used in Android apps. | by adding ProGuard rules in the | build.gradle | file. |  |  |  |  |  |  |  |
| 1) Identifier Renaming (IR): | In | Identifier Renaming | , iden- | ProGuard | can | perform | only | Identifier | Renaming | and |
| tifiers in the code (e.g., class names, method names, and field | Code Optimization as specified in the user guide. |  |  |  |  |  |  |  |  |  |
| names) are substituted with random characters or strings. This | • | Allatori | [28] is a commercial obfuscator by Smardec |  |  |  |  |  |  |  |
| aims to make the code less readable by obfuscating readable | Inc. | It | is | offered | as | both | paid | and | free | educational |
| information without changing the program logic. | versions with equal functionality. Integrating Allatori into |  |  |  |  |  |  |  |  |  |
| 2) Control Flow Modification (CF): | The primary concept | an Android project is similar to ProGuard. However, it |  |  |  |  |  |  |  |  |
| behind Control Flow Modification is to change the sequence | requires adding the Allatori | jar | file and configuration |  |  |  |  |  |  |  |
| of program execution, making it more difficult to understand | file in the | build.gradle | . It supports all three main |  |  |  |  |  |  |  |
| and analyze. This technique is commonly used to protect | obfuscation techniques discussed in Section II-A. |  |  |  |  |  |  |  |  |  |
| software from reverse engineering and tampering. In [31] and | • | DashO | [35] is another commercial obfuscator by Pre- |  |  |  |  |  |  |  |
| [29], various methods for achieving CF are discussed, and we | Emptive Inc. It is a paid tool, with the possibility of |  |  |  |  |  |  |  |  |  |
| outlined the popular techniques below. | requesting a 7-day evaluation licence. Developers can |  |  |  |  |  |  |  |  |  |
| • | Control | flow | flattening | incorporates a construct that | use DashO UI to open source code files and enable |  |  |  |  |  |
| may include an infinite or finite loop with a termination | necessary configurations. DashO UI will then add the |  |  |  |  |  |  |  |  |  |
| condition. Within this construct, individual basic blocks | required settings to the | build.gradle | file. It supports |  |  |  |  |  |  |  |
| are encapsulated as cases of a switch statement. While | all three main obfuscation techniques described earlier. |  |  |  |  |  |  |  |  |  |
| the | original | basic | block | is | executed | during | runtime, | • | Obfuscapk | [36] was initially developed as an open- |
| the process of decompiling the switch case statement | source obfuscation tool for researchers to obfuscate An- |  |  |  |  |  |  |  |  |  |
| and restoring the initial code is challenging, due to the | droid applications. It implements all three techniques |  |  |  |  |  |  |  |  |  |
| convoluted ‘ | if | ’ and ‘ | goto | ’ statements. | discussed in Section II. As a validation dataset, we used |  |  |  |  |  |
| • | Call | indirection | involves | creating | a | new | method | to | the AndroOBFS dataset [37], which was obfuscated using |  |
| invoke the original method. Within the course of code | ObfuscAPK. Further details on this dataset and its role |  |  |  |  |  |  |  |  |  |
| execution, each method call is shadowed by this interme- | in validating our method’s performance will be discussed |  |  |  |  |  |  |  |  |  |
| diary method, which, in turn, invokes the original method. | in Section III-C. |  |  |  |  |  |  |  |  |  |
| It introduces complexity in the process of code restoration | • | DexGuard | [38] is an advanced paid version of ProGuard, |  |  |  |  |  |  |  |
| and impairs readability [29], [32]. | also provided by GuardSquare. DexGuard implements |  |  |  |  |  |  |  |  |  |
| • | Reflection | is a technique in Java to alter the runtime | all three techniques discussed earlier and also supports |  |  |  |  |  |  |  |
| behaviour of a program dynamically. It primarily lever- | Runtime | Application | Self-Protection | (RASP) | for | app |  |  |  |  |
| ages the | Java.lang.reflect.* | API, an integral | hardening. We were unable to obtain a free or evaluation |  |  |  |  |  |  |  |

---

## Page 3

version. Therefore, we do not use it when building the

Table I summarizes the features of these obfuscation tools.

TABLE I

S UMMARY OF A NDROID OBFUSCATION TOOLS

Identifier Control Flow String

tect whether an app is being obfuscated or not, followed by

what tool it has used for obfuscation and, finally, what type of

A. Classifier Banks

Our framework consists of three classifier types as illus-

trated in Figure 1a for i) Obfuscation Detection, ii) Obfusca-

tion Tool Detection, and iii) Obfuscation Technique Detection .

Using our training and validation sets ( cf. Section III-C),

we tested several models, such as MLP, SVM, Random Forest,

and Decision Trees. We selected the best model for each task

and further tuned the hyper-parameters using grid search.

Our models and features are comparable to existing work

in obfuscation detection [25], [26], [30], [34] and provide

similar performance. Here, our methodological contribution

is the comprehensive framework, which facilitates subsequent

large-scale longitudinal analysis of obfuscation adoption.

need to distinguish between multiple classes. Also, it

allows easy scalability by adding new classifiers as data

a bank of three binary Random Forest classifiers for

3

TABLE II

Obfuscation

| Category | Category | Feature |  |
| --- | --- | --- | --- |
| Class | Feature 1 - 5: |  |  |
| Names | Percentage of class names of length 1, 2, 3, 4 and | > | 4 |
| Identifier | Feature 6 - 8: |  |  |
| Renaming | Percentage of class names containing special characters, |  |  |

numeric characters, or both

Feature 14 - 16:

Names Percentage of field names of length 1, 2, 3, 4 and > 4

Percentage of class names containing special characters,

String Feature 25 - 29:

Encryption Strings Percentage of other strings of length 1, 2, 3, 4 and > 4

Feature 30 - 32:

Percentage of class names containing special characters,

Control

Percentage of nop, goto, invoke, if, and move instructions

Given an APK, these classifiers predict whether it is ob-

fuscated with each of these techniques. If the probability

given by a classifier is higher than 0.5, we categorize the

APK as obfuscated using the relevant technique.

B. Feature Engineering

We use 37 features of three types to represent an Android

APK. They are primarily related to obfuscation techniques we

focus on, as summarised in Table II. These features were

selected based on prior works [30], [34]. We use Andro-

guard [39] to extract Identifier names, Strings and Instructions

from APKs’ DEX files. We calculate the percentages of class

names, method names, field names, and other strings based

on their lengths, the presence of special characters, and the

No. of class names with length 1

Total number of class names

| training set later. | E | XTRACTED FEATURE LIST |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Tool | Method | Feature 9 - 13: |  |  |  |  |
| Renaming | Modification | Encryption | Names | Percentage of method names of length 1, 2, 3, 4 and | > | 4 |
| ProGuard | Yes | No | No | Percentage of class names containing special characters, |  |  |
| DashO | Yes | Yes | Yes | numeric characters, or both |  |  |
| Allatori | Yes | Yes | Yes | Field | Feature 17 - 21: |  |
| ObfuscAPK | Yes | Yes | Yes | Feature 22 - 24: |  |  |
| DexGuard | Yes | Yes | Yes | numeric characters, or both |  |  |
| III. O | BFUSCATION | D | ETECTION | F | RAMEWORK | numeric characters, or both |
| We developed a machine learning-based framework to de- | Flow | Instructions | Feature Ins 33 - 37: |  |  |  |
| obfuscation(s) are present. Our framework consists of a bank | [26], [29]–[31]; i) Identifier Renaming (IR), ii) Control |  |  |  |  |  |
| of classifiers that use the same Android APK-level features. | Flow Modification (CF), and iii) String Encryption (SE). |  |  |  |  |  |

• Obfuscation Detector : Our Obfuscation Detector is a presence of numeric characters. Specifically, we count the

binary MLP classifier that makes a prediction of whether occurrences of names with lengths of 1, 2, 3, 4, and greater

a given Android APK is obfuscated or not. than 4, as well as those containing special characters, numeric

• Obfuscation Tool Detector : We use a bank of three characters, or both. For example, Feature 1, described in

binary Random Forest classifiers for obfuscation tool Equation (1), represents the percentage of class names with

detection making decisions: 1. ProGuard vs. Other , 2. a length of 1 relative to the total number of class names

Allatori vs. Other , 3. DashO vs. Other . Each classifier in a given APK. Equation (2) calculates the percentage of

assigns a probability to each tool: Proguard, DashO, and class names containing special characters relative to the total

Allatori. Based on the highest probability, we decide number of class names. We performed similar calculations for

which tool the APK uses. We chose to use a bank of other attributes, as detailed in Table 2. For instructions, we

classifiers rather than a single multi-class classifier to selected five specific instructions: nop, goto, invoke,

handle the other category more effectively, given the if, and move . We then calculated the percentage of these

absence of training data for unknown obfuscation tools. selected instructions out of the total number of available

This approach simplifies decision-making, as they do not instructions, as shown in Equation (3).

| from other tools becomes available. | Feat. 1 | = | × | 100 | (1) |
| --- | --- | --- | --- | --- | --- |
| • | Obfuscation Technique Detector | : Similarly, we train | Total number of class names |  |  |
| Obfuscation Technique Detection. We focused on the | No. of class names consist of special chars |  |  |  |  |
| most commonly used obfuscation techniques that were | Feat. 6 | = | × | 100 |  |
| discussed in Section II-A and in previous works [22], | (2) |  |  |  |  |

---

## Page 4

m x n

F 1 F 2 ..... F 37 Label

ProGuard vs. Other

Samples (n) m = 38 :

Feature Extractor

Features (37)

IR

Label (1)

ProGuard

m x 1 vs. Other

F 1 F 2 .... F 37 Obfuscation

Detector

Sample (1)

Features (m = 37)

Feature Extractor IR

Fig. 1. Overall experiment process: Training and testing and large-scale investigation.

No. of nop Instructions

Total number of Instructions

C. Building the Ground-truth Dataset

APKs from the Google Play Store and manually labelled them

for obfuscation, serving as an additional validation dataset.

apps, we label them only as obfuscated or not.

Using manually created obfuscated and non-obfuscated

validate each classifier. The summary of these data subsets is

discussed below.

4

Obfuscation Detection

Obfuscation Detector

Obfuscation Tool Detector

Allatori vs. Other DashO vs. Other

Optimum

Obfuscation Technique Detector

CF Training and testing Model

SE

Storage

(a) Training and testing

Allatori DashO

vs. Other vs. Other

CF SE

(b) Large-scale analysis

• D1 : Training and testing dataset (349 MC-APKs; 80%

for training and parameter tuning, and 20% for testing).

• D3: Random subset of AndroOBFS (270 APKs).

• D4: Manually labelled 50 Google Play APKs.

Using F-Droid [40] Android projects, we manually created

TABLE III

| Dataset | Obfuscated | N-Obfuscated | Total |
| --- | --- | --- | --- |
| D1 | 274 | 75 | 349 |
| D4 | 33 | 17 | 50 |

Feat. Ins 33 = × 100 (3) • D2: Unseen evaluation dataset (135 MC-APKs).

To build our training dataset, we downloaded app source 87 non-obfuscated APKs and 397 obfuscated APKs (MC-

codes from the F-droid repository [40]. We imported each APKs). Due to the limited number of ground truth APKs, we

source code to Android Studio and disabled any obfuscation divided these manually created APKs into two sets, D1 and

in the build.gradle to produce non-obfuscated samples. D2, as detailed in Table III. We utilized D1 as our training

To create obfuscated samples, we used the same projects and testing dataset, reserving D2 as an unseen validation

imported from F-droid and employed ProGuard [27], Alla- dataset to assess the generalizability of our models. To further

tori [28], and DashO [35] as obfuscation tools. While Proguard enhance the validation of generalizability, we incorporated

is free, for Allatori, we used the educational version, which has the AndroOBFS dataset [37]. We randomly selected D3 from

the same features as the commercial version. For DashO, we the AndroOBFS dataset as our second validation set. As

used the 7-day evaluation licence provided to us by PreEmp- shown in Table III, all APKs in the AndroOBFS dataset

tive Inc., which again has the full features of the commercial are obfuscated; no non-obfuscated APKs were included. To

version. To train the Obfuscation Technique detector, we strengthen the validation of our obfuscation detector, we also

created sets of APKs by applying each technique individually, randomly selected 50 APKs from the Google Play Store and

thereby ensuring separate datasets for each technique. manually labelled them. We examined the identifier names of

Furthermore, we also use the AndroOBFS dataset [37], each APK to identify any anomalies or deviations in natural

comprising malware APKs obfuscated with ObfuscAPK [36]. language. APKs were labelled as obfuscated if anomalies were

Our aim is to select a subset of APKs from AndroOBFS to observed in the identifier names; otherwise, they were labelled

validate our classifiers and verify that they perform well with as non-obfuscated. Out of the 50 APKs, 33 were classified as

unseen obfuscation tools. Finally, we obtained a set of random obfuscated and 17 as non-obfuscated after manual labelling.

| Since we don’t know which tool was used to obfuscate these | O | BFUSCATION | D | ETECTOR | D | ATASET |
| --- | --- | --- | --- | --- | --- | --- |
| APKs | (MC-APKs) | , AndroOBFS APKs, and 50 Google Play | D2 | 123 | 12 | 135 |
| Store APKs | (GP) | , we generated several datasets to train and | D3 | 270 | 0 | 270 |
| 1) Datasets for Obfuscation Detector: | We curated four | 2) Datasets for Obfuscation Tool Detector: | We use MC- |  |  |  |

datasets using MC-APKs, AndroOBFS data, and 50 GP APKs: APKs and AndroOBFS apps to create two datasets:

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

and testing the tool detection model, and keeping D6 as the

Dataset ProGuard DashO Allatori Obfuscapk Total

• D7: Training and testing dataset (324 MC-APKs; 80%

for training and parameter tuning, and 20% for testing).

• D8: Unseen evaluation dataset (52 MC-APKs)

• D9: Random subset of AndroOBFS (90 each for IR, CF,

and SE).

In line with the tool detection process, we removed non-

obfuscated APKs and irregularly combined APKs from the

original dataset (from MC-APKs) to create a set of 376

manually obfuscated APKs for technique detection. As with

the previous cases, we split this dataset into two subsets:

D7 for training and testing, and D8 for unseen evaluation.

The number of APKs in each dataset is detailed in Table V.

Additionally, since the AndroOBFS dataset provides APKs

labelled with obfuscation techniques, we randomly selected

an extra set of APKs (D9) from it to further validate the

generalizability of our method.

TABLE V

O BFUSCATION T ECHNIQUE D ETECTOR ATASET

| D8 | 15 | 7 | 7 | 2 | 2 | 4 | 15 | 52 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D9 | 90 | 90 | 90 | - | - | - | - | 270 |

excluded all non-obfuscated APKs and APKs created using

5

D3 0.88 1.00 0.88 0.94

(ProGuard, Allatori, DashO) or another tool (Other). Here, it

usage must be classified as other. For instance, if an APK

is obfuscated with DashO , ProGuard vs. Other and Allatori

vs. Other should classify it as Other , while DashO vs. Other

should detect it as DashO . For APKs from AndroOBFS, all

three classifiers should classify them as Other . Therefore, we

use macro versions of Precision, Recall, and F1 to evaluate

performance. We summarize the results in Table VII.

On the test set (D5), our classifier bank achieves an average

of 99% which is comparable to previous work [25]. However,

we highlight that [25] operates in a closed-set setting and, as

such, does not have the means to categorize unknown obfus-

cators accurately. To further validate how well the classifiers

perform in detecting unknown tools, we evaluated them on

D6. We achieved an average accuracy of 88% showing that

the obfuscation tool detector indeed works well with unknown

tools and classifies them as others with high accuracy.

TABLE VII

O BFUSCATION TOOL DETECTION - R ESULTS

Macro

P R F1

D5

Allatori vs. Other 1.00 1.00 1.00 1.00

(Test Set)

| DashO vs. Other | 0.98 | 0.97 | 0.97 | 0.97 |
| --- | --- | --- | --- | --- |
| ProGuard vs. Other | 0.82 | 0.91 | 0.86 | 0.90 |

• D5: Training and testing dataset (312 MC-APKs; 80% D. Performance of the Classifiers

for training and parameter tuning, and 20% for testing). 1) Obfuscation Detector: We show the performance of

• D6: Unseen evaluation dataset (50 MC-APKs + 30 An- the obfuscation detector on different datasets in Table VI.

droOBFS) Our results are comparable to those of OBFUSCAN [26],

We excluded all non-obfuscated APKs from the manually which reported similar findings. However, OBFUSCAN targets

created APK dataset (from MC-APKs) because they could not only ProGuard-obfuscated APKs, whereas our tool can handle

be categorized under any obfuscation tools. Additionally, we APKs obfuscated by various obfuscators. To assess how well

removed APKs that were obfuscated using a combination of our obfuscation detector works with unseen data (i.e., not

two tools, as it was challenging to classify such APKs under from a split of the training and test set), we evaluated it

a single tool. Consequently, we had 362 obfuscated APKs on D2, D3 and D4 as well. While the performance dropped

available for tool detection. Similar to the previous scenario, somewhat, detector accuracy was still in the range of 87%–

we divided this dataset into D5 and D6, using D5 for training 92%, suggesting its suitability for the large-scale analysis.

| unseen validation set. To ensure that our model can accurately | TABLE VI |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| classify the “Other” category, we randomly selected 30 APKs | O | BFUSCATION DETECTION | - R | ESULTS |  |  |  |  |  |  |  |  |
| from the AndroOBFS dataset and combined them with D6, | Dataset | Accuracy | Precision | Recall | F1 Score |  |  |  |  |  |  |  |
| as detailed in Table IV. We used D6 as our unseen validation | D1 (Test Set) | 0.97 | 0.96 | 1.00 | 0.98 |  |  |  |  |  |  |  |
| dataset. | D2 | 0.87 | 1.00 | 0.85 | 0.92 |  |  |  |  |  |  |  |
| TABLE IV | D4 | 0.92 | 1.00 | 0.88 | 0.94 |  |  |  |  |  |  |  |
| O | BFUSCATION | T | OOL | D | ETECTOR | D | ATASET | Avg. | 0.91 | 0.99 | 0.90 | 0.95 |
| D5 | 68 | 162 | 82 | 0 | 312 | 2) Obfuscation Tool Detector Bank: | Each classifier in our |  |  |  |  |  |
| D6 | 15 | 20 | 15 | 30 | 80 | bank determines if an APK is obfuscated using a specific tool |  |  |  |  |  |  |

3) Datasets for Obfuscation Technique Detector: We used is crucial to assess that each classifier is not only classifying

376 MC-APKs and AndroOBFS apps to create three datasets: its own target tool usage correctly but also any other tool

| Dataset | IR | CF | SE | IR&CF | IR&SE | CF&SE | All | Total | Dataset | Classifier | Acc. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D7 | 45 | 36 | 36 | 23 | 23 | 23 | 138 | 324 | ProGuard vs. Other | 1.00 | 1.00 | 1.00 | 1.00 |
| Note that there are different numbers of APKs in the MC- | D6 | Allatori vs. Other | 0.89 | 0.91 | 0.90 | 0.94 |  |  |  |  |  |  |  |
| APKs dataset for the three detectors. This is because we | DashO vs. Other | 0.84 | 0.93 | 0.87 | 0.89 |  |  |  |  |  |  |  |  |
| multiple tools (i.e., ProGuard and Allatori combined) from | 3) Obfuscation Technique Detector Bank: | Similarly, we |  |  |  |  |  |  |  |  |  |  |  |

the MC-APKs when creating the tool detector and technique show the performance of the obfuscation technique detector

datasets. Additionally, to balance the unseen evaluation set, bank in Table VIII. On the test set (D7), we achieved an aver-

we used only 30 APKs from AndroOBFS in D6. age accuracy of 88% which is comparable to prior works [23],

---

## Page 6

niques. Additionally, although the results of AndrODet* [30]

O BFUSCATION TECHNIQUE DETECTION - R ESULTS

| Dataset | Classifier | Precision | Recall | F1 | Accuracy |
| --- | --- | --- | --- | --- | --- |
| (IR) | 0.98 | 0.89 | 0.93 | 0.91 |  |
| (IR) | 1.00 | 0.88 | 0.94 | 0.92 |  |
| D8 | (CF) | 0.82 | 0.96 | 0.89 | 0.86 |
| (SE) | 1.00 | 0.79 | 0.88 | 0.79 |  |

In summary, we presented an obfuscation detection frame-

work comprising three machine learning models developed

to detect obfuscation, obfuscation tools, and techniques. We

evaluated the capabilities of these models to perform large-

scale analysis using various ground-truth datasets, which are

employed in the large-scale analysis as illustrated in Figure 1b.

In addition, we have publicly released the source codes of

our classifiers along with its best models and ground-truth

A. Dataset

Our large-scale analysis data is based on two large snapshots

(e.g., app ID, app genre, developer name, number of down-

6

APKs.

as listed in Table IX. The reason for not analysing all apps in

B. Process of APK Analysis

in Section III-B. Next, we make a prediction using our

Obfuscation Tool Detector Bank and Obfuscation Technique

Detector Bank to identify the tool and technique(s) used. In

the Tool Detector step, if all three classifiers give a probability

of less than 0 . 5 , we categorize the APK as using an Other

tool. Otherwise, we use the highest probability to determine

the tool. In the Technique Detector, the classifier identifies the

obfuscation technique (IR, CF, SE) if its probability exceeds

0 . 5 . This overall process is illustrated in Figure 1b.

In this section, we present various analysis results that

A. Overall Obfuscation Trends

development practices.

among developers, likely driven by heightened security and IP

[30], [34]. Our technique outperforms the method described is significantly slower than the metadata crawler. Second, we

in [34]. While [23] focuses solely on identifier renaming, our do not download the APKs of paid apps. Third, some apps

method addresses a broader range of popular obfuscation tech- do not support the Android device we simulated to download

for the training and test datasets are comparable to those One of the fields in app metadata is the “ last update

of our method, they retrained their model before evaluating date ”. We use this field to categorise apps by year as

it on unseen data. This approach converts the unseen data summarised in Table IX. As can be seen, the centre years of

into seen data, which undermines the generalizability of their our two crawls, i.e., 2017 and 2022, have the highest number

method. Such generalizability is crucial for conducting a of apps. We have a notably smaller number of apps for 2019

comprehensive large-scale study. and 2020 because they were only collected in 2022, and only

Further, to examine the generalizability of our method, we a limited number of apps have the last update date in 2019

conducted two validation studies using D8 and D9, which and 2020. These apps can bias our analysis as these represent

are unseen and differently distributed from the original train- apps that have been most likely abandoned by app developers.

ing/test dataset. Still, the classifier bank achieves average As a result, we do not consider 2019 and 2020 in our extended

| accuracies of 88% and 80%. | analysis. For each year, we analyse a random sample of apps |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| TABLE VIII | all the years is the time, as APK decompilation takes time. |  |  |  |  |  |
| D7 (Test Set) | (CF) | 0.87 | 0.91 | 0.89 | 0.85 | For each APK we analyse, we use Androguard [39] and our |
| (SE) | 0.92 | 0.92 | 0.92 | 0.88 | pre-processing scripts to create the feature vector described |  |
| (SE) | 0.83 | 0.93 | 0.88 | 0.86 | Obfuscation Detector | . If the app is predicted as not obfuscated, |
| (IR) | 1.00 | 0.84 | 0.92 | 0.84 | we record this and stop further analysis for that app. If the |  |
| D9 | (CF) | 1.00 | 0.78 | 0.88 | 0.78 | APK is obfuscated, we use the same feature vector with the |
| datasets. | 1 | V. R | ESULTS |  |  |  |
| IV. L | ARGE | S | CALE | A | NALYSIS | demonstrate the adoption of code obfuscation in Google Play. |
| of the Google Play Store collected around 2018 and 2023. | 1) Presence of obfuscation: | Out of the 548,967 Google |  |  |  |  |

The 2018 dataset that was collected as a part of our previous Play Store APKs analyzed, we identified 308,782 obfuscated

work [41], [42] contains metadata of over 1.2 million apps apps, representing approximately 56.25% of the total. In

that were collected between January and March 2018 and Figure 2, we show the year-wise percentage of obfuscated apps

1,023,521 APK files. The 2023 dataset contains metadata of for 2016-2023. There is an overall obfuscation increase of 13%

over one million apps and was collected between January and between 2016 and 2023, and as can be seen, the percentage

November and 395,396 APK files. of obfuscated apps has been increasing in the last few years,

Both datasets were collected in the same way using a barring 2019 and 2020. As explained in Section IV-A, 2019

Python-based crawler. First, the crawler discovered available and 2020 contain apps that are more likely to be abandoned

apps on the Google Play Store. Then, it collected app metadata by developers, and as such, they may not use advanced

loads, rating details) and APK executables for free apps. There From 2016 to 2018, the obfuscation levels were relatively

are several reasons behind the difference between the number stable at around 50-55%, while from 2021 to 2023, there

of apps for which we crawled metadata and the number of apps was a marked rise, reaching approximately 66% in 2023.

for which we downloaded the APKs. First, the APK crawler This indicates a growing focus on app protection measures

1 https://github.com/NSS-USYD/Obfuscation-Large Analysis concerns and the availability of advanced obfuscation tools.

---

## Page 7

TABLE IX

N UMBER OF APK

Average Obfuscation Level (2016 - 2023)

50

Obfuscated Percentage (%)

Year

tool detector identified that 40.92% of the apps use Proguard,

(i.e., unknown) tools. We show the yearly trends in Figure 3.

ProGuard and Allatori are the most consistently used obfus-

cation tools, with ProGuard showing a slight overall increase

ProGuard usage increased by 13% from 2018 to 2021, likely

| 90 | Fig. 4. |
| --- | --- |
| 80 | ProGuard |
| 70 | Allatori |

60

40

30

Percentage (%)

Year

7

S PER YEAR

3) Obfuscation techniques: We show the year-wise break-

down of obfuscation technique usage in Figure 4. Among the

Identifier Renaming (IR) can be attributed to the fact that

adoption of Control Flow Modification and String Encryption

Only SE 0.01 0.06 0.06 0.00 0.00 0.00 40

30

Percentage (%)

10

All Three 63.25 58.47 57.83 52.64 56.38 63.46

Year

Yearly obfuscation technique usage

Next, we investigate the adoption of obfuscation on Google

B. App Genre

We note that 19 genres have more than 60% of the apps

obfuscation percentage. Casino genre has the highest obfus-

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Available APKs | 174,136 | 501,865 | 157,613 | 7,205 | 21,014 | 60,705 | 240,775 | 65,697 | 1,229,010 |
| Analysed APKs | 74,817 | 159,639 | 80,112 | 7,201 | 20,982 | 59,539 | 81,134 | 65,543 | 548,967 |
| 90 | checked a sample of apps from the ‘other’ category and |  |  |  |  |  |  |  |  |
| 80 | Obfuscated Percentage | confirmed they are indeed obfuscated. However, we could not |  |  |  |  |  |  |  |
| 70 | determine which obfuscation tools the developers used. We |  |  |  |  |  |  |  |  |
| 60 | discuss this potential limitation further in Section VII-B. |  |  |  |  |  |  |  |  |
| 40 | various obfuscation techniques, Identifier Renaming emerged |  |  |  |  |  |  |  |  |
| 30 | as the most prevalent, with 99.62% of obfuscated apps using |  |  |  |  |  |  |  |  |
| 20 | it alone or in combination with other methods (Categories of |  |  |  |  |  |  |  |  |
| 10 | Only IR, IR and CF, IR and SE, or All three). Furthermore, |  |  |  |  |  |  |  |  |
| 0 | 81.04% of obfuscated apps used Control Flow Modification, |  |  |  |  |  |  |  |  |

2016 2017 2018 2019 2020 2021 2022 2023 and 62.76% used String Encryption. The pervasive use of

Fig. 2. Percentage of obfuscated apps by year all obfuscation tools support it ( cf. Table I). Similarly, lower

2) Obfuscation tools: Among the obfuscated APKs, our can be attributed to Proguard not supporting it.

| 36.64% use Allatori, 1.01% use DashO, and 21.43% use other | Only IR | 11.00 | 13.84 | 14.45 | 20.82 | 18.92 | 14.21 | 60 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note that we omit results in 2019 and 2020 ( | cf. | Section IV-A). | Only CF | 0.00 | 0.08 | 0.13 | 0.01 | 0.00 | 0.01 | 50 |
| in popularity and Allatori demonstrating variability. This in- | IR & CF | 21.13 | 24.10 | 24.47 | 24.50 | 19.16 | 16.56 |  |  |  |
| clination could be attributed to ProGuard being the default | Category | IR & SE | 4.59 | 2.85 | 2.17 | 2.02 | 5.51 | 5.73 |  |  |
| obfuscator | integrated | into | Android | Studio, | a | widely | used | 20 |  |  |
| development environment for Android applications. Notably, | CF & SE | 0.02 | 0.61 | 0.88 | 0.02 | 0.02 | 0.03 |  |  |  |
| due to the introduction of R8 in April 2019 [43], which further | 0 |  |  |  |  |  |  |  |  |  |
| simplified ProGuard integration with Android apps. | 2016 | 2017 | 2018 | 2021 | 2022 | 2023 |  |  |  |  |
| DashO | Play Store from various perspectives. Same as earlier, due to |  |  |  |  |  |  |  |  |  |
| Other | the smaller dataset size and possible bias ( | cf. | Section IV-A), |  |  |  |  |  |  |  |
| 50 | we exclude the APKs from 2019 and 2020 from this analyses. |  |  |  |  |  |  |  |  |  |
| 20 | First, we investigate whether the obfuscation practices vary |  |  |  |  |  |  |  |  |  |
| 10 | according to the App genre. Initially, we analysed all the APKs |  |  |  |  |  |  |  |  |  |
| 0 | together before separating them into two snapshots. |  |  |  |  |  |  |  |  |  |
| 2016 | 2017 | 2018 | 2021 | 2022 | 2023 | Figure 5 shows the genre-wise obfuscated app percentage. |  |  |  |  |
| Fig. 3. | Yearly obfuscation tool usage | obfuscated, and almost all the genres have more than 40% |  |  |  |  |  |  |  |  |

DashO consistently remains low in usage, likely due to its cation percentage rate at 80%, and overall, game genres tend

high cost. The use of other obfuscation tools decreased until to be more obfuscated than the other genres. The higher

2018 but has shown a resurgence from 2021 to 2023. This obfuscation usage in casino apps is logical due to their nature.

suggests that developers might be using other or custom tools, These apps often simulate or involve gambling activities and

or our detector might be predicting some apps obfuscated with handle monetary transactions and sensitive data related to in-

Proguard or Allatori as ‘other.’ To investigate, we manually game purchases, making them attractive targets for reverse

*[Image: Page 7 Image]*

---

## Page 8

80

40

Percentage (%) 20

0

Casino Action Music Trivia Word Card

Racing Casual Puzzle Board

Strategy Comics Arcade

Weather

Simulation Art & Des. Adventure

Video Players Music & Aud. Entertainment

App Genre

Fig. 5. Obfuscated app percentage by genre (overall)

engineering and hacking. This necessitates robust security

measures to prevent fraud and protect user data.

80

70

60

50 Obfuscation 2023

Average 2023

| Music | Comics | Events | Social | Tools | Puzzle | Dating | Word | Card | Sports |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Education | Weather | Medical | Arcade | Casual | Board | Trivia |  |  |  |
| Shopping | Parenting | Finance | Strategy | Beauty | Lifestyle | Casino | Action | Racing |  |

Adventure Art & Des. Business

| Maps & Nav. | Food & Drink | Health & Fit. | Productivity | Auto & Veh. | Educational | Simulation |
| --- | --- | --- | --- | --- | --- | --- |
| Libs. & Demo | Travel & Local | News & Mag. | Music & Aud. | Photography | Video Players | Role Playing |

Communication Entertainment Books & Ref

House & Home Personalization

App Genre

categories such as Education, Weather, and Parenting, which

had obfuscation levels below the 2018 average, have increased

to above the 2023 average by 2023. One possible reason for

8

Games Category

Tools

Dating Sports Beauty Social Events

Lifestyle Finance Medical

Business

Parenting Shopping Education

News & Mag. Books & Ref. Health & Fit. Food & Drink Maps & Nav. Libs & Demo

Communication

100

90

80

70

Percentage (%) 60 IR

CF

50 SE

Casino Action Music Trivia Word Card

Strategy Racing Casual Puzzle Comics Board

Finance Beauty Social Events

Business Medical

Simulation Art & Des. Adventure Weather Parenting Shopping Education

Personalization Video Players Entertainment Books & Ref. Health & Fit. Educational Auto & Vehi. Food & Drink Productivity

Travel & Local Maps & Nav.

Communication

App Genre

Fig. 7. Obfuscation technique usage by genre (overall)

Casino genre apps employ multiple obfuscation techniques

C. App Developers

| 60 | Applications Category |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Role Playing | Photography | Educational | Auto & Veh. | Productivity |  |  |
| Personalization | House & Home | Travel & Local |  |  |  |  |
| 40 | Obfuscation 2018 | Arcade | Lifestyle | Dating | Sports | Tools |
| Obfuscation Percentage (%) | Average 2018 | Role Playing | Photography | Music & Aud. | News & Mag. |  |
| 30 | House & Home | Libs. & Demo |  |  |  |  |
| Fig. 6. | Percentage of obfuscated apps by genre (2018-2023) | all three obfuscation techniques. Notably, more than 85% of |  |  |  |  |
| 1) Genre-wise obfuscation trends in the two snapshots: | To | 3) Obfuscation tool usage in different app genres: | We also |  |  |  |

investigate the adoption of obfuscation over time, we study investigated whether specific obfuscation tools are favoured

the two snapshots of Google Play separately, i.e., APKs from by developers in different genres. However, apart from the

2016-2018 as one group and APKs from 2021-2023 as another. expected observation that ProGuard and Allatori being the

Figure 6 illustrates the change in obfuscation levels by most used tools, we didn’t find any other interesting patterns.

app genre between 2016-2018 to 2021-2023. Notably, app Therefore, we haven’t included those measurement results.

this in Education and Parenting apps can be the increase in Next, we investigate individual developer-wise code ob-

online education activities during and after COVID-19 and the fuscation practices. From the pool of analyzed APKs, we

developers identifying the need for app hardening. identified the number of apps associated with each devel-

There are some genres, such as Casino and Action, for oper. Subsequently, we sorted the developers according to the

which the percentage of obfuscated apps didn’t change across number of apps they had created and selected the top 100

the two snapshots (i.e., purple and orange circles are close developers with the highest number of APKs for the 2016-

together in Figure 6). This is because these genres are highly 2018 and 2021-2023 datasets. For the 2018 snapshot, we had

obfuscated from the beginning. Finally, the four genres, includ- 8,349 apps among the top 100 developers, while for the 2023

ing Simulation and Role Playing, have a lower percentage of snapshot, we had 11,338 apps among the top 100 developers.

obfuscated apps in the 2021-2023 dataset. Our manual analysis We then proceeded to detect whether or not these developers

didn’t result in a conclusion as to why. obfuscate their apps and, if so, what kind of tools and

2) Obfuscation techniques in different app genres: In Fig- techniques they use. We present our results in five levels;

ure 7, we show the prevalence of key obfuscation techniques developer obfuscating over 80% of their apps, 60%–80% of

among various genres. As expected, almost all obfuscated apps apps, 40%–60% of apps, less than 40%, and no obfuscation.

in all genres used Identifier Renaming. Also, it can be noted Figure 8 compares the two datasets in terms of developer

that genres with more obfuscated app percentages tend to use obfuscation adoption. It shows that more developers have

---

## Page 9

40% - 60% Apps Obfuscated

15

28

6

2

76

19

Fig. 8. Obfuscation usage (Top-100 developers)

TABLE X

Non

Obfuscated

22,214 (45.5%)

2018 26,581

ProGuard Allatori DashO Other

26,084 (57.2%)

| 2023 | 19,510 |
| --- | --- |
| Snapshot | (42.8%) |

2023 dataset (76%) compared to the 2016-2018 dataset (48%).

We also found that among developers who obfuscate more

than 80% of their apps, 73% in 2018 and 93% in 2023 used

the same obfuscation tool. Additionally, these top developers

employ Control Flow Modification (CF) and String Encryption

(SE) above the average values discussed in Section V-A.

Specifically, in 2018, top developers used CF in 81.3% of

cases and SE in 66.7%, while in 2023, these figures increased

to 88.2% and 78.9%. This results in two insights: 1) Most

top developers obfuscate all their apps with advanced tech-

niques, possibly due to concerns about IP and security, and 2)

Developers stick to a single tool, possibly due to specialized

knowledge or because they bought a commercial licence.

Finally, we investigate the obfuscation practices of devel-

opers with only one app in Table X. According to the table,

from those developers, 45.5% of them obfuscated their apps in

the 2016-2018 dataset and 57.2% obfuscated their apps in the

2021-2023 dataset, showing a clear increase. However, these

percentages are approximately 10% lower than the average

obfuscation rate in both cohorts discussed in Section V-A.

criterion used by our previous work [41], [42], [44]. That is,

9

technique usage as summarized in Table XI.

When considering the highly ranked applications (i.e., top-

1,000), the obfuscation percentage is notably higher, at around

93%, in both datasets, which is significantly higher than the av-

Top-ranked apps, likely due to their higher visibility and

potential revenue, invest more in obfuscation to safeguard their

intellectual property and enhance security.

The obfuscation percentage decreases when going from

indicates that the major increase in obfuscation in the 2021-

2023 dataset comes from apps beyond the top 30,000.

When observing the tools used, the usage of ProGuard

datasets. This may be because ProGuard is free and the default

DashO are expensive. There is a notable increase in the use

more heavily protected compared to lower-ranked ones.

A. Obfuscation Detection

Multiple works developed methods to detect obfuscation

and identify the tools and techniques used. For instance,

K¨ uhnel et al. [23] introduced the IREA framework, employing

a rule-based detection algorithm tailored to identify obfusca-

tion techniques such as Identifier Renaming. Despite achieving

high accuracy, this approach’s reliance on specific rules limits

its applicability across diverse scenarios.

Similarly, Wermke et al. [26] developed OBFUSCAN to

emulate ProGuard’s behaviour, focusing primarily on detection

techniques aligned with ProGuard’s functionalities. However,

this specialization restricts its performance with other obfus-

cation tools. In contrast, Wang et al. [25] presented a multi-

class classifier utilizing SVM to identify obfuscation tools

and configurations, demonstrating promising accuracy levels.

Nonetheless, the limited dataset used for validation raises con-

cerns regarding its generalizability. Dong et al. [22] and Park

et al. [24] proposed machine learning-based methods to detect

obfuscation techniques. AndrODet [34] and AndrODet* [30]

also had similar approaches.

framework that facilitates large-scale analysis of APKs. Also,

| 80% - 100% Apps Obfuscated | 0% - 40% Apps Obfuscated | reviewed by a large number of users. Then, we investigated |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 60% - 80% Apps Obfuscated | 0% Apps Obfuscated | the percentage of obfuscated apps and obfuscation tools and |  |  |  |  |  |
| 48 | 1 | erage percentage of obfuscation we observed in Section V-A. |  |  |  |  |  |
| 2 3 | the top 1,000 apps to the top 30,000 apps. Nonetheless, the |  |  |  |  |  |  |
| (a) Obfuscation Usage – | (b) Obfuscation Usage – | obfuscation percentage in both datasets remains around similar |  |  |  |  |  |
| 2018 Snapshot | 2023 Snapshot | values until the top 30,000 (e.g., | ∼ | 74% for top-30,000). This |  |  |  |
| D | EVELOPERS WITH ONLY ONE APP | increases as we move from top to lower-ranked apps in both |  |  |  |  |  |
| Year | Obfuscated | in Android Studio, while commercial tools like Allatori and |  |  |  |  |  |
| Snapshot | (54.5%) | of Allatori among the top apps in the 2021-2023 dataset. |  |  |  |  |  |
| 6,131 | 8,050 | 658 | 7,375 | Regarding obfuscation techniques, the top 1,000 apps utilize |  |  |  |
| ProGuard | Allatori | DashO | Other | all three techniques more frequently than lower-ranked apps |  |  |  |
| 12,697 | 9,672 | 234 | 3,581 | in both snapshots. This indicates that the top 1,000 apps are |  |  |  |
| moved to obfuscate more than 80% of their apps in the 2021- | VI. R | ELATED | W | ORK |  |  |  |
| This indicates that single-app developers may be less aware | In our work, we draw ideas from these machine learning- |  |  |  |  |  |  |
| or concerned about code protection. | based | obfuscation | detectors | and | design | a | comprehensive |
| D. Top-k Apps | in contrast to these works, we train and test our classifiers in |  |  |  |  |  |  |

Next, we investigate the obfuscation practices of top apps a diverse set of datasets to increase the generalizability that is

in Google Play Store. First, we rank the apps using the same required for real-world settings.

we sort the apps in descending order of number of downloads, B. Empirical Studies of Obfuscation

average rating, and rating count, with the intuition that top OBFUSCAN [26] is the most related to our work which

apps have high download numbers and high ratings, even when examined obfuscation usage in the Google Play Store and

---

## Page 10

TABLE XI

S UMMARY OF ANALYSIS RESULTS FOR

In contrast to these works, our research is the largest of its

kind, covers a span of eight years, allowing us to observe

trends, and covers a broader scope of code obfuscation

practices simultaneously .

VII. D ISCUSSION AND C ONCLUDING R EMARKS

A. Implications

10

T OP - K APPS IN 2018 AND 2023

Obfuscation techniques: Our results showed that Identifier

Renaming is the most common obfuscation technique, used

by 99.62% of apps. We also found that 58.7% of apps use

all three main obfuscation techniques. The use of multiple

obfuscation techniques, rather than a single technique, intro-

duces additional complexity to the obfuscated app, thereby

address more complex combinations of obfuscation techniques

in future.

| Top k apps - | Total | Obfuscation | ProGuard | Allatori | DashO | Other | IR | CF | SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Year | Apps | Percentage | Percentage | Percentage | Percentage | Percentage | Percentage | Percentage | Percentage |
| 1k (2018) | 1,000 | 93.40 | 29.98 | 28.48 | 0.64 | 40.90 | 99.90 | 88.76 | 65.42 |
| 10k (2018) | 10,000 | 85.19 | 25.55 | 35.32 | 0.47 | 38.65 | 99.90 | 88.76 | 71.91 |
| 20k (2018) | 20,000 | 78.42 | 26.31 | 36.76 | 0.57 | 36.36 | 99.87 | 87.37 | 71.49 |
| 30k (2018) | 30,000 | 74.40 | 27.30 | 37.71 | 0.64 | 34.36 | 99.82 | 86.75 | 71.11 |
| 30k+ (2018) | 314,568 | 53.36 | 36.72 | 34.70 | 1.33 | 27.24 | 99.34 | 83.54 | 63.11 |
| 1k (2023) | 1,000 | 92.50 | 24.00 | 51.89 | 1.95 | 22.16 | 100.0 | 92.54 | 83.68 |
| 10k (2023) | 10,000 | 81.88 | 26.03 | 56.20 | 1.03 | 16.74 | 99.89 | 89.40 | 82.01 |
| 20k (2023) | 20,000 | 76.62 | 30.48 | 52.92 | 0.96 | 15.64 | 99.93 | 85.80 | 78.01 |
| 30k (2023) | 30,000 | 73.72 | 33.87 | 50.34 | 0.89 | 14.90 | 99.95 | 83.31 | 75.34 |
| 30k+ (2023) | 206,216 | 61.90 | 46.56 | 38.21 | 0.64 | 14.59 | 99.97 | 77.51 | 62.50 |

developer awareness through a survey with 1.7 million apps obfuscation practices will allow app store admins to build

from 2010 to 2017, primarily detecting Identifier Renaming. policies that balance obfuscation and code understandability.

Similarly, Dong et al. [22] introduced an obfuscation detection Use of code obfuscation tools: We found that Proguard is

methodology and conducted a large-scale investigation using the most commonly used obfuscation tool (40.92%), likely

26k Google Play Store apps and 65k 3rd Party Apps from because it is free and the default option in Android Studio.

2016 to 2017. However, the authors mainly focus their study Surprisingly, a significant fraction of apps use the commer-

on obfuscation techniques. cial obfuscator Allatori (36.64%). Additionally, we found

Another study [45] introduced an NLP-based obfuscation that 21.43% of apps use unknown obfuscation tools, which

detection tool focusing on symbol renaming and conducted a presents a potential direction for future research. This trend

large-scale empirical study on the iPhone Operating System. may be driven by developers seeking advanced protection for

Hammad et al. [46] discussed the effects of code obfuscations their intellectual property, opting for more advanced tools like

in Android apps, evaluating commercial anti-malware products DexGuard [38] over more commonly used options such as

against various obfuscation tools and strategies. Additionally, ProGuard. In addition, these empirical findings are important

Karg´ en et al. [47] used anomaly detection followed by man- because often malware analysts conduct code reverse engi-

ual inspection to investigate popular obfuscation techniques neering and must be aware of available obfuscation tools

among Malware and Google Play Store APKs, mainly focus- and techniques [23], [25], [29]. Our results, including details

ing on Control Flow obfuscation with Java Reflections using of commonly used tools and the possible existence of non-

13k apps released in 2020. mainstream/unknown obfuscators, will interest them.

Using our obfuscation detection framework, we conducted making reverse engineering more challenging. This highlights

a large-scale, eight-year investigation into code obfuscation the need for more complex de-obfuscation solutions for app

practices in the Google Play Store, analyzing more than analysis as a necessary future research direction. Current de-

500,000 APKs. To the best of our knowledge, this study is obfuscation methods, such as those proposed in [50]–[52], tend

the first of its kind. Finally, we discuss the implications and to focus on individual obfuscation techniques, which limits

limitations of our findings. their scope. Given the evolving industry trends, it is essential to

Adoption of code obfuscation: Overall, code obfuscation App genres: Our app genre-wise obfuscation analysis found

is on an increasing trend in the Google Play Store. More that Gaming and Casino apps use obfuscation more frequently

specifically, we found that the average percentage of obfus- than others. This is indeed not surprising. Due to financial

cated apps between 2016-2018 was 53%, and that increased transactions and gambling, Casino apps strive for obfuscation.

to 62% in 2021-2023. These results indicate more and more The competitive nature and vulnerability to re-packing in

developers are aware of the associated intellectual property gaming apps also explain their higher obfuscation usage. In

and security issues in Google Play and are taking actions to future, we can expect other app categories that also handle

mitigate them. However, app store administrators may want important data and transactions, such as Finance, Health and

to balance obfuscation and readability since excessive code Fitness, and Medical, to adopt more obfuscation. However, it is

obfuscation can hinder in-build security checks in app stores, important to note that the developers must not use obfuscation

e.g., Bouncer [48], [49]. As a result, understanding existing as a security solution, as many examples in the past have

---

## Page 11

Android ecosystem.

B. Limitations and Future Work

separate datasets collected in 2018 and 2023. As a result, we

in Section III-A could have prediction errors, which may

propagate into our large-scale analysis, potentially influencing

from specific libraries within the APK, whether first-party or

analysis on real-world data without ground truth is challeng-

Section II-B), and our classifier should ideally categorize

mistakenly classified as using ProGuard. A possible future

Guard, to improve the classifier’s capability and address this

11

Applied Computing (SAC) , 2025.

appbrain,” AppBrain, 05 2024. [Online]. Available: https://www.

p. 102087, 2021. [Online]. Available: https://www.sciencedirect.com/

of the second ACM conference on Data and Application Security and

Privacy , 2012, pp. 317–326.

[6] P. Bhat and K. Dutta, “A survey on various threats and current state of

security in Android platform,” ACM Computing Surveys (CSUR) , vol. 52,

no. 1, pp. 1–35, 2019.

[7] A. Albakri, H. Fatima, M. Mohammed, A. Ahmed, A. Ali, A. Ali, and

devices,” Mathematical Problems in Engineering , vol. 2022, pp. 1–7,

2022.

[9] W. F. Elsersy, A. Feizollah, and N. B. Anuar, “The rise of obfuscated

Science , vol. 8, p. e907, 2022.

[10] V. Sihag, M. Vardhan, and P. Singh, “A survey of Android

application and malware hardening,” Computer Science Review , vol. 39,

and J. Miguel-Alonso, “Light up that droid! on the effectiveness of

104094, 2025.

[12] P. Beer, M. Squarcina, L. Veronese, and M. Lindorfer, “Tabbed out:

2024, pp. 105–105.

[13] Z. Tan and W. Song, “PTPDroid: Detecting violated user privacy

pp. 473–485.

[14] C. Gao, G. Huang, H. Li, B. Wu, Y. Wu, and W. Yuan, “A comprehensive

[15] A. Pradeep, A. Feal, J. Gamba, A. Rao, M. Lindorfer, N. Vallina-

2022.

[16] Z. Liu, L. F. Zhang, and Y. Tang, “Enhancing malware detection for

Engineering (ASE) . IEEE, 2023, pp. 1212–1224.

[17] L. Wang, H. Wang, X. Luo, and Y. Sui, “Malwhiteout: Reducing

ing , 2022, pp. 1–13.

[18] C. Wang, Y. Zhang, and Z. Lin, “Uncovering and exploiting hidden

Conference on Computer and Communications Security , 2023, pp.

2471–2485.

[19] H. Li, G. Xu, L. Wang, X. Xiao, X. Luo, G. Xu, and H. Wang,

detection by tackling prediction uncertainty,” in Proceedings of the

2024, pp. 1–13.

| shown that “security by obscurity” doesn’t work. | R | EFERENCES |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Top developers and top apps: | Finally, we found that top | [1] | A. Niroshan, S. Seneviratne, and A. Seneviratne, “State of obfuscation: |  |  |  |  |  |  |  |  |
| developers and apps use obfuscation more frequently, often | A longitudinal study of code obfuscation practices in Google Play Store,” |  |  |  |  |  |  |  |  |  |  |
| preferring commercial obfuscators for added protection. This | to appear in | Proceedings of the 40th ACM/SIGAPP Symposium on |  |  |  |  |  |  |  |  |  |
| highlights the importance of obfuscation tools for app devel- | [2] | 2024. | [Online]. | Available: | https://gs.statcounter.com/os-market-share/ |  |  |  |  |  |  |
| opers, encouraging their use to protect apps and IP [8]. Fur- | mobile/worldwide/#quarterly-200901-202402 |  |  |  |  |  |  |  |  |  |  |
| thermore, it educates small-scale developers on best practices | [3] | “Number | of | Android | applications | on | the | Google | Play | Store | — |
| from top developers and can help establish industry standards | appbrain.com/stats/number-of-android-apps |  |  |  |  |  |  |  |  |  |  |
| for obfuscation, especially in the era of GenAI, where code | [4] | S. | Garg | and | N. | Baliyan, | “Android | security | assessment: | A | review, |
| data are used to train AI models, sometimes without developer | taxonomy and research gap study,” | Computers & Security | , vol. 100, |  |  |  |  |  |  |  |  |
| consent. To a certain extent, longitudinal data demonstrate | science/article/pii/S0167404820303606 |  |  |  |  |  |  |  |  |  |  |
| an increasing adoption of obfuscation by smaller developers, | [5] | W. Zhou, Y. Zhou, X. Jiang, and P. Ning, “Detecting repackaged smart- |  |  |  |  |  |  |  |  |  |
| which is a positive indicator of the overall health of the | phone applications in third-party Android marketplaces,” in | Proceedings |  |  |  |  |  |  |  |  |  |
| Limitations: | In our large-scale analysis, we leveraged two | N. M. Elzein, “Survey on reverse-engineering tools for Android mobile |  |  |  |  |  |  |  |  |  |
| didn’t have sufficient representative samples from 2019 and | [8] | P. Faruki, H. Fereidooni, V. Laxmi, M. Conti, and M. Gaur, “Android |  |  |  |  |  |  |  |  |  |
| 2020. While this is a limitation of our analysis, overall trends | code protection via obfuscation techniques: past, present and future |  |  |  |  |  |  |  |  |  |  |
| we observed are unlikely to change even including those data. | directions,” | arXiv preprint arXiv:1611.10231 | , 2016. |  |  |  |  |  |  |  |  |
| It is also important to note that the classifiers discussed | Android malware and impacts on detection methods,” | PeerJ Computer |  |  |  |  |  |  |  |  |  |
| the | overall | findings. | To | mitigate | this, | we | validated | our | p. 100365, 2021. [Online]. Available: https://www.sciencedirect.com/ |  |  |
| classifiers’ performance on unseen data ( | cf. | Section III-D), | science/article/pii/S1574013721000058 |  |  |  |  |  |  |  |  |

demonstrating their generalizability. However, there can still [11] B. Molina-Coronado, A. Ruggia, U. Mori, A. Merlo, A. Mendiburu,

| be error propagation, and with real-world APKs, there is no | static analysis features against app obfuscation for Android malware |  |  |  |
| --- | --- | --- | --- | --- |
| method for accurate ground-truth establishment. | detection,” | Journal of Network and Computer Applications | , vol. 235, p. |  |
| Future Work: | In our obfuscation detection process, we clas- | Subverting the Android custom tab security model,” in | 2024 IEEE |  |
| sify APKs as a whole. However, obfuscation may originate | Symposium on Security and Privacy (SP) | . | IEEE Computer Society, |  |
| third-party. A potential future research direction is to examine | disclosures to third-parties of Android apps,” in | 2023 IEEE/ACM 45th |  |  |
| which parts of the app are obfuscated. Conducting such an | International Conference on Software Engineering (ICSE) | . | IEEE, 2023, |  |
| ing, as it becomes difficult to identify the exact library once it | study of learning-based Android malware detectors under challenging |  |  |  |
| has been obfuscated. This challenge is commonly encountered | environments,” in | Proceedings of the 46th IEEE/ACM International |  |  |
| in third-party library detection research in Android [53]–[56]. | Conference on Software Engineering | , 2024, pp. 1–13. |  |  |
| Additionally, our analysis focused on three commonly used | Rodriguez, and D. Choffnes, “Not your average app: A large-scale |  |  |  |
| and accessible tools. Some apps may employ DexGuard ( | cf. | privacy analysis of Android browsers,” | arXiv preprint arXiv:2212.03615 | , |
| such apps as ‘Others.’ However, due to similarities between | Android apps: Detecting fine-granularity malicious components,” in |  |  |  |
| DexGuard and ProGuard, apps using DexGuard might be | 2023 38th IEEE/ACM International Conference on Automated Software |  |  |  |
| direction is to extend this research by incorporating additional | label errors in Android malware detection,” in | Proceedings of the 37th |  |  |
| obfuscators, including commercially licensed tools like Dex- | IEEE/ACM International Conference on Automated Software Engineer- |  |  |  |
| limitation. | apis in mobile super apps,” in | Proceedings of the 2023 ACM SIGSAC |  |  |
| A | CKNOWLEDGMENTS | “MalCertain: Enhancing deep neural network based Android malware |  |  |
| This research was supported by the Australian Government | IEEE/ACM 46th International Conference on Software Engineering | , |  |  |

through the Australian Research Council’s Discovery Projects [20] E. Liu, S. Rao, S. Havron, G. Ho, S. Savage, G. M. Voelker, and

funding scheme (Project ID DP220102520). D. McCoy, “No privacy among spies: Assessing the functionality and

---

## Page 12

International Conference on Software Engineering , 2024, pp. 1–13.

scale investigation in the wild,” in Security and Privacy in Commu-

[26] D. Wermke, N. Huaman, Y. Acar, B. Reaves, P. Traynor, and S. Fahl,

[28] “Allatori java obfuscator - professional java obfuscation,” allatori.com.

deobfuscation techniques and their impact on investigations,” Forensic

[30] M. Conti, P. Vinod, and A. Vitella, “Obfuscation detection in Android

applications using deep learning,” Journal of Information Security and

Applications , vol. 70, p. 103311, 2022.

[31] R. Guo, Q. Liu, M. Zhang, N. Hu, and H. Lu, “A survey of obfuscation

and deobfuscation techniques in Android code protection,” in 2022 7th

IEEE International Conference on Data Science in Cyberspace (DSC) .

IEEE, 2022, pp. 40–47.

[32] A. Bacci, A. Bartoli, F. Martinelli, E. Medvet, and F. Mercaldo,

https://doi.org/10.1145/3230833.3232823

ference, SecureComm 2019, Orlando, FL, USA, October 23-25, 2019,

tion Computer Systems , vol. 90, pp. 240–261, 2019.

[35] “Android obfuscation and java security with DashO,”

www.preemptive.com, 03 2023. [Online]. Available: https:

//www.preemptive.com/products/dasho/

[36] S. Aonzo, G. C. Georgiu, L. Verderame, and A. Merlo, “Obfuscapk:

An open-source black-box obfuscation tool for Android apps,”

SoftwareX , vol. 11, p. 100403, 2020. [Online]. Available: https:

//www.sciencedirect.com/science/article/pii/S2352711019302791

[37] S. Kumar, D. Mishra, B. Panda, and S. K. Shukla, “AndroOBFS: Time-

tagged obfuscated Android malware dataset with family information,”

2022. [Online]. Available: https://dx.doi.org/10.21227/9ptx-5d17

[38] “Android app security and obfuscation — DexGuard,”

www.guardsquare.com. [Online]. Available: https://www.guardsquare.

com/dexguard

[39] A. Desnos and G. Gueguen, “Androguard documentation,” Obtenido de

Androguard , 2018.

[40] “F-droid - free and open source Android app repository,” f-droid.org.

[Online]. Available: https://f-droid.org/en/

[41] N. Karunanayake, J. Rajasegaran, A. Gunathillake, S. Seneviratne, and

G. Jourjon, “A multi-modal neural embeddings approach for detecting

12

3165–3171.

agp-3-4-0-release-notes

Security , 2023, pp. 1–12.

379–385.

pp. 343–355.

automated deobfuscation of Android apps,” in Proceedings of the 4th

Workshop on Security in Highly Connected IT Systems , 2017, pp. 7–12.

[52] G. You, G. Kim, S. Han, M. Park, and S.-J. Cho, “Deoptfuscator:

Defeating advanced control-flow obfuscation using Android runtime

(art),” IEEE Access , vol. 10, pp. 61 426–61 440, 2022.

[53] Y. Wang, H. Wu, H. Zhang, and A. Rountev, “Orlis: Obfuscation-

resilient library detection for Android,” in Proceedings of the 5th

International Conference on Mobile Software Engineering and Systems ,

2018, pp. 13–23.

919–930.

and Analysis , 2019, pp. 55–65.

3385–3402.

| insecurity of consumer Android spyware apps,” | Proceedings on Privacy | mobile counterfeit apps: A case study on Google Play Store,” | IEEE |
| --- | --- | --- | --- |
| Enhancing Technologies | , 2023. | Transactions on Mobile Computing | , vol. 21, no. 1, 2022. |

[21] Y. Chen, R. Tang, C. Zuo, X. Zhang, L. Xue, X. Luo, and Q. Zhao, [42] J. Rajasegaran, N. Karunanayake, A. Gunathillake, S. Seneviratne, and

| “Attention! your copied data is under monitoring: A systematic study of | G. Jourjon, “A multi-modal neural embeddings approach for detecting |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clipboard usage in Android apps,” in | Proceedings of the 46th IEEE/ACM | mobile counterfeit apps,” in | The World Wide Web Conference | , 2019, pp. |  |  |  |
| [22] | S. Dong, M. Li, W. Diao, X. Liu, J. Liu, Z. Li, F. Xu, K. Chen, X. Wang, | [43] | “Android | studio,” | Android | Developers. | [Online]. |
| and K. Zhang, “Understanding Android obfuscation techniques: A large- | Available: | https://developer.android.com/build/releases/past-releases/ |  |  |  |  |  |

nication Networks: 14th International Conference, SecureComm 2018, [44] S. Seneviratne, A. Seneviratne, M. A. Kaafar, A. Mahanti, and P. Mo-

Singapore, Singapore, August 8-10, 2018, Proceedings, Part I . Springer, hapatra, “Early detection of spam mobile apps,” in Proceedings of the

2018, pp. 172–192. 24th International Conference on World Wide Web , 2015, pp. 949–959.

[23] M. K¨ uhnel, M. Smieschek, and U. Meyer, “Fast identification of [45] P. Wang, Q. Bao, L. Wang, S. Wang, Z. Chen, T. Wei, and D. Wu,

| obfuscation and mobile advertising in mobile malware,” in | 2015 IEEE | “Software protection on the go: A large-scale empirical study on mobile |  |  |
| --- | --- | --- | --- | --- |
| Trustcom/BigDataSE/ISPA | , vol. 1. | IEEE, 2015, pp. 214–221. | app obfuscation,” in | Proceedings of the 40th International Conference |
| [24] | M. Park, G. You, S.-j. Cho, M. Park, and S. Han, “A framework for iden- | on Software Engineering | , 2018, pp. 26–36. |  |

tifying obfuscation techniques applied to Android apps using machine [46] M. Hammad, J. Garcia, and S. Malek, “A large-scale empirical study

| learning.” | J. Wirel. Mob. Networks Ubiquitous Comput. Dependable | on the effects of code obfuscations on Android apps and anti-malware |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Appl. | , vol. 10, no. 4, pp. 22–30, 2019. | products,” | in | Proceedings | of | the | 40th | international | conference | on |
| [25] | Y. Wang and A. Rountev, “Who changed you? obfuscator identification | software engineering | , 2018, pp. 421–431. |  |  |  |  |  |  |  |

for Android,” in 2017 IEEE/ACM 4th International Conference on [47] U. Karg´ en, N. Mauthe, and N. Shahmehri, “Characterizing the use of

Mobile Software Engineering and Systems (MOBILESoft) . IEEE, 2017, code obfuscation in malicious and benign Android apps,” in Proceedings

pp. 154–164. of the 18th International Conference on Availability, Reliability and

“A large scale investigation of obfuscation use in Google Play,” in Pro- [48] U. Nawaz, M. Aleem, and J. C.-W. Lin, “On the evaluation of Android

ceedings of the 34th annual computer security applications conference , malware detectors against code-obfuscation techniques,” PeerJ Com-

2018, pp. 222–235. puter Science , vol. 8, p. e1002, 2022.

[27] “Java obfuscator and Android app optimizer — ProGuard,” [49] A. Bacci, A. Bartoli, F. Martinelli, E. Medvet, F. Mercaldo, C. A.

| www.guardsquare.com. [Online]. Available: https://www.guardsquare. | Visaggio | et al. | , “Impact of code obfuscation on Android malware |  |
| --- | --- | --- | --- | --- |
| com/proguard | detection based on static and dynamic analysis.” in | ICISSP | , 2018, pp. |  |
| [Online]. Available: https://allatori.com/ | [50] | B. Bichsel, V. Raychev, P. Tsankov, and M. Vechev, “Statistical deob- |  |  |
| [29] | X. Zhang, F. Breitinger, E. Luechinger, and S. O’Shaughnessy, “Android | fuscation of Android applications,” in | Proceedings of the 2016 ACM |  |
| application forensics: A survey of obfuscation, obfuscation detection and | SIGSAC Conference on Computer and Communications Security | , 2016, |  |  |
| Science International: Digital Investigation | , vol. 39, p. 301285, 2021. | [51] | R. Baumann, M. Protsenko, and T. M¨ | uller, “Anti-proguard: Towards |

“Detection of obfuscation techniques in Android applications,” in [54] X. Zhan, L. Fan, T. Liu, S. Chen, L. Li, H. Wang, Y. Xu, X. Luo,

| Proceedings | of | the | 13th | International | Conference | on | Availability, | and Y. Liu, “Automated third-party library detection for Android ap- |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reliability | and | Security | , | ser. | ARES | ’18. | New | York, | NY, | USA: | plications: Are we there yet?” in | Proceedings of the 35th IEEE/ACM |
| Association | for | Computing | Machinery, | 2018. | [Online]. | Available: | International Conference on Automated Software Engineering | , 2020, pp. |  |  |  |  |

[33] Z. Li, J. Sun, Q. Yan, W. Srisa-An, and Y. Tsutano, “Obfusifier: [55] J. Zhang, A. R. Beresford, and S. A. Kollmann, “Libid: reliable identi-

| Obfuscation-resistant Android malware detection system,” in | Security | fication of obfuscated third-party Android libraries,” in | Proceedings of |  |
| --- | --- | --- | --- | --- |
| and Privacy in Communication Networks: 15th EAI International Con- | the 28th ACM SIGSOFT International Symposium on Software Testing |  |  |  |
| Proceedings, Part I 15 | . | Springer, 2019, pp. 214–234. | [56] | Y. Wu, C. Sun, D. Zeng, G. Tan, S. Ma, and P. Wang, “LibScan: Towards |
| [34] | O. Mirzaei, J. M. de Fuentes, J. Tapiador, and L. Gonzalez-Manzano, | more precise Third-Party library identification for Android applications,” |  |  |
| “Androdet: An adaptive Android obfuscation detector,” | Future Genera- | in | 32nd USENIX Security Symposium (USENIX Security 23) | , 2023, pp. |

---

## Page 13

13

VIII. B IOGRAPHIES

Akila Niroshan (Student Member, IEEE) is cur-

rently pursuing a PhD at the School of Electri-

cal Engineering and Telecommunications, Univer-

sity of New South Wales. His research interests

include Android code obfuscation and AI-enhanced

solutions for mobile app security. Before moving

into research, he worked for nearly five years in

the telecommunications industry, focusing on the

Internet of Things. He received his B.Sc. (Hons)

in Electronics and Telecommunications Engineering

from the University of Moratuwa, Sri Lanka, in

2017.

Suranga Seneviratne (Senior Member, IEEE) is

a Lecturer in Security at the School of Computer

Science, The University of Sydney. He received

his PhD from the University of New South Wales,

Australia in 2015. His current research interests

include privacy and security in mobile systems, AI

applications in security, and behavior biometrics.

Before moving into research, he worked for nearly

six years in the telecommunications industry in core

network planning and operations. He received his

bachelor’s degree from the University of Moratuwa,

Sri Lanka in 2005.

Aruna Seneviratne (Senior Member, IEEE) is cur-

rently a Foundation Professor of Telecommunica-

tions with the University of New South Wales,

Australia, where he holds the Mahanakorn Chair

of Telecommunications. He has also worked at a

number of other universities in Australia, U.K.,

and France, and industrial organizations, includ-

ing Muirhead, Standard Telecommunication Labs,

Avaya Labs, and Telecom Australia (Telstra). He has

held visiting appointments with INRIA, France. His

current research interests are in physical analytics:

technologies that enable applications to interact intelligently and securely with

their environment in real-time. Most recently, his team has been working on

using these technologies in behavioral biometrics, optimizing the performance

of wearables, and IoT system verification. He has been awarded a number of

fellowships, including one at British Telecom and one at Telecom Australia

Research Labs.

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

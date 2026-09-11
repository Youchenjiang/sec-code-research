---
title: "Understanding Android Obfuscation Techniques: A Large-Scale Investigation in the Wild"
author: "Shuaike Dong1, Menghao Li2, Wenrui Diao3, Xiangyu Liu4, Jian Liu2, Zhou Li5, Fenghao Xu1, Kai Chen2, XiaoFeng Wang6, and Kehuan Zhang1"
pages: 11
---

# Understanding Android Obfuscation Techniques: A Large-Scale Investigation in the Wild

## Page 1

A Large-Scale Investigation in the Wild

arXiv:1801.01633v1  [cs.CR]  5 Jan 2018

ABSTRACT

Program code is a precious asset to its owner. Due to the easy-
to-reverse nature of Java, code protection for Android apps is of
particular importance. To this end, code obfuscation is widely uti-
lized by both legitimate app developers and malware authors, which
complicates the representation of source code or machine code in
order to hinder the manual investigation and code analysis. Despite
many previous studies focusing on the obfuscation techniques,
however, our knowledge on how obfuscation is applied by real-
world developers is still limited.

In this paper, we seek to better understand Android obfuscation
and depict a holistic view of the usage of obfuscation through a
large-scale investigation in the wild. In particular, we focus on
four popular obfuscation approaches: identifier renaming, string
encryption, Java reflection, and packing. To obtain the meaningful
statistical results, we designed efficient and lightweight detection
models for each obfuscation technique and applied them to our
massive APK datasets (collected from Google Play, multiple third-
party markets, and malware databases). We have learned several
interesting facts from the result. For example, malware authors use
string encryption more frequently, and more apps on third-party
markets than Google Play are packed. We are also interested in
the explanation of each finding. Therefore we carry out in-depth
code analysis on some Android apps after sampling. We believe
our study will help developers select the most suitable obfuscation
approach, and in the meantime help researchers improve code
analysis systems in the right direction.

KEYWORDS

Android, obfuscation, static analysis, code protection

1
INTRODUCTION

Code is a very important intellectual property to its developers, no
matter if they work as individuals or for a large corporation. To
protect this property, obfuscation is frequently used by developers,
which is also considered as a double-edged sword by the security
community. To a legitimate software company, obfuscation keeps
its competitors away from copying the code and quickly building
their own products in an unfair way. To a malware author,
obfuscation raises the bar for automated code analysis and manual
investigation, two approaches adopted by nearly every security
company. For a mobile app, especially the one targeting Android

1

Understanding Android Obfuscation Techniques:

Kai Chen2, XiaoFeng Wang6, and Kehuan Zhang1

platform, obfuscation is particularly useful, given that the task of
disassembling or decompiling Android app is substantially easier
than doing so for other sorts of binary code, like X86 executables.

Android obfuscation arguably is pervasive. On the one hand,
there are already more than 2.8 million apps available for down-
loading just in one app market, Google Play, up to March 2017 [18].
On the other hand, many off-the-shelf obfuscators are developed,
and some authors claim their tools are used by more than 300,000
apps [2]. Consequently, the issues around app obfuscation attract
many researchers. So far, most of the studies focus on the topics
like what obfuscation techniques can be used [26], how they
can be improved [48], how well they can be handled by state-
of-art code analysis tools [47], and how to deobfuscate the code
automatically [28]. While these studies provide solid ground for
understanding the obfuscation techniques and its implications, there
is a still an unfilled gap in this domain: how obfuscation is actually
used by the vast amount of developers?

We believe this topic needs to be studied, and the answer
could enlighten new research opportunities. To name a few, for
developers, learning which obfuscation techniques should be used is
quite important. Not all obfuscation techniques are equally effective,
and using some might even bring the incompatibility issue. Plenty
of code analysis approaches were proposed, but their effects are
usually hampered by obfuscation and the impact greatly differs
based on the specific obfuscation technique in use, e.g., identifier
renaming is much less of an issue comparing to string encryption.
Knowing the distribution of obfuscation techniques can better assist
the design of code analysis tools and prioritize the challenges need
to be tackled. All roads paving to the correct conclusions call for
measurement on real-world apps, and only the result coming from a
comprehensive study covering a diverse portfolio of apps (published
in different markets, in different countries, from both malware
authors and legitimate companies) is meaningful.
Our Work. As the first step, in this paper, we systematically study
the obfuscation techniques used in Android apps and carry out
a large-scale investigation for apps in the wild. We focus on four
most popular Android obfuscation techniques (identifier renaming,
string encryption, Java reflection, and packing) and measure the
base and popular implementation of each technique. To notice, the
existing tools, like deobfuscators, cannot solve our problem here,
since they either work well against a specific technique or a specific
off-the-shelf obfuscator (e.g., ProGuard). As such, they cannot be

Shuaike Dong1, Menghao Li2, Wenrui Diao3, Xiangyu Liu4, Jian Liu2, Zhou Li5, Fenghao Xu1,

1The Chinese University of Hong Kong, Email: {ds016, xf016, khzhang}@ie.cuhk.edu.hk
2Institute of Information Engineering, Chinese Academy of Sciences, Email: {limenghao, liujian6, chenkai}@iie.ac.cn
3Jinan University, Email: diaowenrui@link.cuhk.edu.hk
4Alibaba Inc., Email: eason.lxy@alibaba-inc.com
5ACM Member, Email: lzcarl@gmail.com
6Indiana University Bloomington, Email: xw7@indiana.edu


---

## Page 2

used to provide a holistic view. Our key insight to this end is that
instead of mapping the obfuscated code to its original version, a
challenge not yet fully addressed, we only need to cluster them
based on their code patterns or statistical features. Therefore, we
built a set of lightweight detectors for all studied techniques, based
on machine learning and signature matching. Our tools are quite
effective and efficient, suggested by the validation result on ground-
truth datasets. We then applied them on a real-world APK dataset
with 114,560 apps coming from three different sources, including
Google Play set, third-party markets set, and malware set, for the
large-scale study.
Discoveries. Our study reveals several interesting facts, with some
confirming people’s intuition but some contradicting to common
beliefs: for example, as an obfuscation approach, identifier renaming
is more widely-used in third-party apps than in malware. Also,
though basic obfuscation is prevalently applied in benign apps, the
utilization rate of other advanced obfuscation techniques is much
lower than that of malware. We believe these insights coming from
“big code” are valuable in guiding developers and researchers in

building, counteracting or using obfuscation techniques.
Contributions. We summarize this paper’s contributions as below:

• Systematic Study. We systematically study the current
mainstream Android obfuscation techniques used by app
developers.
• New Techniques. We propose several techniques for
detecting different obfuscation techniques accurately, such
as n-gram -based renaming detection model and backward
slicing-based reflection detection algorithm.
• Large-scale Evaluation. We carried out large-scale ex-
periments and applied our detection techniques on over
100K APK files collected from three different sources. We
listed our findings and provided explanations based on
in-depth analysis of obfuscated code.

Roadmap. The rest of this paper is organized as follows: We
systematically summarize popular Android obfuscation techniques
in Section 2. Section 3 overviews the high-level architecture of
our detection framework. The detailed detection strategies and
statistical results on large-scale datasets are provided in Section 4.
Also, we discuss some limitations and future plans in Section 5.
Section 6 reviews the previous research on Android obfuscation,
and Section 7 concludes this paper.

2
BACKGROUND

In this section, we briefly introduce the structure of APK file and
overview some common Android obfuscation techniques.

2.1
APK File Structure

An APK (Android application package) file is a zip compressed file
containing all the content of an Android app, in general, including
four directories (res, assets, lib, and META-INF) and three files
(AndroidManifest.xml, classes.dex, and resources.arsc). The
purposes of these directories and files are listed as below.

res This directory stores Android resource files which will

be mapped into the .R file in Android and allocated the
corresponding ID.

assets This directory is similar to the res directory and

used to store static files in the APK. However, unlike res
directory, developers can create subdirectories in any depth
with the arbitrary file structure.
lib The code compiled for specific platforms (usually library

files, like .so) are stored in this directory. Subdirectories
can be created according to the type of processors, like
armeabi, armeabi-v7a, x86, x86_64, mips.
META-INF This directory is responsible for saving the signa-

ture information of a specific app, which is used to validate
the integrity of an APK file.
AndroidManifest.xml This XML file is the configuration of

an APK, declaring its basic information, like name, version,
required permissions and components. Each APK has an
AndroidManifest file, and the only one.
classes.dex The dex file contains all the information of the

classes in an app. The data is organized in a way the Dalvik
virtual machine can understand and execute.
resources.arsc This file is used to record the relationship

between the resource files and related resource ID and can
be leveraged to locate specific resources.

2.2
Android Obfuscation Characterization

In general, obfuscation attempts to garble a program and makes the
source or machine code more difficult for humans to understand.
Programmers can deliberately obfuscate code to conceal its purpose
or logic, in order to prevent tampering, deter reverse engineering,
or behave as a puzzle for someone reading the code. Specifically,
there are several common obfuscation techniques used by Android
apps, including identifier renaming, string encryption, excessive
overloading, reflection, and so forth.
Identifier Renaming. In software development, for good read-
ability, code identifiers’ names are usually meaningful, though
developers may follow different naming rules (like CamelCase,
Hungarian Notation). However, these meaningful names also
accommodate reverse-engineers to understand the code logic and
locate the target functions rapidly. Therefore, to reduce the potential
information leakage, the identifier’s name could be replaced by a
meaningless string. The following code snippet gives an example,
in which all identifiers in class Account are renamed.

1 public class a{

2
private Integer a;

3
private Float = b;

4
public void a(Integer a, Float b){

5
this.a = a + Integer.valueOf(b)

6
}

7 }

String Encryption. Strings are very common-used data structures
in software development. In an obfuscated app, strings could be
encrypted to prevent information leakage. Based on cryptographic
functions, the original plaintexts are replaced by random strings and
restore at runtime. As a result, string encryption could effectively
hinder hard-coded static scanning. The following code block shows
an example.

1 String option = "@^@#\x `1 m*7 %**9_!v";
2


---

## Page 3

2 this.execute(decrypt(option));

Java Reflection. Reflection is an advanced feature of Java [21],
which provides developers with a flexible approach to interact
with the program, e.g., creating new object instances and invoking
methods dynamically. One common legitimate usage is to invoke
nonpublic APIs in the SDK (with the annotation @hide). The
following code block gives an example of reflection that invokes a
hidden API batteryinfo.

1 Object object = new Object ();

2 Method getService = Class.forName("android.os.
ServiceManager").getMethod("getService",
String.class);

3 Object obj = getService.invoke(object , new
Object []{ new String("batteryinfo")});

As an obfuscation technique, reflection is a good choice of hiding
program behaviors because it can transfer the control to a certain
function implicitly, which can not be well handled by state-of-the-
art static analysis tools. Therefore, malware developers usually
heavily employ reflection to hide malicious actions.
Packing. Packing is a widely-used code protection technique. The
packed APK file is composed of an encrypted origin APK and a
wrapper APK. When the user launches the APK, the wrapper will
run first, decrypt the original APK and load it into the memory, and
then the execution will be handed to the decrypted APK. Due to
the cryptographic procedure and runtime release, it becomes hard
to get the original code through static analysis. We regard packing
as an obfuscation skill in a broad sense because its goal is to hinder
the reverse-engineering as well.

3
SYSTEM DESIGN

Our target is to systematically study the Android obfuscation
techniques and carry out a large-scale investigation. As the first
step, we design an efficient Android code analysis framework to
identify the obfuscation techniques used by developers. Here we
overview the high-level design of this framework and introduce
the datasets prepared for the subsequent large-scale investigations.

3.1
System Overview

To detect the usage of obfuscation techniques, we propose an
architecture to analyze APK files automatically, as illustrated in
Figure 1. After the APK files collected from several channels (details
are provided in Section 3.2) are stored in our server, this detection
framework will try to unpack them for the primary testing. Some
damaged APK files failing to pass this step will be discarded.
Then this framework applies four targeted detection methods to
identify obfuscated Smali code blocks. These detection methods
could be classified into two categories: signature-based and ma-
chine learning-based. For the obfuscation techniques with specific
features, we search the corresponding signatures in Smali code to
determine the existence. For example, the reflective calls which
implicitly invoke another function can be located by searching the
sequence pattern [Class.forName()→getMethod()→invoke()].
However, it is difficult to extract fixed features for some techniques
(e.g., encrypted strings), so we utilize machine learning algorithms

Table 1: APK Dataset for Investigation

Type
Source
Number

Official Market
Google Play
26,614

Wandoujia
8,979
360
18,724
Huawei
22,048
Anzhi
7,121
Xiaomi
4,649
AppChina
4,145

3rd-party Market

Malware
VirusShare
19,004
VirusTotal
3,267

to classify automatically. The training set comes from F-Droid [12],
an open source Android app repository.

3.2
APK Dataset

We are interested in the obfuscation usage status of apps in different
types, so three representative APK datasets were used in our
experiment: Google Play set (26,614 samples), third-party market set
(65,666 samples), and malware set (22,280 samples). These samples
were collected during 2016 and 2017. In total, our experiment dataset
contains 114,560 sample with the size of around 1.521TB. More
details are given in Table 1.

As the official app store for Android, Google Play is the main
Android app distribution channel. Thus, its sample set could
reflect the deployment status of obfuscation used by mainstream
developers. Also, due to the policy restriction, in some countries
(such as China), Google Play is not available, and users have to
install apps from third-party markets. Therefore, in the second
dataset, we select six popular app markets from China (say
Anzhi [5], Xiaomi [25], Wandoujia [24], 360 [1], Huawei [13], and
AppChina [6]) and developed the corresponding crawlers to collect
their apps. Note that the replicated samples from different markets
have been excluded. Lastly, except for legitimate app samples,
we are also curious about whether malware authors heavily use
obfuscation skills to hide their malicious intentions. So, the last
dataset contains the malware samples coming from VirusShare [22]
and VirusTotal [23, 37].

4
OBFUSCATION DETECTIONS AND
LARGE-SCALE INVESTIGATION

In this section, we introduce the detection approaches for each
obfuscation technique and summarize our findings based on large-
scale experiments.

4.1
Identifier Renaming

Generally, in the software development, the names of identifiers
(variable names, function names, and so forth) are usually meaning-
ful, which could provide good code readability and maintainability.
However, such clear names may leak much information due to the
easy-to-reverse feature of Java. As a solution, identifier renaming
is proposed and widely used in practice.

The renaming operation can be appended at different stages of
APK file packaging. For example, ProGuard [19] and Allatori [3]
3


---

## Page 4

![Figure 1](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_1.jpeg)

![Figure 2](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_2.jpeg)

![Figure 3](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_3.png)

![Figure 4](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_4.jpeg)

![Figure 5](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_5.png)

![Figure 6](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_6.png)

![Figure 7](../assets/AndroidObfuscation (2018) Understanding Android Obfuscation Techniques/fig_p4_7.png)

Official Market

Third-party

Markets

APK Repository

VirusShare.com

Malware 
  Format 
   Check

work at the source-code level, mapping the original names to
mangled ones based on the user’s configuration. The other ob-
fuscators, like DashO [9], DexProtector[11], and Shield4J [20], can
work directly on APK files, modifying .class and .dex files.

Given an identifier, we can easily tell whether some obfuscator
has renamed it based on the information it contains. In other
words, if an identifier name is obscure and meaningless, it can
be regarded as obfuscated because it tries to hide the actual purpose
and intention. A typical renaming operation is changing the original
name to a single character (like "a", "b") or some kind of puzzling
string (like "IlllIlII", "oO00O0oo") [26]. However, the manual check is
obviously not qualified for our large-scale scanning goal. Moreover,
we focus on the whole APK contents rather than a single identifier.
Therefore, we need to design a robust and systematic detection
method for identifier renaming.

Beyond that, as a special case of identifier renaming, the excessive
overloading technique utilizes the overloading feature of Java and
could map irrelevant identifier names to the same one, making the
code more confusing to analysts [27]. For example, in the sample
idfhn1, more than 46 functions are named as idfhn (the same as
the package name). Though the compiler could distinguish these
variables with the same name, security analysts have to face more
troubles. In our research, we also paid attention to the application
of overloading feature and its impact on code analysis.
Identifier Renaming Detection. To the above challenges and
targets, we combine the computational linguistics and machine
learning techniques for accurate renaming detection. The high-
level idea is based on the probabilistic language model. The insight
is that identifier renaming will lead to the abnormal distribution
of characters and character combinations, which can be used to
distinguish from normal ones (non-obfuscated). Here we give our
three-step approach:

(1) Data Pre-processing. As the most frequently used three

identifiers, the names of all classes, methods, and fields of
the target APK sample are extracted as the training candi-
dates. Note that, software developers often introduce third-
party libraries into their apps instead of redevelopment.
However, those third-party libraries may also contain
obfuscated code, which can not reflect the protection

1MD5: 7d9eb791c09b9998336ef00bf6d43387

Machine Learning-based Detection

Testing  Phase

Training Phase

Identifier Renaming

String Encryption

Success

Unpack

Signature-based Detection

Signature Searching

Reflection

Fail

Packing

Statistical 
     Result

Figure 1: Android App Obfuscation Detection Framework

deployed by developers proactively. Therefore, we have
pre-removed over 12,000 common third-party libraries
using the approach of Li et al. [39].
(2) Feature Generation. The amount of identifiers varies among

different apps. To build a uniform expression, we apply the
n-gram algorithm [17] to generate a fixed-length feature
vector for each app. An n-gram is a contiguous sequence
of n items from a given sequence of text or speech. In our
implementation, we apply 3-gram2 to traverse each name
string in extracted raw name set to form a fixed-length3

feature vector. The feature vector records the frequency of
each three continuous characters and will be normalized.
(3) Classification. The training set is based on an open-source

Android app repository – F-Droid [12]. We apply different
obfuscators on these Android source code to generate
obfuscated apps as the ground truth. Lastly, we choose
Support Vector Machine (SVM) as the classification algo-
rithm.

Experiment Settings. We implemented a prototype of our de-
tection model based on Androguard [4] with more than 1,500
Python lines of code. For training, we downloaded 3,147 apps and
their corresponding source code from F-Droid. Two obfuscators,
ProGuard and DashO, were used to generate the obfuscated samples
because they have different renaming policies. Note that, due to
the diversity of apps’ project configurations, not all of them can be
processed by both ProGuard (2,107 successful samples) and DashO
(654 successful samples). Among them, we randomly chose 500
original apps and 500 obfuscated apps (250 for ProGuard and 250
for DashO) as the training set.

We then conducted three steps to validate the effectiveness of
our renaming detection model. First, we randomly selected 1,000
original apps and did manual check to make sure that they were
non-obfuscated. Our classifier completely correctly labeled these
apps as "original", which means the false positive rate is 0%. We
then tested our model on 1,000 obfuscated apps(500 obfuscated
by Proguard and 500 by DashO) and our model mis-classified 6
samples(5 from Proguard, 1 from DashO), reaching a 0.6% false

2For example, if there is a string "abcdefgh", all of the 3-gram sequences it contains
are {abc, bcd, cde, def, efg, fgh}.
3The length is restricted by the legal characters sets used for contracting a name in
Java: ["a-z", " A-Z", "0-9", "_", "$", "\"].
4


---

## Page 5

Google Play

Third-party Markets

Malware

27.0%

36.5%

43.0%
57.0%

63.5%

73.0%

Obfuscated (Renaming)
Non-obfuscated (Renaming)

Figure 2: Ratio of Identifier Renaming in Three Datasets

negative rate in total. Due to identifier renaming will lead to an
abnormal distribution of character combinations, we consider our
model can be generalized to other obfuscators even if they have
different implementing policies. To verify this, we conducted a
third experiment. We collected another testing set consisting of 200
samples obfuscated by another obfuscator Allatori. The completely
successful classification results showed our model’s good attribute
of generalization.
Large-scale Investigation and Findings. The purpose of our
study is to plot the current usage status of Android obfuscation
in the wild. Therefore, we carried out a large-scale detection on
the three typical datasets (Google Play, third-party markets, and
malware) mentioned in Section 3.2. The obfuscation detection result
by dataset is given in Figure 2. According to such statistics, we have
two immediate findings:

⇒1. Compared with the apps on Google Play, the ones from
third-party markets apply more renaming operations.
⇒2. Over one third of malware don’t apply identifier renaming.

To the first finding, we ascribe it to the discrepancy between app
market environments. The piracy issue in Chinese app markets are
quite severe [43], say nearly 20% apps are repacked or cloned [30].
Such situation urges developers to put more effort into protecting
their apps. On the other hand, Google Play provides more strict and
timely supervision, which mitigates the severity of software piracy
largely. The better application ecosystem makes many developers
believe obfuscation is just an optional protection approach.

To the second finding, the percentage of malware utilizing
identifier renaming is only 63.5%, slightly less than third-party
apps, which is opposite our traditional opinion. After manually
checking the code of malware without renaming-obfuscation, we
conclude that two aspects contribute to such phenomenon.

• Script Kiddies. Many entry-level malware authors only
could develop simple malicious apps and lack the knowl-
edge of how to disguise malicious behaviors through
obfuscation.
• False Alarmed "Malware". For some apps, their main
bodies are benign and non-obfuscated, while the imported
third-party libraries contain some kinds of sensitive and
suspicious behaviors which are recognized as malicious
by some anti-virus software. A common example is the
advertising library.

In addition, we explored the difference in renaming implementa-
tion between malware and benign apps. The result reflects:

⇒Malware authors prefer to use more complex renaming
policies.

We find that, in benign apps (the samples on Google Play and
third-party markets), most identifier names are mapped to {a, b,
aa, ab, aaa, . . . } and so on, in lexicographic order. In fact, such
renaming rules accord with the default configurations of many
obfuscators (such as ProGuard). That is to say, app developers do
not intend to change the renaming rules to more ingenious ones.
However, malware authors usually put more effort into configuring
the renaming policies. For example, some malware samples utilize
special characters (encoded in Unicode) as obfuscated names (e.g.,
È, ô), which seems very odd but still be regarded as legal by Java
compilers. Also, some dazzling weird names (like {IlllIlII, oO00O0oo,
. . . }) could be found.

Based on the result of excessive overloading detection, we find:

⇒1. The deployment rate of excessive overloading approximates
that of identifier renaming.
⇒2. Malware may use irrelevant names to hide the true
intention.

Our statistics show that most of the excessive overloading
cases appear along with identifier renaming. The reason may
derive from that many obfuscators configure the excessive over-
loading by default. For example, Proguard provides the option
"-overloadaggressively" for convenient deployment.

To the second finding, we find there are also some non-name-
obfuscated samples applying overloading to confuse analysts. In
sample tw.org.ncsist.mdm4, the name of overloaded function
attachBaseContext (A protected method in class android.app.
Application) will mislead security analysts because the logic of
this function is implemented for encryption.

4.2
String Encryption

The strings in a .dex (Dalvik executable) file may leak a lot of
private information about the program. As security protection,
those hard-coded texts can be stored in an encrypted form to
prevent reverse analysis. In this section, we take a deep insight
into the string encryption and focus on two aspects:

(1) Detect whether an app uses the string encryption.
(2) Analyze the cryptographic functions invoked by apps.

String Encryption Detection. Similar to the approach for identi-
fier renaming detection (Section 4.1), we trained a machine-learning
based model to classify encrypted strings and plain-text strings. We
reused the n-gram algorithm, SVM algorithm, and the open-source
apps from F-Droid. Here we only describe the different steps. At
first, all strings appeared in an app are extracted. Next, a vector
was generated for each app via 3-gram algorithm. Distinct from
the setting for identifier renaming detection, there is no restriction
on the content of a string. Therefore, we extended the acceptable
character set to all ASCII codes.

4MD5: 01a93f7e94531e067310c1ee0f083c07
5


---

## Page 6

Google Play

Third-party Markets

Malware

0.0%

0.1%

5.3%

94.7%

99.9%

100.0%

Obfuscated (Encryption)
Non-obfuscated (Encryption)

Figure 3: Ratio of String Encryption in Three Datasets

In the implementation, we reused most code of identifier
renaming detection model. Since string encryption is not a common
function provided by off-the-shelf obfuscators, we chose DashO
and DexProtector to generate the ground truth and finally obtained
737 string-encrypted samples for training. To avoid the overfitting
caused by unbalanced data, we randomly selected 500 original apps
and 500 string-encrypted apps to train our model. To verify the
effectiveness, we randomly selected another 100 original apps and
100 string-encrypted apps for testing. The result shows our model
could achieve 98.5% success rate with FP 1% and FN 2%.
Cryptographic Function Analysis. Previous work has proposed
various approaches to identify cryptographic functions in a pro-
gram, like [29, 34, 41]. Those methods were specifically designed for
the identification of the standard, modern cryptographic algorithms
in binary code, like AES, DES, and RC4. The features used by the
previous commonly include entropy analysis, searchable constant
patterns, excessive use of bitwise arithmetic operations, memory
fetch patterns and so on, besides, the dynamic binary instrument
is also widely-used by analysts to better locate and identify the
cryptographic primitives. However, previous approaches do not
fit android platform very well due to three reasons: (1) Smali
instructions have different representations from the x86 assembly
language, especially for memory access. (2) Java provides the
complete implementations of standard cryptographic algorithms
through Java Cryptography Extension [15]. Therefore, in most
cases, developers do not need to implement cryptographic related
functions again. (3) Java provides a series of string & character
operations, like concat(), substring(), getChars(), strim()
and so on, which can be used to build an encrypted string.

To better handle the identification in Android apps, we extended
the previous approaches with more empirical features, shown as
below.

• The ratio of bit and loop operations.
• The usage of Java Cryptography Extension API invoking.
• The amount of operations on string & character variables.
• The frequency of encrypted strings as function parameters
(for decryption function).

Large-scale Investigation and Findings. We applied our string
encryption detection model on the testing datasets. The results are
presented in Figure 3. The direct findings are that:

⇒1. Nearly all benign apps don’t use string encryption.
⇒2. String encryption is more popular in malware.

This statistical result complies with our perception, and we could
understand it from two perspectives. (1) String encryption is not a
common feature provided by off-the-shelf obfuscators. For example,
ProGuard [19], as the default obfuscator integrated into Android
Studio, does not provide such option. The obfuscators offering
the string encryption feature are either expensive (DexGuard [10],
DexProtector [11]) or difficult to configure (Allatori [3]). (2) Many
developers may lack the knowledge or awareness of deploying more
advanced obfuscation techniques. They may believe the default
identifier renaming is enough for code protection and it is not
necessary to consider other techniques. (3) String encryption can
help malware evade the signature scanning of some anti-virus
software and hidden the intention effectively, leading to a higher
rate of utilization than benign apps.

In addition, we also conducted an experiment targeting at the
implementations of cryptographic functions for obfuscation. In this
analysis, we focused on the malware set because the other two
benign datasets can not provide enough string-encrypted samples.
Finally, we obtained 1,190 cryptographic functions. Base on the
further reviews, we get the following findings.

⇒The cryptographic functions usually disguise its true inten-
tion by changing to an irrelevant name.

For instance, in sample com.solodroid.materialwallpaper5,
the decryption function is disguised to a common legitimate
API NavigationItem;->getDrawable() which should be used for
retrieving a drawable object.

⇒About 17.6% of string-encrypted malware implement multiple
cryptographic functions and take turns to use them in a single
app.

In sample com.yandex.metrica6, four different cryptographic
functions were implemented. All of them share similar code
structures – first initializing the key, then doing the encryption/de-
cryption. However, the key initialization procedures are quite
different from each other. As a result, the workload of restoring
rises significantly for analysts.

1 // In class com.yandex.metrica.impl.ad;

2 static final String a(String str){

3 if (c == null){

4
a13840 (); // key initialization function

5 }

6
Continue ...

7 }

⇒The secret keys used in cryptographic functions can be
statically defined or dynamically generated.

In the static case, the key is either hard-coded or directly
imported as the parameter, which can be easily located and obtained.
On the other hand, the dynamic key is usually generated at runtime

5MD5: fab2711b0b55eb980f44bfebc2c17f1f
6MD5: 95f7d37a60ef6d83ae7443a3893bb246
6


---

## Page 7

and even could be fluctuating in different runtime context, which
is nearly impossible to be handled by static analysis. The following
code snippet shows an example of dynamic key generation, in
which elements[3] is not a fixed value because of the uncertain
stack trace at runtime.

1 StackTraceElement [] elements = Thread.
currentThread ().getStackTrace ();

2 int hashCode = elements [3]. getClassName ()+
elements [3]. getMethodName ().hashCode ();

4.3
Reflection

Reflection allows programs to create, modify and access an object
at runtime, which brings many flexibilities. However, such dynamic
feature also impedes static analysis due to those reflective invoca-
tions, especially those invoking other functions. Such uncertain
behaviors could result in that the static analysis cannot capture the
real intention.

In this section, we explore two questions on reflection:

(1) How widespread the reflection is used in the wild?
(2) Among these use cases, how many of them are used for

the obfuscation purpose?
Reflection provides diverse APIs targeting at different objects
like Class, Method and Field. In practice, particular APIs are often
executed in sequence to achieve specific functionalities. In our
study, we focus on the sequence pattern [Class.forName() →
getMethod() →invoke()] which is the most frequent pattern for
reflective calls mentioned by Li et al. [38]. Also, in this sequence, the
execution of program is implicitly transfered to another function
(the parameter of getMethod()), which has an obvious influence
on program status, especially the control flow.
Reflection Detection. The first target is fast reflection detection,
which could be achieved through signature searching, say the se-
quence pattern [Class.forName() →getMethod() →invoke()].

Another target is to discover the invoked function in reflection,
that is the input parameter of reflective calls. In theory, dynamic
analysis is the best way to find the input parameter. However, its low
path coverage and efficiency issues are not suitable for large-scale
scanning. To balance the efficiency and coverage, we developed a
light-weight tool to trace the input parameters of Class.forName()
and getMethod(). The high-level idea is to find the real content of
the parameters through backward slicing.

More details, first our tool scans the function body and locates
two reflection calls – Class.forName() and getMethod(). The
parameter registers will be set as slicing criterion. Then it traces
back from the locations, analyzing each instruction to find the
corresponding slices. After that, this tool parses and simulates each
instruction in slices, and calculates the final value of the slicing
criterion. Note that, to reduce the maintenance complexity, we do
not carry out recursive function invoking resolution.

Here, we use a real-world example (see the below code block)
to illustrate such work flow. In this case, our tool will mark
the positions of blue-highlighted reflective calls and trace the
data flow of red-highlighted registers. The final output would be
{"android.os.SystemProperties", "get"}.

1 const/4 v1, 0

Google Play

Third-party Markets

Malware

48.3%
51.7%

51.0%
49.0%

49.7%
50.3%

Reflection
No Reflection

Figure 4: Ratio of Reflection in Three Datasets

Table 2: Ratio of Recovered Targets in Reflection

Dataset
Google Play
3rd-p Markets
Malware

Recovery
65.7%
50.2%
27.1%

2 const-string v0,'android.os.SystemProperties '

3 invoke-static v0,Ljava/lang/Class;->forName(Ljava/
lang/String ;) Ljava/lang/Class;

4 const-string v2, 'get'

5 . . .

6 invoke-virtual v0, v2, v3, Ljava/lang/Class;->
getMethod(Ljava/lang/String; [Ljava/lang/
Class ;) Ljava/lang/reflect/Method;

Large-scale Investigation and Findings. The implementation of
our detection models (reflection usage and invoked functions in
reflection) is still based on Androguard with around 1600 Python
lines of code. After experiments on our APK dataset, the reflection
statistics are shown in Figure 4. We could find:

⇒The proportions of reflection deployment in benign apps and
malware are similar.

We are also interested in the purposes of applying reflec-
tion in apps. Since our detection model does not work at the
dynamic level, part of the invoked targets cannot be precisely
acquired. To some complex invoking cases, our model will try
to record relevant information as much as possible. For example,
if the real target is delivered as the return value of another
function, our tool will record the information of this function.
The percentage of recovered targets is shown in Table 2, which
indicates malware hold the least recovery rate among the three
datasets. Furthermore, we checked the results of our backward
slicing prototype and found that most of the strings delivered
to reflection calls in malware are the return values of certain
cryptographic functions, like Ltp5x/WGt12/StringDecoder; →
decode(Ljava/lang/String;)Ljava/lang/String;.

To the successfully recovered functions, we further explore
why these reflection implementations are necessary. According
to different APK dataset, the most frequently invoked functions
are listed in Table 3, Table 4, and Table 5 respectively. These lists
reflect:
7


---

## Page 8

Table 3: Functions Invoked via Reflection (Google Play)

Frequency Recovered Function

2,275
android.support.v4.content.
LocalBroadcastManager.getInstance
1,297
android.webkit.WebView.onPause
1,250
android.os.SystemProperties.get
821
org.apache.harmony.xnet.provider.jsse
.NativeCrypto.RAND_seed
523
com.google.android.gms.common.GooglePlay-
ServicesUtil.isGooglePlayServicesAvailable

Table 4: Functions Invoked via Reflection (3rd-p Market)

Frequency Recovered Function

3,859
android.os.SystemProperties.get
1,800
android.support.v4.content.
LocalBroadcastManager.getInstance
1,158
org.apache.harmony.xnet.provider.jsse
.NativeCrypto.RAND_seed
721
android.os.ServiceManager.getService
613
android.os.Build.hasSmartBar

Table 5: Functions Invoked via Reflection (Malware)

Frequency Recovered Function

2,977
java.lang.String.valueOf
2,142
android.telephony.gsm.SmsManager.getDefault
687
android.os.SystemProperties.get
518
java.lang.String.charAt
352
java.lang.String.equals

⇒Most of the reflection cases are used to invoke hidden
functions or to support backward compatibility.

In Android system, the functions related to the Android frame-
work and OS itself are usually annotated with the label "@hide",
which can only be called through reflection. In above three tables,
all functions starting with android.os.* and android.webkit.*
are hidden-annotated.

We also manually checked the use case of android.v4.content.
LocalBroadcastManager.getInstance. We found that the corre-
sponding reflective calls are usually enclosed in a try-catch block,
aiming to check the existence of particular class and handle the
not-found exception. Such pattern is a programming standard
recommended by Android official documents [7].

To malware samples, we find:

⇒Compared with benign apps, malware prefers to use more
complex reflection invoking patterns to hide its intentions.

As one example, the following code block is extracted from
an obfuscated malware7. After analysis, the function invoked by
reflection could be restored as:

1 if (!ò.trim().toLowerCase ().contains(ˆ0("G))OCH"
))) {Function Body}

As comparison, the original code is shown below. In this case,
all string operations can be written in non-reflection forms. We
could find such reflection usage makes the code structure more
complicated and confusing, which enhances the effect of code
obfuscation.

1 if (!(( Boolean) Class.forName("java.lang.String
").getMethod("contains", new Class ({
CharSequence.class }).invoke(Class.forName("
java.lang.String").getMethod("toLowerCase",

null).invoke(Class.forName("java.lang.
String").getMethod("trim", null).invoke(ò,
null), null), new Object []{ˆ0("G))OCH")})).
booleanValue ()) { Function Body }

4.4
Packing

Different from previous three obfuscation techniques, packing is a
kind of whole-APK-reinforcing protection, which does not aim at
preventing others from understanding the code, but preventing the
code from being obtained. Currently, many packing services are
provided as online services and free for individual users, such as
Qihoo [2], ijiami [14], and Bangcle [8].
Packing Detection. Our study shows the apps using packing
usually have the following heuristic features:

(1) Derived Application Class. android.app.Application is

the base class maintaining the global app state. When
launching an app, this class (or its subclass) will be
instantiated first. The operation of packing apps usually
needs a derived Application class acting as the wrapper,
preparing for the subsequent APK loading.
(2) Encrypted Data File. The real APK is usually encrypted and

stored in the lib or assets folder.
(3) Thin Wrapper Class. In general, the wrapper class only

performs the bootstrap function, and the core work is
performed by native functions based on Java Native
Interface (JNI) [16].
Also, the packing tools always introduce new files (such as
ijiami.data and baiduproduct.jar) or code into the original
APK file. These modifications usually differ from one packing
service to another and can be the fingerprints of service providers.
Those certain modifications could be treated as a detection feature
as well. To further study, we tested six popular packing services
and analyzed the corresponding packed APK files. The extracted
signatures are listed in Table 6. Noted that, such signatures may be
changed with the update of packing service.
Large-scale Investigation and Findings. We applied our pack-
ing detection prototype (300 Python lines of code) to the three APK
datasets. The statistical results are shown in Figure 5. The direct
finding is:

7MD5: 7ff1b8afd22c1ed77ed70bfc04635315
8


---

## Page 9

Table 6: Signatures of Packing Services

Packer
File Signature(s)
Code Signature(s)

Bangcle
assets/bangcle_classes.jar | lib/armeabi/libsecexe.so |
lib/armeabi/libsecmain.so

Google Play

Third-party Markets

Malware

0.0%

2.1%

10.4%

89.6%

97.9%

100.0%

Obfuscated (Packing)
Non-obfuscated (Packing)

Figure 5: Ratio of Packing in Three Datasets

⇒Third-party apps and malware held a higher deployment rate
of packing services.

As an one-stop approach of code protection, the popularity of
online packing service is reasonable. Currently, the research on
packing and unpacking has become a hot topic, and researchers
have proposed several tools targeting at unpacking apps automati-
cally, like Zhang et al. [54] and Yang et al. [52]. Most of these tools
rely on dumping the code from memory through customized Dalvik
virtual machine (DVM) or Android Runtime (ART). As arm races,
packing providers enhance their services time to time to prevent
cracking.

According to our observation, packing is a practical approach to
code protection for ordinary developers. Its basic functionality has
been able to impede entry-level reverse-engineers from peeping
into the original code. However, the protection may be not strong
enough to prevent an adept analyst from obtaining the code.

5
DISCUSSION

In this section, we discuss some limitations of our study and
then describe the future plan. Though we have conducted a
large-scale investigation of mainstream obfuscation techniques
used in Android apps, we should point out there are still some
existing techniques not involved in our research, say control flow
obfuscation and native code obfuscation.

com.tencent.StubShell

com.baidu.protect.StubApplication

Through our observation, we find that control flow obfuscation
is non-universal and only provided by a minority of obfuscators,
like DashO and Allatori. However, based on our analysis, these
tools do not provide a strong control flow obfuscation method as
they claimed. For example, given an app, only very few methods’
control flows are obfuscated, and the others remain unchanged.
Therefore, at this stage, we cannot capture enough control-flow
obfuscated samples for investigation.

Another uncovered topic is native code obfuscation which could
bring more protection to an app’s binary code. However, native
code programming requires more advanced skills for developers,
which makes it still not a mainstream technique in Android app
development. Also, the implementation of native code obfuscation
is quite different from other Java-level techniques, which could be
treated as an independent research topic. Therefore, we leave it as
our future study.

6
RELATED WORK

Obfuscation is always a hot research topic in Android ecosystem,
and there are several studies performed on how to obfuscate
Android apps effectively and how to measure the obfuscation
effectiveness.

6.1
Obfuscation Measurement and Assessment

Obfuscation techniques have been widely used in the Android app
development. Naturally, in academia, researchers are interested
in whether these techniques do work. An early attempt is [33]
which empirically evaluates a set of 7 obfuscation methods on
240 APKs. Also, Park et al. [44] empirically analyzed the effects
of code obfuscation on Android app similarity analysis. Recently,
Faruki et al. [32] conducted a survey to review the mainstream
Android code obfuscation and protection techniques. However,
they concentrated on the technical analysis to evaluate different
techniques, not like our work based on a large-scale dataset.
They show that many obfuscation methods are idempotent or
monotonous. Wang et al. [51] defined the obfuscator identification
problem for Android and proposed a solution based on machine
learning techniques. The experiments indicated that their approach
could achieve about 97% accuracy to identify ProGuard, Allatori,
DashO, Legu, and Bangcle. On the aspect of deobfuscation research,
Bichsel et al. [28] proposed a structured prediction approach for
9

Ali
lib/armeabi/libmobisec.so | aliprotect.dat
com.ali.fixHelper |
com.ali.mobisecenhance.StubApplication
Tencent
lib/armeabi/libmain.so | lib/armeabi/libshell.so |
lib/armeabi/mix.dex

Qihoo
assets/libjiagu.so
com.qihoo.util.StubApplication
iJiami
assets/ijiami.dat | */armeabi/libexec.so |
*/armeabi/libexecmain.so
com.shell.SuperApplication

com.secshell.shellwrapper.SecAppWrapper |
com.bangcle.protect.ApplicationWrapper
Baidu
assets/baiduprotect.jar |
lib/armeabi/libbaiduprotect.so


---

## Page 10

performing probabilistic layout deobfuscation of Android APKs
and implemented a scalable probabilistic system called DeGuard.

Different from above research, our work is based on a large
Android app datasets which cover official Google play store, third-
party Android markets, and update-to-date malware families. We
attempt to understand the distribution of Android obfuscation
techniques and provide the up-to-date knowledge about app
protection.

6.2
Security Impact of Android Obfuscation

As discussed earlier, the obfuscation will create barriers for Android
program analysis. Works on clone / repackage detection [35, 42, 50,
53, 55] find that obfuscations can impair detection results.
Studies of malware detection also showed that obfuscation
is an obstacle to malware analysis. Rastogi et al. [47] evaluated
several commercial mobile anti-malware products for Android and
tested how resistant they are against various common obfuscation
techniques. Their experiment result showed anti-malware tools
make little effort to provide transformation-resilient detection (in
the year 2013). After that, Maiorca et al. [40] conducted a large-scale
experiment in which the detection performance of anti-malware
solutions are tested against malware samples under different
obfuscation strategies. Their results showed the improvement
of anti-malware engines in recent years. Recently, Hoffmann et
al. [36] developed a framework for automated obfuscation, which
implemented fine-grained obfuscation strategies and could be used
as test benches for evaluating analysis tools. Similar works are also
completed by Preda et al. [46], Pomilia [45], and Faruki et al. [31].
To handle obfuscated samples, Suarez-Tangil et al. [49] propose
DroidSieve, an Android malware classifier based on static analysis
and deep inspection that is resilient to obfuscation.

For malware detection, researchers mainly discussed arms
race between obfuscation and malware detection. Although some
malware detection tools claim to still work well in the presence
of obfuscation, none could eliminate the obfuscation effects in
their experimental evaluation. Our study focuses on the empirical
study of security impacts of obfuscation in the wild from different
views, which are complementary to existing works. That is, we
statistically evaluate the distribution of obfuscation methods from
views of different markets, hardening capability of obfuscations and
temporal evolution, with a light-weight and scalable obfuscation
detection framework. We believe some of our findings would be
useful for developers and researchers to better understand the usage
of obfuscation, for example, keeping pace with the development of
obfuscation technique.

7
CONCLUSION

In this paper, we concentrate on exploring the current deployment
status of Android code obfuscation in the wild. For this target, we
developed specific detection tools for four common obfuscation
techniques and performed a large-scale scanning on three represen-
tative APK datasets. The results show that, to different techniques
and app categories, the status of code obfuscation differs in many
aspects. For example, the basic renaming obfuscation has become
widely-used among Chinese third-party market developers, while
still not pervasive in Google Play market. Besides, malware authors

10

put great efforts on more advanced code protection skills. Also, we
provide the corresponding illustrations to enlighten developers to
select the most suitable code protection methodologies and help
researchers improve code analysis systems in the right direction.

REFERENCES

[1] Accessed: September 2017. 360 Smartphone Assistant. http://zhushou.360.cn/.

(Accessed: September 2017).
[2] Accessed: September 2017. 360jiagu. http://jiagu.360.cn/. (Accessed: September

2017).
[3] Accessed: September 2017.
Allatori.
http://www.allatori.com/. (Accessed:
September 2017).
[4] Accessed: September 2017.
androguard.
https://github.com/androguard/
androguard. (Accessed: September 2017).
[5] Accessed: September 2017. Anzhi. http://www.anzhi.com/. (Accessed: September

2017).
[6] Accessed: September 2017. AppChina. http://www.appchina.com/. (Accessed:

September 2017).
[7] Accessed:
September
2017.
Backward
compatibility
for
Android
applications.
https://android-developers.googleblog.com/2009/04/
backward-compatibility-for-android.html. (Accessed: September 2017).
[8] Accessed: September 2017.
bangcle.
http://www.bangcle.com/. (Accessed:
September 2017).
[9] Accessed: September 2017. DashO. https://www.preemptive.com/products/

dasho/overview. (Accessed: September 2017).
[10] Accessed: September 2017.
DexGuard.
https://www.guardsquare.com/en/
dexguard. (Accessed: September 2017).
[11] Accessed: September 2017. DexProtector. https://dexprotector.com/. (Accessed:

September 2017).
[12] Accessed: September 2017. F-Droid. https://f-droid.org/. (Accessed: September

2017).
[13] Accessed: September 2017. Huawei Appstore. http://appstore.huawei.com/.

(Accessed: September 2017).
[14] Accessed: September 2017. ijiami. http://www.ijiami.cn/. (Accessed: September

2017).
[15] Accessed: September 2017. Java Cryptography Extension. http://www.oracle.

com/technetwork/java/javase/downloads/jce8-download-2133166.html. (Ac-
cessed: September 2017).
[16] Accessed: September 2017. Java Native Interface. http://docs.oracle.com/javase/

7/docs/technotes/guides/jni/. (Accessed: September 2017).
[17] Accessed: September 2017.
n-gram.
https://en.wikipedia.org/wiki/N-gram.
(Accessed: September 2017).
[18] Accessed: September 2017. Number of available applications in the Google Play

Store from December 2009 to March 2017. http://www.statista.com/statistics/
266210/number-of-available-applications-in-the-google-play-store/. (Accessed:
September 2017).
[19] Accessed: September 2017.
ProGuard.
https://www.guardsquare.com/en/
proguard. (Accessed: September 2017).
[20] Accessed: September 2017. Shield4J. http://shield4j.com/. (Accessed: September

2017).
[21] Accessed: September 2017. Trail: The Reflection API. http://docs.oracle.com/

javase/tutorial/reflect/index.html. (Accessed: September 2017).
[22] Accessed: September 2017. VirusShare. https://virusshare.com/. (Accessed:

September 2017).
[23] Accessed: September 2017. VirusTotal. https://www.virustotal.com/. (Accessed:

September 2017).
[24] Accessed: September 2017. Wandoujia. https://www.wandoujia.com/. (Accessed:

September 2017).
[25] Accessed: September 2017.
Xiaomi Application Store.
http://app.mi.com/.
(Accessed: September 2017).
[26] Axelle Apvrille and Ruchna Nigam. 2014. Obfuscation in Android malware, and

how to fight back. Virus Bulletin (2014), 1–10.
[27] Vivek Balachandran, Sufatrio, Darell J. J. Tan, and Vrizlynn L. L. Thing. 2016.

Control flow obfuscation for Android applications. Computers & Security 61
(2016), 72–93.
[28] Benjamin Bichsel, Veselin Raychev, Petar Tsankov, and Martin T. Vechev. 2016.

Statistical Deobfuscation of Android Applications. In Proceedings of the 2016 ACM
SIGSAC Conference on Computer and Communications Security (CCS), Vienna,
Austria, October 24-28, 2016.
[29] Joan Calvet, José M. Fernandez, and Jean-Yves Marion. 2012. Aligot: Crypto-

graphic Function Identification in Obfuscated Binary Programs. In Proceedings
of the 19th ACM Conference on Computer and Communications Security (CCS),
Raleigh, NC, USA, October 16-18, 2012. 169–182.
[30] Kai Chen, Peng Liu, and Yingjun Zhang. 2014. Achieving accuracy and scalability

simultaneously in detecting application clones on Android markets. In Proceeding


---

## Page 11

of the 36th International Conference on Software Engineering (ICSE), Hyderabad,
India, May 31 - June 07, 2014.
[31] Parvez Faruki, Ammar Bharmal, Vijay Laxmi, Manoj Singh Gaur, Mauro Conti,

and Muttukrishnan Rajarajan. 2014.
Evaluation of Android Anti-malware
Techniques against Dalvik Bytecode Obfuscation. In Proceedings of the 13th
IEEE International Conference on Trust, Security and Privacy in Computing and
Communications (TrustCom), Beijing, China, September 24-26, 2014.
[32] Parvez Faruki, Hossein Fereidooni, Vijay Laxmi, Mauro Conti, and Manoj Singh

Gaur. 2016. Android Code Protection via Obfuscation Techniques: Past, Present
and Future Directions. CoRR abs/1611.10231 (2016).
[33] Felix C. Freiling, Mykola Protsenko, and Yan Zhuang. 2014.
An Empirical
Evaluation of Software Obfuscation Techniques Applied to Android APKs. In
International Conference on Security and Privacy in Communication Networks -
10th International ICST Conference, SecureComm 2014, Beijing, China, September
24-26, 2014, Revised Selected Papers, Part II.
[34] Felix Gröbert, Carsten Willems, and Thorsten Holz. 2011. Automated Identifi-

cation of Cryptographic Primitives in Binary Programs. In Recent Advances in
Intrusion Detection - 14th International Symposium, RAID 2011, Menlo Park, CA,
USA, September 20-21, 2011. Proceedings.
[35] Quanlong Guan, Heqing Huang, Weiqi Luo, and Sencun Zhu. 2016. Semantics-

Based Repackaging Detection for Mobile Apps. In Proceedings of the 8th
International Symposium Engineering Secure Software and Systems (ESSoS), London,
UK, April 6-8, 2016.
[36] Johannes Hoffmann, Teemu Rytilahti, Davide Maiorca, Marcel Winandy, Giorgio

Giacinto, and Thorsten Holz. 2016. Evaluating Analysis Tools for Android Apps:
Status Quo and Robustness Against Obfuscation. In Proceedings of the Sixth ACM
on Conference on Data and Application Security and Privacy (CODASPY), New
Orleans, LA, USA, March 9-11, 2016.
[37] Heqing Huang, Cong Zheng, Junyuan Zeng, Wu Zhou, Sencun Zhu, Peng Liu,

Suresh Chari, and Ce Zhang. 2016. Android Malware Development on Public
Malware Scanning Platforms: A Large-scale Date-driven Study. In Proceeding of
the 2016 IEEE International Conference on Big Data (BigData), Washington DC,
USA, December 5-8, 2016.
[38] Li Li, Tegawendé F. Bissyandé, Damien Octeau, and Jacques Klein. 2016. DroidRA:

Taming Reflection to Support Whole-Program Analysis of Android Apps. In
Proceedings of the 25th International Symposium on Software Testing and Analysis
(ISSTA), Saarbrücken, Germany, July 18-20, 2016.
[39] Menghao Li, Wei Wang, Pei Wang, Shuai Wang, Dinghao Wu, Jian Liu, Rui Xue,

and Wei Huo. 2017. LibD: Scalable and Precise Third-party Library Detection in
Android Markets. In Proceedings of the 39th International Conference on Software
Engineering (ICSE), Buenos Aires, Argentina, May 20-28, 2017.
[40] Davide Maiorca, Davide Ariu, Igino Corona, Marco Aresu, and Giorgio Giacinto.

2015. Stealth Attacks: An Extended Insight into the Obfuscation Effects on
Android Malware. Computers & Security 51 (2015), 16–31.
[41] Felix Matenaar, André Wichmann, Felix Leder, and Elmar Gerhards-Padilla. 2012.

CIS: The Crypto Intelligence System for automatic detection and localization of
cryptographic functions in current malware. In Proceeding of the 7th International
Conference on Malicious and Unwanted Software (MALWARE), Fajardo, PR, USA,
October 16-18, 2012.
[42] Jiang Ming, Fangfang Zhang, Dinghao Wu, Peng Liu, and Sencun Zhu. 2016.

Deviation-Based Obfuscation-Resilient Program Equivalence Checking With
Application to Software Plagiarism Detection. IEEE Trans. Reliability 65, 4 (2016),

11

1647–1664.
[43] Maggie Nazarenus. Jul 2015. Chinese app piracy: Why it exists and what you

can do about it. http://www.techinasia.com/talk/chinese-app-piracy-exists. (Jul
2015).
[44] Jonghwa Park, Hyojung Kim, Younsik Jeong, Seong-je Cho, Sangchul Han, and

Minkyu Park. 2015. Effects of Code Obfuscation on Android App Similarity
Analysis.
Journal of Wireless Mobile Networks, Ubiquitous Computing, and
Dependable Applications 6, 4 (2015), 86–98.
[45] Matteo Pomilia. 2016. A Study on Obfuscation Techniques for Android Malware.

Master’s thesis. Sapienza University of Rome.
[46] Mila Dalla Preda and Federico Maggi. 2017. Testing android malware detectors

against code obfuscation: a systematization of knowledge and unified methodol-
ogy. J. Computer Virology and Hacking Techniques 13, 3 (2017), 209–232.
[47] Vaibhav Rastogi, Yan Chen, and Xuxian Jiang. 2013. DroidChameleon: Evaluating

Android Anti-malware against Transformation Attacks. In Proceedings of the
8th ACM Symposium on Information, Computer and Communications Security
(ASIACCS), Hangzhou, China, May 8-10, 2013.
[48] Junliang Shu, Juanru Li, Yuanyuan Zhang, and Dawu Gu. 2014.
Android
App Protection via Interpretation Obfuscation. In Proceeding of the 12th IEEE
International Conference on Dependable, Autonomic and Secure Computing (DASC),
Dalian, China, August 24-27, 2014.
[49] Guillermo Suarez-Tangil, Santanu Kumar Dash, Mansour Ahmadi, Johannes

Kinder, Giorgio Giacinto, and Lorenzo Cavallaro. 2017. DroidSieve: Fast and
Accurate Classification of Obfuscated Android Malware. In Proceedings of the
Seventh ACM on Conference on Data and Application Security and Privacy
(CODASPY), Scottsdale, AZ, USA, March 22-24, 2017.
[50] Haoyu Wang, Yao Guo, Ziang Ma, and Xiangqun Chen. 2015. WuKong: A

Scalable and Accurate Two-Phase Approach to Android App Clone Detection. In
Proceedings of the 2015 International Symposium on Software Testing and Analysis
(ISSTA), Baltimore, MD, USA, July 12-17, 2015.
[51] Yan Wang and Atanas Rountev. 2017. Who Changed You? Obfuscator Identifica-

tion for Android. In Proceedings of the 4th IEEE/ACM International Conference on
Mobile Software Engineering and Systems (MOBILESoft), Buenos Aires, Argentina,
May 22-23, 2017.
[52] Wenbo Yang, Yuanyuan Zhang, Juanru Li, Junliang Shu, Bodong Li, Wenjun Hu,

and Dawu Gu. 2015. AppSpear: Bytecode Decrypting and DEX Reassembling
for Packed Android Malware. In Research in Attacks, Intrusions, and Defenses
- 18th International Symposium, RAID 2015, Kyoto, Japan, November 2-4, 2015,

Proceedings.
[53] Fangfang Zhang, Heqing Huang, Sencun Zhu, Dinghao Wu, and Peng Liu.

2014. ViewDroid: towards obfuscation-resilient mobile application repackaging
detection. In Proceedings of 7th ACM Conference on Security & Privacy in Wireless
and Mobile Networks (WiSec), Oxford, United Kingdom, July 23-25, 2014.
[54] Yueqian Zhang, Xiapu Luo, and Haoyang Yin. 2015.
DexHunter: Toward
Extracting Hidden Code from Packed Android Applications. In Computer Security
- ESORICS 2015 - 20th European Symposium on Research in Computer Security,

Vienna, Austria, September 21-25, 2015, Proceedings, Part II. 293–311.
[55] Wu Zhou, Yajin Zhou, Xuxian Jiang, and Peng Ning. 2012. Detecting repackaged

smartphone applications in third-party android marketplaces. In Proceedings of
the 2nd ACM Conference on Data and Application Security and Privacy (CODASPY),
San Antonio, TX, USA, February 7-9, 2012.


---

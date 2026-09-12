---
title: "Security Analysis on Android Application Through Penetration Testing using Reverse Engineering"
pages: 7
---

# Security Analysis on Android Application Through Penetration Testing using Reverse Engineering

## Page 1

Security Analysis on Android Application 
Through Penetration Testing using Reverse

Shweta Katoch 
ME Scholar, Department of C.S.E 
Chandigarh University, Gharuan (Punjab), India

shwetakatoch21@gmail.com

Abstract— Every person is using smartphones these 
days, and most of the users are Android users, with 
this Android applications are running on a huge scale. 
In the final quarter of 2022, Android is considered as 
the market leader among other mobile operating 
systems, holding a market share of over 71.8 percent, 
which leads to the mass development of Android 
applications and also leads to a problem where some 
applications are developed by young developers 
without considering the security factor and are easily 
downloadable from Google Play Store and open 
source. Since Android is open source and allows 
developers to create applications without restriction, 
some inexperienced developers create numerous apps 
without being aware of the most recent Android 
security challenges. As a result, these apps have an 
open attack surface that hackers can use to steal user 
data. Installing such apps can put other secure apps 
and system in danger, and once a bad app is installed, 
it will have an impact on the entire system. The goal 
of this research is to identify vulnerabilities in 
Android applications and the techniques used to find 
and inspect vulnerabilities. Penetration testing 
identifies security flaws and aids in network security. 
This paper will help future authors to understand 
several elements of penetration testing, including 
tools, attack methodologies and defence strategies.  
More particularly, this study has performed reverse 
engineering by performing penetration tests using a 
private network, devices and tools. The results are 
then summarised and discussed. This study also 
described 
about 
the 
specific 
procedures 
and 
techniques used to carry out these attacks. 
 
Keywords - Penetration testing; Reverse Engineering; 
Ethical hacking; Threat modelling; Android 
application security; Obfuscation.

2023 3rd International Conference on Smart Data Intelligence (ICSMDI) | 978-1-6654-6487-1/23/$31.00 ©2023 IEEE | DOI: 10.1109/ICSMDI57622.2023.00048

I. 
Introduction 
The bulk of users are totally reliant on our mobile 
phones in our daily lives, making them a need in 
our existence. Android OS currently powers the 
vast majority of smartphones. The primary causes 
of this are the enormous number of applications 
produced for the Android Operating system and the 
constantly 
expanding 
developer 
community. 
Security is the key issue because of the risks

216

978-1-6654-6487-1/23/$31.00 ©2023 IEEE
DOI 10.1109/ICSMDI57622.2023.00048

Engineering

Vaneet Garg 
ME Scholar, Department of C.S.E 
Chandigarh University, Gharuan (Punjab), India

aggarwal.vkg@gmail.com

associated 
with 
this 
widespread 
use 
[1]. 
Applications for mobile devices are being used 
more often, and as a result, risks and vulnerabilities 
are growing. Mobile applications can be built or 
created using a variety of coding languages and 
frameworks; however, it can be challenging to find 
flaws 
in 
the 
developed 
code 
and 
mobile 
application. There are numerous vulnerability 
detection scanners and testing tools, but their 
findings often contain false positives. Not only 
automated screening but also manual testing should 
be done in order to produce a susceptible, secure 
code. "With more than 50% of the market share for 
smartphones, Android is one of the most widely 
used smartphone operating systems in use today." It 
has a sizable customer base and excellent developer 
support, which has led to the presence of more than 
a million programmes in the authorised Play Store. 
[1]. "In a relatively short period of time, Android 
has become the world’s most popular mobile 
platform." Despite being made for smartphones 
first, 
it now drives tablets, TVs, wearable 
technology, and may eventually be even used in 
cars. An approximately two major releases are 
made for Android each year, that is being created at 
an incredible rate.

Each new iteration of Android brings with it a 
better user interface (UI), improved performance, 
and a slew of new features that are often blogged 
about and discussed in minute detail by Android 
fans. [2]. "With the rapid advancement of 
technology and the emergence of contemporary 
technologies for digital commerce, there has been a 
strong spread of mobile applications, as a plethora 
of well-known systems had also appeared, that 
have evolved into a large number of apps on the 
Internet, including such Android applications and 
iPhone applications, and have increasingly become 
necessary in a variety of fields, such as the 
education and health fields." Mobile applications 
refer 
to programmes for portable electronic 
devices, such as smartphones, tablets, Chromecast, 
and 
wearable technology (or mobile apps).


---

## Page 2

According to the "Digital 2019 Predictions," 
smartphone platforms have developed greatly and

worldwide used mobile devices last year, and that 
figure is projected to rise sharply in the near future. 
In 
current 
modern 
age, 
people 
are 
using 
smartphones and the apps that go along with them 
more and more frequently [4] because of the ease 
and effectiveness of the numerous apps and the 
continuing development of the hardware and 
software on smart devices. Global smartphone 
usage is anticipated to reach 6.3 billion users by 
2030. [4].

Information assurance and system security are 
severely 
hampered 
by 
vulnerabilities. 
A 
vulnerability-free application can increase data 
assurance and device security. Assessment of 
vulnerabilities 
and 
penetration 
testing 
have 
typically been disregarded up to now. We can 
lessen the possibility of an attack and dispense 
better, 
more 
steady mobile applications by 
conducting regular and appropriate vulnerability 
assessments. In addition to the security flaws in the 
Android platform, there are numerous other 
vulnerabilities in the application system that could 
result in the theft of personal information from 
handsets. The standard method for finding as many 
risks as possible is a penetration testing strategy. It 
is a methodical approach to identifying flaws in 
applications and systems. It is perfect to use this 
method to identify flaws in mobile applications 
because it gives a more comprehensive picture of 
what might or might not be required. The operative 
procedure of examining either verifying the safety 
of a network or computer system is referred to as 
"penetrating testing." It shall consist in the 
enslavement of the discovered vulnerabilities by 
assisting in determining whether the system 
defences are adequate or if other security flaws are 
present, enumerating which ones the test defeated 
in this particular instance. The testing takes place 
over many different stages, Numerous them 
manually conducted by security professionals from 
the vantage place of a malicious user by precisely 
simulating the computer security of an attacker.

The goal of penetration testing is to assess the 
security 
of 
the 
computerized 
system 
or 
environment by simulating an attack. Physical 
testing can be done with equipment or social 
engineering techniques. The goal of this test is to 
analyse how systems, networks, or personnel 
equipment behaves under difficult conditions in 
order to find flaws and vulnerabilities. Penetration 
testing uses both tools that just examine a system 
and ones that actually attack it to uncover faults.

217

mobile application consumption has increased 
significantly. 
[3] 
Total 
5.11 
billion 
people

Penetration testing differs from penetration testing, 
which is what some people believe it to be. Port 
inspecting is like looking through field glasses at 
windows and doors to detect possible access points 
if a networking or hosting system were a house. 
The next step up would indeed be vulnerability 
assessment and management, which in this instance 
would entail sending a home auditor with an 
emphasis on security to the house. The auditor 
would evaluate various elements of the house and 
provide feedback and proposal on how to enhance 
the security investigation. In this case, penetration 
testing would entail actually attempting to sneak 
into the home in order to identify its security flaws 
and weak points.

Pen testing can be carried out manually or 
automatically using software programs. In any 
case, the procedure entails studying as much as 
possible about the target system prior to the testing 
(reconnaissance), inspecting potential entry points, 
making an effort to break in (each of two 
electronically or physically), and relaying the 
results. Finding security holes is the core goal of 
penetration testing. A penetration test may also be 
used to assess an institution's ability to react to 
security problems, employee security knowledge, 
and compliance with security policies.

Penetration testing often falls into one of four 
categories: external, internal, blind, or double blind 
[11]. An external test focuses on a company's 
publicly accessible servers and equipment, such as 
firewalls, email servers, domain name servers 
(DNS) and Web servers. The goal in this case is to 
determine whether an attacker from outside can 
gain unauthorised access and, if so, to what extent. 
In an internal test, a legitimate user with ordinary 
access credentials imitates an inside assault on the 
firewall. A blind test severely restricts the amount 
of information that is provided to the individual or 
team conducting the test beforehand in order to 
imitate the activities and processes of a real 
attacker. Double blind testing considerably extends 
the blind test because only a selected few members 
of the organization will be aware that a test is being 
done.

There are numerous tools available for penetration 
testing from which Several of them are available 
for free download on the internet. Even some of 
them called open-sourced tools can be use. For 
instance, Kali Linux for testing has a built-in 
collection of penetrating tools, but you may also


---

## Page 3

![Figure 1](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p3_1.jpeg)

install and add more tools to it. The vast majority 
of these programmes are being developed for 
Linux, with very few being developed for Windows 
or Mac.

II. 
Related Work 
System 
examine, 
dynamic 
behaviour, 
hybrid 
filtering examine and network examine are the 
research that have been done in the area of mobile 
software safety and examine. Depending on the 
kind of examine, studies in this topic in the 
literature are different.

In 2020, the Mark A. Williams study A solution 
was put out by Mark A. Williams, Roberto 
Camacho Barranco, Sheikh Motahar Naim, Sumi 
Dey, M. Shahriar Hossain, and Monika Akbar, 
utilising data mining methods to track the 
emergence of a specific vulnerability and illustrate 
how smart phone proneness change over period [5]. 
To anticipate certain proneness or the likelihood of 
the future emergence of proneness, a forecasting 
methodology has been existed. The approach is 
described as the Topically Supervised Evolution 
Model, a mechanism for analysing prior proneness 
announces that is accustomed to explain how an 
already existing proneness threat has progressed.

The 2020 research by Francesco Bergadano, 
Milena Boetti, Valerio Costamagna, Mario Leone, 
and Marco Evangelisti was created as a component 
of the modular framework that was established, 
with each module aiming to assess a certain 
vulnerability. 
This 
framework 
has 
multiple 
platforms. On iOS and Android mobile devices, it 
permits analysis. The modules included in the 
extent 
of 
this 
application 
framework's 
implementation concentrate on the analysis of 
manifest files, data storage, and networking-related 
domains. This application framework was used to 
collect and analyse 105 Play Store applications for 
various fields. It is indicated in the results that the 
application framework demonstrates that it is 
correct and efficient. The group of flaws identified 
during the course of the study is  unshared as a 
report [6].

The goal of a study conducted in 2020 by Alde 
Alanda, Deni Satria, H.A. Mooduto, and Bobby 
Kurniawan is to understand the methods used to 
identify vulnerabilities in the Android platform and 
Android applications. Additionally, to offer advice 
and provide protection from susceptibility OWASP 
Foundation's 
research 
on 
10 
significant 
vulnerabilities 
in 
Android 
applications 
with 
incorrect platform usage served as the basis for the 
techniques and methodologies used [7].

218

Ajin Abraham, Magao Fei, Matan Dobrushin, and 
Vincent Nadal began work on an open source 
project to create a mobile testing framework in 
2018. It is an analysis tool that can analyse the 
security of mobile applications running on the 
Android and iOS operating systems both statically 
and dynamically. With the use of the framework's 
capabilities, analysts can check the source code of 
an application file to see if it contains any 
malicious software components or has a previously 
identified vulnerability [8].

In 2018, research on the system security of iOS 
devices was recommended by Arpita Jadhav Bhatt, 
Chetna Gupta, and Sangeeta Mittal [9]. The 
permissions sought by the programmes from the 
users 
are 
statistically 
assessed 
within 
the 
parameters of the study, and a susceptibility 
analysis model is offered through the created risk 
model. A dynamic analysis step is also included 
within the application framework's purview. It 
extracts variables from applications using reverse 
engineering and classification techniques, then 
computes a risk rating for the application. 
The goal of the 2016 survey by Sungho Lee, Julian 
Dolby, and Sukyoung Ryu was to create an 
application framework that could be analysed using 
static methods. An Android static analysis app that 
examines 
the 
interactions 
among 
Java and 
JavaScript has really been developed as part of the 
application. It has been built to detect programming 
faults and data leakage at language frontiers. The 
error detector recognises errors in programming 
due to differences among Java and JavaScript. 
Additionally, possible data breaches brought on by 
the application's advertising platforms were found 
using static analysis [11].

III. 
Methodology 
Internal network penetration testing is the study 
methodology. The following image shows the 
procedures that will be used in this research:

Figure 1 Methodology

1. Preparation, which establishes the parameters of 
security testing and entails identifying the security 
measures employed, testing goals, and sensitive


---

## Page 4

data. The preparation stage typically involves 
complete coordination with the client, and the 
examiner and client have an agreement protecting 
the examiner against legal actions [7]. 
2. Gathering intelligence is a step when the 
application's scope and architecture are examined 
to gain a general knowledge of the application. 
3. Mapping the Application: After completing the 
previous stage's automatic and human application 
exploration, this phase maps the application. A 
fuller knowledge of the application being tested, 
including points of entry, data held, and many other 
potentially severe flaws can be gained through 
mapping. 
4. Penetration is the stage in which security testers 
breach an application by taking use of the flaws 
that were discovered in the earlier procedure. The 
identification of real flaws and real positives is also 
done at this stage. 
5. Reporting, a crucial phase for the client, is where 
security testers deliver reports on applications' 
vulnerabilities 
and 
describe 
the 
negative 
implications of such flaws.

IV. 
Suggested Tools 
Reverse Engineering is a technique where an 
engineer 
tried 
to 
identify 
the design and 
architecture of a final product. There are many 
tools available to help in achieving the objective.

By using these reverse engineering tools, the

software can reveal the original string and table,

source code, libraries, algorithms and embedded

resources/secrets.

This Paper lists the Top 10 Reverse Engineering

Tools that may be used for Penetration Testing. 
1. 
JADX: Tools for command-line and graphical 
user interfaces that generate Java source code 
from Android Dex and APK files. 
2. 
Dex2jar: Converts .dex files to .class files, 
zipped as a jar file. 
3. 
JD-GUI: It is an independent graphical tool 
that shows Java sources from CLASS files. 
4. 
APKTOOL: A tool for decompiling locked, 
binary, third-party Android apps 
5. 
Binwalk is a built-in Linux tool that lets us 
split and examine binary files. 
6. 
The squashfs: file system can be extracted or 
decompressed using the utility known as 
Unsquashfs. 
7. 
Objdump: It is a tool for disassembling 
executable files and displays details about 
object files.

219

8. 
 Strings: enables the extraction of strings from 
executable files and binary files. 
9. 
GDB: The GNU Debugger aids in the 
decompilation of binary files and executables 
created using embedded C, C++, etc. 
10. Radare2 is a framework for analysing and 
reverse engineering binaries.

V. 
Requirements and Setup 
To perform penetration testing we have taken 
reverse engineering tool called JADX.Today Many 
novice or even professional Android developers are 
unaware of how much easier it is to reverse 
engineer an Android app they have developed and 
released. If you are among the programmers who 
believes that secret keys should be hard-coded or 
even stored in the build. You are mistaken in 
thinking that the .gradle file will keep it out of the 
hands of intruders or other developers. 
The basic rule of security is not to trust client-side 
security. Protection has never been simple. Because 
we do not have control over the client-side 
environment, we shouldn't hard-code or store 
sensitive information there. Therefore, the best 
method to avoid being discovered by hackers and 
engineers is to independently reverse engineer the 
program and, if possible, correct the problems. 
Before we can reverse engineer an application, we 
need a few things: 
1. The application's APK. 
2. A series of codes to run 
3. Java Decompiler Tool to see the code that has 
been decompiled. 
The application's code is contained in the APK 
package file. (It is comparable to a zip file.) It 
includes 
classes, 
META-INF, 
AndroidManifest.xml, 
and 
assets 
(binary 
bytecode). The file extension.apk will be changed 
to.zip extension in order to view all of these 
contents. We can unzip the file using this method to 
see its entire contents. 
An jadx-gui or other tool will be instate to change 
the AndroidManifest.xml file to a readable format 
so that it can be read. 
After receiving the source code, it will be 
personally reviewed for any confidential data that 
has been hardcoded into the code, such as 
passwords, API keys, etc. 
Reverse engineering is performed with apk, below 
structure shows the unzipped structure of apk file:


---

## Page 5

![Figure 2](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_2.jpeg)

![Figure 3](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_3.jpeg)

![Figure 4](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_4.jpeg)

![Figure 5](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_5.jpeg)

![Figure 6](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_6.jpeg)

![Figure 7](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p5_7.jpeg)

Figure 2The image below shows the unzipped structure of an

APK file

VI. 
Experiment and Results 
We took two apk’s one which is developed for 
research not released over internet App1 and 
another one is third party apk easily available over 
internet used by millions of users App2 .The tool 
which is used while implementation is JADX. 
 
 
 
 
 
 
Below is the implementation for App1:

Figure 3:The software main window

Figure 4:App1 Decompiled Code

220

The below screenshot highlights, data is the result 
of reverse engineering. Here google API keys and 
client id is exposed which is a very crucial security 
flaw, which enable hacker to collect more api keys 
with that hacker may easily fetch crucial data and 
information.

Figure 5: Keys Exposed

Figure 6: Apk Signature Window

In Above Result Web client id gives us the 
authentication which is required by google servers 
to determine whether it is authenticated user or not. 
So if we have this we can always spoof data from 
in between By man in the middle attack. Further 
google api keys were also exposed which can be 
used in accessing various google APIs as for 
authentication the only require api key. And if we 
provide that the Google servers will authenticate us 
and allow us to see the data that the api is storing as 
it will be related to user.

Implementation for App2:

Figure 7: Exposed code of the application

The above screenshot highlights, that no source 
code of the main application, is exposed other than 
the libraries that were used and are openly available


---

## Page 6

![Figure 8](../assets/AndroidSecurityAnalysis (2023) Security Analysis on Android Applications/fig_p6_8.jpeg)

to the world. The main package of this application 
is com.biomes.vanced has only one class name as 
MyWrapperProxyApplication other than that we 
cannot see a single class or activities. This means 
this app is secured and no code or crucial data is 
exposed. 
Code Obfuscation is done properly in this 
application to make it more secure.

Figure 8 :Android Manifest file which shows activity classes

On the other hand, if we read the manifest file and 
see the activities are placed under this package 
com.biomes.vanced -  For example –  
Activitycom.biomes.vanced.vooapp.RouterActivity 
shown in figure 8.

VII. 
Discussion 
The primary goal of this research is to make it 
easier for future developers to understand code 
obfuscation and its importance in the development 
process. We took two apps: postit.apk, which was 
developed without using ProGuard, so no proper 
code obfuscation was present, and vanced.apk, 
which had a few classes exposed but no data, which 
may make it hard for a hacker to enter into the 
system because the team behind vanced was well 
experienced and well trained, so code obfuscation 
was present and it helped in stopping the researcher 
from 
performing 
reverse 
engineering. 
This 
researcher suggests that every developer take care 
of security, as these days developers are just 
focusing on completing the task of development in 
less time to earn more money. In all of this, users 
have to go through some serious security issues 
without any idea of how much of their personal 
data and information is getting exposed. To protect 
their 
application 
from 
reverse 
engineering, 
developers should take the following precautions:

1. Developers should set ProGuard rules to avoid 
reverse engineering.

2. If the developer is storing data locally, then the 
developer has to make sure that the data is 
encrypted before being stored.

221

3. The developer must not hard code crucial 
information like API credentials, tokens, and the 
base URL; it should be in the build system 
(build.gradle).

VIII. 
CONCLUSIONS 
During penetration testing, developers should 
perform reverse engineering, as IT administrators 
need to be aware of this essential topic. With the 
internet expanding daily, the field of computer 
security has grown to be highly difficult for both 
businesses and common consumers. It's time to 
accept that having an antivirus programme alone 
won't keep us safe anymore. Users' chances of 
being exposed have increased in modern times. 
Penetration testing through reverse engineering 
should 
be 
performed 
before 
releasing 
it. 
Developers should perform reverse engineering to 
identify and fix vulnerabilities in their applications 
before deploying them over the internet. It is the 
development team's responsibility to deploy secure 
applications over the internet. Even though 
developers are conscious of security, not every one 
of them is qualified to identify or resolve security 
problems. Although creating a completely secure 
environment may be unattainable, there are some 
techniques that can help spot threats and stop data 
disclosure. Penetration testing for mobile devices 
aids in identifying security flaws or vulnerabilities 
in the cellular infrastructure. The right security tool 
selection is essential to any pentest's success. 
Security approaches like Proguard tools should not 
hardcode any API keys into string files; code 
obfuscation should be implemented.

IX. 
REFERENCES

[1] Mobile operating systems' market share worldwide from

January  2012 to June 2021, Statista Market Share Report.  
[2] Turkish Statistical Institute, Household Information

Technologies  Usage Survey, 2020.   
 [3] Chao Ding, Nurbol Luktarhan, Bei Lu and Wenhui Zhang, “A

Hybrid  Analysis-Based Approach to Android Malware 
Family  Classification”, 2021.

[4] Mark A. Williams, Roberto Camacho Barranco, Sheikh

Motahar  Naim, Sumi Dey, M. Shahriar Hossain, Monika 
Akbar, “A vulnerability analysis and prediction framework,” 
Computers &  Security, 142-148, 2020.

[5] Francesco Bergadano, Milena Boetti, Fabio Cogno,

Valerio  Costamagna, Mario Leone, Marco Evangelisti, “A 
modular  framework for mobile security analysis,” 
Information Security  Journal A Global Perspective, 2020, 
pp. 1-24.

[6] Alde Alanda, Deni Satria, H.A Mooduto, Bobby Kurniawan,

“Mobile  Application Security Penetration Testing Based on 
OWASP,” IOP  Materials Science and Engineering, 2020, pp. 
846.   
[7] Ajin Abraham, Magao Fei, Matan Dobrushin, Vincent

Nadal,  “Mobile Security Framework Project,” 2018.


---

## Page 7

[8] Elhadje Benkhelifa, Benjamin E.Thomas, Lo’ai Tawalbeh,

Yaser  Jararweh. “Framework for Mobile Devices Analysis,” 
Procedia  Computer Science, 2016, pp. 1188-1193.   
[9] Sungho Lee, Julian Dolby, Sukyoung Ryu, “HybriDroid:

Static  analysis framework for Android hybrid applications,” 
IEEE Explore,  31st IEEE/ACM International Conference on 
Automated Software  Engineering, September 2016, pp. 250- 
261.   
[10] European Union Agency For Network and Information

Security, “Privacy and data protection in mobile applications, 
A study on the  app development ecosystem and the technical 
implementation of  GDPR”, 2017.   
[11] Haipeng Cai, Barbara G. Ryder, “Artifacts for Dynamic

Analysis of Android Apps,” International Conference on 
Software Maintenance and Evolution, September 2017.     
 [12] Internet: OWASP Mobile Security Testing Guide

v1.2, https://owasp.org/www-project-mobile-security-testing-
guide/ (accessed on 31 October 2021).  
[13] Internet: QARK, Tool to look for several security related

application vulnerabilities, https://github.com/linkedin/qark, 
August 2015. (accessed on 31 October 2021).

[14] Internet: Androbugs, AndroBugs Framework is an efficient

Android vulnerability scanner that helps developers or 
hackers find potential securityvulnerabilities in Android 
applications, 
https://github.com/AndroBugs/AndroBugs_Framework, 
November  2015. (accessed on 31 October 2021).  
[15] Internet: APKTool, A tool for reverse engineering Android

apk files, https://github.com/iBotPeaches/Apktool, January 
2017. (accessed on 31 October 2021).

[16] Internet: Cydia, http://www.cydiasubstrate.com/, 2012.

(accessed on 31 October 2021).  
[17] Internet: Drozer, About The Leading Security Assessment

Framework for 
Android, 
https://github.com/FSecureLABS/drozer, 
February 
2016.  (accessed on 31 October 2021).

[18] Internet: Burp Suite, Application Security Testing Software,

https://portswigger.net/burp/enterprise, December 2008. 
(accessed on 31 October 2021).

222


---

---
title: "DroidBot: A Lightweight UI-Guided Test Input Generator for Android"
creator: "TeX"
pages: 4
---

# X_M_Li_DroidBot

> **總頁數**：4 頁

---

## Page 1

DroidBot: A Lightweight UI-Guided Test Input

Generator for Android

Yuanchun Li, Ziyue Yang, Yao Guo, Xiangqun Chen

Key Laboratory of High-Confidence Software Technologies (Ministry of Education)

School of Electronics Engineering and Computer Science, Peking University, Beijing, China

Email: { yuanchun.li, yzydzyx, yaoguo, cherry } @pku.edu.cn

Abstract —As many automated test input generation tools for then generates UI-guided test inputs based on the transition

Android need to instrument the system or the app, they cannot be model. By default the input is generated with a depth-first

used in some scenarios such as compatibility testing and malware strategy, which is effective for most cases. Users can also

analysis. We introduce DroidBot, a lightweight UI-guided test

users to integrate their own strategies or algorithms. DroidBot

is lightweight as it does not require app instrumentation, thus

Droidbot is released as an open-source tool on GitHub [1], and

the demo video can be found at https://youtu.be/3-aHG SazMY.

ware detection; compatibility testing;

I. I NTRODUCTION

However, it is unrealistic to instrument an app or the system

Some malicious apps also apply sandbox detection, which

that it does not require prior knowledge of unexplored code.

might make DroidBot harder to trigger some specific states, the

trade-off enables DroidBot to work with any apps (including

almost any customized device (unless the device intentionally

removes the built-in testing/debugging modules from the orig-

inal Android framework, which rarely occurs.).

and DroidBox [5].

input generator, which is able to interact with an Android app on customize the exploration strategy by writing scripts or inte-

almost any device without instrumentation. The key technique grate their own algorithms by extending the event generation

behind DroidBot is that it can generate UI-guided test inputs modules, making DroidBot a highly extensible tool.

based on a state transition model generated on-the-fly, and allow The main reason why DroidBot is more lightweight is

no need to worry about the inconsistency between the tested Unlike many existing generators which rely on static analysis

version and the original version. It is compatible to most and instrumentation to get knowledge of unexplored code,

Android apps, and able to run on almost all Android-based DroidBot only models the explored states based on a set

systems, including customized sandboxes and commodity devices. of Android built-in testing/debugging utilities. Although this

Keywords -Android; dynamic analysis; automated testing; mal- the obfuscated/encrypted apps that cannot be instrumented) on

In recent years, mobile applications ( apps in short) have DroidBot also offers a new way to evaluate the effectiveness

seen widespread adoption, with over two million apps avail- of test inputs. Existing approaches mainly use EMMA [3] on

able for download in both Google Play and Apple App Store, open-source apps or instrument apps to calculate test coverage.

while billions of downloads have been accumulated. However, for anti-instrumentation apps (for example verifying

As there are many apps and many different devices, au- the signature at runtime or encrypting the code), it is difficult

tomating app testing has become an important research direc- or even impossible to get their test coverage. DroidBot is able

tion. In particular, a great deal of research has been focused to generate the call stack trace for each test input, which

on automated input generation techniques for Android apps. contains the app methods and system methods triggered by

According to a recent survey [2], most approaches make use the test input. We can use the call stack as an approximate

of either app instrumentation or system modification in order metric to quantify the effectiveness of test inputs.

| to get enough information to guide testing. | The source code of DroidBot is available at GitHub [1]. |  |  |  |
| --- | --- | --- | --- | --- |
| in some scenarios. For example, in compatibility testing, an | II. T | OOL | D | ESIGN |
| app should be tested “as is” on commodity devices in order to | The overall architecture of DroidBot is shown in Figure 1. |  |  |  |

find out which device may cause a crash. Another example is To test an app on a device, DroidBot requires the device being

malware analysis. As many malicious apps are obfuscated, it connected via ADB. The device could be an emulator, a com-

might be difficult, even not impossible, to instrument them. modity device, or a customized sandbox such as TaintDroid [4]

might lead to different behaviors on instrumented testing We introduce the Adapter module to provide an abstraction

devices and real devices. of the device and the app under test (AUT). It deals with

This demonstration paper presents DroidBot, a lightweight low-level technical issues such as compatibility with different

UI-guided test input generator for Android apps. The design Android versions and different screen sizes, maintaining con-

principle of DroidBot is to support model-based test input nection with the device, sending commands to the device and

generation with minimal extra requirements. processing command outputs, etc.

DroidBot offers UI-guided input generation based on a state The Adapter also acts as a bridge between the test environ-

transition model, which is generated on-the-fly at runtime. It ment and the test algorithm. On one hand, it monitors the state

---

## Page 2

… script

App model

Brain

GUI input

| GUI info | Intent |
| --- | --- |
| Logs | Sensor |

Adapter

Android

App

Fig. 1. DroidBot Overview.

of the device and AUT and converts the state information to

structured data. On the other hand, it receives the test inputs

generated by the algorithm and translates them to commands.

With the Adapter , DroidBot is able to provide a set of easy-

to-use high-level APIs for users to write algorithms while en-

suring that the algorithms work in different test environments.

The Brain module receives device and app information

produced by the Adapter at run-time, and sends generated

test inputs to the Adapter . Test input generation is based on a

state transition graph constructed on the fly. Each node of the

graph represents a device state, while the edge between each

pair of nodes represents the test input that triggered the state

III. I MPLEMENTATION

A. Lightweight Monitor and Input

TABLE I

TEST INPUT GENERATORS . N OTE THAT SOME DATA IS FROM

C HOUDHARY et al. [2].

Instrumentation

| System | App |  |  |  |
| --- | --- | --- | --- | --- |
| Monkey [6] | 7 | 7 | Random | 7 |
| AndroidRipper [7] | 7 | 3 | Model | 7 |
| DynoDroid [8] | 3 | 3 | Random | 7 |
| SwiftHand [9] | 7 | 3 | Model | 7 |
| PUMA [10] | 7 | 3 | Model | 3 |
| DroidMate [11] | 7 | 3 | Model | 3 |
| DroidBot [1] | 7 | 7 | Model | 3 |

which are available on most Android devices.

The information fetched from the device can be categorized

into three sets:

1) GUI information . For each UI, DroidBot records the

screenshot and the UI hierarchy tree dumped using

UI Automator (for SDK version higher than 16) or

Hierarchy Viewer (for lower versions);

process status using the ps command and app-level

process status using the dumpsys tool in Android.

3) Logs . Logs include the method trace triggered by each

test input and the logs produced by the app. They can

be retrieved from the Android profiling tool and logcat .

The test input types supported by DroidBot include

UI inputs (such as touching, scrolling, etc.), intents

(BOOT COMPLETED broadcast, etc.), documents to upload

(image, txt, etc.) and sensor data (GPS signal etc.). Note that

the sensor simulation is only supported by emulation.

DroidBot provides a list of easy-to-use APIs for fetch-

ing information from the device and sending inputs to

the device. For example, developers can simply call

device.dump_views() to get a list of UI views and call

view.touch() to send a touch input to a view.

details of the test input and the methods/logs triggered by the

input.

The state transition graph is constructed on the fly. DroidBot

maintains the information of the current state, and monitors

| DroidBot | U | SABILITY COMPARISON OF EXISTING PUBLICLY | - | AVAILABLE BLACK | - | BOX |
| --- | --- | --- | --- | --- | --- | --- |
| strategy | Tool | Strategy | Programmable |  |  |  |
| Process info | Document | mostly based on existing Android debugging/testing utilities, |  |  |  |  |
| Device | 2) | Process information | . DroidBot monitors system-level |  |  |  |

transition. DroidBot integrates a simple but effective depth- B. On-the-fly Model Construction

first exploration algorithm to generate test inputs. It also allows DroidBot generates a model of AUT based on the infor-

users to integrate their own algorithms or use app-specific mation monitored at runtime. The model aims to help input

| scripts to improve the test strategy. | generation algorithms to make better test input choices. |
| --- | --- |
| Such design improves the usability of DroidBot. Table I | Figure 2 shows an example of a state transition model. |

shows the usability comparisons between DroidBot and other Basically, the model is a directed graph, in which each node

public-available test input generation tools. We can see that represents a device state, and each edge between two nodes

DroidBot requires as little requirements as Monkey, while represents the test input event that triggered the state transition.

providing much more extensible features comparable to other A state node typically contains the GUI information and the

tools requiring instrumentation. running process information, and an event edge contains the

DroidBot fetches device/app information from the device the state changes after sending a test input to the device. Once

and sends test inputs to the device through ADB. Both the the device state is changed, it adds the test input and the new

monitoring and input phases are lightweight because they are state to the graph, as a new edge and a new node.

---

## Page 3

| State 1 | Event 1 |  |
| --- | --- | --- |
| GUI: | FrameLayout | Input: |
| TableLayout | FrameLayout | Type: Touching |

TableRow TableRow TableRow adMobView AdView

… … id/ View:

frm_weather View id/ frm_mylocati View id/ on

Command: adb shell input …

| Process info: | Logs: |
| --- | --- |
| System: zygote, … | Trace: onTouch(), startActivity(), … |
| Activity: HomeActivity | Logcat: |
| Services: PushService, … | <debug output> |

<error messages>

(a) Total number of sensitive behaviors in four categories.

event 1

event 2

state 1

event 3 state 2

state 3

Fig. 2. An example of state transition graph. Note that the data in this graph

is simplified for easy understanding. (b) Speed of triggering sensitive behaviors.

The graph construction process relies on the underlying state Fig. 3. Comparison of the effectiveness in triggering sensitive behaviors

when testing a malware with Monkey and DroidBot.

comparison algorithm. Currently, DroidBot uses content-based

comparison, where two states with different UI contents are IV. U SAGE S CENARIOS

considered as different nodes.

A. Compatibility Analysis

C. Quantifying the Effectiveness of Test Input

One of the useful scenarios of DroidBot is compatibility

One problem faced by researchers and testers when con- testing, which is aimed at evaluating the app’s correctness and

ducting black-box testing is the difficulty to evaluate testing robustness when running on different devices. Compatibility

effectiveness, as the existing test coverage methods either testing should be performed on many different commodity

require the source code of AUT [3] or need to instrument devices thus system instrumentation is unrealistic. Meanwhile,

the AUT [12]. app instrumentation might also be unwanted because instru-

DroidBot integrates two methods to quantify the test effec- mented app may behave differently from the original app.

tiveness without source code or instrumentation: With DroidBot, a developer is able to test his/her app on

• Method tracing. DroidBot is able to print the method trace different devices without instrumentation, reaching more UI

of each test input using the Android official profiling tool. states in much shorter time compared to Monkey. Moreover,

The method trace contains the app methods and system with the scripting feature provided by DroidBot, the developer

methods triggered by the test input. With the method can customize the test input to generate.

trace, we are also able to calculate the method coverage

if the total number of methods is available. B. Malware Analysis

• Sensitive behavior monitoring. For malware analysis, the Malware analysis is also a useful scenario of DroidBot. As

number of sensitive behaviors triggered can reflect the test many malware encrypt their code or check their signature

effectiveness. For example, DroidBot can be used with before doing malicious things, it might be impossible to

DroidBox [5] to monitor the sensitive behaviors triggered instrument them or guarantee the consistency between the

by each input. instrumented app and the original app.

The method tracing mechanism scales better as it works Monkey [6] is able to test malware without instrumentation,

with almost any device and any app, while the sensitive but the random strategy of Monkey might not be efficient in

behavior monitoring mechanism requires apps running in a discovering the malicious behaviors. DroidBot is as easy-to-

certain sandbox. However, the number of sensitive behaviors use as Monkey but is better in app exploration as it uses a

might be more intuitive in malware analysis. Both methods are model-based strategy. For example, if a malware does not per-

unable to give a normalized value of how effective a test case form malicious behavior until the user clicks certain buttons,

exactly is, but they can provide meaningful statistics when it might be difficult for randomized test input generator to

comparing different test cases on the same app. find the correct buttons, while model-based generator have the

---

## Page 4

information about the AUT fetched from the device at runtime, scenarios including compatibility testing, malware analysis

thus is easier to trigger the sensitive behaviors. and other cases where instrumentation is unwanted.

Figure 3 shows the comparison to Monkey in a proof-of- A CKNOWLEDGMENT

concept example of using DroidBot in malware analysis. We

selected a malware which encrypted its code as the app under

test, and used DroidBox [5] as the testing device in order to

monitor the sensitive behaviors, such as file accesses, network

accesses, data leaks, etc.

V. R ELATED W ORK

testing, and it is the most light-weighted. However, the inputs

also generates randomized input, but it is smarter in selecting

using different methods to construct the model and generate

key, while providing much advanced features as most other

Besides regular testing tasks, DroidBot can also be used in

This work is partly supported by the National Key Research

and Development Program under Grant No.2016YFB1000105

and the National Natural Science Foundation of China under

Grant No.61421091.

[2] S. R. Choudhary, A. Gorla, and A. Orso, “Automated test input gen-

Computer Society, 2015, pp. 429–440.

realtime privacy monitoring on smartphones,” in Proceedings of the 9th

[5] A. Desnos and P. Lantz, “Droidbox: An android application sandbox for

dynamic analysis,” 2011.

[6] A. Developers, “Ui/application exerciser monkey,” 2012.

applications,” in Proceedings of the 27th IEEE/ACM International

pp. 258–261.

system for android apps,” in Proceedings of the 2013 9th Joint Meeting

pp. 224–234.

with minimal restart and approximate learning,” in Proceedings of the

’13, 2013, pp. 623–640.

[10] S. Hao, B. Liu, S. Nath, W. G. Halfond, and R. Govindan, “Puma:

204–217.

2016, pp. 293–294.

systematic testing of android apps,” in Proceedings of the 2013 ACM

641–660.

[14] Y.-M. Baek and D.-H. Bae, “Automated model-based android gui

Engineering , ser. ASE 2016, 2016, pp. 238–249.

droid: An automatic system for revealing ui-based trigger conditions in

’12, 2012, pp. 93–104.

Conference on Security Symposium , ser. SEC’14, 2014, pp. 1021–1036.

arXiv:1410.7751 , 2014.

| We use Monkey and DroidBot to generate test input respec- | R | EFERENCES |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tively. The result shows that the amount of sensitive behaviors | [1] | honeynet, “Droidbot: A lightweight test input generator for android,” |  |  |  |  |  |  |  |  |
| triggered by DroidBot is much higher than Monkey, while the | https://github.com/honeynet/droidbot, 2016, accessed: 2016-11-10. |  |  |  |  |  |  |  |  |  |
| inputs generated by Monkey almost did not trigger any extra | eration for android: Are we there yet? (e),” in | Proceedings of the |  |  |  |  |  |  |  |  |
| sensitive behaviors. We inspected the test processes of Monkey | 2015 30th IEEE/ACM International Conference on Automated Software |  |  |  |  |  |  |  |  |  |
| and DroidBot. The reason for Monkey’s ineffectiveness is that | Engineering (ASE) | , ser. ASE ’15. | Washington, DC, USA: IEEE |  |  |  |  |  |  |  |
| the app requires users to touch two buttons in a pop-up dialog | [3] | V. Roubtsov, “Emma: a free java code coverage tool,” 2006. |  |  |  |  |  |  |  |  |
| successively to enter a malicious state. DroidBot successfully | [4] | W. Enck, P. Gilbert, B.-G. Chun, L. P. Cox, J. Jung, P. McDaniel, |  |  |  |  |  |  |  |  |
| found the buttons and touched them in around 80 seconds, | and A. N. Sheth, “Taintdroid: An information-flow tracking system for |  |  |  |  |  |  |  |  |  |
| while the randomized test inputs generated by Monkey failed | USENIX Conference on Operating Systems Design and Implementation | , |  |  |  |  |  |  |  |  |
| to pass the pop-up dialog. | ser. OSDI’10, 2010, pp. 393–407. |  |  |  |  |  |  |  |  |  |
| Test input generation for Android has been drawing re- | [7] | D. Amalfitano, A. R. Fasolino, P. Tramontana, S. De Carmine, and |  |  |  |  |  |  |  |  |
| searchers’ interests for a long time. | A. M. Memon, “Using gui ripping for automated testing of android |  |  |  |  |  |  |  |  |  |
| Monkey [6] is the most popular tool to perform black box | Conference on Automated Software Engineering | , ser. ASE 2012, 2012, |  |  |  |  |  |  |  |  |
| generated by Monkey are completely random, which is not ex- | [8] | A. Machiry, R. Tahiliani, and M. Naik, “Dynodroid: An input generation |  |  |  |  |  |  |  |  |
| tensible and easy to be intentionally bypassed. DynoDroid [8] | on Foundations of Software Engineering | , ser. ESEC/FSE 2013, 2013, |  |  |  |  |  |  |  |  |
| test inputs. | [9] | W. Choi, G. Necula, and K. Sen, “Guided gui testing of android apps |  |  |  |  |  |  |  |  |
| AndroidRipper | [7], | SwiftHand | [9], | A | 3 | E | [13] | and | 2013 ACM SIGPLAN International Conference on Object Oriented |  |
| GUICC [14] are model-based automated test generators, while | Programming Systems Languages &#38; Applications | , ser. OOPSLA |  |  |  |  |  |  |  |  |
| input based on the model. PUMA [10] is a model-based | Programmable ui-automation for large-scale dynamic analysis of mobile |  |  |  |  |  |  |  |  |  |
| test framework, which is programmable with PUMAScript. | apps,” in | Proceedings of the 12th Annual International Conference on |  |  |  |  |  |  |  |  |
| SmartDroid [15] and Brahmastra [16] are focused on targeted | Mobile Systems, Applications, and Services | , ser. MobiSys ’14, 2014, pp. |  |  |  |  |  |  |  |  |
| testing which aims to trigger certain pieces of code. | [11] | K. Jamrozik and A. Zeller, “Droidmate: A robust and extensible test |  |  |  |  |  |  |  |  |
| Andlantis | [17] | is | designed | for | malware | analysis. | It | is | generator for android,” in | Proceedings of the International Conference |
| focused on large-scale virtual machine management and able | on Mobile Software Engineering and Systems | , ser. MOBILESoft ’16, |  |  |  |  |  |  |  |  |
| to execute malware on multiple emulators at the same time. | [12] | ylimit, | “androcov: | measure | test | coverage | without | source | code,” |  |
| DroidMate [11] is a similar approach to DroidBot as it also | https://github.com/ylimit/androcov, 2016, accessed: 2016-11-10. |  |  |  |  |  |  |  |  |  |

emphasizes robustness and extensible strategy, however it still [13] T. Azim and I. Neamtiu, “Targeted and depth-first exploration for

| needs a slight instrumentation to enable API monitoring. | SIGPLAN International Conference on Object Oriented Programming |  |  |
| --- | --- | --- | --- |
| Compared to these tools, DroidBot is as easy to use as Mon- | Systems Languages &#38; Applications | , ser. OOPSLA ’13, 2013, pp. |  |
| tools, including model-based input generation and extensible | testing using multi-level gui comparison criteria,” in | Proceedings of |  |
| scripting, etc. | the 31st IEEE/ACM International Conference on Automated Software |  |  |
| VI. C | ONCLUSION | [15] | C. Zheng, S. Zhu, S. Dai, G. Gu, X. Gong, X. Han, and W. Zou, “Smart- |
| This demonstration presents DroidBot, a lightweight test | android applications,” in | Proceedings of the Second ACM Workshop on |  |
| input generator for Android apps. DroidBot is able to test an | Security and Privacy in Smartphones and Mobile Devices | , ser. SPSM |  |

Android app on almost any device with minor environment [16] R. Bhoraskar, S. Han, J. Jeon, T. Azim, S. Chen, J. Jung, S. Nath,

requirements. It is easy to use, because on one hand, it is R. Wang, and D. Wetherall, “Brahmastra: Driving apps to test the

extensible based on a set of high-level APIs and a state security of third-party components,” in Proceedings of the 23rd USENIX

transition model constructed on the fly, on the other hand, [17] M. Bierma, E. Gustafson, J. Erickson, D. Fritz, and Y. R. Choe,

it provides a set of utilities to evaluate the test effectiveness. “Andlantis: large-scale android dynamic analysis,” arXiv preprint

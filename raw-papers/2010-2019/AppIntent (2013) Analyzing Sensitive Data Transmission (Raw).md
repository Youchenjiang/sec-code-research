---
title: "41_Yang_et_al.,_AppIntent_Analyzing_Sensitive_Data_Transmission"
creator: " TeX output 2013.08.24:0006"
pages: 12
---

# 41_Yang_et_al.,_AppIntent_Analyzing_Sensitive_Data_Transmission

> **總頁數**：12 頁

---

## Page 1

AppIntent: Analyzing Sensitive Data Transmission in Android for

Privacy Leakage Detection

| Zhemin Yang | Min Yang | Yuan Zhang |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Fudan University | Fudan University | Fudan University |  |  |  |
| yangzhemin@fudan.edu.cn | m_yang@fudan.edu.cn | yuanxzhang@fudan.edu.cn |  |  |  |
| Guofei Gu | Peng Ning | X. Sean Wang |  |  |  |
| Texas A&M University | NC State University | Fudan University |  |  |  |
| guofei@cse.tamu.edu | pning@ncsu.edu | xywangcs@fudan.edu.cn |  |  |  |
| Abstract | 1. | INTRODUCTION |  |  |  |
| Android phones often carry personal information, attracting | With the growing popularity of Android, millions of ap- |  |  |  |  |
| malicious developers to embed code in Android applications | plications (or | apps | for short) are available to users from a |  |  |
| to steal sensitive data. | With known techniques in the lit- | variety of Internet sites (called | app markets | ). | While users |
| erature, one may easily determine if sensitive data is being | enjoy the rich features of the apps, their sensitive personal |  |  |  |  |
| transmitted out of an Android phone. | However, transmis- | data, such as phone numbers, current locations, and con- |  |  |  |
| sion of sensitive data in itself does not necessarily indicate | tact information, may be stealthily collected and misused |  |  |  |  |
| privacy leakage; a better indicator may be whether the trans- | by the ill-intended developers of some apps. A recent study |  |  |  |  |
| mission is by user intention or not. | When transmission is | has showed that Android apps frequently transmit private |  |  |  |
| not intended by the user, it is more likely a privacy leak- | data to unknown destinations without user consent [46]. To |  |  |  |  |
| age. | The problem is how to determine if transmission is | protect users, there is a great need for strong analysis tools |  |  |  |
| user intended | . | As a | rst solution in this space, we present | that Android app markets can use to identify and remove |  |
| a new analysis framework called AppIntent. For each data | malicious apps. |  |  |  |  |
| transmission, AppIntent can efficiently provide a sequence of | State-of-the-art approaches of privacy leakage detection |  |  |  |  |
| GUI manipulations corresponding to the sequence of events | on smartphones focus on detecting sensitive data transmis- |  |  |  |  |
| that lead to the data transmission, thus helping an analyst | sion, i.e., whether personal data leaves the device [21, 22, 26, |  |  |  |  |
| to determine if the data transmission is user intended or | 30, 40, 29]. However, in this era of mobile apps with cloud |  |  |  |  |
| not. | The basic idea is to use symbolic execution to gener- | computing, what constitutes a privacy leakage by mobile |  |  |  |
| ate the aforementioned event sequence, but straightforward | apps is a subject that needs reconsideration. Many benign |  |  |  |  |
| symbolic execution proves to be too time-consuming to be | apps provide services from the cloud to end users. | These |  |  |  |
| practical. | A major innovation in AppIntent is to leverage | apps normally need to collect sensitive data such as loca- |  |  |  |
| the unique Android execution model to reduce the search | tion, contact, to send out to the cloud. Malicious apps that |  |  |  |  |
| space without sacri cing code coverage. We also present an | steal user data may also exhibit the same behavior, namely |  |  |  |  |
| evaluation of AppIntent with a set of 750 malicious apps, as | transmitting private information to the cloud (or via other |  |  |  |  |
| well as 1,000 top free apps from Google Play. | The results | means). | Therefore, transmission of sensitive data by itself |  |  |
| show that AppIntent can effectively help separate the apps | may not indicate true privacy leakage; a better indicator |  |  |  |  |
| that truly leak user privacy from those that do not. | should be whether the transmission is | user intended or not | . |  |  |

 User-intended data transmission . To use the func-

tion provided by an app, a user often tolerates his/her

Categories and Subject Descriptors

private data being sent out via some communication

| D.4.6 [ | Operating Systems | ]: Security and Protection; D.2.5 | channels. For example, when using SMS management |  |  |
| --- | --- | --- | --- | --- | --- |
| [ | Software Engineering | ]: | Testing and Debugging\| | Sym- | apps [3], a user can forward an SMS message to a third |
| bolic execution | party, by several button clicking on the touchscreen. |  |  |  |  |

As another example, when using a location-based ser-

Keywords vice [7], a user usually knows his/her location is sent

out to get interesting contents tailored to the location.

| Android security; privacy leakage detection; symbolic exe- | Since this kind of functional use of sensitive data is |
| --- | --- |
| cution | consistent with user intention, we should not treat this |

kind of transmission as a privacy leakage.

Permission to make digital or hard copies of all or part of this work for personal or  Unintended data transmission . The irregular transmis-

classroom use is granted without fee provided that copies are not made or distributed sion of sensitive data performed by an app, which is

for profit or commercial advantage and that copies bear this notice and the full cita-

| tion on the first page. Copyrights for components of this work owned by others than | unknown to users and irrelevant to the function user |  |
| --- | --- | --- |
| ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or re- | enjoys, is de ned as unintended data transmission, or |  |
| publish, to post on servers or to redistribute to lists, requires prior specific permission | privacy leakage. | In most cases, users are unaware of |
| and/or a fee. Request permissions from permissions@acm.org. | this kind of transmission because the malicious apps |  |
| CCS’13, | November 4–8, 2013, Berlin, Germany. | always do that in a stealthy manner. |

Copyright 2013 ACM 978-1-4503-2477-9/13/11 ...$15.00.

http://dx.doi.org/10.1145/2508859.2516676 .

---

## Page 2

| The above shows that whether sensitive data transmission | The contribution of this paper is fourfold. First, we note |
| --- | --- |
| is a privacy leakage or not actually depends on whether the | that sensitive data transmission does not always indicate pri- |
| transmission is user intended or not. Unfortunately, due to | vacy leakage; rather, user-intended data transmission should |

the complex nature of user intention and different/unpredictable be discriminated from user-unintended. Second, we develop

| settings of different apps, it is almost impossible to have an | an event-space constraint guided symbolic execution tech- |  |  |  |
| --- | --- | --- | --- | --- |
| automated method to determine user intentions. | Alterna- | nique, which effectively reduces the event search space in |  |  |
| tively, it is more practical to design an automated tool to | symbolic execution for Android apps. As a result, event in- |  |  |  |
| provide a human analyst with the context information in | puts as well as data inputs related to each propagation path |  |  |  |
| which the data transmission occurs. | Intuitively presented | of data transmission can be effectively extracted. Third, we |  |  |
| context information will make the task of the human an- | develop a dynamic program analysis platform to execute the |  |  |  |
| alyst easier in determining if the transmission is user in- | app driven by the discovered event and data inputs, so that |  |  |  |
| tended. | This motivates our work on the | AppIntent | frame- | we can display the sequence of UI manipulations, emulating |
| work. Given sensitive data transmission, AppIntent derives | the entire process leading to the data transmission. Finally, |  |  |  |
| the input data and user interaction inputs that lead to the | we evaluate our approach by using 750 reported malicious |  |  |  |
| transmission. | The context information of the transmission | apps, as well as 1,000 top free apps from Google Play. Some |  |  |
| shown to the analyst is in the form of a sequence of UI | interesting | ndings are also provided together with the eval- |  |  |
| manipulations (i.e., GUI screens along with the highlighted | uation results. |  |  |  |
| GUI controls that indicate the supposed user operations) | The rest of this paper is organized as follows. | Section 2 |  |  |
| that is captured from a controlled execution of the app with | introduces the challenge of symbolic execution for Android, |  |  |  |
| the derived input data and user interaction. By looking at | and Section 3 gives an overview of the AppIntent frame- |  |  |  |
| the displayed UI manipulations, a human analyst can then | work. Section 4 presents the details of event-space constraint |  |  |  |
| make a judgement. | guided symbolic execution. The dynamic analysis platform |  |  |  |
| Symbolic execution is an effective technique to extract fea- | of AppIntent is depicted in Section 5. | Section 6 presents |  |  |
| sible inputs that can trigger speci c behaviors of a program | the evaluation of AppIntent using real-world Android apps. |  |  |  |
| such as particular transmission of sensitive data. | The key | Section 7 discusses the related work, and Section 8 concludes |  |  |
| idea of symbolic execution is to systematically explore fea- | this paper and points out some future research directions. |  |  |  |

sible paths of the program under analysis by reducing the

search space from an in nite number of possible data inputs

to a nite number of data scopes (represented by symbolic

Dealing with events triggered by user actions in GUI apps is

challenging because the possibly large number of combina-

tions of input events can severely worsen the path explosion

problem during symbolic execution. However, in AppIntent,

user interactions cannot be abstracted away from apps for

symbolic execution because user interaction is an essential

part to judge whether the transmission is intended by the

user or not.

To deal with the path explosion problem, we have devel-

oped a new symbolic execution technique called event-space

constraint guided symbolic execution for Android apps. We

rst apply static analysis to the target app to identify the

possible execution paths leading to the sensitive data trans-

mission under analysis (such as sending SMS). We then use

these paths as the basis to generate our event-space con-

straints, which represent all the possible event sequences for

the given execution paths by considering the call graph and

the Android execution model. Our guided symbolic execu-

tion then considers only the paths that satisfy the event-

space constraints. Our experiments show that these con-

straints restrict the search space very effectively since the

number of execution paths to be explored during the guided

symbolic execution is usually small.

To evaluate the effectiveness of AppIntent , we perform an

extensive experimental evaluation using real-world apps in-

cluding 750 malicious apps reported in [46] and 1,000 top

free apps from Google Play, to detect whether they trans-

mit user's private data and to distinguish whether the trans-

mission is user intended or not. In our experimental results,

252 apps have sensitive data transmission, among which 224

apps contain user unintended transmission while other 28

apps contain only user-intended data transmission.

Symbolic execution is a program analysis technique that

has been used in a wide range of applications such as test

case generation [14, 17, 27, 28, 34, 39], fuzz testing [35], and

security aws detection [13, 15, 20, 26, 31, 42]. It is a traver-

sal process, which explores a search space during the analysis

process. The general idea of symbolic execution is to limit

the search space because its execution time and practica-

bility depend on this scope. For those non-interactive pro-

grams, symbolic execution can efficiently explore the search

space of data inputs through a well-de ned classi cation of

these inputs. However, symbolic execution faces unresolved

challenges when it is applied to GUI apps.

GUI apps, which are widely used in computers and hand-

held devices, are driven by not only data inputs, but also

event inputs. Users can interact with apps by triggering

runtime events such as clicking a certain button. Event in-

puts, which introduce highly variable program behaviors and

hard to be classi ed into input scopes, greatly increase the

search space of GUI apps. To the best of our knowledge,

there are no efficient solutions to this problem, and most

of the existing symbolic execution approaches for GUI apps

sacri ce code coverage for performance by applying random

scheduling strategy [38], exhaustively searching possibilities

(to an upper bound of event sequences) [25], or assuming

that event handlers will not cooperate with each other [24].

Recently, Contest [9] reduces the symbolic execution time of

smartphone apps to 5%-36% of the original running time by

utilizing pro ling results, but the cost of this analysis is still

too high.

When modeling the space of runtime event inputs, the

most important characteristic of the space is the possible

orders of events. In most cases, the behavior of a GUI app

inputs). However, existing symbolic execution techniques 2. BACKGROUND: SYMBOLIC EXECUTION

mainly focus on non-interactive programs [10, 16, 28, 39]. FOR ANDROID APPS

---

## Page 3

can be represented by the events triggered by the user along its execution is typically driven by events from the speci c

with the order of these events. GUI controls (represented as a View object) that the user

interacts with. An app contains a collection of nested in-

| 2.1 | Android Basis | terfaces, called event listeners. These listeners capture user |
| --- | --- | --- |
| Similar to Java GUI apps, Android apps are usually driven | interactions with the app GUI. When respective interactions |  |
| by runtime events and callbacks. The non-determinism in- | occurs on the GUI controls, for example, if a button is clicked |  |
| troduced by arbitrarily and distinctively triggered events in- | by a user, the pre-de ned event handlers are triggered cor- |  |
| creases the complexity when exploring the search space and | respondingly. | System events are handled in the same way. |
| severely challenges the symbolic execution of GUI apps. The | Like callbacks, runtime events are also non-deterministic. |  |
| search space of events is decided by Android programming | They can be triggered in any order and at any time, thus |  |
| and execution model, which needs a careful consideration in | exhaustively executing all possible sequences of events is a |  |
| analysis. | task that will never end. Fortunately, events in an Android |  |

app are commonly invoked when the state of the app is

GUI Evenets OnResume() RUNNING . In this state, the main thread is hung to wait

System Events for incoming events. Thus, the event triggering behavior

commonly depends on the order, not the exact triggering

| RUNNING | PAUSED |
| --- | --- |
| OnPause() | time. |
| OnResume() | OnStop() |

3. GOAL AND OVERALL ARCHITECTURE

| STARTED | OnRestart() | STOPPED | AppIntent is not an automated method to detect unin- |
| --- | --- | --- | --- |
| OnStart() | tended data transmission, which is probably a mission im- |  |  |
| OnStart() | OnDestroy() | possible. Instead, as a | rst step in this space, AppIntent is |

designed to be an automated tool to present to a human an-

CREATED DESTORYED alyst the sequence of UI manipulations that corresponds to

the sequence of events that leads to the sensitive data trans-

mission, thereby facilitating the discrimination of whether

| OnCreate() | KILLED | sensitive data transmission is user intended or not. |
| --- | --- | --- |
| NOT | Our Goal | . To achieve our vision, we have the following |

LAUCHED

three goals:

 Produce the critical app inputs that lead to sensitive

| Figure 1: | Android application model. | This | gure depicts | data transmission. Speci c to Android GUI apps, in- |
| --- | --- | --- | --- | --- |
| the lifecycle of Android activities. | The lifecycle of other | puts are always composed of: | a) Data inputs which |  |
| components are similar. | contain text inputs from outside; b) Event inputs from |  |  |  |

user interactions through GUI interface and from sys-

| There are two major kinds of events in Android: callbacks | tem through IPC. In addition, we need to track down |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| to manipulate the state transition of an app, and listeners to | the root-cause that gives rise to the transmission and |  |  |  |  |  |  |  |  |
| handle system events and user interactions with GUI com- | lter out the massive set of irrelevant inputs. |  |  |  |  |  |  |  |  |
| ponents: |  | Guarantee a good code coverage. | To | nd all feasible |  |  |  |  |  |
| Android Events: Callbacks of Lifecycle States. | Un- | paths, we need to thoroughly traverse diverse program |  |  |  |  |  |  |  |
| like in the common Java world, Android app does not have | paths that may lead to a leakage, and at the same |  |  |  |  |  |  |  |  |
| a unique program entry such as main(). Instead, it is com- | time, we want to ensure low false positive as well as low |  |  |  |  |  |  |  |  |
| posed of one or more components which work together to | false negative rate during this analysis. In addition, to |  |  |  |  |  |  |  |  |
| ful ll the functionality. | The major type of components in | enable large-scale validation tasks, we do not want too |  |  |  |  |  |  |  |
| Android is activity. | An activity represents a single screen | much overhead. |  |  |  |  |  |  |  |
| with a user interface. The other components, e.g., services, |  | Provide an easy-to-understand tool for human ana- |  |  |  |  |  |  |  |
| content providers, and BroadcastReceivers, are background | lysts to ascertain under what circumstance the sen- |  |  |  |  |  |  |  |  |
| tasks that perform long-running operations or respond to | sitive data transmission happens. Using the produced |  |  |  |  |  |  |  |  |
| other threads. For each component, app developers override | app inputs, we need to conduct the execution of an app |  |  |  |  |  |  |  |  |
| callback functions, which are commonly used to maintain | according to each feasible path. | We want to exercise |  |  |  |  |  |  |  |
| its lifecycle, as depicted in Figure 1. These callbacks are ex- | the app's functionality automatically, which can em- |  |  |  |  |  |  |  |  |
| pected to be automatically invoked by Android application | ulate users' operations, and by observing the UI ma- |  |  |  |  |  |  |  |  |
| manager. Therefore, symbolic execution faces a severe chal- | nipulation and prompting, we can then easily judge |  |  |  |  |  |  |  |  |
| lenge because of the non-deterministic and unbounded trig- | whether the data transmission is essential for a user- |  |  |  |  |  |  |  |  |
| gering order of callbacks. For example, a possible execution | intended functionality. |  |  |  |  |  |  |  |  |
| could be | (OnStart | ) | OnPause | ) | OnResume | ) | OnPause | Overall Architecture | . Figure 2 depicts the overall ar- |
| ) | OnResume | ) | ...) | . It will further worsen the already noto- | chitecture of AppIntent, which analyzes a target app in two |  |  |  |  |
| rious search space explosion problem of traditional symbolic | steps: |  |  |  |  |  |  |  |  |
| execution. | Actually, symbolic execution may never | nish |  | Event-space Constraint Guided Symbolic Execution | . The |  |  |  |  |
| because the search space is in nite. | We propose a guided | rst step is to generate critical inputs incurring sensi- |  |  |  |  |  |  |  |
| symbolic execution mechanism which can effectively solve | tive data transmission. We adopt static taint analysis |  |  |  |  |  |  |  |  |
| this problem with static analysis. | to preprocess and extract all possible data transmis- |  |  |  |  |  |  |  |  |
| Android Events: | GUI Events and System Events. | sion paths as well as possible events related to each |  |  |  |  |  |  |  |
| An app running on Android is commonly GUI based, and | path, which helps to construct an event-space con- |  |  |  |  |  |  |  |  |

---

## Page 4

Figure 2: Overall Architecture of AppIntent

| straint graph. | Subsequently the graph is used in the | extract instructions of sensitive data propagation with the |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| guided symbolic execution to extract critical inputs. | context information along each path. In our example, we get |  |  |  |  |  |  |  |  |  |  |
| Meanwhile, code coverage is guaranteed due to the na- | the path: | f | OnReceive | , i1 | g ) f | startNewMessagesQuery | , i2 | g |  |  |  |
| ture of symbolic technique. | The detail is introduced | ) f | forward | , i3 | g ) f | forward | , i4 | g ) f | sendMessage | , i5 | g ) |
| in Section 4. | f | sendMessage | , i6 | g | . Then we construct an event-space con- |  |  |  |  |  |  |
|  | Dynamic Program Analysis Platform | . | Inputs gener- | straint graph according to the information gathered in static |  |  |  |  |  |  |  |
| ated in the | rst step is not intuitive enough though | analysis. As Figure 4 shows, those massive irrelevant events |  |  |  |  |  |  |  |  |  |
| they precisely tell under what conditions transmission | to this path have been | ltered out, and only 18 events related |  |  |  |  |  |  |  |  |  |
| would happen. Using these inputs, we adopt Android | to this path, including lifecycle callbacks, GUI events, and |  |  |  |  |  |  |  |  |  |  |
| InstrumentationTestRunner | [1] to automate the app | system events, are kept. We connect these events with edges |  |  |  |  |  |  |  |  |  |
| execution step by step, which re ects users' interac- | according to the lifecycle state transition and the call graph. |  |  |  |  |  |  |  |  |  |  |
| tions in UI manipulations, and the sensitive data prop- | This event-space constraint graph is used as a guideline for |  |  |  |  |  |  |  |  |  |  |
| agation is also tailored to the related UI for a better | symbolic execution to | nd sequenced events that possibly |  |  |  |  |  |  |  |  |  |
| understanding. We believe it can effectively visualize | incur the transmission. | Since our goal is to | nd the root |  |  |  |  |  |  |  |  |
| the root cause of the transmission so that we can intu- | cause and disclose the context of the user actions, we only |  |  |  |  |  |  |  |  |  |  |
| itively judge whether the transmission is user intended | need to | nd the shortest paths that cover the sensitive data |  |  |  |  |  |  |  |  |  |
| or not. | transmission instructions respectively. | As Figure 5 shows, |  |  |  |  |  |  |  |  |  |

for the given transmission, we get only two chains of events

4. EVENT-SPACE CONSTRAINT GUIDED in sequence, which will be veri ed during symbolic execu-

tion, with a very small overhead. On our dynamic program

SYMBOLIC EXECUTION

analysis platform, the feasible chain is used to emulate a

| In this section, we present our event-space constraint guided | user's operations step by step automatically, which demon- |  |
| --- | --- | --- |
| symbolic execution technique for Android apps. | We show | strates which functionality is executed when sensitive data |
| how to reduce the search space considerably and | nish the | transmission happens. In this case, we can easily determine |
| symbolic execution in an acceptable amount of time without | that this is indeed user-intended data transmission. |  |

sacri cing the code coverage.

We begin with an intuitive example, and then present an

4.2 Overview of Event-space Constraint Guided

overview of this stage, followed by a detailed description

| of how to construct the event-space constraint graph using | Symbolic Execution |
| --- | --- |
| static analysis. Finally we describe how the graph facilitates | As stated earlier, the major challenge symbolic execution |
| guided symbolic execution. | faces is the problem of space explosion, which is dramati- |

cally worsened by the Android GUI interaction and execu-

| 4.1 | A Concrete Example | tion model. A complete app-wide symbolic execution is not |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Here we use an app, | Anzhuoduanxin | [3], to demonstrate | scalable due to the large number of possible events. | Actu- |  |
| how our event-space constraint guided symbolic execution | ally, to achieve sensitive data transmission, usually only a |  |  |  |  |
| works. | The app has a program path containing the trans- | small portion of events will be triggered in sequence, along |  |  |  |
| mission of an SMS message when a user forwards a new in- | with sequenced instructions that propagate the data. This |  |  |  |  |
| coming message. For easy understanding, as depicted in Fig- | motivates us that if we are provided with a set of instruc- |  |  |  |  |
| ure 3, we simplify the data propagation to a path involving | tions that possibly incur the transmission, we only need to |  |  |  |  |
| only one BroadcastReceiver, | PushReceiver | , and two activi- | consider and extract the events that may trigger at least |  |  |
| ties, | MessagePopup | and | ComposeMessageActivity | . The new | one instruction of the set, as well as the possible prerequi- |
| message is handled in the | onReceive() | method of | PushRe- | sites of these events. In this way, the event search scope can |  |
| ceiver | that starts up the activity | MessagePopup | , and the | be greatly limited to those related events instead of massive |  |
| message is displayed in the foreground on which a user can | irrelevant events while code coverage is guaranteed. We con- |  |  |  |  |
| click the FORWARD button to invoke the | forward() | method | struct an event-space constraint graph aided by static anal- |  |  |
| that starts up the activity | ComposeMessageActivity | . On the | ysis, and it facilitates symbolic execution in | nding possible |  |
| next user interface, the user can click the SEND button to | sequences of events that are used to reproduce the transmis- |  |  |  |  |
| invoke the | sendMessage() | method to have the message for- | sion. |  |  |
| warded. | In the following, we | rst give a de nition of this special |  |  |  |
| In our symbolic execution, we | rst use static taint analy- | graph, and then explain how to obtain this graph by static |  |  |  |
| sis to identify all possible transmission paths, and then we | program analysis. |  |  |  |  |

---

## Page 5

PushReceiver MessagePopup ComposeMessageActivity

OnReceive() OnStart() OnNewIntent() OnClick() OnClick()

startNewMessa

gesQuery()

I1: a=intent.getByteArrayExtra(s); I2: b=a.abytes; case v1:

intent1 =

}

Figure 3: A simpli ed SMS forwarding case.

dence for two adjacent nodes. Edges can be calculated ac-

together.

Basically, for the graph, we ensure:

 All critical events should be included.

 All lifecycle callbacks of an activity that contains a

critical event should be included.

 Any event belonging to a prerequisite component that

eventually starts up an activity containing a critical

event should be included, as well as its lifecycle call-

backs.

 No edge violates the prede ned order of the lifecycle

state transition or the sequence of the call graph.

| forward() | sendMessage() |
| --- | --- |
| switch(view) { | switch(view){ |

case v2:

I5: c = intent.getExtra("sms_body");

| ComposeMessageActivity.createIntent(this, l); | I6: addMessageToUri(c) |
| --- | --- |
| I3: intent1.putExtra("sms_body", b); | } |

I4: startActivity(intent1);

So far, we get all the critical events that contain the in-

structions of the given transmission path, but they are just

the critical interior nodes to symbolically execute the path.

According to the Android runtime execution model, we also

need to collect the essential events that are the prerequisites

to the critical nodes, in order to behave well during sym-

bolic execution. For example, an execution can not directly

invoke OnResume() before the app is activated by invoking

OnCreate() and OnStart() in sequence. Actually, an app

strictly follows the state transition order of the app lifecy-

cle, as illustrated in Figure 1. For each critical event of a

component, we rst supplement those missing lifecycle call-

| OnReceive | (): | startNewMessagesQuery | (): | forward | (v): | sendMessage | (v): |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.3 | Construction of the Event-space Constraint | ical events, | < | PushReceiver | , | onReceive | > | , | < | MessagePopup | , |
| Graph | OnStart | j | OnNewIntent | > | , | < | MessagePopup | , | OnClick | > | , and |
| As depicted in Figure 4, the event-space constraint graph | < | ComposeMessageActivity | , | OnClick | > | . |  |  |  |  |  |
| is a directed graph, with each node in the graph representing | An activity may have different views to lay out various |  |  |  |  |  |  |  |  |  |  |
| a lifecycle callback, a GUI event, or a system event. There | user controls (e.g. buttons), on which a user interacts with |  |  |  |  |  |  |  |  |  |  |
| are two kinds of nodes: | the app, and user interactions of various views are usually |  |  |  |  |  |  |  |  |  |  |
|  | A thick-line node represents an event of which the | handled by the same handler method. | The above critical |  |  |  |  |  |  |  |  |
| event handler method contains at least one instruc- | events that we have extracted are from only the call graph |  |  |  |  |  |  |  |  |  |  |
| tion of a given data propagation path. | We call this | and does not have the information about views except the |  |  |  |  |  |  |  |  |  |
| kind of events | critical events | . | handler methods. | It poses a difficulty for the later guided |  |  |  |  |  |  |  |
|  | A thin-line node represents an event which is a prereq- | symbolic execution. To solve this issue, we build a program |  |  |  |  |  |  |  |  |  |
| uisite for a critical event, and it does not contain any | dependency graph, extract branch conditions for view pa- |  |  |  |  |  |  |  |  |  |  |
| instructions of the given path. | Such an event could | rameters from the graph, and annotate the critical events |  |  |  |  |  |  |  |  |  |
| be either a lifecycle callback of the activity that con- | with these conditions as the context information. | As de- |  |  |  |  |  |  |  |  |  |
| tains this critical event, or an event belonging to any | picted in Figure 3, the extracted branch condition for i3 |  |  |  |  |  |  |  |  |  |  |
| prerequisite component that eventually starts up the | and i4 is | view==v1 | . | After that, if we | nd that a critical |  |  |  |  |  |  |
| activity that contains this critical event. We call this | event involves different views, we divide this event into sev- |  |  |  |  |  |  |  |  |  |  |
| kind of events | essential events | . | eral thick-line nodes, with respect to each view. Other GUI |  |  |  |  |  |  |  |  |
| A directed edge in the graph represents the order of prece- | events are handled in a similar way. |  |  |  |  |  |  |  |  |  |  |
| cording to the lifecycle state transition and the call graph | 4.3.2 | Extracting Essential Events |  |  |  |  |  |  |  |  |  |
| 4.3.1 | Extracting Critical Events | backs with directed edges according to the origin order. And |  |  |  |  |  |  |  |  |  |
| To build the the event-space constraint graph, | rst of all, | then, aided by the call graph, we supplement all prerequi- |  |  |  |  |  |  |  |  |  |
| we need to extract all critical events according to the given | site components that eventually start up the activity which |  |  |  |  |  |  |  |  |  |  |
| data transmission path. For each instruction in the path, we | contains a critical event, as well as edges produced accord- |  |  |  |  |  |  |  |  |  |  |
| backward traverse the call graph to | nd all events that might | ing the call graph. | Meanwhile, the corresponding lifecycle |  |  |  |  |  |  |  |  |
| trigger it. As shown in Figure 3, backward traversing the call | callbacks of these prerequisite components are added in. In |  |  |  |  |  |  |  |  |  |  |
| graph from instruction 2 (i2), we can get two critical events, | Android, inter-component communications are implemented |  |  |  |  |  |  |  |  |  |  |
| OnStart() | and | OnNewIntent() | . | We may introduce some | through | Intents | . | Thus, if a component receives an intent |  |  |  |
| false positives due to the limitation of static analysis tech- | from another one, we treat the sender of the intent as the |  |  |  |  |  |  |  |  |  |  |
| niques, but symbolic execution can eliminate these false pos- | prerequisite of the receiver component, and add a directed |  |  |  |  |  |  |  |  |  |  |
| itives later. In this phase, we | nally obtain sequenced crit- | edge to represent their order. Especially, if an intent is used |  |  |  |  |  |  |  |  |  |

---

## Page 6

Critical Event Chain

OnReceive()

OnReceive()

MessagePopup

OnCreate() OnStart() OnResume()

OnRestart()

OnCreate() OnStart() OnResume()

OnRestart()

ComposeMessageActivity

Figure 4: The extracted event-space constraint graph of the given example.

to start a new activity or service, the onCreate() callback of

created component is marked as the receiver of the intent. In

the current version of AppIntent, we only track intents that

eventually start a new activity or service, as well as broad-

cast messages that are properly handled by a BroadcastRe-

ceiver , because they are officially documented by Google [2]

vision could be handled in a similar way) are left to future

cluding the critical and the essential events, have been ex-

traverse this graph for sequenced events that possibly trig-

ger the transmission and veri es whether it is a valid path.

Since massive irrelevant events have been ltered out, the

search scope is greatly reduced while the code coverage is

guaranteed well.

We now explain how to traverse the above constructed

graph to derive all possible sequenced events as the guide-

line to symbolic execution. The process of guided symbolic

ful lled to reach the current execution point. If C is empty,

then none of the data inputs can result in the target exe-

cution, i.e., the path can never be covered in any program

execution.

Algorithm 1 works as follows. Our symbolic execution tra-

verses the event-space constraint graph using the thick-line

nodes as step stones. Each time when we proceed from a

MessagePopup:

OnStart()

OnClick(v1) OnClick(v2)

MessagePopup:

OnNewIntent()

OnNewIntent() OnPause() OnStop() OnDestory()

OnClick(v1)

| OnClick(v2) | OnPause() | OnStop() | OnDestory() |  |
| --- | --- | --- | --- | --- |
| C | ∅ | , | P | ∅ |
| P | P |  | mp |  |

Output: C as Data Constraint, P as Event

Inputs

exit()

end

else if C != ∅ then

TraverseGraph( ne )

end

P P   mp

end

end

Execution

| PushReceiver | PushReceiver: | MessagePopup: | ComposeMessageActivity: |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| and most of the apps use these two approaches to send in- | G | Event-space Constraint Graph |  |  |  |  |  |  |  |
| tents. The intents with undocumented usage (which we en- | CEC | Critical Events Chain of | G |  |  |  |  |  |  |
| work. The supplemental process will not end until there is | StartP oint | App Entrance of the Main Activity |  |  |  |  |  |  |  |
| no any prerequisite components found. | Procedure | TraverseGraph( | ce | ) |  |  |  |  |  |
| Upon | nishing the above steps, we | nish constructing the | forall the | ne | : | < ce, ne > | 2 | CEC | do |
| event-space constraint graph. | As noted earlier in this sec- | mp | FindMinimalPath( | ce | , | ne | , | G | ) |
| tion, for a given transmission path, all related events, in- | C | SymbolicExecute Forward( | C | , | mp | ) |  |  |  |
| tracted. | The subsequent symbolic execution only needs to | if | 8 | e | : | < ne, e > / | 2 | CEC | then |
| 4.4 | Guided Symbolic Execution | C | SymbolicExecute Rollback( | C | , | mp | ) |  |  |
| execution is depicted in Algorithm 1, in which | P | represents | TraverseGraph | ( | StartP oint | ) |  |  |  |
| the events that are triggered before the last traversed critical | Output: | No feasible inputs found |  |  |  |  |  |  |  |
| event, and | C | represents the data constraints that should be | Algorithm 1: | Event-space Constraint Guided Symbolic |  |  |  |  |  |

---

## Page 7

| thick-line node, possible successors of this critical event are | responding text | eld with the expected value. | Some |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| extracted from the event-space constraint graph. Since any | app inputs are messages from system or other apps, |  |  |  |  |  |  |  |  |  |  |  |  |
| of the successors can be the next critical event, we randomly | so we can attach these inputs to corresponding event |  |  |  |  |  |  |  |  |  |  |  |  |
| pick an event | rst and calculate a feasible path from the cur- | messages. Besides, some apps trigger speci c behavior |  |  |  |  |  |  |  |  |  |  |  |
| rent critical event to the chosen successor. | Since only the | based on the wall time of the Android system. | For |  |  |  |  |  |  |  |  |  |  |
| essential prerequisites are needed, we extract the minimal | example, some malicious behavior happens only if a |  |  |  |  |  |  |  |  |  |  |  |  |
| path (using the Dijistra's algorithm) as a chain of events, | certain amount of time passed in the current execu- |  |  |  |  |  |  |  |  |  |  |  |  |
| which are sequentially triggered in the symbolic execution. | tion. | We explicitly generate sleep operations if data |  |  |  |  |  |  |  |  |  |  |  |
| If the event chain is revealed to be not available to any in- | constraint relies on the current system time. | In the |  |  |  |  |  |  |  |  |  |  |  |
| puts ( | C | == | ∅ | ), or all possible successors in critical event | current version of AppIntent, we do not support net- |  |  |  |  |  |  |  |  |
| chains are already explored ( | 8 | e | : | < ne, e > / | 2 | CEC | ), we | work inputs because we generate test cases through |  |  |  |  |  |
| rollback the symbolic execution and try to trigger other fea- | Android | InstrumentationTestRunner | [1], which can- |  |  |  |  |  |  |  |  |  |  |
| sible critical events. | not intercept and modify network inputs. This could |  |  |  |  |  |  |  |  |  |  |  |  |
| Using Figure 4 as an example, guided by the event-space | be improved by hooking the network interfaces in the |  |  |  |  |  |  |  |  |  |  |  |  |
| constraint graph, our symbolic execution explores a much | Android framework, which is our future work. |  |  |  |  |  |  |  |  |  |  |  |  |
| smaller event space, as illustrated in Figure 5, and reports |  | Highlight activated views of GUI events | . | Activated |  |  |  |  |  |  |  |  |  |
| the following event chain as event inputs: | f | < | PushReceiver | , | view of each GUI event provides essential context, which |  |  |  |  |  |  |  |  |
| OnReceive | > | , | < | MessagePopup | , | OnCreate | > | , | < | MessagePopup | , | represents a GUI element on the screen, for each user |  |
| OnStart | > | , | < | MessagePopup | , | OnResume | > | , | < | MessagePopup | , | interaction. | For example, if a clicking event is trig- |
| OnClick | (v1) | > | , | < | ComposeMessageActivity | , | OnCreate | > | , | < | gered, we need to know what element on the user in- |  |  |
| ComposeMessageActivity | , | OnStart | > | , | < | ComposeMessage- | terface is clicked by user. Thus, AppIntent highlights |  |  |  |  |  |  |
| Activity | , | OnResume | > | , | < | ComposeMessageActivity | , | OnClick | (v2) | > | GUI element by setting its background color to red, |  |  |
| g | . | In addition, by using a modi ed version of | choco | data | as depicted in Figure 7(a) and Figure 7(b). | For GUI |  |  |  |  |  |  |  |
| constraint solver [6], we generate corresponding data inputs | elements whose view cannot be obtained by Android |  |  |  |  |  |  |  |  |  |  |  |  |
| according to the data constraints calculated in the symbolic | InstrumentationTestRunner | , e.g., the list items, we |  |  |  |  |  |  |  |  |  |  |  |
| execution. | highlight these elements by triggering some dialog box |  |  |  |  |  |  |  |  |  |  |  |  |

By using our event-space constraint guided symbolic exe-

cution, we can extract app inputs to trigger a given sensitive

data transmission path. Although these inputs provide all

the preconditions of target data transmission, they might

not be intuitive enough for human to understand. To display

these preconditions in an easy-to-understand manner, we set

up a dynamic analysis platform to present which function-

ality is used when the transmission happens. With the help

pIntent currently does not support runtime events like

of each step.

to display the view information.

ure out whether the functionality of the app requires

sensitive data transmission, our controlled execution

needs to reveal when the data loading and transmission

happen during the presented event chain. We highlight

these two execution points by raising a noti cation di-

alog box, as depicted in Figure 7(c) and Figure 7(d).

6. EVALUATION

user-intended one?

| 5. | DYNAMIC ANALYSIS PLATFORM |  | Highlight sensitive data read and transmission | . To | g- |
| --- | --- | --- | --- | --- | --- |
| of Android | InstrumentationTestRunner | [1], a driven exe- | In the implementation of AppIntent, we | rst leverage DED |  |
| cution can be conducted for each sensitive data transmission | [23] to decompile Android DEX | les into Java bytecode. We |  |  |  |
| path. AppIntent automatically generates a test case based | implement our event-space constraint graph extraction on |  |  |  |  |
| on the inputs gathered before, and attaches it to the app by | top of soot [8] and the guided symbolic execution engine on |  |  |  |  |
| repackaging the original Android apk. Then, by running the | top of JavaPath nder [10]. | We implement the controlled |  |  |  |
| test case though the Android activity manager, a controlled | execution and dynamic analysis platform on top of | Instru- |  |  |  |
| execution with the following features are presented: | mentationTestRunner | [1]. | In this section, we present our |  |  |
|  | Automatically trigger Event Inputs | . Events in the event | evaluation results on the effectiveness and accuracy of Ap- |  |  |
| chain are automatically triggered by performing corre- | pIntent. In our evaluation, the event-space constraint guided |  |  |  |  |
| sponding operations. For example, to trigger a clicking | symbolic execution uses an Intel Xeon machine with 2 eight- |  |  |  |  |
| event, a | performClick | operation is applied to the cor- | core 2.0Ghz CPUs and 32 GB physical memory, which runs |  |  |
| responding view, and we call the | setTestProvider- | Debian Linux with kernel version 2.6.32. The controlled ex- |  |  |  |
| Location | method for a location change event. | Ap- | ecution of AppIntent is run on Android 2.3. |  |  |
| phone call events because Android | Instrumentation- | 6.1 | Evaluation Methodology |  |  |
| TestRunner | does not support them. | Since in most | In order to evaluate the effectiveness of AppIntent and its |  |  |
| cases, view context of each event is already attached | key techniques, we need to answer the following two ques- |  |  |  |  |
| to the event chain, we can use the attached context | tions: (i) When producing app inputs leading to some sensi- |  |  |  |  |
| directly for GUI events. On the other hand, if there is | tive data transmission, to what extent does event-space con- |  |  |  |  |
| no view constraint, we randomly pick a view from the | straint guided symbolic execution reduce the search space |  |  |  |  |
| manifest | le as the context of event. In addition, be- | while guaranteeing the code coverage? | (ii) Using the con- |  |  |
| tween each two GUI events, we generate a short delay | trolled execution based on app inputs, how effective is Ap- |  |  |  |  |
| so that analysts have time to observe the GUI display | pIntent to distinguish unintended data transmission with |  |  |  |  |
|  | Automatically provide Data Inputs | . | Most of the data | In the following, we evaluate the execution time of sym- |  |
| inputs generated by symbolic execution are text in- | bolic execution with or without our technique to answer the |  |  |  |  |
| puts to GUI elements, and we directly set the cor- | rst question and use two sets of real-world Android apps |  |  |  |  |

---

## Page 8

5: rollback

| PushReceiver | MessagePopup |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |  |
| OnReceive() | OnCreate() | OnStart() | OnResume() | OnNewIntent() |

MessagePopup

6

7 8 9

OnCreate() OnStart() OnResume() OnClick(v1)

Figure 5: Event chains explored in symbolic execution by traversing the graph in Figure 4

To illustrate the effect of event-space constraint guided

| Maps | 5.43 | > | 120 | 0.40 |
| --- | --- | --- | --- | --- |
| Youlu | 0.97 | > | 120 | 0.13 |
| WeChat | 21.56 | > | 120 | 1.33 |

Table 1: Running time of symbolic execution. Column 2 and

3 represent the running time when symbolic execution ex-

plores ten or twenty triggered events without the help of our

event-space constraint guided symbolic execution. Column

4 shows the execution time of AppIntent.

6.3 Effectiveness on Analyzing Sensitive Data

Transmission

from Google Play. To compare with state-of-the-art pri-

ComposeMessageActivity

| 10 | 11 | 12 | 13 |
| --- | --- | --- | --- |
| OnCreate() | OnStart() | OnResume() | OnClick(v2) |

we perform manual analysis, in which we not only check

contain sensitive transmission.

ti ed as unintended data transmission. We notice that the

age of SMS and contacts are all found in SNS apps. On the

other side, malware may also contain both user intended and

non-intended transmission, because malicious data leakage

can hide behind some normal data transmission to bypass

the state-of-the-art security validations. For example, we

found that an application acts like an SNS app in disguise,

but in the background, it stealthily transmits user contacts

without user consent. It is worth noting that the current

version of AppIntent failed to execute test cases of 43 apps

because they are driven by network input, which is not sup-

ported by InstrumentationTestRunner . This could be fur-

ther supported by instrumenting control code in Android

framework.

| to answer the second one. | Besides, we provide some | nd- | vacy leakage approaches, we evaluate the same test datasets |
| --- | --- | --- | --- |
| ings about sensitive data transmission patterns which are | with TaintDroid [22] driven by MonkeyRunner. The results |  |  |
| revealed by the result of AppIntent. | are depicted in Table 2. To verify the result of AppIntent, |  |  |

6.2 Effectiveness of Event-space Constraint Guided whether apps reported by AppIntent transmit sensitive data,

| Symbolic Execution | but also verify whether apps eliminated by AppIntent do not |  |  |  |
| --- | --- | --- | --- | --- |
| symbolic execution, we choose 3 famous apps from Google | As from the table, static taint analysis (the | rst step of |  |  |
| Play as samples. | Among them, Maps is the Google map, | AppIntent) detects 582 (442+140) cases of possible sensi- |  |  |
| Youlu is an SMS management app, | and WeChat (a.k.a. | tive data transmission from two datasets. We | nd that 164 |  |
| Weixin) is a popular chatting tool. As presented in Table 1, | cases are false positives, which are eliminated by the next |  |  |  |
| without the help of event-space constraint graph, symbolic | step of AppIntent, guided symbolic execution. With a man- |  |  |  |
| execution cannot | nish in 5 days when we explore only 20 | ual analysis of the code of these programs, we | nd that most |  |
| triggered events for the target app. | This clearly demon- | false positives in static analysis are caused by the insufficient |  |  |
| strates that exhaustively exploring event space is not scal- | context information and dead code, such as debugging code |  |  |  |
| able and practical. On the other hand, symbolic execution | wrapped by | if(debug) | branches. There are another 44 cases |  |
| cannot cover the critical events in | WeChat | in this con gu- | from static analysis that failed to pass our symbolic execu- |  |
| ration, and failed to cover critical events in two cases( | Youlu | tion. A further investigation shows that DED is unable to |  |  |
| and | WeChat | ) if we lower the threshold to 10 events. | This | transform 42 cases from dex format to Java class le, and |
| means that naively limiting the search space can damage | the other two cases contain native code that currently can- |  |  |  |
| the effectiveness of symbolic execution. However, guided by | not be handled by AppIntent. To check whether the app in- |  |  |  |
| event-space constraint graph, normally less than two hours | puts generated by symbolic execution trigger sensitive data |  |  |  |
| are needed to explore the limited exploration space, and ex- | transmission, we applied manual analysis on the result of |  |  |  |
| tract app inputs corresponding to the sensitive data trans- | symbolic execution, and found that all cases transmit sensi- |  |  |  |
| mission, without sacri cing the code coverage. | Thus, it is | tive data de ned in this paper. |  |  |
| clear that compared to existing approaches, guided symbolic | With the app inputs extracted in symbolic execution, Ap- |  |  |  |
| execution proposed in this paper can greatly increase the ex- | pIntent successfully generates controlled executions for 358 |  |  |  |
| ploration effectiveness. | (288+70) apps, among which, 245 (219+26) have been iden- |  |  |  |
| Case | Origin | Origin | AppIntent | top free apps still have user unintended leakages, among |
| (10 events) | (20 events) | (hours) | which most apps are SNS (Social Networking Service) apps |  |
| (hours) | (hours) | or apps that have embedded advertising modules. The leak- |  |  |
| In this experiment, two sets of real-world Android apps | As a comparison, TaintDroid can only detect 165 (125+40) |  |  |  |
| are selected to evaluate the effectiveness of AppIntent. The | cases as possible privacy leakage, most of which are leakage |  |  |  |
| rst set contains 750 malware apps from [46], which are | of device IDs. This is much less than AppIntent. Further- |  |  |  |
| known to perform malicious activities such as information | more, the result of TaintDroid is hard to verify because it |  |  |  |
| leakage, money stealing, and privilege escalation. The sec- | does not contain corresponding app inputs. | Through our |  |  |
| ond set contains 1,000 top free Android apps downloaded | manual investigation, among these cases, 151 cases are also |  |  |  |

---

## Page 9

| Malicious Apps | Google Play Apps |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Source | AppIntent | Unintended/ | Local | TaintDroid | AppIntent | Unintended/ | Local | TaintDroid |
| (Static/ | Intended | Logging | (Static/ | Intended | Logging |  |  |  |
| Symbolic/ | Data | Symbolic/ | Data |  |  |  |  |  |
| Controlled | Transmission | Controlled | Transmission |  |  |  |  |  |
| Execution) | Execution) |  |  |  |  |  |  |  |
| Device | 389/256/ | 198/0 | 73 | 101 | 98/43/43 | 24/0 | 19 | 37 |
| ID | 246 |  |  |  |  |  |  |  |
| Phone | 53/50/50 | 50/0 | 1 | 0 | 0/0/0 | 0/0 | 0 | 19 |

Info

| Location | 76/68/67 | 46/4 | 18 | 11 | 36/15/15 | 0/13 | 2 | 5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contacts | 13/13/13 | 1/10 | 2 | 0 | 10/10/10 | 1/9 | 1 | 3 |
| SMS | 27/27/17 | 16/3 | 0 | 0 | 9/8/8 | 1/7 | 0 | 0 |
| Total | 442/304/288 | 219/17 | 74 | 125 | 140/70/70 | 26/29 | 22 | 40 |

Table 2: Sensitive data transmission apps detected. The rst part depicts the results of the chosen malware, and the second

part are results of apps from Google Play. For each dataset, the rst column represents the type of sensitive data transmitted,

while Column 2 depicts the reported data transmission cases after each phase of AppIntent. Column 3 presents the number of

data transmission of each kind. Column 4 depicts the number of sensitive data written to the local logging system. Column

5 lists the number of possible leakage cases detected by TaintDroid.

| covered by AppIntent while 14 cases not. | We manually | analysis time is almost negligible to the Android market op- |
| --- | --- | --- |
| checked the code of ten apps reported by TaintDroid but | erators. |  |
| not reported in AppIntent, and found that nine of them do | Our symbolic execution costs 5 to 134 minutes to verify a |  |
| not actually leak privacy information. | The remaining four | certain path reported by static analysis, depending on the |
| cases either failed in DED, or contain native code that is not | search space and the complexity of the app. Verifying differ- |  |
| covered by AppIntent. In the 151 cases that are reported by | ent paths can also be processed in parallel because exploring |  |
| both AppIntent and TaintDroid, 20 cases are actually classi- | the possible search space of each sensitive data transmission |  |
| ed as user-intended data transmission by AppIntent, which | path does not depend on information of other paths. As an |  |
| means they are not true privacy leakage. Since TaintDoird | offline analysis tool, such a validation time is also acceptable |  |
| does not provide corresponding app input to trigger the sen- | to the marketplaces that have enough computing power. |  |

sitive data transmission, it cannot distinguish user-intended

| data transmission from unintended one. | 6.5 | Case Studies |  |  |  |
| --- | --- | --- | --- | --- | --- |
| In addition, we also have several interesting | ndings: | We now present two case studies from our evaluation: |  |  |  |
| Finding 1: | Data transmission of device IDs and phone | one represents user-intended data transmission ( | Anzhuod- |  |  |
| numbers are very common but typically not noticed by most | uanxin | ) and the other represents unintended transmission |  |  |  |
| smartphone users. | Among the detected unintended data | ( | Tapsnake | ). | Video demonstrations of AppIntent for both |
| transmission in the two selected datasets, most cases are | cases are available at [4, 5]. |  |  |  |  |
| transmission of device IDs or phone numbers. We also no- | Anzhuoduanxin | [3] is an SMS management app that pro- |  |  |  |
| tice that almost all data transmission cases of device IDs | vides a set of SMS-related functions such as creating new |  |  |  |  |
| and phone numbers do not inform users the operation. We | messages or forwarding a cached message to another user. |  |  |  |  |
| believe that it occurs because Android apps use such infor- | With the help of our event-space constraint guided symbolic |  |  |  |  |
| mation as the unique user identi er when connected to their | execution, AppIntent generates two feasible app inputs that |  |  |  |  |
| own server. | trigger sensitive SMS data transmission: Figure 6(a) depicts |  |  |  |  |
| Finding 2: Lots of apps write sensitive data into local log- | one of the feasible inputs, and a simpli ed version of the |  |  |  |  |
| ging system. | Among the tested datasets, 96 (74+22) apps | other is depicted in Figure 5. Without loss of generality, we |  |  |  |
| log sensitive data into local logging system, which is bad | choose the | rst one to illustrate here. |  |  |  |
| practice and may lead to indirect privacy leakage. Addition- | Our dynamic analysis platform accepts this input and cre- |  |  |  |  |
| ally, we | nd that not only device IDs and phone numbers | ates an execution as demonstrated in the video [4]. In this |  |  |  |
| are written to Android logs, but also locations and user con- | case, the controlled execution | rst selects a record among |  |  |  |
| tacts are temporally stored in several cases. | These logged | the list which represents all conversation records stored in |  |  |  |
| data can be leveraged by malicious apps that steal Android | this phone. Then, by choosing a message and clicking a but- |  |  |  |  |
| log instead of transmitting sensitive data directly. | Since | ton that presents "forward" in Chinese (Figure 7(a)), the app |  |  |  |
| privacy leakage detection approaches do not cover leakage | user can forward this message to someone else. | This mes- |  |  |  |
| of local logging, such apps could bypass existing detection | sage can be sent to anyone by typing a named receiver and |  |  |  |  |
| tools. | clicking a button titled "send"(Figure 7(b) and Figure 7(c)). |  |  |  |  |

This execution is commonly used for forwarding a stored

message to a friend of the app user, thus it should not be

| 6.4 | Analysis Time | classi ed as malicious/unintended behavior. |
| --- | --- | --- |
| Our static analysis phase costs 96 hours to analyze all | Tapsnake | is a malicious app that stealthily transmits user |
| 1,750 apps, among which 70 hours are used in static taint | locations to a prede ned third party receiver. | Depicted in |
| analysis. The analysis time can be further reduced by dis- | Figure 6(b), the app input generated by AppIntent shows |  |
| tributing the analysis workload to multiple machines. Since | that two components are activated when the location infor- |  |
| each application costs about 3.3 minutes on average, the | mation is transmitted to a third-party user in Tapsnake: the |  |

---

## Page 10

Figure 7: Screen shots of case studies.

ConversationList After that, participants were asked to ll a sheet in which

OnCreate() OnStart() OnResume() onItemClick()

v1==0x7f02011c

v2.getText==1000000

| OnCreate() | OnStart() | OnResume() | onOptionsItem |
| --- | --- | --- | --- |
| Selected() | onClick(v1) |  |  |
| OnCreate() | OnCreate() | onLocationC |  |

Figure 6: Feasible app inputs for sensitive data transmission

in case studies.

main activity of this app, and an embedded Service which

each case should be classi ed as "user-intended" or "unin-

tended". We nd that they can make their decision in less

than one minute after the driven execution nishes, which

dating Android apps.

The results from these three users are unambiguously the

IMEI number to ful ll their functionality, while we classi ed

direct relation between the data transmission and the user

experience. This evaluation shows that AppIntent is still a

great assistance tool with high usability in practice. And it

certainly also has some room to be improved in the future.

cannot separate user-intended operations from unintended

| ComposeMessageActivity | menuitem==0x15 | v2==7f020106 | shows that AppIntent greatly speeds up the process in vali- |
| --- | --- | --- | --- |
| (a) | same as our judgement in 98 cases. However, there are some |  |  |
| location.getTime >= | different opinions in two cases, which are both data trans- |  |  |
| Snake | SnakeService | 0xdbba0 | mission of IMEI. Two out of three expects classi ed them |
| hanged() | into user-intended because they think these apps need the |  |  |
| (b) | them as unintended data transmission because there is no |  |  |
| registers an event listener for location change event. Based | 7. | RELATED WORK |  |
| on this input, the corresponding execution, demonstrated | AppIntent seems to be the | rst to systematically study |  |
| in the video [5], waits until the current time is greater than | a method to separate user-intended Android data transmis- |  |  |
| 0xdbba0 (which represents 15 minutes from the beginning of | sion from unintended ones. All other existing Android pri- |  |  |
| the wall time) Then, the location information is sent after a | vacy leakage detection approaches only detect sensitive data |  |  |
| location change event is performed (Figure 7(d)). Since the | transmission. Static Taint Analysis [21, 40] focuses on iden- |  |  |
| original application is a simple "snake" video game, and its | tifying the possible privacy leakage path with the help of |  |  |
| functionality does not depend on the location information, | reachability analysis and program slicing. | However, these |  |
| thus this behavior is unintended. | approaches commonly introduce a lot of false positives and |  |  |
| 6.6 | Usability of AppIntent | ones because of lacking user intention and context infor- |  |
| To evaluate how useful the information provided by Ap- | mation. | On the other side, Dynamic Taint Tracking tech- |  |
| pIntent is, we randomly selected 100 cases reported, and | niques [22, 41] track the sensitive data at runtime by in- |  |  |
| used them to evaluate the user experience. Since AppIntent | strumenting pro ling code to the original app code. | They |  |
| mainly focuses on providing enough information for discrimi- | cannot be applied to automatically detect privacy leakages |  |  |
| nating user-intended data transmission from unintended one | in marketplaces because they report leakage only if such |  |  |
| at app markets, we invited three Android experts in our us- | dangerous propagation happens to occur in the execution. |  |  |
| ability study. | During the evaluation, we | rst introduced | While not implemented, Vision [26] argues that user grant- |
| AppIntent to them with less than 15 minutes, and let them | ing of sensitive data usage can be represented by End-user |  |  |
| get familiar with the given cases. Then, we ran the driven | license agreements(EULA) and explicit noti cation during |  |  |
| executions generated by AppIntent in our Samsung Nexus | the execution. | Similarly, BLADE [32] detects web drive- |  |
| S mobile phone and showed them to all three participants. | by download malware by recognizing whether it has user |  |  |

*[Image: Page 10 Image]*

---

## Page 11

| consent or not. | However, mobile apps commonly do not | the help of event-space constraint guided symbolic execu- |  |
| --- | --- | --- | --- |
| provide EULA or noti cation even if the data transmission | tion technique proposed in this paper, the search space of |  |  |
| is user-intended (e.g. | SMS forwarding). | Pegasus [18] de- | symbolic execution is effectively bounded so that AppIntent |
| tects malicious behaviors that can be characterized by the | can extract app inputs that represent user interactions in an |  |  |
| temporal order in which an application uses APIs and per- | acceptable amount of time. | With the help of the dynamic |  |
| missions, and similar to this paper, it focuses on detecting | analysis platform, AppIntent can also intuitively display the |  |  |
| malicious app behaviors that are inconsistent with the GUI | context information of the sensitive data transmission. |  |  |
| events. Nevertheless, privacy leakages cannot be modeled as | Our current techniques have the following limitations, which |  |  |
| app usage of permissions or APIs, thus many privacy leak- | are also our future work. First, native code is currently not |  |  |
| ages cannot be detected by such approach. | Besides, Pega- | supported by AppIntent. | Thus, privacy leakages in native |
| sus veri es program behaviors based on application-speci c | code cannot be captured. | Second, since the Android | In- |
| properties, which are difficult to specify without the knowl- | strumentationTestRunner | [1] does not support instrumen- |  |
| edge of application code. Recently, VetDroid [44] enhances | tation of network input, our dynamic analysis platform can- |  |  |
| Dynamic Taint Tracking by generating speci cations for sen- | not simulate network inputs generated by symbolic execu- |  |  |
| sitive operations. However, the speci cation mainly focuses | tion. This could be solved by instrumenting code in Android |  |  |
| on the application logic but does not pay attention to the | network interface. Finally, AppIntent fails to analyze some |  |  |
| trigger condition of each operation. | apps because the DEX decompilation tool, DED [23], failed |  |  |
| AppIntent needs to extract app inputs to distinguish user- | to decompile these apps. We plan to use Dexpler [12], which |  |  |
| intended data transmission from unintended one. | Smart- | can directly parse DEX | les, in soot, so that the decompi- |
| Droid [45] proposes a hybrid static and dynamic analysis | lation from DEX to Java bytecode is not needed. |  |  |

method to reveal UI-based event trigger conditions based

on sensitive Android APIs. However, in order to generate

a reproducible driven execution, we need both event inputs

iting the event space. In order to limit the search space,

Ganov, et.al [25] set an upper bound to the number of event

sequences generated, Kudzu [38] used a random generated

event order, and Ganov, et.al [24] proposed to generate test

cases by symbolically executing each event handler sepa-

rately. Although these features can limit the exploration of

event space, they greatly sacri ce the code coverage. Con-

droid apps. Unlike previous approaches that simply consider

Acknowledgments

der Grant no. CNS-0954096.

9. REFERENCES

[1] Android instrumentationtestrunner. http://develop-

er.android.com/reference/android/test/Instrumenta-

tionTestRunner.html.

[8] soot analysis framework.

Proc. FSE , 2012.

| and data inputs. In this sense, AppIntent provides a more | We thank the anonymous reviewers for their insightful com- |  |  |
| --- | --- | --- | --- |
| complete and systematic approach. Besides, instead of An- | ments, and ChenHao Qu for his assistance in experiments. |  |  |
| droid APIs, we need | ner-grained analysis of app behav- | This work is funded by China National Natural Science |  |
| iors to detect privacy leakages. AppIntent proposes a sym- | Foundation under grants numbered 61103078 and 61300027, |  |  |
| bolic execution approach for Android GUI apps to extract | grants from the Science and Technology Commission of Shang- |  |  |
| inputs. | The search space explosion of symbolic execution | hai Municipality numbered 11DZ2281500, 11511504404, 135- |  |
| is a well-known issue. | Earlier guided symbolic executions | 11504402 and 13JC1400800, a research grant from a joint |  |
| direct the exploration with static analysis result [11, 33, 36, | program between China Ministry of Education and Intel |  |  |
| 37] or pro led program behavior[14, 19, 43]. | All these ap- | numbered MOE-INTEL201202, Fundamental Research Funds |  |
| proaches focus on the explosion caused by the data input | for the Central Universities in China and Shanghai Leading |  |  |
| space, and cannot reduce the search space of runtime events | Academic Discipline Project numbered B114. This work is |  |  |
| in Android. On the other hand, there is little work on lim- | partially supported by the National Science Foundation un- |  |  |
| test [9] seeks to prune redundant event sequences by check- | [2] Android intent. http://developer.android.com- |  |  |
| ing | subsumption conditions | , and can reduce the running time | /reference/android/content/Intent.html. |
| of symbolic execution to 5%-36% of the original execution | [3] anzhuoduanxin. http://dx.91.com/. |  |  |
| time. However, the event space is still large after the prun- | [4] Appintent demo: Anzhuoduanxin. |  |  |
| ing and the path explosion problem still exists. To the best | http://www.youtube.com/watch?v=RRqWQk4ztmI. |  |  |
| of our knowledge, all existing approaches either trade accu- | [5] Appintent demo: Tapsnake. |  |  |
| racy for performance or suffering poor scalability. | In this | http://www.youtube.com/watch?v=L4IvXzpYqzw. |  |
| paper, by using the result of static analysis as the guideline, | [6] Choco data constraint solver. |  |  |
| event-space constraint guided symbolic execution explores | http://www.emn.fr/z-info/choco-solver/. |  |  |
| event space efficiently without sacri cing the accuracy. | [7] Google map. http://www.google.com/mobile/maps/. |  |  |
| 8. | CONCLUSION AND FUTURE WORK | http://www.sable.mcgill.ca/soot/. |  |
| This paper addresses one of the major challenges faced by | [9] S. Anand, M. Naik, H. Yang, and M. J. Harrold. |  |  |
| smartphone markets - how to detect privacy leakage in An- | Automated concolic testing of smartphone apps. In |  |  |
| the transmission of private data as privacy leakage, we ar- | [10] S. Anand, C. S. Pasareanu, and W. Visser. Jpf-se: A |  |  |
| gue that such transmission may not indicate a true privacy | symbolic execution extension to java path nder. In |  |  |
| leakage, instead, a better indicator should be whether the | TACAS 2007 | , pages 134{138, 2007. |  |
| transmission is user intended or not. We present AppIntent, | [11] D. Babic, L. Martignoni, S. McCamant, and D. Song. |  |  |
| a new app validation framework to help human analysts de- | Statically-directed dynamic automated test |  |  |
| termine if data transmission is intended by the user. With | generation. In | Proc. ISSTA | , pages 12{22, 2011. |

---

## Page 12

| [12] A. Bartel, J. Klein, Y. Le Traon, and M. Monperrus. | [30] P. Hornyack, S. Han, J. Jung, S. Schechter, and |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Dexpler: converting android dalvik bytecode to jimple | D. Wetherall. These aren't the droids you're looking |  |  |  |  |
| for static analysis with soot. In | Proc. SOAP | , 2012. | for: retro tting android to protect data from |  |  |
| [13] P. Bisht, T. Hinrichs, N. Skrupsky, and V. N. | imperious applications. In | CCS | , pages 639{652, 2011. |  |  |
| Venkatakrishnan. Waptec: whitebox analysis of web | [31] A. Kieyzun, P. J. Guo, K. Jayaraman, and M. D. |  |  |  |  |
| applications for parameter tampering exploit | Ernst. Automatic creation of sql injection and |  |  |  |  |
| construction. In | CCS | , pages 575{586, 2011. | cross-site scripting attacks. In | ICSE | , pages 199{209, |
| [14] P. Boonstoppel, C. Cadar, and D. R. Engler. Rwset: | 2009. |  |  |  |  |
| Attacking path explosion in constraint-based test | [32] L. Lu, V. Yegneswaran, P. Porras, and W. Lee. Blade: |  |  |  |  |
| generation. In | TACAS | , 2008. | an attack-agnostic approach for preventing drive-by |  |  |
| [15] D. Brumley, J. Newsome, D. Song, H. Wang, and | malware infections. In | Proc. CCS | , pages 440{450, |  |  |
| S. Jha. Towards automatic generation of vulnerability | 2010. |  |  |  |  |
| signatures. In | IEEE Symposium on Security and | [33] K.-K. Ma, K. Y. Phang, J. S. Foster, and M. Hicks. |  |  |  |
| Privacy | , 2006. | Directed symbolic execution. In | Proc. SAS | , 2011. |  |
| [16] C. Cadar, D. Dunbar, and D. R. Engler. Klee: | [34] D. Molnar, X. C. Li, and D. A. Wagner. Dynamic test |  |  |  |  |
| Unassisted and automatic generation of high-coverage | generation to | nd integer bugs in x86 binary linux |  |  |  |
| tests for complex systems programs. In | OSDI | , pages | programs. In | USENIX Security | , pages 67{82, 2009. |
| 209{224, 2008. | [35] G. Patrice, Y. L. Michael, and A. M. David. |  |  |  |  |
| [17] C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, | Automated whitebox fuzz testing. In | NDSS | , 2008. |  |  |
| and D. R. Engler. Exe: automatically generating | [36] N. Rungta, E. G. Mercer, and W. Visser. Efficient |  |  |  |  |
| inputs of death. In | CCS | , pages 322{335, 2006. | testing of concurrent programs with |  |  |
| [18] K. Z. Chen, N. Johnson, V. D'Silva, S. Dai, | abstraction-guided symbolic execution. In | Proc. SPIN | , |  |  |
| K. MacNamara, T. Magrino, E. X. Wu, M. Rinard, | 2009. |  |  |  |  |
| and D. Song. Contextual policy enforcement in | [37] R. Santelices and M. J. Harrold. Exploiting program |  |  |  |  |
| android applications with permission event graphs. In | dependencies for scalable multiple-path symbolic |  |  |  |  |
| Proc. NDSS | , 2013. | execution. In | Proc. ISSTA | , 2010. |  |
| [19] C. Y. Cho, D. Babic, P. Poosankam, K. Z. Chen, | [38] P. Saxena, D. Akhawe, S. Hanna, F. Mao, |  |  |  |  |
| D. Song, and E. X. Wu. Mace: | S. McCamant, and D. Song. A symbolic execution |  |  |  |  |
| Model-inference-assisted concolic exploration for | framework for javascript. | Security and Privacy, IEEE |  |  |  |
| protocol and vulnerability discovery. In | USENIX | Symposium on | , 0:513{528, 2010. |  |  |
| Security | , 2011. | [39] K. Sen, D. Marinov, and G. Agha. Cute: a concolic |  |  |  |
| [20] M. Costa, M. Castro, L. Zhou, L. Zhang, and | unit testing engine for c. In | ESEC/SIGSOFT FSE | , |  |  |
| M. Peinado. Bouncer: securing software by blocking | pages 263{272, 2005. |  |  |  |  |
| bad input. In | SOSP | , pages 117{130, 2007. | [40] O. Tripp, M. Pistoia, S. J. Fink, M. Sridharan, and |  |  |
| [21] M. Egele, C. Kruegel, E. Kirda, and G. Vigna. Pios: | O. Weisman. Taj: effective taint analysis of web |  |  |  |  |
| Detecting privacy leaks in ios applications. In | NDSS | , | applications. In | PLDI | , pages 87{97, 2009. |
| 2011. | [41] N. Vachharajani, M. J. Bridges, J. Chang, R. Rangan, |  |  |  |  |
| [22] W. Enck, P. Gilbert, B.-G. Chun, L. P. Cox, J. Jung, | G. Ottoni, J. A. Blome, G. A. Reis, M. Vachharajani, |  |  |  |  |
| P. McDaniel, and A. N. Sheth. Taintdroid: an | and D. I. August. Ri e: An architectural framework |  |  |  |  |
| information- ow tracking system for realtime privacy | for user-centric information- ow security. In | MICRO | , |  |  |
| monitoring on smartphones. In | OSDI | , pages 1{6, 2010. | pages 243{254, 2004. |  |  |
| [23] W. Enck, D. Octeau, P. McDaniel, and S. Chaudhuri. | [42] T. Wang, T. Wei, Z. Lin, and W. Zou. Intscope: |  |  |  |  |
| A Study of Android Application Security. In | USENIX | Automatically detecting integer over ow vulnerability |  |  |  |
| Security | , 2011. | in x86 binary using symbolic execution. In | NDSS | , |  |
| [24] S. R. Ganov, C. Killmar, S. Khurshid, and D. E. Perry. | 2009. |  |  |  |  |
| Test generation for graphical user interfaces based on | [43] T. Xie, N. Tillmann, P. de Halleux, and W. Schulte. |  |  |  |  |
| symbolic execution. In | AST | , pages 33{40, 2008. | Fitness-guided path exploration in dynamic symbolic |  |  |
| [25] S. R. Ganov, C. Killmar, S. Khurshid, and D. E. | execution. In | Proc. DSN | , 2009. |  |  |
| Perry. Event listener analysis and symbolic execution | [44] Y. Zhang, M. Yang, B. Xu, Z. Yang, G. Gu, P. Ning, |  |  |  |  |
| for testing gui applications. In | ICFEM | , 2009. | X. Wang, and B. Zang. Vetting undesirable behaviors |  |  |
| [26] P. Gilbert, B.-G. Chun, L. P. Cox, and J. Jung. | in android apps with permission use analysis. In | CCS | , |  |  |
| Vision: automated security validation of mobile apps | 2013. |  |  |  |  |
| at app markets. In | Proc. MCS) | , 2011. | [45] C. Zheng, S. Zhu, S. Dai, G. Gu, X. Gong, and |  |  |
| [27] P. Godefroid. Compositional dynamic test generation. | W. Zou. Smartdroid: An automatic system for |  |  |  |  |
| In | POPL | , pages 47{54, 2007. | revealing ui-based trigger conditions in android |  |  |
| [28] P. Godefroid, N. Klarlund, and K. Sen. Dart: directed | applications. In | Proc. SPSM | , October 2012. |  |  |
| automated random testing. In | PLDI | , pages 213{223, | [46] Y. Zhou and X. Jiang. Dissecting android malware: |  |  |
| 2005. | Characterization and evolution. In | IEEE Symposium |  |  |  |
| [29] M. C. Grace, W. Zhou, X. Jiang, and A.-R. Sadeghi. | on Security and Privacy | , 2012. |  |  |  |

Unsafe exposure analysis of mobile in-app

advertisements. In WiSec , 2012.

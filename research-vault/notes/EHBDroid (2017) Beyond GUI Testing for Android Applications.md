---year: 2017

secverify_category: "Category A"
categories:
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
title: "EHBDroid: Beyond GUI Testing for Android Applications"
author: "Wei Song, Xiangxing Qian, and Jeff Huang"
creator: "LaTeX with hyperref package"
pages: 11
source: "EHBDroid (2017) Beyond GUI Testing for Android Applications.pdf"
---

# EHBDroid: Beyond GUI Testing for Android Applications

> **文獻存檔**：[PDF 原文](<../../raw-papers/2010-2019/EHBDroid (2017) Beyond GUI Testing for Android Applications.pdf>) | [Markdown 原文](<../../raw-papers/2010-2019/EHBDroid (2017) Beyond GUI Testing for Android Applications (Raw).md>)

> **作者**：Wei Song, Xiangxing Qian, and Jeff Huang
> **總頁數**：11 頁

---

## Page 1

EHBDroid: Beyond GUI Testing for

Android Applications

| Wei Song | Xiangxing Qian | Jeff Huang |
| --- | --- | --- |
| School of Computer Sci. & Eng. | School of Computer Sci. & Eng. | Parasol Laboratory |
| Nanjing University of Sci. & Tech. | Nanjing University of Sci. & Tech. | Texas A&M University |
| Nanjing, China | Nanjing, China | College Station, TX, USA |
| wsong@njust.edu.cn | xiangxingqian@gmail.com | jeff@cse.tamu.edu |
| Abstract | —With the prevalence of Android-based mobile de- | Although mobile app testing has attracted a large body |

vices, automated testing for Android apps has received increasing of active research [1], [2], [4]–[13], existing approaches and

attention. However, owing to the large variety of events that tools are still unsatisfactory. According to a recent study [14],

Android supports, test input generation is a challenging task.

In this paper, we present a novel approach and an open source

invokes callbacks of event handlers. By doing so, EHBDroid can

efficiently simulate a large number of events that are difficult to

generate by traditional UI-based approaches. We have evaluated

efficient than Monkey and Dynodroid: in a much shorter time,

EHBDroid achieves as much as 22.3% higher statement coverage

event handlers

I. INTRODUCTION

In addition, certain UI events can only be triggered if their pre-

978-1-5386-2684-9/17/$31.00 c © 2017 IEEE 27

most existing approaches are UI-based, and they are either

security of mobile apps.

In this paper, we present a new approach and an open source

EHBDroid is based on a simple, but important observation:

Hence, instead of attempting to generate UI events, we can

trigger their event handlers (callbacks) directly. The callback

instrumentation can be inserted into the app via either static

functions repeatedly.

ASE 2017, Urbana-Champaign, IL, USA

Technical Research

tool called EHBDroid for testing Android apps. In contrast to too slow to generate events, or cannot effectively generate

conventional GUI testing approaches, a key novelty of EHBDroid certain events. More efficient and effective automated testing

is that it does not generate events from the GUI, but directly techniques are required to ensure correctness, reliability, and

EHBDroid on a collection of 35 real-world large-scale Android tool, called EHBDroid (Event Handler Based), for testing

apps and compared its performance with two state-of-the-art UI- Android apps. EHBDroid is implemented and evaluated for

based approaches, Monkey and Dynodroid. Our experimental Android. However, the idea of event handler-based testing is

results show that EHBDroid is significantly more effective and not limited to Android, but general to event-driven systems.

(11.1% on average) than the other two approaches, and found 12 In event-driven systems, there often exists a correspondence

bugs in these benchmarks, including 5 new bugs that the other between an event and an event handler. The events that

two failed to find. occur on the UI are eventually passed to and are handled by

Index Terms —Android, automated testing, event generation, their event handlers, e.g., callback functions in Android [15].

Despite the popularity of mobile apps, testing them faces analysis or code re-writing at class loading time.

significant challenges. The difficulty lies in two main aspects. There are several advantages of EHBDroid over traditional

First, the space of events is often enormous. There could be UI-based approaches. First, it can invoke a set of callback

an infinite number of UI events if the app’s state is cyclic, functions quickly because the testing does not need to wait

and there are more than a hundred different kinds of system for the latency induced by GUI and the cost of message

broadcasting events supported by Android currently [1]. It passing in the system. Second, it can test the callback functions

is impractical to generate all possible events and their per- thoroughly even if some of them cannot be easily invoked

mutations. Second, many UI events (e.g., drag, hover) and through the GUI. For many events such as system events and

most system and inter-app events, are difficult to generate. complex UI events, it is much easier to generate calls to their

For example, generating a drag event requires that the drag event handlers directly than to generate events from the UI.

should start at a certain position and end at another, and only Consequently, it provides high code coverage in a short testing

when the distance between the two positions is larger than a time. Third, the events for the test are systematically generated

certain value, can the event be regarded as a successful drag. and are not redundant, i.e., the events do not invoke the same

conditions are satisfied (e.g., inputs to all the relevant widgets Although the basic idea of EHBDroid is simple, we are not

are provided) [2]. The probability to simulate all combinations aware of any previous research or infrastructure that explored

of the widget inputs is very small [3]. Thus, it is hard to this idea. A most related tool is Dynodroid [1]. It instruments

simulate such UI events thoroughly. For many system events, the Android framework and relies on the VM to generate a

proper data (e.g., arguments) needs to be constructed and considerable number of UI inputs and system-level events that

dispatched correctly to the app. For inter-app events, they can are relevant for the apps, and uses a pre-configured selection

only be triggered by external apps under certain conditions. strategy to select an event to execute. However, Dynodroid


---

## Page 2

| is less effective and efficient than | EHBDroid | because of its | TABLE I |  |  |
| --- | --- | --- | --- | --- | --- |
| black-box nature, i.e., it only generates a limited range of | ANDROID EVENT TYPES AND THEIR REGISTRATION PATTERNS |  |  |  |  |
| events, and for each generated event it relies on the Android |  |  |  |  | Pattern |

1) How to identify the event handlers in Android and

construct their invocations?

2) How to construct valid runtime event data passed to the

event handlers?

3) How to systematically invoke the event handlers such

that the app behavior can be effectively tested without

redundant exploration?

These challenges are often specific to the implementation of

in the app context) for those of reference types, EHBDroid

We implement EHBDroid as an automated testing tool

odroid [1]. The results suggest that EHBDroid is significantly

To summarize, we make the following contributions:

simulate UI, system, and inter-app events in Android by

28

Dynamic

Event   Static (a) Static (b) Overridden

Receiver

Service √

Inter-app

We have successfully instrumented all 58 callbacks in

Android API with valid arguments.

• We present an open source tool that realizes our approach

and we have conducted extensive experiments showing

significant performance improvements of our approach

over the state-of-the-art.

of our approach.

handler of s .

its attribute.

handler.

ridden pattern is defined as s.callback , where s is the source

| framework to pass the event to the event handler, rather than |  |  | √ | √ | √ |
| --- | --- | --- | --- | --- | --- |
| invoking the event handler directly. | UI | √ | √ |  |  |
| To realize | EHBDroid | , there are several challenges: | System | √ | √ |
| the event-driven framework. For the first challenge, we identify | The remainder of the paper is organized as follows. Sec- |  |  |  |  |

three registration patterns for event handlers in Android. tion II introduces the background on Android event regis-

Based on these patterns, EHBDroid is able to automatically trations. Section III presents our approach. Section IV intro-

instrument all 58 callbacks in the Android API. For the second duces the implementation of EHBDroid . Section V evaluates

challenge, by using default value for data of primitive types EHBDroid . Section VI discusses limitations of EHBDroid .

and runtime instances of event sources (which are available Section VII reviews related work and Section VIII concludes.

| constructs many meaningful runtime arguments for invoking | II. ANDROID EVENT REGISTRATION |
| --- | --- |
| the callbacks. For the third challenge, instead of invoking those | Android apps are event-driven programs with abundant UI |

callbacks randomly, EHBDroid performs an activity-directed events, system events, and inter-app events. Based on our

depth-first search to effectively traverse different activities study of the Android API, we identify three event registration

without redundant exploration. patterns (cf. Table I), which are useful for the instrumentation

based on the Soot framework [16]. EHBDroid is open source Pattern 1 ( Static registration pattern ): A static registration

and is publicly available on Github: 1 . EHBDroid has been pattern is defined as s.elm , where s is an event source declared

evaluated on 35 real-world Android apps from F-droid [17] in the XML resource file, and elm represents an element

and Google Play store [18], and compared with two state- (method or field) of s declared in the same file:

of-the-art UI-based testing tools, Monkey [19] and Dyn- (a) If s is a view, elm is the method invoked by the event

more efficient and effective than the other two approaches. (b) If s is a component (i.e., activity, service, or receiver), elm

EHBDroid achieves as much as 22.3% higher statement is an intent-filter object defined by s .

coverage (11.1% on average) than Monkey and Dynodroid Pattern 1(a) is only applicable to UI events and their

for these apps. For all apps, EHBDroid can quickly cover handlers, and Pattern 1(b) is only applicable to system and

all activities in ten minutes, whereas for many apps Monkey inter-app events and their handlers. Fig. 1(a) shows an example

and Dynodroid either cannot generate events to cover certain of static registration pattern for UI events, where Button is a

activities or get a much lower code coverage even in an hour. view and click is the method invoked by the event handler

Besides, EHBDroid detected 12 bugs in these apps, 5 of which of Button . Fig. 2(a) presents an example for service event

| were not found by the other two. | registration, where | service | is a component and | intent-filter | is |
| --- | --- | --- | --- | --- | --- |
| • | We develop an event handler-based testing approach, | Pattern 2 ( | Dynamic registration pattern | ): | A dynamic reg- |

EHBDroid , for testing Android apps without the need istration pattern is defined as s.rm(h) in the app code, where

to generate events. The approach of EHBDroid applies s is the source of an event, rm is the registration method of s ,

not only to Android apps, but also to general event-driven and h is the event handler that s registers.

systems. Though conceptually simple, to the best of our Pattern 2 applies to both UI and system events. In Fig. 1(b),

knowledge, EHBDroid is the first event handler-based btn is a view, setOnClickListener is the registration method,

approach for Android app testing. and listener is the event handler. In Fig. 2(b), sm is a service,

• We present a general and systematic testing strategy to registerListener is the registration method, and l is the event

instrumenting and automatically invoking their callbacks. Pattern 3 ( Callback overridden pattern ): A callback over-

1 https://github.com/wsong-nj/EHBDroid of an event e , and callback corresponds to e ’s event handler.


---

## Page 3

Pattern 3 is only applicable to view events. For this

the app code. The following six callbacks are frequently

Fig. 1(c) presents an example, where MyView is a view and

(a)

1 btn . setOnClickListener ( listener ) ;

(b)

1 Class MyView extends View {

2 void performClick () {

(c)

Fig. 1. Examples of UI event registration

1 < service name= "MusicService" >

3 < /service >

(a)

3 void onSensorChanged(); }

4 sm. registerListener ( l ) ;

(b)

Fig. 2. Examples of service event registration

III. EHB TESTING

A. Motivation and Challenges

system event needs to simulate a sensor change. Moreover,

once being triggered, these two events have to be analyzed

by the underlying Android OS and then passed to their event

29

 FODVV )ROGHU/LVW$FWLYLW\ H[WHQGV /LVW$FWLYLW\ ^

|  | V\VWHP HYHQW |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 6HQVRU0DQDJHU VP JHW6\VWHP6HUYLFH |  |  |  |  |  |
|  | VPUHJLVWHU/LVWHQHU |  | VH | O |  |  |
|  | 8, |  | HYHQW |  |  |  |
|  | ` |  |  |  |  |  |
|  | LQYRNHG ZKHQ OLVW LWHP LV FOLFNHG |  |  |  |  |  |
|  | LSXW([WUD (;75$B)2/'(5B,' LG  |  |  |  |  |  |
|  | VWDUW$FWLYLW\ L |  |  |  |  |  |

 ``

YRLG HKE7HVW ^

|  | V\VWHP HYHQW |  |  |
| --- | --- | --- | --- |
|  | 6HQVRU(YHQW VH VPJHW6HQVRU(YHQW |  |  |
|  | VHORQ6HQVRU&KDQJHG VH  |  |  |
|  | 8, HYHQW |  |  |
|  | IRU LQW L LOYVL]H | L ^ |  |
|  | 9LHZ Y | OYJHW&KLOG$W L  |  |
|  | ORQJ LG | OYJHW$GDSWHU | JHW,WHP,G L  |
|  | WKLV RQ/LVW,WHP&OLFN OYYLLG |  |  |
|  | ` |  |  |

 `

of events and the difficulty of event generation in many cases,

our approach is a promising alternative for app testing.

Challenges . However, there are several challenges in real-

izing the idea above:

1) We need to identify the event handlers (that is, the call-

back functions) and construct their invocations. Android

callbacks. It is challenging to correctly identify them and

construct their invocations.

B. Invoking Event Handlers

| pattern, one should override the corresponding callbacks in |  | YRLG RQ&UHDWH %XQGOH EXQGOH | ^ |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| used in this pattern: | onListItemClick() | , | performClick() | , | on- |  | 6HQVRU(YHQW/LVWHQHU VHO QHZ 6HQVRU(YHQW/LVWHQHU | ^ |  |  |  |  |  |  |  |
| Touchevent() | , | onKeyUp() | , | onKeyDown() | , | performLongClick() | . |  | YRLG |  | RQ6HQVRU&KDQJHG 6HQVRU(YHQW |  | V ` |  |  |
| performClick | is the overridden method. |  | /LVW9LHZ |  | OY JHW/LVW9LHZ |  |  |  |  |  |  |  |  |  |  |
| 1 | // View + Callback |  | YRLG RQ/LVW,WHP&OLFN /LVW9LHZ O9LHZ YLQW SRVORQJ LG ^ |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | < | Button android:id= | "." | android:onClick= | "click" | > |  | ,QWHQW L QHZ ,QWHQW WKLV6XGRNX/LVW$FWLYLW\FODVV  |  |  |  |  |  |  |  |
| 3 | } | &DOOEDFN |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | } | LQYRFDWLRQV |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | < | intent | − | filter | > | ... | < | / intent | − | filter | > | Fig. 3. | A motivating example from the | OpenSudoku | app |
| 1 | SensorManager sm = getSystemService(); | events can be simulated easily, but the testing itself can also |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | l = new SensorEventListener () | { | be performed more efficiently. Considering the large number |  |  |  |  |  |  |  |  |  |  |  |  |
| In this section, we propose the event handler-based testing | provides 58 different callbacks as a part of the framework, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| approach for Android apps. | and besides, there can be many user-defined or overridden |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Fig. 3 exhibits a code snippet from the | OpenSudoku | app, | 2) We have to construct valid arguments for the callback |  |  |  |  |  |  |  |  |  |  |  |  |
| which involves one UI event and one system event. For the | invocations. For example, the callback | onListItemClick() |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UI event, the corresponding UI element, event handler, and | has four different types of parameters: | listView | , | view | , |  |  |  |  |  |  |  |  |  |  |
| callback are | listView | , | FolderListActiviy | , and | onListItemClick() | , | position | and | id | . It is uneasy to obtain valid values for |  |  |  |  |  |
| respectively. For the system event, the corresponding event | the parameters from the app. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| handler and callback are | sm | and | onSensorChanged() | . To test | 3) We should insert these callbacks at proper locations in the |  |  |  |  |  |  |  |  |  |  |
| this app with traditional UI-based approaches, these two events | app and to control their invocations such that the app can |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| must be triggered as the test inputs. However, generating these | be systematically tested. It is challenging to insert these |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| two events is not easy, because triggering the UI event needs | invocations without breaking the lifecycle of activities |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to click the right list item on the screen, and triggering the | and to invoke them to effectively cover different activities. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| handlers through numerous layers of the Android framework, | We first identify all event registration statements in the app |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| which can slow down the testing. | based on the three patterns presented in Section II. Algorithm 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

To test this app, we directly invoke both of the two callbacks performs a linear scan of the app to find all events and their

onListItemClick() and onSensorChanged() in the app code (as handlers (declared either in the XML resource files or in the

shown in the grey region), rather than trigger the correspond- app code). Then, for each event registration statement, we

ing events from the UI hierarchy. In this way, not only the two construct an instrumented invocation statement (which will be


---

## Page 4

| Algorithm 1: | Search for events and their handlers | this subsection, we describe how to construct valid arguments |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Input: | The APK file of an Android app | for these callback invocations. |  |  |  |
| Output: | E | : XML elements matching with Pattern 1, | S | : Statements | One way to construct the callback arguments is to collect the |

matching with Pattern 2, M : Methods matching with Pattern 3

1 for each XML resource file f ∈ app do

4 E ← E ∪ { e }

5 for each class c ∈ app do

| 8 | M | ← | M | ∪ { | m | } |
| --- | --- | --- | --- | --- | --- | --- |
| 9 | for | each statement | s | ∈ | m | do |

2 Object c = m.getClass () .newInstance () ;

3 c . click (btn) ;

(b) (c)

1 Activity mainActivity ;

2 Receiver ma = BootReceiver.newInstance() ;

(d)

C. Constructing Callback Arguments

runtime data for a few test runs (e.g., with existing test cases)

ing the 58 callbacks, we propose a simple yet effective method

to construct valid arguments based on the default values and

• Using default values . Data types in Java can be divided

values. For this kind of parameters, we use their default

values as arguments for the corresponding callback in-

vocations. If a callback involves several parameters, we

enumerate all combinations of their default values.

the first parameter lv , and thus can be constructed from it.

arguments. Line 9 is the instrumented callback invocation. The

of primitive types is to enumerate all possible values. Note

from the correlated objects using Android APIs.

D. Exploration Strategy

ities and edges the activity transitions caused by events (cf.

OpenSudoku app. Note that the state machine is just to help

readers understand our approach; it is unnecessary to explicitly

construct it in our approach.

30

| 2 | for | each XML element | e | ∈ | f | do | and use the collected data as the arguments. Nevertheless, this |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | if | e | matches with Pattern 1 | then | method requires the existence of good test inputs. After analyz- |  |  |  |  |  |
| 6 | for | each | m | ∈ | c | do | from the app context. This method is complementary to the |  |  |  |
| 7 | if | m | matches with Pattern 3 | then | first method, and it does not require extra test runs. |  |  |  |  |  |
| 10 | if | s | matches with Pattern 2 | then | into primitive types and reference types. For primitive |  |  |  |  |  |
| 11 | S | ← | S | ∪ { | s | } | data types, Android API usually provides default valid |  |  |  |
| inserted into the app), according to the invocation pattern of | • | Deriving | from | app | context | . | For | parameters | of | the |
| event handlers defined below. | reference data types, the valid values (objects) can be |  |  |  |  |  |  |  |  |  |
| Pattern 4 ( | Invocation Pattern | ): | The invocation pattern for | obtained from the app context. These parameters are |  |  |  |  |  |  |
| event handlers used for the instrumentation is defined as | usually connected with the event source, and thus can be |  |  |  |  |  |  |  |  |  |
| h.callback(s) | , where | s | is the event source, | h | the registered | obtained by invoking relevant APIs of the event source. |  |  |  |  |
| event handler, and | callback() | the callback method of | h | . | For arguments that cannot be directly obtained from the |  |  |  |  |  |
| To construct the callback invocation, we need to identify the | app context, we can get them through Java reflection. |  |  |  |  |  |  |  |  |  |
| three elements | s | , | h | , and | callback | for each event registration | For instance, to construct the arguments for the | onDrag() |  |  |
| pattern. For Pattern 1(a) and Pattern 3, view | s | is the event | callback, we cannot get a | DragEvent | instance via | new |  |  |  |  |
| source, | elm | is the callback, and the object that defines | elm | is | DragEvent() | directly because only a private construction |  |  |  |  |
| the event handler | h | . For Pattern 1(b), component | s | is the event | method is provided. Instead, we utilize Java reflection to |  |  |  |  |  |
| source and | elm | is the intent-filter. In this case, the life-cycle | get the private constructor, set its accessibility to true, and |  |  |  |  |  |  |  |
| method of | s | is the callback, and the class that defines this | finally get an instance via invoking | class.newInstance() | . |  |  |  |  |  |
| method is the corresponding event handler. For this pattern, | Example | . The grey region in Fig. 3 illustrates how we |  |  |  |  |  |  |  |  |

besides s , the intent-filter elm is also the parameter of the construct the callback arguments for the motivating example.

callback. For Pattern 2, we can obtain the callback from Take the callback onListItemClick(ListView lv, View v, int pos,

the event handler registered by the registration method rm . long id) as an example. Its first argument is a ListView instance

Figs. 4a-4c present the instrumented invocation statements for which can be obtained from the app context. The second is

the UI event registration examples in Figs. 1a-1c, respectively. the view that is clicked within the ListView. The third is the

Fig. 4d shows the instrumented invocation statements for the position of the view in the ListView. The last is the row id

| service event registration examples in Fig. 2. | of the view. The last three parameters are all correlated with |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | // m is | click | method | Lines 6-8 show how to obtain the second, third and fourth |  |  |  |
| (a) | reason why we do not use default values for the parameters |  |  |  |  |  |  |
| 1 | listener .onClick(btn) ; | 1 | MyView.newInstance().performClick() ; | that our approach can automatically construct such arguments |  |  |  |
| 3 | Intent | intent | = | createIntent ( | intentfilter | ) ; | The logic of an app can often be described as a state |
| 4 | ma.onReceiver(mainActivity , | intent ) ; | machine (or a directed graph) where nodes represent activ- |  |  |  |  |
| Fig. 4. | Examples of invocation patterns for instrumentation | Definition 1). Fig. 5 depicts a part of the state machine of the |  |  |  |  |  |
| For all the 58 callbacks provided in the Android API, we | Definition 1 ( | App abstraction | ): | An app can be abstracted |  |  |  |

have successfully instrumented their invocations in apps. In as a state machine ( A , E , → ) where


---

## Page 5

Soduku Algorithm 2: EHBDroid Test exploration

List

| e3 | e0 |  |  |
| --- | --- | --- | --- |
| e2 | e1 | e4 |  |
| Sudoku | Folder | Sudoku |  |
| Play | List | Edit |  |
| Game | Sudoku | File |  |
| 6 | ettings | Export | List |

Fig. 5. Part of the state machine of the OpenSudoku app.

be visited. Android provides an activity stack managing all

0 , we first identify the

event handlers (callbacks) of events in E ( A

0 ). Then, we invoke

0 ; if there is more

0 to other activities. These

activities are automatically pushed into the Android activity

stack. After all event handlers in A 0 are invoked, the activity

1 MenuItem menuItem = new MenuItem( "test" );

5 // inserting invoking statements

Input: The instrumented APK file of an Android app

1 S ← S .push( M ainActivity )

2 while S is non-empty do

| 3 | currentActivity | ← | S | .pop() |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | if | currentActivity / | ∈ | L | then |  |  |
| 5 | L | = | L | ∪ { | currentActivity | } | trigger new event “test” |
| 7 | S | .push( | A | i | ) |  |  |
| 8 | else |  |  |  |  |  |  |
| 9 | click navigation “Back” |  |  |  |  |  |  |

in the number of activities.

dlers of the five events e

0 ∼ e 4 in SodukuList are triggered

IV. IMPLEMENTATION

these tuples are stored in a map. The Recognizer then searches

contain the event sources identified by the XML Parser and the

31

e5 e6 e7 e8 6 for each activity A i generated by “test” do

• A is an activity set; A 0 ∈A is the main activity, and A i ∈A besides the Android activity stack, a list L is utilized to denote

is called the current activity if it is active on the screen the activities that have been explored. Algorithm 2 works as

of the user device. follows: If currentActivity has not been explored, all event

• E is the set of all possible events in the app, and E ( A i ) handlers in currentActivity are triggered (by clicking “test”)

⊂ E is the set of events that can be triggered in A i . and the generated activities are all pushed into S . Otherwise,

• → ⊂ A × E × A is a ternary transition relation. the testing continues to explore next activity on the top of the

Without loss of generality, our testing focuses on event stack (by pressing “back”). The algorithm terminates when

coverage, i.e., aiming to cover all events in an app. To this the activity stack S becomes empty. Since each activity is

end, all nodes (activities) where events can be triggered should explored only once, time complexity of Algorithm 2 is linear

| activities, which allows us to use a depth-first-search strategy | Example | . | Consider | the | example | in | Fig. | 5 | where |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| for activity (event) traversal. | SodukuList | is the main activity. When the instrumented |  |  |  |  |  |  |  |
| Beginning from the main activity | A | “test” menu-item in | SodukuList | is “clicked”, event han- |  |  |  |  |  |

all these callbacks in a random but valid order CS . That and the generated activities are pushed into the stack S

is, each callback can only be invoked if the corresponding following a random order, e.g., SodukuEdit , SodukuP lay ,

event is valid at the current state of A SodukuP lay , F olderList , and SodukuEdit . Although there

than one valid event, the invocation order of these callbacks is are repeated activities in S , their exploration is not redundant

| random. Notably, the invocation of some event handlers in | CS | according to Algorithm 2. Next, | SodukuEdit | is explored as it |  |
| --- | --- | --- | --- | --- | --- |
| may cause the transitions from | A | is at the top of | S | . The other activities are all explored similarly. |  |
| A | i | at the top of the stack is popped. The same strategy is | We have implemented | EHBDroid | as a fully automated tool |

used to explore all event handlers in A i . The above procedure based on Soot [16]. Fig. 6 depicts its architecture which

iterates until all activities of the app are explored. consists of two main parts: an Instrumentor that instruments

To ensure that our instrumentation is valid, the callbacks the target app, and a testing Explorer that tests the app.

should be invoked in a similar way as the user’s click on Important modules of the two parts are explained below.

the UI elements. With this in mind, for each activity, we XML Parser and Recognizer . The first step of EHBDroid

build a specific menu-item “test” with its event handler en- is to search different event registration patterns in both the

capsulating a valid callback sequence of events in E ( A i ). XML resource files and the app code. The XML Parser utilizes

In the following example, the menu-item “test” registers a XMLPrinter [20] to parse the input XML resource files. Based

listener onMenuItemClickListener whose callback is onMenu- on Pattern 1, it searches for two kinds of tuples. The first

ItemClick() . In the callback, the invocations of event handlers kind consists of a view and a method, while the second kind

| are instrumented. | consists of a component and one or more intent-filters. All |  |  |
| --- | --- | --- | --- |
| 2 | OnMenuItemClickListener oml; | for all statements that match with Pattern 2 and Pattern 3. All |  |
| 3 | oml = new OnMenuItemClickListener( | { | qualified statements are summarized in a set of Java objects. |
| 4 | void onMenuItemClick() | { | In each of the Java objects, there are three different fields: |
| 6 | }} | ; | event source, registered methods, event handlers. |
| 7 | menuItem.setOnClickListener(oml); | Dispatcher | . The Dispatcher determines the activities that |

Algorithm 2 presents our test exploration strategy, which Recognizer. It constructs in each activity a “test” menu-item

accepts the instrumented APK file as input. In the algorithm, that manages the invocation statements for the corresponding


---

## Page 6

,QVWUXPHQWHU

'H[

| 5HFRJQL]HU | ,QYRFDWLRQ |
| --- | --- |
| )LOH | %XLOGHU |

APK

;0/ 'LVSDWFKHU

3DUVHU +\KTZ .GTJRKXY /RJJHU

Fig. 6. Architecture of

source is a component (i,e., activity, service, receiver), the

corresponding event can be triggered in any activity. Without

loss of generality, in this case, the main activity is considered

exception information and go on testing.

Enhancing debugging . EHBDroid also allows to piggy-

32

&XUUHQW

$FWLYLW\ ([SORUHU

APK ?

YLVLWHG \HV

&OLFN

EDFN

,QYRFDWLRQ 0DQDJHU QR

/T\UIGZOUTGTJ RUMMOTMYZSZY

,QVWUXPHQWHG &OLFN

7HVW

EHBDroid .

failing event handler.

V. EVALUATION

A. Code Coverage

callbacks. The target activity of the invocation statement is occurs, the recorded events can be used by Robotium [22]

determined as follows. If the event source is a view, the or other UI-based tools to reproduce the failure. Moreover,

target activity is obtained by view.getContext() . If the event the corresponding bug can be easily located by inspecting the

as the target activity. We have evaluated EHBDroid on a collection of 35 real-

Invocation Builder . This module constructs the invocation world Android apps from F-droid and Google Play, and com-

statements according to Pattern 4. The arguments of callbacks pared it with two popular UI-based app testing approaches:

are constructed according to the two means presented in Monkey and Dynodroid , both of which have proven fault

Section III-C. For inter-app events, since the corresponding detection ability [14]. Through the experimental evaluation,

activities are started by third-party apps, we simulate these we aim at answering the following three research questions:

| apps by directly instrumenting the statements that start new ac- | • | RQ1 | - Code coverage: Can | EHBDroid | achieve a higher |
| --- | --- | --- | --- | --- | --- |
| tivities (like | startActivity(intentFromIntentFilter) | ) in the main | code coverage than the other two approaches? |  |  |
| activity of the app to be tested. | • | RQ2 | - Testing efficiency: How efficient is | EHBDroid | in |
| Invocation Manager | . An Invocation Manager corresponds | terms of event handlers triggered per minute? |  |  |  |
| to our instrumented event “test”, and is realized by a “test” | • | RQ3 | - Fault detection ability: Compared with the other |  |  |
| menu-item in each activity. A valid sequence of callback | two approaches, can | EHBDroid | find more bugs? |  |  |
| invocations in an activity is gathered in the event handler of | Benchmarks | . Table II lists the apps used in our evaluation. |  |  |  |

“test”. Once the “test” menu-item is clicked, all instrumented These apps are randomly chosen from F-droid and Google

statements in the activity will be triggered. Play with no prior knowledge about their event handlers. The

Explorer . By maintaining a list of visited activities, the first 25 (from F-droid) are popular benchmarks with a wide

Explorer can determine whether the current activity has been variety of functionalities, with 21K lines of code (Jimple),

explored. If an activity has not been explored, the Explorer 2,000 methods, and 9 activities on average for each app. The

will automatically click the “test” menu-item in the activity other 10 apps (from Google Play) are all large and complex

to explore it. Otherwise, the Explorer clicks “back”, and the apps among the top 1,000 in the Android market, with 96K

another activity on the top of the Android activity stack lines of code, 6.7K methods, and 18 activities on average.

becomes the current activity. The above step iterates until the Experimental setup . The Monkey [19] tool is a part of

activity stack becomes empty. We leverage MonkeyRunner in the Android SDK and is widely used by developers. It regards

the Android automated testing framework to send the device the app under test as a black-box and randomly generates UI

two UI events: click “test” and press “back”. The current ( touch(x,y) ) events. Since the number of generated events in

activity is obtained by the command: adb shell dumpsys Monkey can be configured by users, in our experiment, we set

activity of Android Debugging Bridge [21]. a sufficiently high bound (1M events) to ensure that Monkey

After introducing the implementation of EHBDroid , we dis- does not stop too early, in order to make a fair comparison.

cuss how it handles crashes and how it is used for debugging. Dynodroid [1] enhances Monkey by reducing the possibility

Handling crashes . In Android, when an uncaught exception of redundant event generation. We employ the default setting

occurs, the app will crash and terminate. To ensure that the (BiasedRandom strategy) of Dynodroid in our experiment.

testing continues until all event handlers are explored, we All experiments were performed on a PC with a 4GB

instrument every invocation statement in a try-catch block. memory and 2.4GHz processor, running Linux and Android

Thus, when an exception (bug) is found, we can record the 4.4. All experimental data were averaged over three runs.

back the instrumentation to generate execution logs ( Logger We use statement coverage as the criterion to compare the

is in charge of this.). The log records the runtime state of each testing effectiveness of different approaches. Because existing

event (e.g., activity, event source, event handler, and callback), tools for calculating statement coverage such as JaCoCo [23]

which is useful for debugging. For example, when a failure and Emma [24] require Java source code, they cannot be


![Page 6 Image](data:image/png;base64,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NXtywo8LnxxfqpjO1StOO/Tk3hcO7r3u1lsa115U3DvYvmhx4cjkgrPPffTAvqef3FvX1DTt6+G3fw2fbnlRbDIp70rqWZG5bHPcaZvdnZvNrmuU7ht9HVvyBjfmdK8NjcsAQHTHaidU1v+z8Jkajjbc4c6QzqKqzX3+6LBoi1tUZpIITA0KteGTS5MqIVn21TDhlif0Fx99+uFHn7334X273r5vw96y7z9Vftm+hqufqLtp26AnO3rqoEla6ZjvqfwcdKd746plTx144rH9T1x6xaV5o4vuuXXrQ7fdMLlq9eSatffsfWL/wSfqqyqPHl7bBYlLLbWpNhdfMksqp80r4wa/F7v6Bveq68miG9jkddra3ca5u2Zdel/B5dsTKjs0VygWtyx912FzKDEr4lOqZubc2O1/f9mieRmzEyNjTcKQBr4FPoLttlpKkAZUw3K7wmM+/uT373/8u/ffu/O19++75enSKw+WX7S3cccz9Q/fOkCSQo4HnyImpWrQcn5/zcon9z+xf9/jO2+4aumFF52z5dp7brnhvI0Xn3Phph379z22b09RUZFO6HHhiy80M1vMzjUhPWuNpVew07d4TtsWvWxb4yUPV1z8SMdld/ZdvT2/fQx4IzWMmXmiG1IHxlc3+0/vHFzY2jfWM+Rv7+/zOE0A7GtGAnc8yu6rQPtSFbK2JKXnl6Xuum78reuXbVozPBSa3BEywy1amiFkCHH7ZhhIITWoqUmejsphupjo7lDvF5+895tPP/ztl3/69E9//ui3v33/15/86ndfffr7r35952aaOfeYidPHjEsHQJEXBf43Yjs3X/zok/tffP7JnU8+eeWefevvuG/1HTu2Hnjh+/teeHT3A089uru0tk7BBGoanJodfqwjAtPL0ZxBR/15pG2TZ8GW+AVXea/YGXbZffkPvpL24Gtzr35k8Y17CjtXalGpiJr4hDdl/bPwNVmhdyfOyKrMPrB17I4rl79744rBsJTvpRa7xYA9DIUGzL5lTtzcScVlaZKS0wSBqemq2+v64yfv/uHTn/72D3/44s9//v3nn33+20+FXuYPX32184bIsvnHg0+XslngC9+x+eIH9u/fe+CJJ5858MoLTx3cvev++3fuf+rpg88++/6+3QcfeXBWcanCzePCF1foLV7ka9sIm9Zr41uiF10b+f1dsd/fVfHo65n3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)

![Page 6 Image](data:image/png;base64,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)

![Page 6 Image](data:image/png;base64,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)

---

## Page 7

| TABLE II | than | Monkey | and | Dynodroid | , respectively. For the 10 Google |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BENCHMARKS USED IN OUR EXPERIMENTS | Play apps, the difference is even larger. | EHBDroid | achieves |  |  |  |  |  |  |
| App name | LOC | #Class | #Method | #Act | as much as 26% more coverage than | Monkey | (on | ColorNote | ) |
| AGrep | 2,106 | 39 | 129 | 6 | and 15.1% on average. | Dynodroid | failed to run on all of these |  |  |
| AndroidomaticK | 1,859 | 26 | 111 | 4 | apps, because it requires instrumenting the Manifest file before |  |  |  |  |
| audiobook | 54,752 | 892 | 3,648 | 7 | testing, which throws exceptions in these large apps. |  |  |  |  |
| browser | 9,592 | 128 | 681 | 5 | Given more testing time, both | Monkey | and | Dynodroid |  |

| dalvikexplorer | 2,081 | 43 | 212 | 16 |
| --- | --- | --- | --- | --- |
| kolen | 1,803 | 25 | 95 | 4 |
| Notepad | 549 | 10 | 32 | 4 |
| OpenSudoku | 7,624 | 104 | 561 | 10 |
| Vudroid | 2,762 | 47 | 270 | 3 |
| dashclock | 3,059 | 15 | 129 | 7 |
| Editor | 8,864 | 121 | 832 | 5 |
| QKSMS | 119,005 | 1,100 | 6,279 | 9 |
| ColorNote | 57,825 | 748 | 3,249 | 20 |
| podcast | 165,850 | 2,210 | 12,205 | 17 |
| WikiPedia | 48,711 | 406 | 3,239 | 12 |
| Average | 96,565 | 1,035 | 6,723 | 18 |

used in our scenario where only the APK file is available. We

hence implement a new tool called Asc (Android statement

coverage) for calculating the statement coverage for APK files.

Asc first uses static analysis to extract the length of each basic

block of each method. Then, it instruments a statement at the

end of each block to print the length of the executed block.

The total lines and visited lines of statements can be calculated

by L = l i and L v = b i × l i , respectively, where n is the

33

were able to increase coverage for many apps. However, after

Play, the difference is still significant. Compared to Monkey ,

based testing approaches. This confirms the advantage of

OpenSudoku app contains a few context-menu events which

to generate events associated with navigation drawers, list

items is clicked, other items are invisible again. Hence, given

a limited time, Monkey and Dynodroid can only trigger a few

items but not all of them. In contrast, EHBDroid guarantees to

trigger callbacks for all items, because those events correspond

to the same callback and their event handlers can be invoked

easily by EHBDroid with different parameters.

Another reason why EHBDroid achieves a higher statement

coverage than the other two tools is that when most events in

an activity do not cause activity jump, the UI-based approaches

often fall into a loop, which is hard to jump out. The loop

| vector | 77,994 | 890 | 4,551 | 21 | one hour, their achieved statement coverage is still smaller |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic | 1,078 | 157 | 1,9137 | 10 | than that by | EHBDroid | . For apps from F-droid, the average |  |  |  |  |  |
| podax | 20,130 | 222 | 1,097 | 4 | coverage by | Monkey | and | Dynodroid | is close to (1%-2% |  |  |  |
| Nectroid | 5,185 | 88 | 516 | 6 | smaller than) | EHBDroid | . Nevertheless, for those from Google- |  |  |  |  |  |
| ringdroid | 7,860 | 64 | 332 | 3 | EHBDroid | achieved | as | much | as | 22.3% | higher | statement |
| Sanity | 13,046 | 204 | 1,048 | 28 | coverage and 11.1% higher on average in an hour. |  |  |  |  |  |  |  |
| TippyTipper | 2,998 | 47 | 238 | 5 | Result analysis | . Our empirical results suggest that | EHB- |  |  |  |  |  |
| VirtualDataLine | 2,489 | 41 | 256 | 4 | Droid | is more effective and efficient than the other two UI- |  |  |  |  |  |  |
| pedometer | 2,502 | 28 | 173 | 2 | EHBDroid | over | Monkey | and | Dynodroid | by directly trigger- |  |  |
| Apollo | 19,446 | 156 | 1,391 | 9 | ing event handlers of UI, system, and inter-app events, whereas |  |  |  |  |  |  |  |
| SipUA | 41,127 | 284 | 2,488 | 12 | Monkey | and | Dynodroid | can only trigger a part of UI events |  |  |  |  |
| Anima | 4,840 | 86 | 404 | 8 | and some system events ( | Monkey | cannot). For instance, the |  |  |  |  |  |
| K9 | 127,012 | 931 | 6,532 | 28 | require two steps to trigger: long pressing and clicking on the |  |  |  |  |  |  |  |
| Average | 2,1591 | 230 | 2,046 | 9 | pop-up menu item. | Monkey | and | Dynodroid | hardly trigger |  |  |  |
| TinyFlashLightED | 75,459 | 756 | 4,666 | 6 | these events, as they do not consider long-press events, let |  |  |  |  |  |  |  |
| AdobeReader | 61,734 | 709 | 5,445 | 15 | alone their combinations with a successive click. |  |  |  |  |  |  |  |
| fightpic | 59,210 | 679 | 7,689 | 9 | We also found that it is difficult for | Monkey | and | Dynodroid |  |  |  |  |
| AdobeAir | 194,275 | 1,841 | 12,371 | 15 | items, preferences, etc. For instance, the app | ColorNote | has |  |  |  |  |  |
| WordPress | 11,2941 | 1,270 | 7,594 | 54 | a navigation drawer containing a few items that drive users |  |  |  |  |  |  |  |
| pokegowallpaper | 22,131 | 239 | 1,482 | 9 | to different activities. Usually, these items are invisible until |  |  |  |  |  |  |  |
| BeautyPlus | 167,516 | 1,493 | 9,293 | 24 | the navigation view is clicked. However, when one of these |  |  |  |  |  |  |  |
| ∑ | n | ∑ | n | consumes time but does not explore more app behavior. For |  |  |  |  |  |  |  |  |
| i | =1 | i | =1 | example, in an activity of the | podcast | app (also | ColorNote | ), |  |  |  |  |
| number of blocks in the app, | l | i | the length of a block, and | b | i | there are many enabled events that do not cause activity jump; |  |  |  |  |  |  |
| (= 1 or 0) indicates whether the block is executed. | Monkey | stayed in this activity for a long time until the sole |  |  |  |  |  |  |  |  |  |  |

Overall results . We test each benchmark with the three event that can cause activity jump was triggered.

tools and collect the coverage statistics for both the first 10 For a few apps such as AGrep and kolen , the statement

minutes and the end of an hour. Table III reports the results. coverage of EHBDroid is lower than that of Monkey or

For all the benchmarks, EHBDroid was able to finish testing Dynodroid . The reasons are two-fold. First, EHBDroid cur-

(i.e., no more activities to explore) in 10 minutes, and for rently does not support text input [25]. In AGrep , a “submit”

most benchmarks (20/25 in F-droid and 10/10 in Google Play), button is unavailable when the edit texts for userID and

EHBDroid achieved a much higher coverage than the other password are empty. Hence, EHBDroid cannot reach the suc-

two tools in 10 minutes. For the 25 F-droid benchmarks, on cessor activities. Second, for performance reason, EHBDroid

average, the coverage of EHBDroid is 7.6% and 9.39% higher currently does not handle all items in a list, because such


---

## Page 8

TABLE III

EXPERIMENTAL RESULTS - RQ1: CODE COVERAGE AND RQ2: TESTING EFFICIENCY

| App name | Statement coverage(10min)(%) | Statement coverage(1h)(%) | #Events per minute |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Monkey | Dynodroid | EHB | Monkey | Dynodroid | EHB | Monkey | Dynodroid | EHB |  |
| AGrep | 74.28 | 70.23 | 69.34 | 74.28 | 70.23 | 69.34 | 1,500 | 12 | 18 |
| AndroidomaticK | 66.39 | 55.98 | 79.80 | 83.11 | 88.78 | 79.80 | 1,818 | 12 | 28 |
| audiobook | 24.03 | 32.94 | 35.02 | 35.09 | 41.67 | 35.02 | 1,340 | 12 | 21 |
| browser | 58.89 | 57.49 | 59.38 | 59.38 | 57.49 | 59.38 | 1,412 | 12 | 36 |
| dalvikexplorer | 50.25 | 29.21 | 56.14 | 57.02 | 40.56 | 56.14 | 1,500 | 12 | 24 |
| kolen | 72.89 | 67.86 | 67.86 | 72.89 | 67.86 | 67.86 | 1101 | 12 | 44 |
| vector | 36.89 | 37.90 | 47.44 | 48.61 | 45.79 | 47.44 | 2,143 | 12 | 20 |
| atomic | 54.67 | 58.89 | 66.47 | 66.47 | 66.47 | 66.47 | 1,500 | 12 | 26 |
| podax | 59.27 | 65.66 | 46.77 | 67.99 | 65.66 | 46.77 | 1,519 | 12 | 25 |
| Nectroid | 55.27 | 65.89 | 76.63 | 76.63 | 85.72 | 81.63 | 1,519 | 12 | 25 |
| Notepad | 69.88 | 66.37 | 82.37 | 72.88 | 73.00 | 82.37 | 1,463 | 12 | 15 |
| OpenSudoku | 60.03 | 40.63 | 71.97 | 71.97 | 64.57 | 71.97 | 1,846 | 12 | 35 |
| ringdroid | 55.65 | 43.19 | 73.49 | 78.35 | 73.97 | 73.49 | 1,579 | 12 | 22 |
| Sanity | 50.18 | 50.18 | 50.18 | 50.18 | 50.18 | 50.18 | 1,000 | 12 | 29 |
| TippyTipper | 42.86 | 41.41 | 78.29 | 60.57 | 53.78 | 78.29 | 1,714 | 12 | 78 |
| VirtualDataLine | 32.39 | 53.08 | 36.33 | 42.15 | 53.08 | 36.33 | 1,538 | 12 | 25 |
| Vudroid | 64.01 | 58.10 | 72.41 | 72.41 | 68.35 | 77.41 | 952 | 12 | 30 |
| dashclock | 82.18 | 82.18 | 82.18 | 82.18 | 82.18 | 82.18 | 1,538 | 12 | 42 |
| pedometer | 88.45 | 73.89 | 88.45 | 88.45 | 84.23 | 88.45 | 1,846 | 12 | 38 |
| Apollo | 56.73 | 55.76 | 70.46 | 56.73 | 55.76 | 70.46 | 2,297 | 12 | 29 |
| SipUA | 18.74 | 22.35 | 17.98 | 18.74 | 22.35 | 17.98 | 1,846 | 12 | 31 |
| Anima | 66.08 | 69.28 | 74.26 | 66.08 | 75.50 | 74.26 | 469 | 12 | 32 |
| Editor | 54.44 | 62.02 | 63.22 | 65.57 | 62.02 | 63.22 | 543 | 12 | 32 |
| QKSMS | 38.98 | 32.57 | 39.51 | 39.51 | 32.57 | 39.51 | 403 | 12 | 26 |
| K9 | 43.66 | 40.18 | 62.88 | 51.91 | 54.56 | 62.88 | 3,333 | 12 | 41 |
| Mean | 55.08 | 53.36 | 62.75 | 62.37 | 61.45 | 62.75 | 1,488 | 12 | 31 |
| animeradio | 28.67 | - | 47 | 32.75 | - | 47 | 2,595 | - | 40 |
| AdobeReader | 27.88 | - | 46.78 | 29.36 | - | 46.78 | 3,141 | - | 27 |
| fightpic | 33.56 | - | 49.99 | 35.83 | - | 49.99 | 3,750 | - | 23 |
| ColorNote | 24.57 | - | 50.21 | 27.88 | - | 50.21 | 3,380 | - | 18 |
| podcast | 27.04 | - | 38.92 | 34.39 | - | 38.91 | 3,692 | - | 35 |
| AdobeAir | 14.84 | - | 20.09 | 15.43 | - | 20.09 | 2,390 | - | 23 |
| WordPress | 26.57 | - | 35.47 | 36.67 | - | 35.47 | 2,521 | - | 31 |
| pokegowallpaper | 36.06 | - | 48.97 | 41.27 | - | 48.97 | 2,312 | - | 55 |
| BeautyPlus | 27.89 | - | 45.97 | 32.98 | - | 45.97 | 3,774 | - | 19 |
| WikiPedia | 32.63 | - | 47.24 | 32.63 | - | 47.24 | 3,015 | - | 46 |
| Mean | 27.97 | - | 43.06 | 31.92 | - | 43.06 | 3,057 | - | 32 |

item events often trigger the same behavior. We set a fixed ordinary users. For example, commercial apps usually provide

number (e.g., 10) to limit the invocation times of the callback both a free version and a paid version. The paid functionalities

onItemClicked() , with the assumption that most of the items can only be explored via a paid account.

are handled in the same way. Thus, if a ListItem contains more

than 10 items each of which is handled differently, some app B. Testing Efficiency

behavior may be missed. The last three columns in Table III report the number of

Low code coverage . For most apps, the achieved statement events (for Monkey and Dynodroid ) or event handlers (for

coverage by all the three tools is low (less than 50%). There are EHBDroid ) generated per minute by the three tools. We use

several reasons. First, in many apps there exists a large portion this metric to further show the testing efficiency of the three

of code that is not relevant to the business logic of the app. approaches. Monkey is the fastest approach among the three. It

Such code can only be reached under specific scenarios such generates 1.5K events and 3K events per minute for the F-droid

as bug reporting, version updating, exception handling, etc. and Google Play apps, respectively. However, these events

Second, some apps have dead code that can never be explored. contain a large number of redundant (i.e., repeated) or invalid

For example, SipUA contains a large number of branches and events that are not useful in exploring new app behavior.

methods that can never be reached. Third, some activities fail Dynodroid collects events and sends them to the app at a fixed

to be explored due to the missing of certain events for activity frequency (once every 5s) via the Android Debug Bridge.

jumping. When such an event is missed, the target activity and Accordingly, the number of events generated per minute by

its successor activities may not be explored. Fourth, certain Dynodroid is a constant 12. Among these events, there may

code requires special permissions and is not accessible to also exist redundant or invalid events. In contrast, each event

34


---

## Page 9

TABLE IV is due to the fact that in the corresponding event handler, K9

EXPERIMENTAL RESULTS - RQ3: FAULT DETECTION ABILITY uses an implicit intent to start a new activity, but neither the

| App name | Monkey | Dynodroid | EHBDroid |
| --- | --- | --- | --- |
| Sanity | 1* | 1* | 1 |
| padometer | 1 | 1* | 1 |
| Total | 7* | 7* | 12 |

handler invocation by EHBDroid is unique and non-redundant.

Moreover, the speed of EHBDroid is more than twice as

that of Dynodroid , generating 32 events per minute. Since

in our experiment the average time to instrument one app

is one minute, EHBDroid is still more efficient even if the

instrumentation time is included.

Monkey and Dynodroid lies in the fact that with one click

on “test”, all event handlers in the current activity are invoked

GUI and the cost of message passing in the system. In

particular, if an activity contains many events that cause

by Dynodroid , because activity jumping is expensive and the

a rate calculator containing 20 buttons. To test all the buttons,

Dynodroid needs 20 × 5 = 100s, while EHBDroid takes only

C. Fault Detection Ability

Dynodroid were also found by EHBDroid . These 12 bugs fall

into three classes: UI bugs, inter-app bugs, and special bugs.

We have also manually inspected these bugs and confirmed

their validity. We next describe them in detail.

OpenSudoku , ringdroid , Sanity , padometer , Apollo , K9 , and

ColorNote by EHBDroid . Except ColorNote , the other seven

were also found by Monkey and Dynodroid . When the corre-

app nor the device can handle the intent. The UI bug of the

NotePad , OpenSudoku , and K9 by EHBDroid . These bugs

sageList employs the method decodeExtra to resolve intents,

requiring that the attribute action of the intent should be

“android.view.action.View” (Line 2) and the attribute data of

the intent should contain a non-null path (Line 5). If data

does not contain a path attribute, when Line 5 is executed,

an exception is thrown and the app crashes. Monkey and

Dynodroid failed to find this kind of bugs, because they do

not consider inter-app events.

2 boolean decodeExtras( Intent intent ) {

| 3 | if (( | "android.intent.action.VIEW" | .equals(action)) |
| --- | --- | --- | --- |
| 4 | &&(intent.getData () != null ) ) | { |  |
| 6 | String | path = ( String ) localList . get (0) ; |  |
| 7 | } |  |  |

8 }}

10 < intent − filter >

11 < action name= "android.intent.action.VIEW" / >

14 < / intent − filter >

15 < / activity >

by EHBDroid . It is special because it is in an event handler

of a view that is invisible from the screen. Thus, from

onOptionsItemSelected(item) .

1 boolean onOptionsItemSelected(MenuItem item) {

2 swtich (item . getId () )

3 case 2131231108:

5 startActivity ( i ) ;

6 }

35

| AGrep | 1 | 1* | 1 | app | ColorNote | was found in activity | PreferenceActivity | by |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Notepad | 1 | EHBDroid | . The other two tools failed to find this bug because |  |  |  |  |  |  |  |  |  |  |
| OpenSudoku | 1 | 1 | 2 | they did not reach activity | PreferenceActivity | . |  |  |  |  |  |  |  |
| ringdroid | 1 | 1 | 1 | Three | inter-app | bugs | . | These | bugs | are | found | in | apps |
| Apollo | 1* | 1* | 1 | are caused by the mismatches between some intent-filters |  |  |  |  |  |  |  |  |  |
| K9 | 1 | 1 | 2 | and the received intents. The code below shows such a bug |  |  |  |  |  |  |  |  |  |
| ColorNote | 1 | detected in | K9 | . The activity | MessageList | defines an intent- |  |  |  |  |  |  |  |
| AdobeReader | 1 | filter in the Manifest file to filter the incoming intents. | Mes- |  |  |  |  |  |  |  |  |  |  |

Another reason why EHBDroid is more efficient than 1 class MessageList extends Activity {

together by EHBDroid , which avoids the latency caused by 5 List localList = intent . getData () .getPathSegments() ;

activity jumping, the testing time can be improved significantly 9 < activity name= "MessageList" >

UI-based approaches must jump back and forth repeatedly to 12 < data host= "messages" scheme= "email" / >

trigger all events in that activity. For example, TippyTipper is 13 < category name= "android.intent.category.DEFAULT" / >

2s to invoke the callbacks 20 times. One special “bug” . This bug was found in AdobeReader

Table IV summarizes all bugs found by the three tools in our the perspective of end users, it is not a bug, but from the

experiments, where ∗ represents bugs found after an hour. In perspective of programmers, it is. The code below illustrates

ten minutes, EHBDroid found a total of 12 bugs (manifested the bug. Note that Automationt.class is not declared in the

as crashes or runtime exceptions) in these 35 apps, whereas Manifest file. Hence, the app violates the rule that an activity

Monkey and Dynodroid only found five and four, respectively. is valid only if it is declared in the Manifest file. When the non-

After running for an hour, Monkey and Dynodroid found visible menu item 2131231108 is triggered, the app crashes.

two and three more bugs, respectively. Overall, EHBDroid Neither Monkey nor Dynodroid can find this bug, whereas

found five new bugs that could not be found by Monkey EHBDroid can because it can obtain all the menu items via

and Dynodroid , and all bugs that found by Monkey and menu.getMenuItems() and directly trigger the events through

Eight UI bugs . These bugs were found in apps AGrep , 4 Intent i=new Intent( this , Automationt. class )

sponding events are triggered, these apps crash. For example, VI. LIMITATIONS

in the K9 Mail client, when an option button in the Setting Except the 58 callbacks provided by Android, currently

activity is clicked, the app terminates abnormally. The error EHBDroid does not specially consider user-defined callbacks.


---

## Page 10

Fortunately, we find that many user-defined callback functions generated to systematically explore the behavior of the app.

are invoked by the callbacks in Android, and thus these user- For instance, GUIRipper [6] dynamically constructs an event

defined callback functions can also be explored by EHBDroid . flow graph for an Android app and follows a depth-first

Nevertheless, since an event handler may be called in a exploration strategy to test the app. ORBIT [7] adopts the

partial invocation context that differs from the real scenario, same exploration strategy, but it is a white-box approach that

EHBDroid may yield false alarms (false positives) that are utilizes the source code of the app to determine the events

never triggered by end users, though some of the false alarms that can be triggered in each activity. Similar approaches and

are still helpful for programmers. tools can be found in [8], [9], [35]. However, the effectiveness

Since the mechanism of EHBDroid is parallel to the event of these approaches heavily relies on the quality of the GUI

generation, it is orthogonal to the coverage criteria and ex- model. In practice, the models are often very abstract and may

ploration strategy. Currently, EHBDroid is at an early stage. not capture the complete behavior of the apps.

Although a depth-first-search strategy is used for activity Advanced testing . Jensen et al. use symbolic testing to gen-

exploration, the event handlers belonging to an activity are erate event sequences that reach specified target locations [33].

invoked in a random (though valid) order and only event ACTEve [4] utilizes concolic execution to track events from

coverage is considered. Thereby, EHBDroid is not compared their generation to their processing. These approaches in-

with the model-based and more advanced app testing tools strument both the Android framework and the app, and can

that are based on event (event sequence) generation, such as generate more complex event sequences that the other tools

GUIRipper [6], SwiftHand [9], Sapienz [11], etc. cannot. However, the scalability of symbolic testing is often

EHBDroid relies on Soot for app instrumentation. How- limited. Similar approaches can be found in [8], [36]–[38].

ever, Soot fails to instrument certain large apps with more By analyzing the interactions between widgets, Trim-

than two DEX files. Besides, some apps prevent from being Droid [2] employs the constraint solver to generate a subset

instrumented by hiding DEX files, checking signatures, etc. of event sequences, which can achieve a comparable cover-

Thus, EHBDroid may fail to instrument such apps. age as the exhaustive combinatorial testing. EvoDroid [37]

employs evolutionary algorithms to generate complex event

VII. RELATED WORK

sequences. Sapienz [11] uses search-based testing to auto-

For Android app testing, a large body of work focuses on matically explore test sequences to minimize the length of

test input generation, i.e., event generation. According to their event sequences, and simultaneously maximize code coverage

exploration strategies, existing approaches fall into three cat- and fault revelation. The tool AppDoctor [39] also triggers

egories: random testing (or fuzzing ), which generates random event handlers to simulate events. However, it only considers

events to apps; model-based testing , which generates events 20 types of events and merely focuses on specific bugs that

according to certain models (such as finite state machines) cause apps to crash. In addition, it uses Java reflection to

of apps; and advanced testing , which uses more sophisticated trigger event handlers, which is not so efficient. In contrast to

techniques such as symbolic execution to generate events. AppDoctor , EHBDroid directly invokes event handlers based

Compared to existing work, EHBDroid is distinguished by on instrumentation, which is more general and more efficient.

not generating events but directly invoking callbacks of the

| relevant event handlers, which is more efficient and effective. | VIII. CONCLUSIONS |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Considering the correlation between events and event handlers, | We have presented a new approach called | EHBDroid | for |  |  |  |  |
| our testing approach applies to general event-driven systems. | testing | event-driven | systems | and | specifically | discussed | its |

Random testing . Besides Monkey and Dynodroid , most concretization for testing Android apps. The key advantage of

early work focuses on random testing [6], [26]–[31]. Amal- EHBDroid is that by directly invoking the event handlers, it

fitano et al. [6], [27] present a crawling-based approach to avoids the difficulty of generating complex events that are hard

generate random but unique test inputs. There exist many to trigger by traditional UI-based approaches, and it avoids

tools for generating inter-app events by random generation the latency induced by the GUI and the cost of message

of intent values [1], [19], [28]–[31]. Null intent fuzzer [28] passing in the system. We have presented an open source

concentrates on revealing crashes of activities that fail to tool and evaluated its performance on a collection of 35 real-

properly check input intents. Intent Fuzzer [29] focuses on world Android apps. Experimental results demonstrate that

generating invalid test events with the goal of testing the EHBDroid can quickly reach higher statement coverage than

robustness of apps. The primary limitation of random testing the state-of-the-art UI-based testing approaches, and it is more

is that it often generates redundant events that are not useful powerful than the other approaches for finding bugs.

for exploring new app behavior.

Model-based testing . This line of research often requires ACKNOWLEDGMENTS

a GUI model of the application and has been intensively This work was supported in part by the National Key R&D

studied in GUI testing [6]–[10], [32]. The GUI model can Program of China under Grant No. 2017YFB1001801, the

be obtained manually [33] or via static/dynamic analysis [8]. Natural Science Foundation of Jiangsu Province under Grant

Hierarchy Viewer [34] is a tool for generating GUI models No. BK20171427, and the Fundamental Research Funds for

for Android apps. Based on the GUI model, events can be the Central Universities under Grant No. 30917011322.

36


---

## Page 11

REFERENCES [18] Google, “Google play store,” https://www.androidcentral.com/

[1] A. Machiry, R. Tahiliani, and M. Naik, “Dynodroid: an input generation

system for Android apps,” in Joint Meeting of the European Software

Engineering Conference and the ACM SIGSOFT Symposium on the

Foundations of Software Engineering, ESEC/FSE’13, Saint Petersburg,

Russian Federation, August 18-26 , 2013, pp. 224–234.

[2] N. Mirzaei, J. Garcia, H. Bagheri, A. Sadeghi, and S. Malek, “Reducing

combinatorics in GUI testing of android applications,” in Proceedings

of the 38th International Conference on Software Engineering, ICSE’16,

Austin, TX, USA, May 14-22 , 2016, pp. 559–570.

[3] M. Ermuth and M. Pradel, “Monkey see, monkey do: effective genera-

tion of GUI tests with inferred macro events,” in Proceedings of the 25th

International Symposium on Software Testing and Analysis, ISSTA’16,

Saarbr¨ ucken, Germany, July 18-20 , 2016, pp. 82–93.

[4] S. Anand, M. Naik, M. J. Harrold, and H. Yang, “Automated concolic

testing of smartphone apps,” in 20th ACM SIGSOFT Symposium on

vol. 19, no. 7, pp. 385–394, 1976.

pp. 258–261.

[8] T. Azim and I. Neamtiu, “Targeted and depth-first exploration for sys-

anapolis, IN, USA, October 26-31 , 2013, pp. 641–660.

[10] Y. M. Baek and D. Bae, “Automated model-based android GUI testing

Germany, July 18-20 , 2016, pp. 94–105.

in android applications,” in Proceedings of the ACM SIGPLAN Inter-

android wear applications,” in Proceedings of the 39th International

flow analysis of user-driven callbacks in android applications,” in 37th

framework,” in Addendum to the Proceedings of the Conference on

2010.

google-play-store, 2016.

[19] ——, “The monkey ui android testing tool,” http://developer.android.

com/tools/help/monkey.html, 2015.

[20] XMLPrinterGroup, “Xmlprinter,” http://www.xmlprinter.com, 2005.

[21] Google, “Android debug bridge,” http://developer.android.com/tools/

help/adb.html, 2015.

[22] RobotiumTech, “Robotium,” https://code.google.com/p/robotium, 2010.

[23] EclEmmaTeam, “Jacoco: Java code coverage library,” http://www.

eclemma.org/jacoco/, 2009.

[24] SourceForge, “Emma: a free java code coverage tool,” http://emma.

sourceforge.net/, 2006.

[25] P. Liu, X. Zhang, M. Pistoia, Y. Zheng, M. Marques, and L. Zeng,

“Automatic text input generation for mobile testing,” in Proceedings of

the 39th International Conference on Software Engineering, ICSE’17,

Buenos Aires, Argentina, May 20-28 , 2017, pp. 643–653.

pp. 77–83.

2011, pp. 252–261.

2014, pp. 1–5.

Austria, December 2-4 , 2013, p. 68.

- 11 , 2014, p. 29.

15-20 , 2013, pp. 67–77.

hierarchy-viewer.html, 2012.

16-19 , 2014, pp. 204–217.

pp. 599–609.

471.

18:15.

37

the Foundations of Software Engineering, SIGSOFT/FSE’12, Cary, NC, [26] C. Hu and I. Neamtiu, “Automating GUI testing for android applica-

USA - November 11 - 16 , 2012, p. 59. tions,” in Proceedings of the 6th International Workshop on Automation

[5] J. C. King, “Symbolic execution and program testing,” Commun. ACM , of Software Test, AST’11, Waikiki, Honolulu, HI, USA, May 23-24 , 2011,

[6] D. Amalfitano, A. R. Fasolino, P. Tramontana, S. D. Carmine, and [27] D. Amalfitano, A. R. Fasolino, and P. Tramontana, “A GUI crawling-

| A. M. Memon, “Using GUI ripping for automated testing of android | based technique for android mobile application testing,” in | the Fourth |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| applications,” in | IEEE/ACM International Conference on Automated | IEEE International Conference on Software Testing, Verification and |  |  |  |  |  |  |  |
| Software Engineering, ASE’12, Essen, Germany, September 3-7 | , 2012, | Validation, | Berlin, | Germany, | 21-25 | March, | Workshop | Proceedings | , |

[7] W. Yang, M. R. Prasad, and T. Xie, “A grey-box approach for auto- [28] N. Group, “Intent fuzzer,” http://www.isecpartners.com/tools/

mated gui-model generation of mobile applications,” in Fundamental mobile-security/intent-fuzzer.aspx, 2009.

Approaches to Software Engineering - 16th International Conference, [29] R. Sasnauskas and J. Regehr, “Intent fuzzer: crafting intents of death,” in

| FASE’13, Held as Part of the European Joint Conferences on Theory and | Proceedings of the Joint International Workshop on Dynamic Analysis |  |
| --- | --- | --- |
| Practice of Software, ETAPS’13, Rome, Italy, March 16-24. Proceedings | , | (WODA) and Software and System Performance Testing, Debugging, and |
| 2013, pp. 250–265. | Analytics (PERTEA), WODA+PERTEA’14, San Jose, CA, USA, July 22, | , |

tematic testing of android apps,” in Proceedings of the ACM SIGPLAN [30] H. Ye, S. Cheng, L. Zhang, and F. Jiang, “Droidfuzzer: Fuzzing the

International Conference on Object Oriented Programming Systems android apps with intent-filter tag,” in The 11th International Conference

Languages & Applications, OOPSLA’13, part of SPLASH’13, Indi- on Advances in Mobile Computing & Multimedia, MoMM’13, Vienna,

[9] W. Choi, G. C. Necula, and K. Sen, “Guided GUI testing of android [31] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein, Y. L.

| apps with minimal restart and approximate learning,” in | Proceedings of | Traon, D. Octeau, and P. McDaniel, “Flowdroid: precise context, flow, |
| --- | --- | --- |
| the 2013 ACM SIGPLAN International Conference on Object Oriented | field, object-sensitive and lifecycle-aware taint analysis for Android |  |
| Programming Systems Languages & Applications, OOPSLA’13, part of | apps,” in | ACM SIGPLAN Conference on Programming Language Design |
| SPLASH’13, Indianapolis, IN, USA, October 26-31 | , 2013, pp. 623–640. | and Implementation, PLDI ’14, Edinburgh, United Kingdom - June 09 |

using multi-level GUI comparison criteria,” in Proceedings of the 31st [32] F. Gross, G. Fraser, and A. Zeller, “EXSYST: search-based GUI testing,”

IEEE/ACM International Conference on Automated Software Engineer- in 34th International Conference on Software Engineering, ICSE’12,

ing, ASE’16, Singapore, September 3-7 , 2016, pp. 238–249. June 2-9, Zurich, Switzerland , 2012, pp. 1423–1426.

[11] K. Mao, M. Harman, and Y. Jia, “Sapienz: multi-objective automated [33] C. S. Jensen, M. R. Prasad, and A. Møller, “Automated testing with

testing for android applications,” in Proceedings of the 25th International targeted event sequence generation,” in International Symposium on

Symposium on Software Testing and Analysis, ISSTA’16, Saarbr¨ ucken, Software Testing and Analysis, ISSTA ’13, Lugano, Switzerland, July

[12] Z. Shan, T. Azim, and I. Neamtiu, “Finding resume and restart errors [34] Google, “Hierarchy viewer,” http://developer.android.com/tools/help/

national Conference on Object-Oriented Programming, Systems, Lan- [35] S. Hao, B. Liu, S. Nath, W. G. J. Halfond, and R. Govindan, “PUMA:

| guages, and Applications, OOPSLA’16, part of SPLASH’16, Amsterdam, | programmable ui-automation for large-scale dynamic analysis of mobile |  |  |
| --- | --- | --- | --- |
| The Netherlands, October 30 - November 4 | , 2016, pp. 864–880. | apps,” in | The 12th Annual International Conference on Mobile Systems, |
| [13] | H. Zhang and A. Rountev, “Analysis and testing of notifications in | Applications, and Services, MobiSys’14, Bretton Woods, NH, USA, June |  |

Conference on Software Engineering, ICSE’17, Buenos Aires, Argentina, [36] H. van der Merwe, B. van der Merwe, and W. Visser, “Execution

| May 20-28 | , 2017, pp. 347–357. | and property specifications for jpf-android,” | ACM SIGSOFT Software |
| --- | --- | --- | --- |
| [14] | S. R. Choudhary, A. Gorla, and A. Orso, “Automated test input genera- | Engineering Notes | , vol. 39, no. 1, pp. 1–5, 2014. |

tion for android: Are we there yet? (E),” in 30th IEEE/ACM International [37] R. Mahmood, N. Mirzaei, and S. Malek, “EvoDroid: segmented evo-

| Conference on Automated Software Engineering, ASE’15, Lincoln, NE, | lutionary testing of android apps,” in | Proceedings of the 22nd ACM |  |
| --- | --- | --- | --- |
| USA, November 9-13 | , 2015, pp. 429–440. | SIGSOFT International Symposium on Foundations of Software Engi- |  |
| [15] | S. Yang, D. Yan, H. Wu, Y. Wang, and A. Rountev, “Static control- | neering, ESEC/FSE’14, Hong Kong, China, November 16 - 22 | , 2014, |

IEEE/ACM International Conference on Software Engineering, ICSE’15, [38] N. Mirzaei, H. Bagheri, R. Mahmood, and S. Malek, “SIG-Droid:

| Florence, Italy, May 16-24 | , 2015, pp. 89–99. | Automated system input generation for android applications,” in | the 26th |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [16] | R. | Vall´ | ee-Rai, | P. | Lam, | C. | Verbrugge, | P. | Pominville, | and | F. | Qian, | IEEE International Symposium on Software Reliability Engineering, |
| “Soot (poster session): A java bytecode optimization and annotation | ISSRE’15, Gaithersbury, Maryland, USA, November 2-5 | , 2015, pp. 461– |  |  |  |  |  |  |  |  |  |  |  |

Object-oriented Programming, Systems, Languages, and Applications [39] G. Hu, X. Yuan, Y. Tang, and J. Yang, “Efficiently, effectively detect-

| (Addendum) | , ser. OOPSLA’00, 2000, pp. 113–114. | ing mobile app bugs with appdoctor,” in | Ninth Eurosys Conference, |
| --- | --- | --- | --- |
| [17] | F. Limited, “Free and open source app repository.” https://f-droid.org/, | EuroSys’14, Amsterdam, The Netherlands, April 13-16 | , 2014, pp. 18:1– |


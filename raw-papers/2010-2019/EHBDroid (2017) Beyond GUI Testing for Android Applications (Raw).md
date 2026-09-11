---
title: "EHBDroid: Beyond GUI Testing for Android Applications"
author: "Wei Song, Xiangxing Qian, and Jeff Huang"
creator: "LaTeX with hyperref package"
pages: 11
---

# EHBDroid: Beyond GUI Testing for Android Applications

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


*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

*[Image: Page 6 Image]*

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


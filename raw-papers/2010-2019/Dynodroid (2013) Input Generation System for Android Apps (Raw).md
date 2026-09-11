---
title: "29_Machiry_et_al.,_Dynodroid_Input_Generation_System"
creator: "TeX"
pages: 11
---

# 29_Machiry_et_al.,_Dynodroid_Input_Generation_System

> **總頁數**：11 頁

---

## Page 1

Dynodroid: An Input Generation System for Android Apps

Aravind Machiry Rohan Tahiliani Mayur Naik

Georgia Institute of Technology, USA

{amachiry, rohan_tahil, naik}@gatech.edu

| ABSTRACT | What-if analyses of programs are broadly classified into |  |  |
| --- | --- | --- | --- |
| We present a system Dynodroid for generating relevant in- | static and dynamic. Static analyses are hindered by features |  |  |
| puts to unmodified Android apps. Dynodroid views an app | commonly used by mobile apps such as code obfuscation, na- |  |  |
| as an event-driven program that interacts with its environ- | tive libraries, and a complex SDK framework. As a result, |  |  |
| ment by means of a sequence of events through the Android | there is growing interest in dynamic analyses of mobile apps |  |  |
| framework. | By instrumenting the framework once and for | (e.g., [1, 12, 13, 25]). | A key challenge to applying dynamic |
| all, Dynodroid monitors the reaction of an app upon each | analysis ahead-of-time, however, is obtaining program in- |  |  |
| event in a lightweight manner, using it to guide the gener- | puts that adequately exercise the program’s functionality. |  |  |
| ation of the next event to the app. | Dynodroid also allows | We set out to build a system for generating inputs to |  |
| interleaving events from machines, which are better at gen- | mobile apps on Android, the dominant mobile app platform, |  |  |
| erating a large number of simple inputs, with events from | and identified five key criteria that we felt such a system |  |  |
| humans, who are better at providing intelligent inputs. | must satisfy in order to be useful: |  |  |

We evaluated Dynodroid on 50 open-source Android apps,

| and compared it with two prevalent approaches: users man- | • | Robust | : Does the system handle real-world apps? |  |
| --- | --- | --- | --- | --- |
| ually exercising apps, and Monkey, a popular fuzzing tool. | • | Black-box | : | Does the system forgo the need for app |
| Dynodroid, humans, and Monkey covered 55%, 60%, and | sources and the ability to decompile app binaries? |  |  |  |
| 53%, respectively, of each app’s Java source code on average. | • | Versatile | : | Is the system capable of exercising impor- |
| Monkey took 20X more events on average than Dynodroid. | tant app functionality? |  |  |  |
| Dynodroid also found 9 bugs in 7 of the 50 apps, and 6 bugs | • | Automated | : Does the system reduce manual effort? |  |

in 5 of the top 1,000 free apps on Google Play.

• Efficient : Does the system generate concise inputs, i.e.,

Categories and Subject Descriptors avoid generating redundant inputs?

D.2.5 [ Software Engineering ]: Testing and Debugging

This paper presents a system Dynodroid that satisfies

General Terms the above criteria. Dynodroid views a mobile app as an

event-driven program that interacts with its environment by

Reliability, Experimentation means of a sequence of events. The main principle under-

Keywords lying Dynodroid is an observe-select-execute cycle, in which

it first observes which events are relevant to the app in the

GUI testing, testing event-driven programs, Android current state, then selects one of those events, and finally

executes the selected event to yield a new state in which

| 1. | INTRODUCTION | it repeats this process. | This cycle is relatively straightfor- |  |
| --- | --- | --- | --- | --- |
| Mobile apps—programs that run on advanced mobile de- | ward for | UI events | —inputs delivered via the program’s user |  |
| vices such as smartphones and tablets—are becoming in- | interface (UI) such as a tap or a gesture on the device’s |  |  |  |
| creasingly prevalent. Unlike traditional enterprise software, | touchscreen. | In the | observer | stage, Dynodroid determines |
| mobile apps serve a wide range of users in heterogeneous and | the layout of widgets on the current screen and what kind |  |  |  |
| demanding conditions. As a result, mobile app developers, | of input each widget expects. | In the | selector | stage, Dyno- |
| testers, marketplace auditors, and ultimately end users can | droid uses a novel randomized algorithm to select a widget |  |  |  |
| benefit greatly from what-if analyses of mobile apps. | in a manner that penalizes frequently selected widgets with- |  |  |  |

out starving any widget indefinitely. Finally, in the executor

stage, Dynodroid exercises the selected widget.

In practice, human intelligence may be needed for exer-

| Permission to make digital or hard copies of all or part of this work for | cising certain app functionality, in terms of generating both |  |
| --- | --- | --- |
| personal or classroom use is granted without fee provided that copies are | individual events (e.g., inputs to text boxes that expect valid |  |
| not made or distributed for profit or commercial advantage and that copies | passwords) and sequences of events (e.g., a strategy for win- |  |
| bear this notice and the full citation on the first page. To copy otherwise, to | ning a game). | For this reason, Dynodroid allows a user to |
| republish, to post on servers or to redistribute to lists, requires prior specific | observe an app reacting to events as it generates them, and |  |

permission and/or a fee.

ESEC/FSE ’13, August 18-26, 2013, Saint Petersburg, Russia lets the user pause the system’s event generation, manually

Copyright 2013 ACM 978-1-4503-2237-9/13/08 ...$15.00. generate arbitrary events, and resume the system’s event

---

## Page 2

| generation. Our overall system thereby combines the bene- | 1. We propose an effective approach for generating in- |  |  |
| --- | --- | --- | --- |
| fits of both the automated and manual approaches. | puts to mobile apps. It is based on a “observe-select- |  |  |
| We discussed how Dynodroid handles UI events, but sig- | execute” principle that efficiently generates a sequence |  |  |
| nificant functionality of mobile apps is controlled by non-UI | of relevant events. | To adequately exercise app func- |  |
| events we call | system events | , such as an incoming SMS mes- | tionality, it generates both UI and system events, and |
| sage, a request by another app for the device’s audio, or a | seamlessly combines events from human and machine. |  |  |
| notification of the device’s battery power running low. Sat- | 2. We show how to observe, select, and execute system |  |  |
| isfying our five desirable criteria in the presence of system | events for Android in a mobile device emulator with- |  |  |
| events is challenging for two reasons. | First, the number of | out modifying the app. | The central insight is to tai- |
| possible system events is very large, and it is impractical to | lor these tasks to the vast common framework against |  |  |
| generate all possible permutations of those events. | For in- | which all apps are written and from which they pri- |  |
| stance, Android supports 108 different broadcast receivers, | marily derive their functionality. |  |  |
| each of which can send notifications called | intents | to an app. | 3. We present extensive empirical evaluation of the sys- |
| Second, many system events have structured data that must | tem, comparing it to the prevalent approaches of man- |  |  |
| be constructed and dispatched correctly to the app along- | ual testing and automated fuzzing, using metrics in- |  |  |
| side an intent. | For example, generating an incoming SMS | cluding code coverage and number of events, for di- |  |
| message event entails constructing and sending a suitable | verse Android apps including both open-source apps |  |  |
| object of class | android.telephony.SmsMessage | . | and top free marketplace apps. |

A distinctive aspect of mobile apps is that all such apps,

Dynodroid addresses the problem of handling a very large

number of system events by using the observation that in

them we call relevant events. An event is relevant to an app

if the app has registered a listener for the event with the

framework. Finding when an app registers (or unregisters)

such a listener does not require modifying the app: it suf-

fices to instrument the framework once and for all. The ob-

server monitors the app’s interaction with the framework via

this instrumentation, and presents the selector only events

that the app has registered to listen. Finally, the executor

constructs any data associated with the selected event and

dispatches it to the app. A salient aspect of Dynodroid con-

cerns how it constructs this data. For instance, the listener

for network connectivity change events expects an object of

class android.net.NetworkInfo describing the new status

of the network interface. Dynodroid cannot arbitrarily cre-

ate such objects; it must obtain them from a pool maintained

by system service android.net.ConnectivityManager . Fi-

nally, whenever an event is executed, any previously relevant

event may become irrelevant and vice versa, for the next

observe-select-execute cycle.

We implemented Dynodroid for the Android platform and

applied it to 50 diverse, real-world, open-source apps. We

compared the performance of Dynodroid in terms of each

app’s Java source code coverage to two prevalent approaches:

one involving expert users manually exercising these apps,

and another using Monkey [7], a popular fuzzing tool. Dyno-

droid, humans, and Monkey covered 55%, 60%, and 53%

code, respectively, on average per app. Dynodroid was able

to cover 83% of the code covered by humans per app on av-

erage, showing its ability to automate testing. Also, Dyno-

droid achieved peak coverage faster than Monkey, with Mon-

key requiring 20X more events on average, showing the ef-

fectiveness of our randomized event selection algorithm. Fi-

nally, Dynodroid found 9 bugs in 7 of the 50 apps. In a

separate experiment, we applied Dynodroid to the top 1,000

free apps in Google Play, and it found 6 bugs in 5 of them.

We summarize the main contributions of our work:

Section 8 concludes.

This section presents the system architecture of Dyno-

droid. Algorithm 1 shows the overall algorithm of Dyno-

droid. It takes as input the number n of events to generate

to an app under test. It produces as output a list L of n

events it generates. The first generated event is to install and

start the app in a mobile device emulator. The remaining

n − 1 events are generated one at a time in an observe-select-

execute cycle. Each of these events constitutes either a UI

input or non-UI input to the app, which we call UI event

and system event , respectively. The two kinds of events are

conceptually alike: each event of either kind has a type and

associated data. We distinguish between them because, as

we explain below, Dynodroid uses different mechanisms to

handle them. The executor executes the current event, de-

noted e , in the current emulator state, denoted s , to yield a

new emulator state that overwrites the current state. Next,

the observer computes which events are relevant in the new

state. We denote the set of relevant events E . Finally, the

selector selects one of the events from E to execute next,

and the process is repeated.

Figure 1 presents a dataflow diagram of Dynodroid that

provides more details about the mechanisms it uses to im-

plement the executor , the observer , and the selector

on the Android platform.

The executor triggers a given event using the appropri-

ate mechanism based on the event kind. It uses the Android

Debug Bridge ( adb ) to send the event to an Android device

emulator that is running the app under test. For UI events,

the ADB host talks to the ADB daemon ( adbd ) on the emu-

lator via the monkeyrunner tool. Note that this tool, which

is used to send events to an emulator via an API, is unre-

lated to the Monkey fuzz testing tool, which runs in an adb

shell directly on the emulator. For system events, the ADB

host talks to the Activity Manager tool ( am ) on the emu-

lator, which can send system events as intents to running

apps. Section 3 describes the executor in further detail.

| regardless of how diverse their functionality, | are written | The rest of the paper is organized as follows. | Section 2 |
| --- | --- | --- | --- |
| against a common framework that implements a significant | describes the overall system. The next three sections present |  |  |
| portion of the app’s functionality. | Dynodroid exploits this | its three main parts: Section 3 the executor, Section 4 the |  |
| aspect pervasively in observing, selecting, and executing sys- | observer, and Section 5 the selector. Section 6 presents our |  |  |
| tem events, as we describe next. | experimental results. | Section 7 surveys related work and |  |
| practice, a mobile app reacts to only a small fraction of | 2. | SYSTEM ARCHITECTURE |  |

---

## Page 3

Ini=al(event( e (((install(and(start(app) %

(

(

(

e (is(system( (

App(under(test(

event(

| event( | ( |  |
| --- | --- | --- |
| Monkey( | ( | ADB(Host( |
| Runner( | ( | ADB(Daemon( |

(

(

Executor( Device(Emulator(

(

(

Figure 1 :

e := event to install and start app under test

append e to L

// Execute event e in current state s to yield updated state.

// Compute set E of all events relevant in current state s .

// Select an event e ∈ E to execute in next iteration.

e := selector ( E )

end for

The observer computes the set of events that are rele-

vant to the app under test in the current emulator state. It

consists of two parts to handle the two kinds of events: the

Hierarchy Viewer tool for UI events, and the instrumented

framework (SDK) for system events. Hierarchy Viewer pro-

vides information about the app’s GUI elements currently

displayed on the device’s screen. The observer computes

the set of relevant UI events E 1 from this information. The

instrumented SDK provides information about broadcast re-

ceivers and system services for which the app is currently

registered. The observer computes the set of relevant sys-

tem events E 2 from this information. It provides the set of

all relevant events E = E 1 ∪ E 2 to the selector . Section 4

provides more details about the observer .

The selector selects an event from E as the next event

to be triggered. Dynodroid implements various selection

strategies that one can choose from upfront, including deter-

ministic vs. randomized, and history dependent vs. history

manual input generation. Figure 2 shows how Dynodroid

allows switching between machine and human. The execu-

Selected(event( e (from( E%

Intercepted( System(

events(

calls(from(

apps(to(SDK( E2%

Selector(

Observer(

Hierarchy(

Viewer( UI(

events(

E1%

Dataflow diagram of Dynodroid for the Android platform.

start% START& human% machine%

console%commands%

events%to%app% final%

allows the human to exercise the app uninterrupted in the

emulator, until a RESUME command is received from the

console. At this point, the executor switches to machine

mode and generates events until the given bound n is reached

or a PAUSE command is received from the console. In the

latter case, the executor switches to human mode again.

Human inputs do not count towards the bound n . Also,

nothing prevents the human from exercising the app in ma-

chine mode as well, along with the machine. Finally, the

STOP command from the console stops Dynodroid.

The executor executes an event, chosen by the selec-

tor , on the emulator via the Android Debug Bridge ( adb ).

It uses separate mechanisms for executing UI events and sys-

tem events. UI events are triggered using the monkeyrunner

tool. This tool is a wrapper around adb that provides an

API to execute UI events. System events are triggered us-

ing the Activity Manager tool ( am ). Broadcast events of any

type can be triggered using this tool provided the correct

arguments are supplied.

4. OBSERVER

goal of the observer is to efficiently compute as small a

4.1 UI Events

| ( | Ac=vity( | Instrumented( | All(relevant( |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ( | Manager( | SDK( | events( |  |  |  |  |  |
| e | (is(UI( | ( | E | (=( | E1 | (U( | E2% |  |
| Algorithm 1 | Overall algorithm of Dynodroid. | RESUME& |  |  |  |  |  |  |
| INPUT: | Number | n > | 0 of events to generate. | emulator% |  |  |  |  |
| OUTPUT: | List | L | of | n | events. | human% | executor% |  |
| L | := empty list | state% | mode% | mode% |  |  |  |  |
| s | := initial program state | console% |  |  |  |  |  |  |
| for | i | from | 1 | to | n | do | state%transi1ons% | PAUSE& |
| s | := | executor | ( | e | , | s | ) | state% |
| E | := | observer | ( | s | ) | Figure 2 | : | State transition diagram of Dynodroid. |
| oblivious strategies. Section 5 describes these strategies and | The | observer | computes the set of relevant events after an |  |  |  |  |  |
| Section 6 evaluates them on a code coverage client for 50 | event is executed. We consider an event | relevant | if triggering |  |  |  |  |  |
| open-source apps. | it may result in executing code that is part of the app. The |  |  |  |  |  |  |  |
| 3. | EXECUTOR | set of relevant events as possible without missing any. This |  |  |  |  |  |  |
| Dynodroid allows both machine and human to generate | section describes how the | observer | computes relevant UI |  |  |  |  |  |
| events in order to combine the benefits of automated and | events (Section 4.1) and relevant system events (Section 4.2). |  |  |  |  |  |  |  |
| tor | listens to commands from a console and starts in | human | These are events generated by the SDK in response to |  |  |  |  |  |
| mode | , in which it does not trigger any events and instead | interaction by users with the device’s input mechanisms. |  |  |  |  |  |  |

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

---

## Page 4

Table 1 : Mapping registered callback methods and location, etc. The SDK provides one of two means by which

overridden methods to relevant UI events. an app can receive each type of system event: broadcast

Relevant Event

Tap Tap Drag Text

(short) (long)

| onTouchEvent | X | X | X |
| --- | --- | --- | --- |
| performLongClick | X |  |  |
| performClick | X |  |  |

are the most common input mechanisms, the mechanisms

we do not support (keyboard, trackball, etc.) are device-

dependent, and there is often redundancy among different

UI inputs, such as an incoming phone call, a change in geo-

receiver and system service . In either case, the app registers

a callback to be called by the SDK when the event occurs.

The app may later unregister it to stop receiving the event.

manually modified to inject the instrumentation. A system

event becomes relevant when an app registers to receive it

not only which system events are relevant, but also what

data to associate with each. Unlike for UI events, however,

tem services (Section 4.2.2).

4.2.1 Broadcast Receiver Events

Object[] p = (Object[]) b.get("pdus");

for (int i = 0; i < pdus.length; i++)

} };

| If app registers callback: | The | observer | uses the same mechanism for extracting |  |
| --- | --- | --- | --- | --- |
| onClickListener | X | relevant system events via broadcast receivers and system |  |  |
| onLongClickListener | X | services: | it instruments the SDK to observe when an app |  |
| onTouchListener | X | X | X | registers (or unregisters) for each type of system event. This |
| onKeyListener | X | instrumented SDK is a file system.img that is loaded on the |  |  |
| onCreateContextMenuListener | X | emulator during bootup. | It is produced once and for all |  |
| If app overrides method: | by compiling Java source code of the original SDK that is |  |  |  |
| onKeyDown | X | and, conversely, it becomes irrelevant when an app unregis- |  |  |
| onKeyUp | X | ters it. As in the case of UI events, the | observer | computes |
| Dynodroid supports two input mechanisms: touchscreen and | this data can be highly-structured SDK objects (instead of |  |  |  |
| navigation buttons (specifically, “back” and “menu” buttons). | primitive-typed data). We next outline how the | observer |  |  |
| We found these sufficient in practice, for three reasons: they | handles specific broadcast receivers (Section 4.2.1) and sys- |  |  |  |
| input mechanisms. | Android provides two ways for apps to register for system |  |  |  |
| The | observer | analyzes the app’s current UI state in order | events via a broadcast receiver, depending on the desired |  |
| to compute relevant UI events. First, it deems clicking each | lifetime: dynamically or statically. In the dynamic case, the |  |  |  |
| navigation button as a relevant UI event, since these buttons | receiver’s lifetime is from when Context.registerReceiver() is |  |  |  |
| are always enabled. Second, it inspects the | view hierarchy | , | called to either until Context.unregisterReceiver() is called |  |
| which is an Android-specific tree representation of the app’s | or until the lifetime of the registering app component. | In |  |  |
| UI currently displayed on the touchscreen. | The SDK pro- | the static case, the receiver is specified in file AndroidMani- |  |  |
| vides two ways by which an app can react to inputs to a UI | fest.xml, and has the same lifetime as the app. In either case, |  |  |  |
| element: by overriding a method of the corresponding View | the receiver defines a callback method overriding Broadcas- |  |  |  |
| object’s class, or by registering a callback with it. | tReceiver.onReceive() that the SDK calls when the event |  |  |  |
| The SDK dispatches each input on the touchscreen to the | occurs (we provide an example below). The | observer | sup- |  |
| root node of the view hierarchy, which in turn depending on | ports both kinds of receivers. |  |  |  |
| the position of the input dispatches it recursively to one of | The Gingerbread SDK version we instrumented has 108 |  |  |  |
| its children, until the view to which the input was intended | different kinds of system events as | intents | for which an app |  |
| executes a callback and returns true, denoting that the in- | may register via a broadcast receiver. | As a proof of con- |  |  |
| put was successfully handled. | The | observer | obtains the | cept, we chose the top 25 receivers used by the top 1,000 |
| view hierarchy from a service called ViewServer that runs | free apps in the Google Play market. Supporting additional |  |  |  |
| on Android devices having debug support. Once it obtains | intents is straightforward: it involves identifying the type of |  |  |  |
| the view hierarchy, it considers only the View objects at leaf | data associated with the intent and providing valid values |  |  |  |
| nodes of the tree as interesting, as these correspond to visi- | for the data. The data includes an optional URI, and a Bun- |  |  |  |
| ble UI elements that users can interact with. It extracts two | dle object which is a key-value map that contains any extra |  |  |  |
| kinds of data from each such object about the correspond- | information. | Finally, for statically registered receivers, we |  |  |
| ing UI element: (a) the set of callback methods registered | also explicitly identify the receiver in the intent, since un- |  |  |  |
| and the set of methods overridden by the app, for listening | like UI events which are dispatched to a single View object, |  |  |  |
| to inputs to this UI element, and (b) the location and size | broadcast intents are by default dispatched to all receivers |  |  |  |
| of the UI element on the touchscreen (the position of its | (possibly from several apps) that register for them. |  |  |  |
| top left corner, its width, height, and scaling factor). | The | Table 3 shows the type and values of the data used by the |  |  |
| native Hierarchy Viewer does not provide all of the above | observer | for our 25 chosen broadcast intents. All the data |  |  |
| data; we modified the Android SDK source to obtain it. The | shown, except those of type URI, are provided in a Bun- |  |  |  |
| observer | uses the data in item (a) to compute which UI | dle object. For instance, an app may register the following |  |  |
| events are relevant, as dictated by Table 1. It supports all | receiver for the | SMS RECEIVED | intent which is broadcast |  |
| common touchscreen inputs: | tap inputs, limited kinds of | upon incoming SMS messages: |  |  |
| gestures, and text inputs. | Finally, the | observer | uses the | public class SmsReceiver extends BroadcastReceiver { |
| data in item (b) to compute the parameters of each such | @Override public void onReceive(Context c, Intent e) { |  |  |  |
| event, as dictated by Table 2. | Bundle b = e.getExtras(); |  |  |  |
| 4.2 | System Events | SmsMessage[] a = new SmsMessage[p.length]; |  |  |
| These are events generated by the SDK in response to non- | a[i] = SmsMessage.createFromPdu((byte[]) p[i]); |  |  |  |

---

## Page 5

Table 2 : User event parameters: l , t , w , h denote left position, top position, width, and height of the

view, respectively. TL, TR, BL, BR, MB, MT, ML, MR denote top left/right, bottom left/right, and mid

bottom/top/left/right points of the view, respectively.

| Event Type | Parameters | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tap | Tap( | l | + | w | /2, | t | + | h | /2) | trigger Tap at center of view |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LongTap | LongTap( | l | + | w | /2, | t | + | h | /2) | trigger LongTap at center of view |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Drag | random one of: Drag( | l | , | t | , | l | + | w | , | t | + | h | ), Drag( | l | + | w | , | t | + | h | , | l | , | t | ), | randomly trigger one of gestures: |  |  |  |
| Drag( | l | , | t | + | h | , | l | + | w | , | t | ), Drag( | l | + | w | , | t | , | l | , | t | + | h | ), | TL to BR, BR to TL, BL to TR, |  |  |  |  |
| Drag( | l | , | t | + | h | /2, | l | + | w | , | t | + | h | /2), Drag( | l | + | w | , | t | + | h | /2, | l | , | t | + | h | /2), | TR to BL, ML to MR, MR to ML, |
| Drag( | l | + | w | /2, | t | , | l | + | w | /2, | t | + | h | ), Drag( | l | + | w | /2, | t | + | h | , | l | + | w | /2, t) | MT to MB, MB to MT |  |  |
| Text | arbitrary fixed string | trigger arbitrary text input |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To trigger this event, the | executor | serializes the appro- | Algorithm 2 | Event selection algorithm | BiasedRandom | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| priate intent along with a Bundle object that maps a kay | 1: | var | G | : map from (event, set of events) pairs to int |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| named “pdus” to an SmsMessage object array representing | 2: | G | := empty map |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| arbitrary but well-formed phone numbers and message texts. | 3: | INPUT: | Set | E | of relevant events. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

4: OUTPUT: An event in E .

| 4.2.2 | System Service Events | 5: | for each | ( | e | in | E | ) | do |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| System services are a fixed set of processes that provide | 6: | if | (( | e, E | ) is not in domain of | G | ) | then |  |  |  |  |
| abstractions of different functionality of an Android device. | 7: | // Initialize score of event | e | in context | E | . |  |  |  |  |  |  |
| We distinguish services whose offered functionality depends | 8: | G | ( | e, E | ) := init score( | e | ) |  |  |  |  |  |
| on app-provided data from those that are independent of | 9: | end if |  |  |  |  |  |  |  |  |  |  |
| such data. | We call such services | internally | vs. | externally | 10: | end for |  |  |  |  |  |  |
| triggered, as they depend on data internal or external to | 11: | var | L | : map from events to int |  |  |  |  |  |  |  |  |
| the app under test. For instance, the AlarmManager service | 12: | L | := map from each event in | E | to 0 |  |  |  |  |  |  |  |
| is internally triggered, as it depends on the alarm duration | 13: | while | true | do |  |  |  |  |  |  |  |  |
| given by an app, but the LocationManager service is exter- | 14: | e | := event chosen uniformly at random from | E |  |  |  |  |  |  |  |  |
| nally triggered, as it depends on the device’s geo-location. | 15: | if | ( | L | ( | e | ) = | G | ( | e, E | )) | then |
| Dynodroid only controls externally triggered services as the | 16: | // Select | e | this time, but decrease its chance of being |  |  |  |  |  |  |  |  |
| app itself controls internally triggered services. | 17: | // selected in context | E | in future calls to | selector | . |  |  |  |  |  |  |
| Table 4 shows how Dynodroid handles events of each ex- | 18: | G | ( | e, E | ) := | G | ( | e, E | ) + 1 |  |  |  |
| ternally triggered service. | The “Register/Unregister Mech- | 19: | return | e |  |  |  |  |  |  |  |  |
| anism” shows how an app registers or unregisters for the | 20: | else |  |  |  |  |  |  |  |  |  |  |
| service, which the | observer | observes via SDK instrumen- | 21: | // Increase chance of selecting | e | in the next iteration. |  |  |  |  |  |  |
| tation. Since services are global components, the | observer | 22: | L | ( | e | ) := | L | ( | e | ) + 1 |  |  |
| uses the ID of the app under test to filter out observing other | 23: | end if |  |  |  |  |  |  |  |  |  |  |
| apps that may also register or unregister for these services. | 24: | end while |  |  |  |  |  |  |  |  |  |  |
| The “Callback Mechanism” shows how the app specifies the | 25: | procedure | init score( | e | ) : | int |  |  |  |  |  |  |
| callback to handle events by the service. Lastly, the “Trigger | 26: | case | (e) | of |  |  |  |  |  |  |  |  |
| Mechanism” shows how the | executor | triggers the callback, | 27: | Text event: | return | -1 |  |  |  |  |  |  |
| usually via a command sent from the ActivityManager tool | 28: | non-Text UI event: | return | 1 |  |  |  |  |  |  |  |  |
| running on the emulator (see Section 3). | 29: | system event: | return | 2 |  |  |  |  |  |  |  |  |
| The following example showing how an app may use the | 30: | end case |  |  |  |  |  |  |  |  |  |  |

LocationManager service:

GpsStatus.Listener l = new GpsStatus.Listener() {

@Override public void onGpsStatusChanged(int event) {...} 5. SELECTOR

};

| LocationManager lm = getSystemService(LOCATION_SERVICE); | The | selector | selects an event for the | executor | to ex- |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lm.addGpsStatusListener(l); | ecute from the set of relevant events | E | computed by the |  |  |  |  |
| ...; | observer | . We implemented three different selection strate- |  |  |  |  |  |
| lm.removeGpsStatusListener(l); | gies in the | selector | , called | Frequency | , | UniformRandom | , and |

BiasedRandom . This section describes these strategies.

| From the point at which the app registers to listen to GPS | The | Frequency | strategy selects an event from | E | that has |
| --- | --- | --- | --- | --- | --- |
| status changes by calling addGpsStatusListener() to the point | been selected least frequently by it so far. The rationale is |  |  |  |  |
| at which it unregisters by calling removeGpsStatusListener(), | that infrequently selected events have a higher chance of ex- |  |  |  |  |
| the | observer | regards GPS status change as a relevant sys- | ercising new app functionality. A drawback of this strategy |  |  |
| tem event. | If the | selector | described in the next section | is that its deterministic nature leads the app to the same |  |
| selects this event, then the | executor | triggers it by sending | state in repeated runs. In practice, different states might be |  |  |
| telnet command “geo fix | G | ” to the emulator, where | G | is an | reached in different runs because of non-determinism inher- |
| arbitrary geo-location (a triple comprising a latitude, longi- | ent in dynamic analysis of Android apps, due to factors such |  |  |  |  |
| tude, and altitude). This in turn results in invoking callback | as concurrency and asynchrony; however, we cannot rely on |  |  |  |  |
| onGpsStatusChanged() defined by the app. | them to cover much new app functionality. |  |  |  |  |

---

## Page 6

Table 3 : Broadcast receiver events with associated data as implemented in Dynodroid. These implemented

events have no associated data: BATTERY [CHANGED | LOW | OKAY] , ACTION POWER [DIS]CONNECTED ,

ACTION SHUTDOWN , TIME SET , AUDIO BECOMING NOISY , DATE CHANGED , USER PRESENT , ME-

DIA EJECT , and BOOT COMPLETED .

| Action Name | Data Type : Description | Data Value |
| --- | --- | --- |
| APPWIDGET UPDATE | int[] : IDs of App Widgets to update | random (1-10) sized array of random (0-1000) ints |
| android.net.NetworkInfo : status of | random NetworkInfo object from |  |

CONNECTIVITY CHANGE

| the network interface | android.net.ConnectivityManager |  |
| --- | --- | --- |
| int : uid assigned to new package, | uid of random installed package, |  |
| PACKAGE ADDED | bool : true if this follows a ‘removed’ | random bool |

broadcast for the same package

| int : uid previously given to package, | uid of random installed package, |
| --- | --- |
| bool : true if removing entire app, | random bool, |

PACKAGE REMOVED

bool : true if an ‘added’ broadcast random bool

for the same package will follow

PACKAGE REPLACED int : uid assigned to new package uid of random installed package

URI : path to mount point of media, “/mnt/sdcard”,

MEDIA MOUNTED

| bool : true if media is read-only | false |  |
| --- | --- | --- |
| TIMEZONE CHANGED | TimeZone : time-zone representation | America/Los Angeles time-zone |
| android.view.KeyEvent : key event | KeyEvent object with action as ACTION UP and |  |

MEDIA BUTTON

| that caused this broadcast | value as KEYCODE MEDIA PLAY PAUSE |
| --- | --- |
| android.telephony.SmsMessage[] : | array of 1 SmsMessage object with arbitrary |

SMS RECEIVED

array of received SMS messages MSISDN and message

MEDIA UNMOUNTED URI : path to mount point of media “/mnt/sdcard”

int : phone state (idle | ringing | offhook), 1 (ringing),

PHONE STATE

| String : incoming phone number | an arbitrary MSISDN |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MEDIA SCANNER FINISHED | URI | “/mnt/sdcard” |  |  |  |  |  |  |
| NEW OUTGOING CALL | String: outgoing phone number | an arbitrary MSISDN |  |  |  |  |  |  |
| The | UniformRandom | strategy circumvents the above prob- | recorded in global variable | G | that maps each pair ( | e, E | ) to a |  |
| lem by selecting an event from | E | uniformly at random. This | score. The map starts empty and is populated lazily. At any |  |  |  |  |  |
| is essentially the strategy used by the Monkey fuzz testing | instant, the score for a pair ( | e, E | ) in the map is either | − | 1, |  |  |  |
| tool, with three key differences. | First, Monkey can only | meaning event | e | is blacklisted in context | E | (i.e., | e | will never |
| generate UI events, preventing it from covering app func- | be selected in context | E | ), or it is a non-negative integer, |  |  |  |  |  |
| tionality controlled by system events. Second, Monkey does | with higher values denoting lesser chance of selecting event |  |  |  |  |  |  |  |
| not compute relevant events and can send many events that | e | in context | E | in the future. We found it suitable to use the |  |  |  |  |
| are no-ops in the current state, hindering efficiency and con- | set of relevant events | E | as context because it is efficient to |  |  |  |  |  |
| ciseness of the generated event sequence. | Third, Monkey | compute (the | observer | already computes | E | ) and it strikes |  |  |
| does not compute a model of the app’s UI, which has pros | a good balance between factoring too little and too much of |  |  |  |  |  |  |  |
| and cons. On one hand, it prevents Monkey from identifying | the state into the context. |  |  |  |  |  |  |  |
| observationally equivalent | UI events (e.g., taps at different | Each time the | selector | is called using this strategy in an |  |  |  |  |
| points of the same button that have the same effect, of click- | observe-select-execute cycle, it runs the algorithm on lines |  |  |  |  |  |  |  |
| ing the button) and hinders efficiency and conciseness; on | 3-25, taking as input the set of relevant events | E | from the |  |  |  |  |  |
| the other hand, Dynodroid sends mostly fixed inputs (see | observer | and producing as output the selected event | e | ∈ | E |  |  |  |
| Table 2) to a widget, and may fail to adequately exercise | for the | executor | to execute. It starts by mapping, for ev- |  |  |  |  |  |
| custom widgets (e.g., a game that interprets taps at differ- | ery | e | ∈ | E | , the pair ( | e, E | ) to its initial score in global map |  |
| ent points of a widget differently). | G | , unless it already exists in | G | . | We bias the initial score |  |  |  |
| A drawback of the | UniformRandom | strategy is that it does | (lines 26-31) depending on the kind of event. If | e | is a Text |  |  |  |
| not take any domain knowledge into account: | it does not | event, its initial score is | − | 1. | In other words, text inputs |  |  |  |
| distinguish between UI events and system events, nor be- | are blacklisted in all contexts. Intuitively, the reason is that |  |  |  |  |  |  |  |
| tween different contexts in which an event may occur, nor | text inputs are interesting only if they are followed by a non- |  |  |  |  |  |  |  |
| between frequent and infrequent events. | For instance, an | text input, e.g., a button click. | Hence, we forbid selecting |  |  |  |  |  |
| event that is always relevant (e.g., an incoming phone call | text inputs in the | selector | altogether, and instead require |  |  |  |  |  |
| event) stands to be picked much more often than one that | the | executor | to populate all text boxes in the current UI |  |  |  |  |  |
| is relevant only in certain contexts (e.g., only on a certain | before it executes the selected non-Text event. | We distin- |  |  |  |  |  |  |
| screen of the app). As another example, navigation buttons | guish between two kinds of non-Text events: | non-Text UI |  |  |  |  |  |  |
| (“back” and “menu”) are always relevant, but often have dif- | events and system events. | We choose initial score of 1 for |  |  |  |  |  |  |
| ferent behavior on different screens. These observations mo- | the former and 2 for the latter, reducing the relative chance |  |  |  |  |  |  |  |
| tivate our final and default selection strategy | BiasedRandom | . | of selecting system events. This bias stems from our obser- |  |  |  |  |  |
| This strategy is shown in Algorithm 2. Like the | Frequency | vation that system events tend to be relevant over longer |  |  |  |  |  |  |
| strategy, it maintains a history of how often each event has | periods than UI events, with UI events typically being rel- |  |  |  |  |  |  |  |
| been selected in the past, but it does so in a context-sensitive | evant only when a certain screen is displayed. | A hallmark |  |  |  |  |  |  |
| manner: the | context | for an event | e | at a particular instant is | of our algorithm, however, is that it never starves any event |  |  |  |
| the set | E | of all relevant events at that instant. This history is | in any context. | This is ensured by lines 11-25, which re- |  |  |  |  |

---

## Page 7

Table 4 : Handling of events of externally triggerable system services in Dynodroid.

| Service | Register/Unregister Mechanism | Callback Mechanism | Trigger Mechanism |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| registerMediaButtonEventReceiver( | C | ) / | invoke component denoted by | send KeyPress event with keycode of |  |  |
| unregisterMediaButtonEventReceiver() | ComponentName object | C | any | MEDIA BUTTON | via | monkeyrunner |

Audio-

Manager requestAudioFocus( L ) /

abandonAudioFocus()

Location-

Manager

on[Location

onProvider[Enabled

removeUpdates()

requestSingleUpdate() /

auto unregister after update

Telephone- listen( L , S ), with

Manager state S non-zero / zero

Table 5 : Emulator configuration in our evaluation.

| Feature Name | Feature Value |
| --- | --- |
| Device RAM size | 4 GB |
| Emulator hardware features | All except GPU emulation |
| Sdcard size | 1 GB |
| Files on Sdcard | pdf:2, img:2, vcf:11, arr:2, zip:4, |
| (type:count) | 3gp:1, m4v:1, mov:1, mp3:3 |

one satisfies condition L ( e ) = G ( e, E ), in which case it is

returned as the event selected by the current selector call.

chance of picking e in context E in a future selector call.

L is a local map that records the number of times event e

was randomly picked by the above process in the current se-

lector call but passed over for not satisfying the condition.

Thus, fewer the number of times that e has been chosen in

context E in past selector calls, or higher the number of

times that e has been passed over in context E in the current

selector call, the higher the chance that e will be selected

to execute in context E in the current selector call.

| call onAudioFocusChange() in | simulate incoming phone call |  |  |  |
| --- | --- | --- | --- | --- |
| AudioManager.OnAudioFocus- | from a fixed MSIDN | N | via |  |
| ChangeListener object | L | telnet command “gsm call | N | ” |

trigger PendingIntent P

| if LocationListener specified, call | set geo-location twice, via |  |  |  |
| --- | --- | --- | --- | --- |
| \| | Status]Changed() or | commands “geo fix | G |  |
| \| | Disabled](); | “geo fix | G | is random |

2 ”; G 1

| else call PendingIntent or post to | geo-location, | G | 2 | is based on |  |
| --- | --- | --- | --- | --- | --- |
| message queue of given Looper | G | 1 | and registered criteria. |  |  |
| same as above | same as above |  |  |  |  |
| call onDataActivity() or any of | trigger state change via telnet |  |  |  |  |
| several on*Changed() methods | command “gsm | C D | ”; | C | is random gsm |
| on PhoneStateListener object | L | command and | D | is random valid data. |  |

Our first study measures the app source code coverage

that different input generation approaches are able to achieve.

We randomly chose 50 apps from the Android open-source

apps repository F-Droid [3] for this study. These 50 apps

are sufficiently diverse as evidenced in Figure 3. The SLOC

of these apps ranges from 16 to 21.9K, with a mean of 2.7K.

We obtained app coverage metrics by using Emma [2],

a popular Java source code coverage tool. Emma generates

detailed line coverage metrics to the granularity of branches,

and provides coverage reports in different formats that assist

in analysis and gathering statistics.

| addGpsStatusListener( | L | ) / | call onGpsStatusChanged() in | set geo-location to fixed value | G |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| removeGpsStatusListener() | GpsStatus.Listener object | L | via telnet command “geo fix | G | ” |  |  |  |  |  |  |  |
| addNmeaListener( | L | ) / | call onNmeaReceived() in | send fixed NMEA data | S | via |  |  |  |  |  |  |
| removeNmeaListener() | GpsStatus.NmeaListener object | L | telnet command “geo nmea | S | ” |  |  |  |  |  |  |  |
| addProximityAlert( | G | , | P | ) / | set geo-location to registered proximal |  |  |  |  |  |  |  |
| removeProximityAlert() | value | G | via telnet command “geo fix | G | ” |  |  |  |  |  |  |  |
| requestLocationUpdates() / | 1 | ” and |  |  |  |  |  |  |  |  |  |  |
| Sensor- | registerListener( | L | , | S | ) / | call on[Accuracy | \| | Sensor]Changed() | set random values | x, y, z | for sensor | S |
| Manager | unregisterListener() | on SensorEventListener object | L | via telnet command “sensor set | S | x | : | y | : | z | ” |  |
| peatedly pick an event | e | from | E | uniformly at random, until | Figure 3 | : | Distribution of open-source apps. |  |  |  |  |  |
| Just before returning, we increment | G | ( | e, E | ) to reduce the | 6.1 | Study 1: App Source Code Coverage |  |  |  |  |  |  |
| 6. | EMPIRICAL EVALUATION | Evaluated Approaches. | We evaluated the following |  |  |  |  |  |  |  |  |  |
| We evaluated Dynodroid on real-world Android apps, and | five approaches in this study: Dynodroid using each of the |  |  |  |  |  |  |  |  |  |  |  |
| compared it to two state-of-the-art approaches for testing | three selection strategies ( | Frequency | , | UniformRandom | , | Biase- |  |  |  |  |  |  |
| such apps: manual testing and automated fuzzing. All our | dRandom | ); the Monkey fuzz testing tool provided in the An- |  |  |  |  |  |  |  |  |  |  |
| experiments were done on Linux machines with 8GB mem- | droid platform; and manual testing conducted in a study in- |  |  |  |  |  |  |  |  |  |  |  |
| ory and 3.0GHz processors. We used the Gingerbread ver- | volving ten users. Table 6 shows the setup we used for each |  |  |  |  |  |  |  |  |  |  |  |
| sion of Android, which is the most popular version, installed | of these five approaches on each app. | We ran each of the |  |  |  |  |  |  |  |  |  |  |
| on 50% of all devices that recently accessed Google Play [6]. | three variants of Dynodroid for 2,000 events, we ran Monkey |  |  |  |  |  |  |  |  |  |  |  |
| Table 5 shows the emulator configuration that we used in all | for 10,000 events, and we allowed the users in our study to |  |  |  |  |  |  |  |  |  |  |  |
| experiments. For each run, an app was given a freshly cre- | manually generate an unlimited number of events. |  |  |  |  |  |  |  |  |  |  |  |
| ated emulator along with only default system applications | We used different numbers of events for Dynodroid and |  |  |  |  |  |  |  |  |  |  |  |
| and the above configuration. We next describe two studies | Monkey because those are the numbers of events that the |  |  |  |  |  |  |  |  |  |  |  |
| we performed: measuring app source code coverage (Section | two tools were able to generate in roughly the same duration |  |  |  |  |  |  |  |  |  |  |  |
| 6.1) and finding bugs in apps (Section 6.2). | in three hours for each of the 50 apps on average. Dynodroid |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

Table 6 : Testing approaches used to test each app. under test, we prevented both Dynodroid and Monkey from

| Dynodroid | Frequency | 2,000 | 1 |
| --- | --- | --- | --- |
| Dynodroid | UniformRandom | 2,000 | 3 |
| Apps Switch | 2% |  |  |
| Others (keyboard/volume/camera buttons) | 16% |  |  |

runs 5X slower than Monkey primarily due to performance

issues with the version of the off-the-shelf Hierarchy Viewer

tool it calls after each event. On the plus side, as we show

below, Dynodroid achieves peak code coverage much faster

than Monkey, requiring far fewer than even the 2,000 events

we generated.

Monkey triggers a large variety of UI events but no system

events. Table 7 summarizes the kinds of UI events it triggers

in its default configuration that we used. These events are

strictly a superset of the kinds of UI events that Dynodroid

can generate (see Section 4.1).

All ten users that we chose in our study are graduate stu-

dents at Georgia Tech who have experience with not only

using Android apps, but also developing and testing them

using Android developer tools. We provided each of them

with each app’s source code, the ability to run the app any

number of times in the Android emulator, and the ability

to inspect app source code coverage reports produced from

those runs. They were allowed to provide any kind of GUI

inputs, including intelligent game inputs and login creden-

tials to websites. They were also allowed to modify the en-

vironment by adding/removing files from the emulator’s Sd-

card, to manually trigger system events via a terminal by

studying the apps’ source code, etc.

We ensured that each app was assigned to at least two

users. Likewise, we ran each automated approach involv-

ing randomization (Monkey, and the UniformRandom and

BiasedRandom strategies in Dynodroid) three times on each

app. We considered the highest coverage that a user or

run achieved for each app. Perhaps surprisingly, for cer-

tain apps, we found fairly significant variation in coverage

achieved across the three runs by any of the random ap-

proaches. Upon closer inspection, we found certain events in

these apps that if not selected in a certain state, irreversibly

prevent exploring entire parts of the app’s state space. Two

possible fixes to this problem are: (i) allowing a relatively

expensive event during testing that removes and re-installs

the app (Dynodroid currently installs the app only once in

a run); and (ii) to simply run the app multiple times and

aggregate their results.

Finally, Android apps may often call other apps such as

a browser, a picture editor, etc. To prevent the automated

approaches in the study from wandering far beyond the app

exercising components not contained in the app under test.

study for the 50 apps are shown in the three plots in Figure 4.

Figure 4a compares the code coverage achieved for each

notes the user who achieved the best coverage of all users

but not the other).

Both Dynodroid and Human cover 4-91% of code per app,

for an average of 51%. Dynodroid exclusively covers 0-26%

of code, for an average of 4%, and Human exclusively cov-

ers 0-43% of code, for an average of 7%. In terms of the

total code covered for each app, Human easily outperforms

Dynodroid, achieving higher coverage for 34 of the 50 apps.

This is not surprising, given that the users in our study were

expert Android users, could provide intelligent text inputs

and event sequences, and most importantly, could inspect

Emma’s coverage reports and attempt to trigger events to

cover any missed code.

But all the ten users in our study also reported tedious-

ness during testing, how easy it was to miss combinations of

events, and that it was especially mundane to click various

options in the settings of apps one by one. Dynodroid could

be used to automate most of the testing effort of Human, as

measured by what we call the automation degree , measured

as the ratio of coverage achieved by the intersection of Dyno-

droid and Human, to the total coverage achieved by Human.

This ratio varies from 8% to 100% across our 50 apps, with

mean 83% and standard deviation 21%. These observations

justify Dynodroid’s vision of synergistically combine human

and machine. It already provides support for intelligent text

inputs, where a user with knowledge of an app can specify

the text that it should use (instead of random text) in the

specific text box widget prior to execution, or can pause

its event generation when it reaches the screen, key in the

input, and let it resume (as described in Section 3).

Figure 4b compares the code coverage achieved for each of

the 50 apps by Dynodroid vs. Monkey. It is analogous to Fig-

ure 4a with Monkey instead of Human. Both Dynodroid and

Monkey cover 4-81% of code per app, for an average of 47%.

Dynodroid exclusively covers 0-46% of code, for an average

of 8%, which is attributed to system events that only Dyno-

droid can trigger. Monkey exclusively covers 0-61% of code,

for an average of 6%, which is attributed to the richer set of

UI events that Monkey can trigger (see Table 2 vs. Table 7).

Another reason is that Dynodroid only generates straight

(Drag) gestures but Monkey combines short sequences of

such gestures to generate more complex (e.g., circular) ges-

tures. Finally, Dynodroid uses fixed parameter values for UI

events whereas Monkey uses random values, giving it supe-

rior ability to exercise custom widgets. In terms of the total

code covered for each app, however, Dynodroid outperforms

Monkey, achieving higher coverage for 30 of the 50 apps.

| Approach | #Events | #Runs | Coverage Results. | The results of our code coverage |
| --- | --- | --- | --- | --- |
| Dynodroid | BiasedRandom | 2,000 | 3 | To enable comparisons for each app across plots, each point |
| Monkey | 10,000 | 3 | on the X axis of all three plots denotes the same app. We |  |
| Humans | no limit | ≥ | 2 | next elaborate upon the results in each of these plots. |
| Table 7 | : | Kinds of UI events triggered by Monkey. | of the 50 apps by Dynodroid vs. Human, where Human de- |  |
| Event Type | Proportion | in our user study for a given app, and Dynodroid uses the |  |  |
| Touch | 15% | BiasedRandom | strategy. | The bar for each app has three |
| Motion | 10% | parts: the bottom red part shows the fraction of code that |  |  |
| Trackball | 15% | both Dynodroid and Human were able to cover (i.e., the in- |  |  |
| Minor Navigation | 25% | tersection of code covered by them). Atop this part are two |  |  |
| Major Navigation | 15% | parts showing the fraction of code that only Dynodroid and |  |  |
| System keys | 2% | only Human were able to cover (i.e., the code covered by one |  |  |

---

## Page 9

100

80

60

40

% App Code Coverage

20

0

(a) Code coverage achieved by Dynodroid (

100

80

60

40

% App Code Coverage

20

0

(b) Code coverage achieved by Dynodroid (

10000

1000

Number of Events

100

(c)

to do so. Note that the Y axis in Figure 4c uses a logarithmic scale.

Dynodroid using each of the selection strategies—to achieve

Monkey for 10,000 events and Dynodroid for 2,000 events).

To strike a good tradeoff between measurement accuracy

and performance, we invoke Emma to aggregate coverage

after every 100 events for each approach on each app, and

hence the minimum number of reported events is 100. It

is evident that all three strategies in Dynodroid require sig-

nificantly fewer events than Monkey; in particular, Monkey

requires 20X more events than BiasedRandom on average.

This is despite Dynodroid considering both system and UI

events at each step. The reason is that Dynodroid only ex-

ercises relevant events at each step and also because it iden-

tifies observationally equivalent events. Finally, of the three

selection strategies in Dynodroid, BiasedRandom performs

common

only Dynodroid

only Human

BiasedRandom ) vs. Human.

common

only Dynodroid

only Monkey

BiasedRandom ) vs. Monkey.

BiasedRandom

UniformRandom

Frequency

Monkey

Minimum number of events needed for peak code coverage by various approaches.

The second study we performed shows that Dynodroid is

an effective bug-finding tool and is also robust. To demon-

strate its robustness, we were able to successfully run Dyno-

droid on the 1,000 most popular free apps from Google Play.

The popularity metric used is a score given to each app by

Google that depends on various factors like number of down-

loads and ratings. These apps are uniformly distributed over

all 31 app categories in Google Play: the minimum, maxi-

mum, mean, and standard deviation of the number of apps

in these categories is 26, 55, 40.3, and 6.3, respectively.

We also found that Dynodroid exposed several bugs in

both the 50 open-source apps we chose from F-Droid and

the 1,000 most popular free apps from Google Play. Table 8

Figure 4 : Results of the app source code coverage study. Each point on the X axis in all three plots denotes

the same app from the 50 open-source apps used in the study. Figure 4a shows that Dynodroid can be used

to automate to a significant degree the tedious testing done by humans. Figure 4b shows that Dynodroid

and Monkey get comparable coverage, but Figure 4c shows that Monkey requires significantly more events

| Figure 4c compares the minimum number of events that | the best, with each of the other two strategies requiring 2X |  |
| --- | --- | --- |
| were needed by each automated approach—Monkey, and | more events than it on average. |  |
| peak code coverage for each of the 50 apps (recall that we ran | 6.2 | Study 2: Bugs Found in Apps |

---

## Page 10

Table 8 : Bugs found by Dynodroid in the 50 open-source apps from F-Droid and the 1,000 top free apps from

Google Play. The two classes of apps are separated by the double line, with all the open-source apps listed

above. NULL PTR denotes a “null pointer dereference” exception and ARRAY IDX an “array index out of

bounds” exception.

| App Name | # Bugs | Kind | Description |
| --- | --- | --- | --- |
| PasswordMakerProForAndroid | 1 | NULL PTR | Improper handling of user data. |
| com.morphoss.acal | 1 | NULL PTR | Dereferencing null returned by an online service. |
| hu.vsza.adsdroid | 2 | NULL PTR | Dereferencing null returned by an online service. |
| cri.sanity | 1 | NULL PTR | Improper handling of user data. |
| com.zoffcc.applications.aagtl | 2 | NULL PTR | Dereferencing null returned by an online service. |
| org.beide.bomber | 1 | ARRAY IDX | Game indexes an array with improper index. |
| com.addi | 1 | NULL PTR | Improper handling of user data. |
| com.ibm.events.android.usopen | 1 | NULL PTR | Null pointer check missed in onCreate() of an activity. |
| com.nullsoft.winamp | 2 | NULL PTR | Improper handling of RSS feeds read from online service. |
| com.almalence.night | 1 | NULL PTR | Null pointer check missed in onCreate() of an activity. |
| com.avast.android.mobilesecurity | 1 | NULL PTR | Receiver callback fails to check for null in optional data. |
| com.aviary.android.feather | 1 | NULL PTR | Receiver callback fails to check for null in optional data. |
| summarizes these bugs. | We mined the Android emulator | using the GUITAR [4] framework. | GUITAR has been ap- |
| logs for any unhandled exceptions that were thrown from | plied to Android apps, IPhone apps, and web apps, among |  |  |
| code in packages of the app under test while Dynodroid ex- | others. | In general, model-based testing requires users to |  |
| ercised the app in the emulator. | To be conservative, we | provide a model of the app’s GUI [24, 27], though auto- |  |
| checked for only | FATAL EXCEPTION | , as this exception is | mated GUI model inference tools tailored to specific GUI |
| the most severe and causes the app to be forcefully termi- | frameworks exist as well [8, 23]. | One such tool in the An- |  |
| nated. We manually ascertained each bug to eliminate any | droid platform, that Dynodroid also uses for observing rele- |  |  |
| false positives reported by this method but found that all the | vant UI events, is Hierarchy Viewer [5]. Model-based testing |  |  |
| bugs were indeed genuine and did cause the app to crash. | harnesses human and framework knowledge to abstract the |  |  |

input space of a program’s GUI, and thus reduce redun-

dancy and improve efficiency, but existing approaches pre-

7. RELATED WORK

dominantly target UI events as opposed to system events.

| There are broadly three kinds of approaches for generating | The EXSYST tool [15] extends model-based testing using a |  |  |
| --- | --- | --- | --- |
| inputs to mobile apps: | fuzz testing | , which generates random | genetic algorithm to continually refine models from run-time |
| inputs to the app; | systematic testing | , which systematically | feedback, with the goal of maximizing the code coverage of |
| tests the app by executing it symbolically; and | model-based | the given app. | It uses guidance based on branch distance |
| testing | , which tests a model of the app. We elaborate upon | measurement and also aims to produce small test suites. |  |

each of these three approaches in this section.

Fuzz Testing. The Android platform includes a fuzz

| testing tool Monkey [7] that generates a sequence of random | 8. | CONCLUSION |
| --- | --- | --- |
| UI events to Android apps in a mobile device emulator. Re- | We presented a practical system Dynodroid for generat- |  |
| cent work has applied Monkey to find GUI bugs [16] and | ing relevant inputs to mobile apps on the dominant Android |  |
| security bugs [19]. Fuzz testing is a black-box approach, is | platform. | It uses a novel “observe-select-execute” princi- |
| easy to implement robustly, is fully automatic, and can effi- | ple to efficiently generate a sequence of such inputs to an |  |
| ciently generate a large number of simple inputs. But it is | app. It operates on unmodified app binaries, it can generate |  |
| not suited for generating inputs that require human intel- | both UI inputs and system inputs, and it allows combin- |  |
| ligence (e.g., playing and winning a game) nor is it suited | ing inputs from human and machine. | We applied it to a |
| for generating highly specific inputs that control the app’s | suite of 50 real-world apps and compared its performance to |  |
| functionality, and it may generate highly redundant inputs. | two state-of-the-art input generation approaches for Android |  |
| Finally, Monkey only generates UI events, not system events. | apps: manual testing done by expert users and fuzz testing |  |
| It is challenging to randomly generate system events due to | using the popular Monkey tool. We showed that Dynodroid |  |
| the large space of possible such events and highly structured | can significantly automate testing tasks that users consider |  |
| data that is associated with them. | tedious, and generates significantly more concise input se- |  |
| Systematic Testing. | Several recent efforts [9, 17, 22] | quences than Monkey. We also showed its robustness by ap- |
| have applied symbolic execution [11, 14, 18] to generate in- | plying it to the top 1,000 free apps on Google Play. Lastly, |  |
| puts to Android apps. | Symbolic execution automatically | it exposed a few bugs in a handful of the apps to which it |
| partitions the domain of inputs such that each partition cor- | was applied. |  |

responds to a unique program behavior (e.g., execution of a

unique program path). Thus, it avoids generating redundant

| inputs and can generate highly specific inputs, but it is dif- | ACKNOWLEDGMENTS |  |
| --- | --- | --- |
| ficult to scale due to the notorious path explosion problem. | We thank the anonymous reviewers for insightful comments. |  |
| Moreover, symbolic execution is not black-box and requires | We thank the ten users in our study for their participation. |  |
| heavily instrumenting the app in addition to the framework. | This research was supported in part by DARPA contract |  |
| Model-based Testing. | Model-based testing has been | #FA8750-12-2-0020, NSF award #1253867, and awards from |
| widely studied in testing GUI-based programs [10,20,21,26] | Google and Microsoft. |  |

---

## Page 11

9. REFERENCES ACM Conf. on Programming Language Design and

testing. http://guitar.sourceforge.net/ .

[6] Historical distribution of Android versions in use.

[8] D. Amalfitano, A. Fasolino, S. Carmine, A. Memon,

and P. Tramontana. Using GUI ripping for automated

testing of Android applications. In Proceedings of 27th

[9] S. Anand, M. Naik, H. Yang, and M. Harrold.

markets. In Proceedings of 2nd Intl. Workshop on

Implementation (PLDI) , 2005.

Test (AST) , 2011.

//www.cs.umd.edu/~jfoster/papers/symdroid.pdf .

automated security testing of Android applications on

the cloud. In Proceedings of 7th IEEE/ACM Workshop

on Automation of Software Test (AST) , 2012.

Foundations of Software Engineering (FSE) , 2000.

Engr. , 37(4), 2011.

| [1] DroidBox: Android application sandbox. | [15] F. Gross, G. Fraser, and A. Zeller. Search-based |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| http://code.google.com/p/droidbox/ | . | system testing: high coverage, no false alarms. In |  |  |  |
| [2] EMMA: a free Java code coverage tool. | Proceedings of the 2012 International Symposium on |  |  |  |  |
| http://emma.sourceforge.net/ | . | Software Testing and Analysis (ISSTA) | , 2012. |  |  |
| [3] Free and Open Source App Repository. | [16] C. Hu and I. Neamtiu. Automating GUI testing for |  |  |  |  |
| https://f-droid.org/ | . | Android applications. In | Proceedings of 6th |  |  |
| [4] GUITAR: A model-based system for automated GUI | IEEE/ACM Workshop on Automation of Software |  |  |  |  |
| [5] Hierarchy Viewer. | http://developer.android.com/ | [17] J. Jeon, K. Micinski, and J. Foster. Symdroid: |  |  |  |
| tools/help/hierarchy-viewer.html | . | Symbolic execution for dalvik bytecode, 2012. | http: |  |  |
| http://developer.android.com/about/dashboards/ | [18] J. King. Symbolic execution and program testing. |  |  |  |  |
| index.html | . | CACM | , 19(7):385–394, 1976. |  |  |
| [7] UI/Application Exerciser Monkey. | http: | [19] R. Mahmood, N. Esfahani, T. Kacem, N. Mirzaei, |  |  |  |
| //developer.android.com/tools/help/monkey.html | . | S. Malek, and A. Stavrou. A whitebox approach for |  |  |  |
| Intl. Conf. on Automated Software Engineering | [20] A. Memon, M. Pollack, and M. Soffa. Automated test |  |  |  |  |
| (ASE) | , 2012. | oracles for GUIs. In | Proceedings of ACM Conf. on |  |  |
| Automated concolic testing of smartphone apps. In | [21] A. Memon and M. Soffa. Regression testing of GUIs. |  |  |  |  |
| Proceedings of ACM Conf. on Foundations of Software | In | Proceedings of ACM Conf. on Foundations of |  |  |  |
| Engineering (FSE) | , 2012. | Software Engineering (FSE) | , 2003. |  |  |
| [10] R. Bryce, S. Sampath, and A. Memon. Developing a | [22] N. Mirzaei, S. Malek, C. Pasareanu, N. Esfahani, and |  |  |  |  |
| single model and test prioritization strategies for | R. Mahmood. Testing Android apps through symbolic |  |  |  |  |
| event-driven software. | Trans. on Soft. Engr. | , 37(1), | execution. In | Java Pathfinder Workshop (JPF) | , 2012. |
| 2011. | [23] T. Takala, M. Katara, and J. Harty. Experiences of |  |  |  |  |
| [11] C. Cadar, D. Dunbar, and D. Engler. KLEE: | system-level model-based GUI testing of an Android |  |  |  |  |
| Unassisted and automatic generation of high-coverage | app. In | Proceedings of 4th Intl. Conf. on Software |  |  |  |
| tests for complex systems programs. In | Proceedings of | Testing, Verification and Validation (ICST) | , 2011. |  |  |
| 8th USENIX Symp. on Operating Systems Design and | [24] L. White and H. Almezen. Generating test cases for |  |  |  |  |
| Implementation (OSDI) | , 2008. | GUI responsibilities using complete interaction |  |  |  |
| [12] W. Enck, P. Gilbert, B.-G. Chun, L. Cox, J. Jung, | sequences. In | Proceedings of 11th IEEE Intl. Symp. on |  |  |  |
| P. McDaniel, and A. Sheth. Taintdroid: An | Software Reliability Engineering (ISSRE) | , 2000. |  |  |  |
| information-flow tracking system for realtime privacy | [25] L. Yan and H. Yin. DroidScope: Seamlessly |  |  |  |  |
| monitoring on smartphones. In | Proceedings of 9th | reconstructing the OS and Dalvik semantic views for |  |  |  |
| USENIX Symp. on Operating Systems Design and | dynamic Android malware analysis. In | Proceedings of |  |  |  |
| Implementation (OSDI) | , 2010. | 21st USENIX Security Symposium | , 2012. |  |  |
| [13] P. Gilbert, B.-G. Chun, L. Cox, and J. Jung. Vision: | [26] X. Yuan, M. Cohen, and A. Memon. GUI interaction |  |  |  |  |
| automated security validation of mobile apps at app | testing: Incorporating event context. | Trans. on Soft. |  |  |  |
| Mobile Cloud Computing and Services (MCS) | , 2011. | [27] X. Yuan and A. Memon. Generating event |  |  |  |
| [14] P. Godefroid, N. Klarlund, and K. Sen. DART: | sequence-based test cases using GUI runtime state |  |  |  |  |
| Directed automated random testing. In | Proceedings of | feedback. | Trans. on Soft. Engr. | , 36(1), 2010. |  |
